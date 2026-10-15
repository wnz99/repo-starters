---
type: Reference
title: Development
description: Commands, configuration ownership and adaptation limits.
---

# Development

Run `sh tools/quality/setup.sh`, then `sh tools/quality/check.sh`. Pre-push uses `sh tools/quality/check-static.sh`; both preserve nonzero failures. Native manifests expose component commands and explicit format/fix tasks. Root owns shared policy, hooks and helper checks. Components own runtime/test dependencies and artifacts.

Profile: `monorepo`. Python: 3.14.8. Bun: 1.3.13. Node tooling: 24.19.0. Versions are explicit starter choices, not automatic upgrades. Adapt supported runtimes deliberately and rerun applicable gates. No cloud setup, branch promotion, merge policy, remote protection, Serena, semantic MCP, self-hosted runner, or agent-skill installation is implied.

Python uses Ruff, strict BasedPyright, Pylint/Clean Code, Deptry, pytest and wheel isolation. TypeScript uses strict tsc, typed ESLint/Clean Code/SonarJS/Unicorn, Prettier, Bun tests, packed consumers, Knip and Fallow. Only the applicable ecosystem is installed. Small tests protect whitespace normalization, invalid input and installed-package reachability; replace them with meaningful project behavior tests.

CI is GitHub Actions on ubuntu-24.04 with action commits pinned. The local starter validation does not prove every OS, browser, Node application, optional integration or affected-selection matrix. Monorepos use explicit Nx projects, cache inputs and full CI checks; enable affected execution only after validating the real dependency graph/base history. Record project-specific verification and unrun gates here during the POLISH pass.

For TypeScript tooling, the external `uv` executable is a checked runtime prerequisite, not an npm dependency. Knip therefore lists only `uv` under `ignoreBinaries`; no dependency/export/file findings are suppressed. Python helper annotations use a TYPE_CHECKING import for Path under Python 3.14, preserving runtime behavior and the full Ruff policy.

Only tests/isolation may use the library public name from the same Nx project: allowCircularSelfDependency permits that packaged-consumer contract. Production source keeps the complete boundary rule. Fallow may warn that a component helper command traverses to the root; that helper is explicitly included in root entrypoints.
