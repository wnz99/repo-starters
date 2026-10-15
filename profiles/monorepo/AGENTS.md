# Development rules

- Read README.md, docs/index.md and .bootstrap.json before changing the setup. Preserve unrelated edits and existing hook ownership.
- Root owns shared quality policy. Component manifests own runtime/test dependencies. Use the documented native commands; lint/check tasks are read-only. Use explicit format/fix commands for source changes.
- Keep strict types, deterministic Clean Code rules, Deptry, Knip/Fallow, tests, real builds and isolated consumers connected. Never weaken a gate or broadly exclude code to obtain a pass.
- Use Pydantic at Python external-data boundaries. For Python LLM work use PydanticAI with only required provider extras (https://ai.pydantic.dev/install/). For MCP servers use Python FastMCP (https://pypi.org/project/fastmcp/) or the distinct TypeScript FastMCP (https://www.npmjs.com/package/fastmcp); verify the chosen protocol and transport.
- Use the project documentation/review/test-quality/language skills after installing them from trusted sources in POLISH.md. Preserve their licenses; report unavailable sources.
- Keep credentials external and local state ignored. Repository-scoped MCP settings require an explicit selection, external credentials, and removing the local-only ignore for that exact secret-free file.
- Ask before adding branch promotion, merge policy, cloud authentication, Serena, semantic MCP or self-hosted runners. Explain the effect; silence leaves choices pending.
- Keep docs/index.md as canonical navigation; concept docs use YAML type/title/description. Document exact supported runtimes and exceptions.
- Require fresh applicable checks before completion. Test actual behavior and failure paths. Remove code only after tracing its public/dynamic consumers.
- Do not commit, publish, deploy, provision resources, or change account-wide settings without task authorization. No Co-Authored-By trailers or timeline estimates.
