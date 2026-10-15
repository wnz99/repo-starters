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
2. Rename packages/imports, component paths, exports, .bootstrap.json, Nx projects/tags and the small smoke fixtures consistently. Keep only real components. Update lockfiles and consumer records intentionally after changes.
3. Preserve the full applicable quality toolset. Add project/framework tools and meaningful tests where the project needs them. Adapt TypeScript configs, emitted artifacts and consumer test runners to Bun/Node/browser. Pydantic stays the Python boundary choice; use PydanticAI for Python LLM work and FastMCP for MCP work. Keep credentials external.
4. Install applicable skills from the sources below into .agents/skills, preserving references and licenses. Record source commits/digests and client discovery. Missing sources remain incomplete; do not invent them.
5. Explain and ask about each unanswered option: branch promotion (extra integration/staging/production branches and promotion PRs); merge policy (merge/squash/rebase plus cleanup choices); cloud authentication (provider/account/credential method and local/CI scope); Serena (symbol navigation MCP); semantic Clean Code MCP (advisory pattern lookup); self-hosted runners (machine maintenance, access and job isolation). Record include/exclude/pending and needed details. Pending choices generate no settings. Included unavailable integrations remain incomplete.
6. Run setup, native full checks, builds and isolated consumers. Show a deliberate behavior or lint defect fails in a disposable copy, then restore and rerun. Verify affected/cache behavior for the actual monorepo graph, OS support and safe repeated setup. Preserve local edits; never overwrite generated files blindly. Record results and unrun gates in docs/development.md.
7. Update README, AGENTS and the OKF docs index. Report changes, tool versions, optional choices and fresh verification. Publish or provision only within supplied authorization.
```

The starter contains working baseline files; project choices and optional integrations are deliberately left to this pass. `LICENSE` covers reusable starter content under CC0; confirm the target project's license before treating that as its intended license.

## Acquisition sources

Tool pins are in the manifests and lockfiles. Installation/source links for every package and optional integration: https://llms.wnz.sh/docs/quality-baseline-v1 . Runtime installation: [uv](https://docs.astral.sh/uv/getting-started/installation/), [Python](https://www.python.org/downloads/), [Bun](https://bun.sh/docs/installation), [Node](https://nodejs.org/en/download), [Git](https://git-scm.com/downloads).

Skills (copy the complete linked directory and upstream licensing):

- [wnz-doc-write-expert](https://github.com/wnz99/llm-dev-skills/tree/1e6b0d8cc149ee26729319bc109414ca7d77145b/skills/wnz-doc-write-expert)
- [wnz-code-reviewer](https://github.com/wnz99/llm-dev-skills/tree/1e6b0d8cc149ee26729319bc109414ca7d77145b/skills/wnz-code-reviewer)
- [wnz-test-quality](https://github.com/wnz99/llm-dev-skills/tree/1e6b0d8cc149ee26729319bc109414ca7d77145b/skills/wnz-test-quality)
- [wnz-clean-code-py](https://github.com/wnz99/llm-dev-skills/tree/1e6b0d8cc149ee26729319bc109414ca7d77145b/skills/wnz-clean-code-py)
- [wnz-clean-code-js](https://github.com/wnz99/llm-dev-skills/tree/1e6b0d8cc149ee26729319bc109414ca7d77145b/skills/wnz-clean-code-js)
- [clean-code-tools](https://github.com/wnz99/clean-code-tools/tree/c51c7aa0a9ad555f81e8096e4a7e1c83f9156c1a/skills/clean-code-tools)
- `verify-before-complete`: require a supplied trusted installed copy or source URL; no verified public source in the pinned trees.
