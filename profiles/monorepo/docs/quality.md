---
type: Reference
title: Quality baseline
description: Configuration owners and adaptation rules for the working starter.
---

# Quality baseline

Copy the working files, then use [POLISH.md](../POLISH.md) to adapt names, real components, frameworks, skills and explicit optional choices. Do not regenerate configuration from prose.

## Policy owners

| Responsibility                               | Authoritative files                                                                                                                      |
| -------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------- |
| Setup and full/static gates                  | [setup.sh](../tools/quality/setup.sh), [check.sh](../tools/quality/check.sh)                                                             |
| Git hooks and staged snapshots               | [hooks.sh](../tools/quality/hooks.sh), [format-index.sh](../tools/quality/format-index.sh)                                               |
| Python rules and type policy                 | [Shared policy](../quality/pyproject.toml), [BasedPyright](../quality/basedpyright.json)                                                 |
| Python tasks, dependencies and builds        | [Native manifest](../packages/python/core/pyproject.toml), [uv lock](../uv.lock)                                                         |
| TypeScript rules, types and packages         | [ESLint](../eslint.config.mjs), [Compiler base](../tsconfig.base.json), [Native tasks](../package.json), [Bun lock](../bun.lock)         |
| Unused files, exports and dependencies       | [Knip](../knip.json), [Fallow](../.fallowrc.json)                                                                                        |
| Project boundaries, targets and cache inputs | [Nx](../nx.json), [Python project](../packages/python/core/project.json), [TypeScript project](../packages/typescript/core/project.json) |
| CI runtime installation and gates            | [Workflow](../.github/workflows/check.yml)                                                                                               |
| Agent behavior                               | [AGENTS.md](../AGENTS.md)                                                                                                                |
| Inputs, options and content digests          | [Input record](../.bootstrap.json), [Lock record](../.bootstrap-lock.json), [Record contract](bootstrap-records.md)                      |

Check commands are read-only; explicit format/fix commands own mutations. Shared root policy must remain wired into component commands. Installed wheel/packed consumers check artifacts outside workspace dependencies. Hooks preserve another owner and validate staged or pushed content. Local ignored state is allowed; tracked ignored state is rejected.

## Adaptation and evidence

Use [acquisition sources](sources.md) to install tools and skills. Pydantic remains the Python external-boundary choice. Add PydanticAI for actual Python LLM features and the language's FastMCP for actual MCP work, with chosen provider extras, clients and transports. These feature packages are not installed merely by copying a starter.

Explain and ask every unanswered option in POLISH.md. Pending choices create no settings. Preserve credentials externally, existing edits and hook ownership. Refresh [records](bootstrap-records.md) only for accepted changes, after formatting and verification.

Follow the [acceptance checklist](verification.md) and record results/unrun gates in [Development](development.md). The manifests, locks and source files are the policy; this guide maps ownership without duplicating rule presets or versions.
