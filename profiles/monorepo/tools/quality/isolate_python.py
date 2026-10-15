# SPDX-License-Identifier: CC0-1.0
"""Test a component using installed wheels outside its workspace."""

from __future__ import annotations

import argparse
import os
import shutil
import subprocess
import tempfile
import tomllib
from graphlib import TopologicalSorter
from pathlib import Path

from packaging.requirements import Requirement
from packaging.utils import canonicalize_name, parse_wheel_filename

from isolation_models import Inventory, Manifest, Project

SOURCE_PATH_ENVIRONMENT_KEYS = ("PYTHONPATH", "PYTHONHOME")


def contained(root: Path, relative: str) -> Path:
    path = (root / relative).resolve()
    path.relative_to(root)
    return path


def command(arguments: list[str]) -> list[str]:
    executable = shutil.which(arguments[0])
    if executable is None:
        raise FileNotFoundError(arguments[0])
    return [executable, *arguments[1:]]


def run(arguments: list[str], directory: Path) -> None:
    environment = os.environ.copy()
    for name in SOURCE_PATH_ENVIRONMENT_KEYS:
        environment.pop(name, None)
    subprocess.run(command(arguments), cwd=directory, env=environment, check=True)  # noqa: S603


def load_projects(root: Path, inventory: Inventory) -> dict[str, Project]:
    projects: dict[str, Project] = {}
    for item in inventory.components:
        if item.language != "python":
            continue
        directory = contained(root, item.path)
        manifest = Manifest.model_validate(
            tomllib.loads((directory / "pyproject.toml").read_text())
        )
        name = canonicalize_name(manifest.project.name)
        if name in projects:
            message = "Duplicate Python distribution name"
            raise ValueError(message)
        projects[name] = Project(directory, manifest)
    return projects


def group_requirements(
    manifest: Manifest, group: str = "test", seen: frozenset[str] = frozenset()
) -> list[str]:
    if group in seen:
        message = "Dependency group cycle"
        raise ValueError(message)
    entries = manifest.groups.get(group)
    if entries is None:
        message = "Component must declare a test dependency group"
        raise ValueError(message)
    result: list[str] = []
    for entry in entries:
        if isinstance(entry, str):
            Requirement(entry)
            result.append(entry)
        else:
            result.extend(group_requirements(manifest, entry.include_group, seen | {group}))
    return result


def runtime_requirements(manifest: Manifest, extras: set[str]) -> list[Requirement]:
    entries = list(manifest.project.dependencies)
    optional = {
        canonicalize_name(name): values
        for name, values in manifest.project.optional_dependencies.items()
    }
    for extra in sorted(extras):
        entries.extend(optional[canonicalize_name(extra)])
    return [Requirement(entry) for entry in entries]


def dependency_closure(target: str, projects: dict[str, Project], tests: list[str]) -> list[str]:
    graph: dict[str, set[str]] = {}
    extras: dict[str, set[str]] = {}
    pending = [(target, set[str]())]
    for entry in tests:
        requirement = Requirement(entry)
        if requirement.marker and not requirement.marker.evaluate():
            continue
        name = canonicalize_name(requirement.name)
        if name in projects:
            pending.append((name, set(requirement.extras)))
    while pending:
        name, requested = pending.pop()
        if name in graph and requested <= extras[name]:
            continue
        extras.setdefault(name, set()).update(requested)
        graph.setdefault(name, set())
        for requirement in runtime_requirements(projects[name].manifest, extras[name]):
            if requirement.marker and not any(
                requirement.marker.evaluate({"extra": extra}) for extra in extras[name] | {""}
            ):
                continue
            dependency = canonicalize_name(requirement.name)
            if dependency in projects:
                graph[name].add(dependency)
                pending.append((dependency, set(requirement.extras)))
    return list(TopologicalSorter(graph).static_order())


def build_wheels(projects: dict[str, Project], name: str, tests: list[str], sandbox: Path) -> None:
    wheels = sandbox / "wheels"
    wheels.mkdir()
    for dependency in dependency_closure(name, projects, tests):
        run(
            ["uv", "build", "--no-sources", "--wheel", "--out-dir", str(wheels)],
            projects[dependency].directory,
        )


