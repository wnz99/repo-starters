# Repository starters

Working base configuration for Python, TypeScript and mixed Nx monorepos. Copy a starter, then give [POLISH.md](POLISH.md) to your LLM to adapt it. Configuration lives in files; the prompt handles project choices and extra tools.

| Starter                            | Contents                                                                                                   |
| ---------------------------------- | ---------------------------------------------------------------------------------------------------------- |
| [Python](profiles/python/)         | uv/Poe, Ruff, BasedPyright, Pylint/Clean Code, Deptry, pytest, Pydantic and wheel-consumer checks          |
| [TypeScript](profiles/typescript/) | Bun/strict TypeScript, ESLint/Clean Code/SonarJS/Unicorn, Prettier, Knip/Fallow and packed-consumer checks |
| [Monorepo](profiles/monorepo/)     | Both ecosystems, root-owned quality policy and explicit Nx projects/targets                                |

Each directory contains locked dependencies, native commands, Git hooks, CI, agent rules and short indexed docs. Tiny input-validation fixtures prove the tooling is connected; this is not an example application.

```sh
git clone --branch v1.1.1 --depth 1 https://github.com/wnz99/repo-starters.git
mkdir my-project
cp -R repo-starters/profiles/python/. my-project/
cd my-project
git init
sh tools/quality/setup.sh
sh tools/quality/check.sh
```

Choose `typescript` or `monorepo` instead of `python` as appropriate. Copy into a new empty directory. For an existing repository, ask the LLM to merge the relevant configuration after inspecting its owners; do not overwrite files with this command. Do not copy `.git`, dependency folders or local state from a used checkout.

Read the selected starter README for runtime prerequisites and commands. The LLM pass installs agent skills, adapts runtime/framework needs, uses PydanticAI/FastMCP where applicable, asks about optional integrations, updates names and records verification. It does not treat silence as approval or publish/deploy without authorization.

[Local documentation](docs/index.md) includes policy owners, acquisition sources, record contracts and acceptance checklists. [Pasteable setup prompt](https://llms.wnz.sh/docs/python-typescript-bootstrap). [CC0-1.0](LICENSE) covers reusable starter content; dependencies and skills retain their own licenses. Confirm your new project's license during adaptation.
