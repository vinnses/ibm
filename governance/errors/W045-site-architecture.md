# W045 error log

No agent, tool, validation, review, source-access, Git, environment or orchestration errors recorded at work start. Append events; do not erase failed attempts after recovery.

## E-W045-001 — Combined patch rejected

- **Date/time:** 2026-09-24, America/Sao_Paulo.
- **Work / branch:** W045 / `work/w045-site-architecture`.
- **Actor:** Primary agent / patch tool.
- **Operation:** Add the document catalogue and replace the existing detail route in one patch.
- **Expected result:** New and updated SvelteKit source files.
- **Actual result:** Patch rejected with `multiple operations target .../+page.server.ts` because delete and add targeted the same path.
- **Affected paths/state:** No route file changed by the failed patch; architecture document already present.
- **Impact:** Brief implementation delay; no public service or evidence affected.
- **Attempts:** (1) Combined patch rejected. (2) Reapply as separate add and update patches, then run Svelte checks.
- **Resolution/status:** Recovery pending in subsequent patch.
- **Prevention/follow-up:** Use `Update File` when replacing an existing path.
- **Evidence:** W045 patch tool output and subsequent validation.

## E-W045-002 — Host npm unavailable in new worktree

- **Date/time:** 2026-09-24, America/Sao_Paulo.
- **Work / branch:** W045 / `work/w045-site-architecture`.
- **Actor:** Primary agent / host environment.
- **Operation:** Run `npm run check` in the new site worktree.
- **Expected result:** Svelte type/markup validation.
- **Actual result:** `npm: command not found` (exit 127); the new worktree also had no `node_modules`.
- **Affected paths/state:** No repository files changed by the failed command; public service unchanged.
- **Impact:** Host cannot validate this checkout directly.
- **Attempts:** (1) Host npm failed. (2) Inspected the existing pinned Node Dockerfile and locally cached Node image. (3) Run the check/build in an isolated container using the worktree as input.
- **Resolution/status:** Recovery pending container validation.
- **Prevention/follow-up:** Use the project's containerized Node toolchain for worktrees without host npm.
- **Evidence:** Host command output and `site/Dockerfile`.

### Resolution update for E-W045-001 and E-W045-002

- **Attempts continued:** Reapplied route files using separate add/update operations. Built the site with its pinned Node Docker image; `svelte-check` reported zero errors and zero warnings, and the production build passed.
- **Resolution/status:** Both resolved. The public service remained unchanged.
- **Verification:** `docker build -t ibm-web:w045-check site`, W045 local route checks.

## E-W045-003 — Local preview restart raced container removal and startup

- **Date/time:** 2026-09-24, America/Sao_Paulo.
- **Work / branch:** W045 / `work/w045-site-architecture`.
- **Actor:** Primary agent / Docker preview environment.
- **Operation:** Restart the isolated preview container after a final date-format change and smoke-test routes.
- **Expected result:** The previous `--rm` container exits and is removed before a new same-name container starts, then HTTP responds immediately.
- **Actual result:** First restart returned a container-name conflict during asynchronous removal; the next immediate HTTP request returned `curl: (56) Recv failure: Connection reset by peer` while the new server was starting.
- **Affected paths/state:** Only temporary local preview container; production `ibm-web-1` and Funnel were untouched.
- **Impact:** Brief validation delay; no source or published site change.
- **Attempts:** (1) Inspected the previous container and found it already removed. (2) Started the new preview. (3) Waited for its `Listening` log; catalogue, document detail and original PDF then each returned HTTP 200. (4) Stopped and removed the isolated preview.
- **Resolution/status:** Resolved.
- **Prevention/follow-up:** Wait for container removal and readiness before issuing preview HTTP requests.
- **Evidence:** W045 Docker/curl tool outputs.
