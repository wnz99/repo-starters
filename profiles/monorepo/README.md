# Monorepo starter

Copy this directory as the root of your project. Replace the tiny input-validation smoke fixtures with your project code through [POLISH.md](POLISH.md).

Prerequisites: Git, uv 0.13.1, Bun 1.3.13 and Node 24.19.0. Python components use Python 3.14.8; uv selects/downloads it during setup. [Acquisition sources](docs/sources.md).

```sh
git init
sh tools/quality/setup.sh
sh tools/quality/check.sh
```

Setup installs locked tools and repository-local hooks, preserving another hook owner. It does not install agent skills, configure optional integrations, create remotes, or deploy. The LLM pass in POLISH.md owns those project decisions.

Format/fix: `bun run format` / component `bun run fix`.

[Development commands and limits](docs/index.md). [Quality baseline](docs/quality.md). Starter content is CC0; dependencies retain their licenses.
