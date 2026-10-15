---
type: Reference
title: Acquisition sources
description: Runtime, package, skill and optional-integration installation sources.
---

# Acquisition sources

Use these official runtime downloads and package-registry pages to obtain the tools named below. The copied manifests and frozen lockfiles own installed versions: a landing page may show a newer release, which is not an instruction to upgrade. Install packages through the selected uv/Bun workflow and preserve frozen lockfiles. The Python and npm packages named FastMCP and Clean Code Tools have distinct distributions.

| Runtime or prerequisite | Installation source                                                                                                                         |
| ----------------------- | ------------------------------------------------------------------------------------------------------------------------------------------- |
| Python                  | [Official downloads](https://www.python.org/downloads/); [uv-managed Python installation](https://docs.astral.sh/uv/guides/install-python/) |
| uv                      | [Official installation guide](https://docs.astral.sh/uv/getting-started/installation/)                                                      |
| Bun                     | [Official installation guide](https://bun.sh/docs/installation)                                                                             |
| Node.js                 | [Official downloads](https://nodejs.org/en/download)                                                                                        |
| Git and its shell       | [Official downloads](https://git-scm.com/downloads)                                                                                         |

The original baseline pins have these acquisition sources. They are reference pins; record accepted changes in manifests and locks instead of upgrading from a landing page:

| Ecosystem | Package and pinned version       | Registry source                                                     |
| --------- | -------------------------------- | ------------------------------------------------------------------- |
| Python    | `basedpyright==1.40.1`           | [PyPI](https://pypi.org/project/basedpyright/1.40.1/)               |
| Python    | `clean-code-tools-python==1.0.7` | [PyPI](https://pypi.org/project/clean-code-tools-python/1.0.7/)     |
| Python    | `deptry==0.25.1`                 | [PyPI](https://pypi.org/project/deptry/0.25.1/)                     |
| Python    | `packaging==26.3`                | [PyPI](https://pypi.org/project/packaging/26.3/)                    |
| Python    | `poethepoet==0.48.0`             | [PyPI](https://pypi.org/project/poethepoet/0.48.0/)                 |
| Python    | `pylint==4.0.8`                  | [PyPI](https://pypi.org/project/pylint/4.0.8/)                      |
| Python    | `pytest==9.1.1`                  | [PyPI](https://pypi.org/project/pytest/9.1.1/)                      |
| Python    | `pydantic==2.13.5`               | [PyPI](https://pypi.org/project/pydantic/2.13.5/)                   |
| Python    | `ruff==0.16.8`                   | [PyPI](https://pypi.org/project/ruff/0.16.8/)                       |
| Python    | `shellcheck-py==0.11.0.1`        | [PyPI](https://pypi.org/project/shellcheck-py/0.11.0.1/)            |
| Python    | `uv==0.13.1`                     | [PyPI](https://pypi.org/project/uv/0.13.1/)                         |
| Python    | `hatchling==1.32.4`              | [PyPI](https://pypi.org/project/hatchling/1.32.4/)                  |
| Python    | `pydantic-ai-slim==2.56.0`       | [PyPI](https://pypi.org/project/pydantic-ai-slim/2.56.0/)           |
| Python    | `fastmcp==4.1.0`                 | [PyPI](https://pypi.org/project/fastmcp/4.1.0/)                     |
| npm       | `@eslint/js@10.0.1`              | [npm](https://www.npmjs.com/package/@eslint/js/v/10.0.1)            |
| npm       | `@types/bun@1.3.13`              | [npm](https://www.npmjs.com/package/@types/bun/v/1.3.13)            |
| npm       | `@types/node@24.19.2`            | [npm](https://www.npmjs.com/package/@types/node/v/24.19.2)          |
| npm       | `clean-code-tools@1.0.7`         | [npm](https://www.npmjs.com/package/clean-code-tools/v/1.0.7)       |
| npm       | `eslint@10.11.0`                 | [npm](https://www.npmjs.com/package/eslint/v/10.11.0)               |
| npm       | `eslint-plugin-sonarjs@4.2.1`    | [npm](https://www.npmjs.com/package/eslint-plugin-sonarjs/v/4.2.1)  |
| npm       | `eslint-plugin-unicorn@69.0.0`   | [npm](https://www.npmjs.com/package/eslint-plugin-unicorn/v/69.0.0) |
| npm       | `fallow@3.27.0`                  | [npm](https://www.npmjs.com/package/fallow/v/3.27.0)                |
| npm       | `globals@17.12.0`                | [npm](https://www.npmjs.com/package/globals/v/17.12.0)              |
| npm       | `knip@6.37.0`                    | [npm](https://www.npmjs.com/package/knip/v/6.37.0)                  |
| npm       | `prettier@3.9.8`                 | [npm](https://www.npmjs.com/package/prettier/v/3.9.8)               |
| npm       | `typescript@6.0.3`               | [npm](https://www.npmjs.com/package/typescript/v/6.0.3)             |
| npm       | `typescript-eslint@8.70.0`       | [npm](https://www.npmjs.com/package/typescript-eslint/v/8.70.0)     |
| npm       | `nx@23.2.1`                      | [npm](https://www.npmjs.com/package/nx/v/23.2.1)                    |
| npm       | `@nx/eslint-plugin@23.2.1`       | [npm](https://www.npmjs.com/package/@nx/eslint-plugin/v/23.2.1)     |
| npm       | `fastmcp@4.22.10`                | [npm](https://www.npmjs.com/package/fastmcp/v/4.22.10)              |
| npm       | `zod@4.6.5`                      | [npm](https://www.npmjs.com/package/zod/v/4.6.5)                    |

Skill download locations point to complete directories at the fixed revisions. Preserve their references and upstream licensing when copying them into `.agents/skills/`.

| Skill                    | Source directory                                                                                                                                                                                                                                         |
| ------------------------ | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `wnz-doc-write-expert`   | [Pinned skill directory](https://github.com/wnz99/llm-dev-skills/tree/1e6b0d8cc149ee26729319bc109414ca7d77145b/skills/wnz-doc-write-expert)                                                                                                              |
| `wnz-code-reviewer`      | [Pinned skill directory](https://github.com/wnz99/llm-dev-skills/tree/1e6b0d8cc149ee26729319bc109414ca7d77145b/skills/wnz-code-reviewer)                                                                                                                 |
| `wnz-test-quality`       | [Pinned skill directory](https://github.com/wnz99/llm-dev-skills/tree/1e6b0d8cc149ee26729319bc109414ca7d77145b/skills/wnz-test-quality)                                                                                                                  |
| `wnz-clean-code-py`      | [Pinned skill directory](https://github.com/wnz99/llm-dev-skills/tree/1e6b0d8cc149ee26729319bc109414ca7d77145b/skills/wnz-clean-code-py)                                                                                                                 |
| `wnz-clean-code-js`      | [Pinned skill directory](https://github.com/wnz99/llm-dev-skills/tree/1e6b0d8cc149ee26729319bc109414ca7d77145b/skills/wnz-clean-code-js)                                                                                                                 |
| `clean-code-tools`       | [Pinned skill directory](https://github.com/wnz99/clean-code-tools/tree/c51c7aa0a9ad555f81e8096e4a7e1c83f9156c1a/skills/clean-code-tools)                                                                                                                |
| `verify-before-complete` | No verified public URL in the pinned trees. Require a user-supplied trusted repository/download URL or installed copy; record its license, source and content digest. Do not invent an upstream link or report installation complete without the source. |

Optional integrations have their own acquisition sources and still require explicit inclusion: [Serena source](https://github.com/oraios/serena) and [setup guide](https://oraios.github.io/serena/02-usage/020_running.html); [Clean Code semantic MCP source](https://github.com/wnz99/clean-code-tools/tree/c51c7aa0a9ad555f81e8096e4a7e1c83f9156c1a). Their links do not authorize server registration, account changes, or installing an unpinned revision.
