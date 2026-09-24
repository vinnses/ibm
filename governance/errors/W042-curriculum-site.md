# W042 error log

## E-W042-001 — Host npm unavailable

- **Date/time:** 2026-09-23, America/Sao_Paulo.
- **Work / branch:** W042 / `work/w042-curriculum-site`.
- **Actor:** Primary agent / environment.
- **Operation:** `npm ci` in `site/`.
- **Expected result:** Install locked site dependencies for validation.
- **Actual result:** `/usr/bin/bash: line 1: npm: command not found` (exit 127).
- **Affected paths/state:** No tracked files changed; dependencies not installed.
- **Impact:** Host-based check/build unavailable until alternative runtime is used.
- **Attempts:** (1) Checked available tools; Node and Docker are present, npm absent. (2) Docker-based npm validation planned.
- **Resolution/status:** Resolved. The pinned Node Docker image installed dependencies; `npm run check` and `npm run build` passed in that container.
- **Prevention/follow-up:** Use the pinned Node container described by the site Dockerfile on hosts lacking npm.
- **Evidence:** Command output from W042 execution.

## E-W042-002 — Patch rejected

- **Date/time:** 2026-09-23, America/Sao_Paulo.
- **Work / branch:** W042 / `work/w042-curriculum-site`.
- **Actor:** Primary agent / patch tool.
- **Operation:** Replace several Svelte route files in one patch with delete/add pairs.
- **Expected result:** Apply the redesigned route shell.
- **Actual result:** `apply_patch verification failed: invalid patch: multiple operations target .../+layout.svelte`.
- **Affected paths/state:** No files modified by the rejected patch.
- **Impact:** Implementation delayed; no data impact.
- **Attempts:** (1) Rejected combined patch. (2) Retry with separate delete and add operations.
- **Resolution/status:** Resolved. Separate delete and add patches applied; Svelte check and build passed.
- **Prevention/follow-up:** Do not target the same path twice within one patch.
- **Evidence:** Patch tool response from W042 execution.

## E-W042-003 — Repository validator scanned installed dependencies

- **Date/time:** 2026-09-23, America/Sao_Paulo.
- **Work / branch:** W042 / `work/w042-curriculum-site`.
- **Actor:** Primary agent / validator.
- **Operation:** `python scripts/validate_repository.py` after installing site dependencies.
- **Expected result:** Validate tracked repository material.
- **Actual result:** 31 broken Markdown links inside ignored `site/node_modules/` packages; exit 1.
- **Affected paths/state:** No research data affected; validation gate falsely failed on third-party installed files.
- **Impact:** Required a narrow validator exclusion before a meaningful repository check.
- **Attempts:** (1) Inspected the 31 paths and validator traversal. (2) Excluded `node_modules` from CSV and Markdown scans. (3) Rerun pending.
- **Resolution/status:** Resolved. Validator reran with 0 warnings and 0 errors.
- **Prevention/follow-up:** Keep generated dependencies outside repository validation scope.
- **Evidence:** Validator output and script diff in W042.
