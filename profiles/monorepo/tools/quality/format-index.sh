#!/bin/sh
set -eu
repo_root=$1
snapshot_root=$2
cd "$snapshot_root"
ruff="$repo_root/.venv/bin/ruff"
[ -x "$ruff" ] || ruff="$repo_root/.venv/Scripts/ruff.exe"
"$ruff" format --check --config "$snapshot_root/quality/pyproject.toml" packages/python/core/src
"$ruff" format --check --config "$snapshot_root/quality/pyproject.toml" packages/python/core/tests
"$ruff" format --check --config "$snapshot_root/quality/pyproject.toml" tools/quality
bun "$repo_root/node_modules/prettier/bin/prettier.cjs" --config "$snapshot_root/.prettierrc.json" --ignore-path "$snapshot_root/.prettierignore" --check --ignore-unknown .
