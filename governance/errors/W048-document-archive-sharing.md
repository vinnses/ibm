# W048 error log

## E-W048-001 — Inspection referenced nonexistent paths

- **Date/time:** 2026-09-24, America/Sao_Paulo.
- **Work / branch:** W048 / `work/w048-document-archive-sharing`.
- **Actor:** Primary agent / repository inspection.
- **Operation:** Read route metadata and local governance context from guessed files `site/src/routes/+layout.server.ts` and `governance/AGENTS.md`.
- **Expected result:** Find shared metadata and governance instructions.
- **Actual result:** Both paths do not exist; `sed` returned file-not-found after other requested files were read.
- **Affected paths/state:** No source changed.
- **Impact:** No data or implementation impact; lookup required correction.
- **Attempts:** (1) Inspected actual route-level `<svelte:head>` declarations with targeted `rg`. (2) Re-read the repository's supplied `AGENTS.md` context and required governance files from their actual paths.
- **Resolution/status:** Resolved; shared layout has no route metadata module and governance instructions are at repository root.
- **Prevention/follow-up:** Resolve exact files with `rg --files` before guessing paths.
- **Evidence:** Inspection outputs and subsequent path inventory.

## E-W048-002 — Router retained stale upstream addresses after services were replaced

- **Date/time:** 2026-09-24, America/Sao_Paulo.
- **Work / branch:** W048 / `main` deployment.
- **Actor:** Primary agent / Docker Compose and NGINX runtime.
- **Operation:** Replace the Web and Dash containers with the new builds and request the public pages.
- **Expected result:** Router forwards requests to the newly healthy Web and Dash containers.
- **Actual result:** Web and Dash became healthy on new container IPs, but the long-running router continued using its resolved old IPs; public and local router requests returned HTTP 502 (`connect() failed (111: Connection refused)`). Direct Web returned HTTP 200.
- **Affected paths/state:** Temporary public route outage during W048 rollout; site source and data were intact. The router and Tailscale configurations were unchanged.
- **Impact:** New metadata/archive could not be checked through the public URL until router recovery.
- **Attempts:** (1) Checked direct Web, router, container health and router logs to isolate upstream address mismatch. (2) A normal `docker compose up -d router` did not recreate the unchanged router. (3) Explicitly forced recreation of only the router after confirming Web and Dash were healthy. (4) Public requests then returned current HTML; all production containers were healthy.
- **Resolution/status:** Resolved. Router recovered and public routes returned HTTP 200.
- **Prevention/follow-up:** Recreate the router after replacing upstream Web/Dash containers when the NGINX resolver captures their addresses at startup.
- **Evidence:** W048 deployment command results, router logs, public metadata/archive responses and `docker ps` health status.

## E-W048-003 — Worktree audit helper had invalid JavaScript regex syntax

- **Date/time:** 2026-09-24, America/Sao_Paulo.
- **Work / branch:** W048 integration / `main`.
- **Actor:** Primary agent / tool orchestration.
- **Operation:** Parse `git worktree list --porcelain` and inspect every worktree status from one JavaScript orchestration call.
- **Expected result:** Report only worktrees with tracked or untracked changes.
- **Actual result:** The helper failed at parse time with `SyntaxError: Invalid regular expression flags`; no nested shell commands ran.
- **Affected paths/state:** None; this was an orchestration-script syntax error.
- **Impact:** No Git or file state changed; status audit was briefly delayed.
- **Attempts:** (1) Replaced regex parsing with simple line-prefix/string-split parsing. (2) Read each worktree status successfully; only the active W041 worktree's untracked PDF and a pre-existing W027 `scripts/__pycache__/` were reported.
- **Resolution/status:** Resolved. Both user/worktree items remain untouched and uncommitted.
- **Prevention/follow-up:** Prefer literal string splitting for this small worktree listing instead of escaped nested regexes.
- **Evidence:** Successful status audit output.
