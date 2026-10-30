---
type: Guide
title: Shared Serena configuration
description: Standard serena-shared setup and verification for optional Serena integration.
---

# Shared Serena configuration

When Serena is selected, use [serena-shared](https://github.com/wnz99/serena-shared) as the standard configuration. Serena remains optional; confirm the client, source revisions and repository/user registration scope before installation. Follow the upstream README for installation. The wrapper supports macOS and Linux and requires Serena 2.x installed as a regular command launcher. An unsupported platform or missing prerequisite leaves this integration incomplete.

## Configure the client

Record Serena's version and the immutable serena-shared source revision in the Serena option details in `.bootstrap.json`. Use `serena-shared` as the MCP command, with `start-mcp-server`, the appropriate client context (`--context=codex` or `--context=claude-code`), and `--project-from-cwd`. Preserve compatible existing arguments and the selected scope; user-wide settings require authorization. Keep credentials external and local state ignored. Restart affected sessions after changing registration.

The wrapper shares a server between compatible sessions in the same repository and client context. Git worktrees remain separate. Point a pinned Serena installation through `SERENA_SHARED_SERENA` at its regular launcher when needed. Do not replace this with a per-session `uvx --from git+...` invocation, which does not use sharing.

## Verify

Verify client discovery and a real symbol-navigation call. Open two sessions in the same repository and context, then inspect the wrapper's state directory (normally `~/.local/state/serena-shared/`, or the configured override). Confirm both use one running `server.json` entry. Different client contexts or worktrees get separate entries. Check MCP logs for private-server fallback: a successful tool call alone does not prove sharing.

Record the source revisions, registration scope, commands, actual results and unrun checks in `docs/development.md`. Do not report integration complete when discovery, tool calls or sharing verification remain unrun.