def export_requirements(root: Path, arguments: list[str], destination: Path) -> None:
    subprocess.run(  # noqa: S603
        command(
            [
                "uv",
                "export",
                "--frozen",
                *arguments,
                "--no-emit-workspace",
                "--output-file",
                str(destination),
            ]
        ),
        cwd=root,
        stdout=subprocess.DEVNULL,
        check=True,
    )


def install_dependencies(
    root: Path, project: Project, projects: dict[str, Project], sandbox: Path, interpreter: Path
) -> None:
    runtime, constraints = sandbox / "runtime.txt", sandbox / "constraints.txt"
    export_requirements(
        root,
        ["--package", project.manifest.project.name, "--no-dev", "--no-default-groups"],
        runtime,
    )
    export_requirements(root, ["--all-packages", "--all-groups"], constraints)
    with constraints.open("a") as output:
        for item in projects.values():
            output.write(f"\n{item.manifest.project.name}=={item.manifest.project.version}\n")
    run(["uv", "pip", "sync", "--python", str(interpreter), str(runtime)], sandbox)
    runtime_names = dependency_closure(
        canonicalize_name(project.manifest.project.name), projects, []
    )
    wheels = [
        str(path)
        for path in sorted((sandbox / "wheels").glob("*.whl"))
        if parse_wheel_filename(path.name)[0] in runtime_names
    ]
    run(["uv", "pip", "install", "--python", str(interpreter), "--no-deps", *wheels], sandbox)


def run_tests(
    root: Path, project: Project, import_package: str, sandbox: Path, interpreter: Path
) -> None:
    tests = project.directory / "tests"
    if tests.is_symlink() or any(path.is_symlink() for path in tests.rglob("*")):
        message = "Isolation fixtures must not link to source outside tests"
        raise ValueError(message)
    shutil.copytree(
        tests,
        sandbox / "tests",
        ignore=shutil.ignore_patterns("__pycache__", "*.pyc", ".pytest_cache"),
    )
    policy = sandbox / "pyproject.toml"
    shutil.copyfile(root / "quality/pyproject.toml", policy)
    run(
        [
            str(interpreter),
            "-I",
            "-c",
            "import importlib,sys; importlib.import_module(sys.argv[1])",
            import_package,
        ],
        sandbox,
    )
    run(
        [
            "uv",
            "pip",
            "install",
            "--python",
            str(interpreter),
            "--no-deps",
            *map(str, sorted((sandbox / "wheels").glob("*.whl"))),
        ],
        sandbox,
    )
    run(
        [
            "uv",
            "pip",
            "install",
            "--python",
            str(interpreter),
            "--no-sources",
            "--constraints",
            str(sandbox / "constraints.txt"),
            *group_requirements(project.manifest),
        ],
        sandbox,
    )
    run(
        [
            str(interpreter),
            "-I",
            "-m",
            "pytest",
            "-c",
            str(policy),
            "--rootdir",
            str(sandbox),
            str(sandbox / "tests"),
        ],
        sandbox,
    )


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("component")
    arguments = parser.parse_args()
    root = Path(__file__).resolve().parents[2]
    inventory = Inventory.model_validate_json((root / ".bootstrap.json").read_bytes())
    selected = next(
        (item for item in inventory.components if item.name == arguments.component), None
    )
    if selected is None:
        parser.error("Unknown component")
    if selected.language != "python" or not selected.import_package:
        message = "Selected component must be Python with an importPackage"
        raise ValueError(message)
    projects = load_projects(root, inventory)
    directory = contained(root, selected.path)
    project = next(item for item in projects.values() if item.directory == directory)
    python_version = inventory.runtimes["python"]
    if not python_version:
        message = "Exact Python version is required"
        raise ValueError(message)
    with tempfile.TemporaryDirectory(prefix="repo-python-isolation-") as temporary:
        sandbox = Path(temporary).resolve()
        if sandbox.is_relative_to(root):
            message = "Isolation temporary directory must be outside the workspace"
            raise ValueError(message)
        build_wheels(
            projects,
            canonicalize_name(project.manifest.project.name),
            group_requirements(project.manifest),
            sandbox,
        )
        environment = sandbox / "environment"
        run(["uv", "venv", "--python", python_version, str(environment)], sandbox)
        interpreter = environment / ("Scripts/python.exe" if os.name == "nt" else "bin/python")
        install_dependencies(root, project, projects, sandbox, interpreter)
        run_tests(root, project, selected.import_package, sandbox, interpreter)


if __name__ == "__main__":
    main()
