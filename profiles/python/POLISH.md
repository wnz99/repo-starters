# Adapt this starter

Paste this instruction into an LLM agent after copying the chosen starter:

```text
Adapt this working starter to the project below. Reuse its configuration and native commands; do not regenerate the same setup from prose.

Purpose: <what to build>
Names/components: <real packages and applications>
Runtime targets and required operating systems: <Python patch; Bun, Node or browser; platforms>
LLM/MCP features: <providers, clients, protocols, transports, none, or pending>
Project license and documentation language: <choices or pending>
Authorized external actions: <actions and destinations, or none>

1. Inspect instructions, Git status, manifests, locks and tests. Preserve unrelated work. Map the starter to existing owners rather than replacing a functioning toolchain.
2. Rename packages/imports, component paths, exports, .bootstrap.json, Nx projects/tags and the small smoke fixtures consistently. Keep only real components. Update language/consumer locks and bootstrap records under docs/bootstrap-records.md intentionally after changes.
3. Preserve the full applicable quality toolset. Add project/framework tools and meaningful tests where the project needs them. Adapt TypeScript configs, emitted artifacts and consumer test runners to Bun/Node/browser. Pydantic stays the Python boundary choice; use PydanticAI for Python LLM work and FastMCP for MCP work. Keep credentials external.
4. Install applicable skills from docs/sources.md into .agents/skills, preserving references and licenses. Record source commits/digests and client discovery. Missing sources remain incomplete; do not invent them.
5. Explain and ask about each unanswered option: branch promotion (extra integration/staging/production branches and promotion PRs); merge policy (merge/squash/rebase plus cleanup choices); cloud authentication (provider/account/credential method and local/CI scope); Serena (symbol navigation MCP); semantic Clean Code MCP (advisory pattern lookup); self-hosted runners (machine maintenance, access and job isolation). Record include/exclude/pending and needed details. Pending choices generate no settings. Included unavailable integrations remain incomplete. If Coolify is explicitly selected, apply docs/coolify.md to the actual deployment; pending cloud selection leaves that adaptation pending.
6. Run setup, native full checks, builds and isolated consumers. For selected Coolify deployments, record the docs/coolify.md acceptance checks and unrun gates. Show a deliberate behavior or lint defect fails in a disposable copy, then restore and rerun. Verify affected/cache behavior for the actual monorepo graph, OS support and safe repeated setup. Preserve local edits; never overwrite generated files blindly. Record results and unrun gates in docs/development.md.
7. Update README, AGENTS and the OKF docs index. Report changes, tool versions, optional choices and fresh verification. Publish or provision only within supplied authorization.
```

The starter contains working baseline files; project choices and optional integrations are deliberately left to this pass. `LICENSE` covers reusable starter content under CC0; confirm the target project's license before treating that as its intended license.

## Local references

For an explicitly selected Coolify deployment, use [Coolify deployment adaptation](docs/coolify.md).

Use [Quality baseline](docs/quality.md), [Acquisition sources](docs/sources.md), [Bootstrap records](docs/bootstrap-records.md) and [Acceptance checklist](docs/verification.md). Copy complete skill directories with references and upstream licensing; record exact sources and digests. Missing trusted sources remain incomplete.
