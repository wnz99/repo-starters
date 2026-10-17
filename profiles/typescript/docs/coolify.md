---
type: Guide
title: Coolify deployment adaptation
description: Cache, build inputs and shutdown acceptance for explicitly selected Coolify deployments.
---

# Coolify deployment adaptation

Use this policy when adapting a real application for an explicitly selected Coolify deployment. Keep the existing hardware and native framework/tool owners. Record the selected account, application, deployment method and authorized external actions before changing remote settings. A library or browser package does not imply a deployable server.

## Automatic and adapted behavior

On an already configured server, its saved cleanup policy applies automatically to applications using that server. Application defaults below become mandatory when POLISH adapts an explicit cloud selection for Coolify; they require inspection of the real deployment inputs and runtime. Ordinary setup installs local quality tooling only: it cannot make remote deployment calls, provision resources or start containers. Pending cloud selection leaves deployment adaptation pending while local quality setup can proceed. Do not add bootstrap option keys or infer consent from silence.

## Server cache retention

Keep existing disk-threshold cleanup enabled with forced daily purge disabled. Preserve the current threshold, schedule and safety settings; keep volume/network deletion disabled and retained rollback images protected. Do not add a gratuitous prune command to builds or scheduled jobs. Inspect disk usage and cleanup history before changing retention. This is the selected adaptation policy, not a claim about every Coolify installation's defaults. See [Coolify cleanup controls](https://coolify.io/docs/core/infrastructure/servers/automated-docker-cleanup).

## Application build inputs

Enable Docker build caches for routine deployments. Keep custom Compose build commands cache-enabled too; Coolify's generated-build setting does not override their flags. Enable shallow clone and repository preservation where the installed version supports them and the build does not need history. Record unsupported settings and any history-dependent exception rather than inventing API fields. Read the installed version's settings/help before applying changes. See [Coolify advanced settings](https://coolify.io/docs/applications/configuration/advanced).

Derive a complete per-application watch list from its Dockerfile/Compose and build context. Trace every COPY/ADD source, runtime dependency closure, root and member manifests, lockfiles, ignore files, build configuration, entrypoints and packaged assets. Include shared packages actually used by the deployed artifact. Resolve paths against the application's configured base directory and verify the installed Coolify watch-pattern semantics. A top-level directory guess is insufficient. Record each watched input and why it affects this application; identify unrelated paths for negative watch fixtures. Watch paths filter Git-provider events with changed-file information; they do not block manual deployments or authenticated Deploy Webhooks. See [automatic deployments](https://coolify.io/docs/applications/deployments/automatic-deployments). Keep credentials outside the repository and image layers.

## Dependency layers

Copy dependency manifests and lockfiles before source so source edits can reuse external dependency installation. Keep necessary build dependencies in build stages and only required runtime dependencies in the final artifact. Preserve existing tool and dependency pins; do not switch package managers or weaken frozen installation to obtain a faster build. See [Docker cache optimization](https://docs.docker.com/build/cache/optimize/).

For TypeScript, retain the project's existing locked Bun/Node install mode before copying source. For this Bun baseline use `bun install --frozen-lockfile` with the root and required workspace manifests available; preserve a Node-target project's existing lockfile-based install command. Install build tools where the real framework needs them, then package only the deployed runtime closure. Do not invent a universal Dockerfile for a library or browser package. See [Bun locked installation](https://bun.sh/docs/pm/cli/install).

## Graceful shutdown

Run the real entrypoint as PID 1 using exec-form CMD/ENTRYPOINT or an appropriate init. A shell wrapper must forward signals or exec its final process. Handle SIGTERM and SIGINT: stop accepting work, bound drain time, close resources, terminate and reap only owned child processes, then exit before the configured stop grace period. Avoid machine-wide process killing. Use offline fixtures for long-running or external work so shutdown tests cannot invoke paid services. See [Docker signal handling](https://docs.docker.com/reference/build-checks/json-args-recommended/).

## Verification and rollback

Record commands, expected/actual outcomes and sanitized evidence in docs/development.md. Local checks below prove the adapted artifact; remote checks require the selected destination and explicit external-action authorization. Unrun required checks stay pending.

1. Build twice with identical inputs, then make a source-only change. Require an external-dependency-layer cache hit and rebuilt application content. Change a real dependency lock entry consistently with its manifest; require a dependency-layer cache miss. Restore fixtures and rerun the native quality, build and isolated-consumer gates. Logs must distinguish cached dependency work from skipped application builds.
2. Exercise positive watch fixtures for application source, each shared runtime dependency, manifests/lockfiles, Dockerfile/Compose, ignore files and assets. Require deployment selection for each affected application. Exercise negative watch fixtures in unrelated components/docs not packaged by that application; require no deployment selection. Cover rename/delete paths. Use isolated branches or a local selector first; perform live webhook checks only within authorization.
3. Start an owned disposable container offline with the actual PID 1 entrypoint and fixture work. Send SIGTERM and SIGINT in separate runs. Assert bounded exit before the grace deadline, cleanup of owned child processes, and no remaining owned processes. Include in-flight and idle cases, without live inference or production starts/stops.
4. After authorized settings changes, read back cache, clone/repository, watch and server cleanup settings. Compare with the intended values and preserve existing safety controls. Save sanitized before/after values; ordinary setup must leave .bootstrap.json cloud pending and remote settings untouched.
5. Treat application health separately from deployment completion. Check the expected revision, readiness and representative offline-safe behavior after completion. A green deployment status alone does not prove health. No live inference smoke runs without explicit authorization.
6. Before rollout, retain the previous image and recorded application/settings revision. On failed health or acceptance, restore that known-good image and settings using the existing rollback path; confirm health and read back restored settings. Confirm database/schema compatibility before rollback; never erase persistent data or prune rollback artifacts as recovery.
