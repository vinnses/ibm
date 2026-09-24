# W046 error log

## E-W046-001 — SSH Git fetch denied during updated-main check

- **Date/time:** 2026-09-24, America/Sao_Paulo.
- **Work / branch:** W046 / `work/w046-publish-dash` preparation.
- **Actor:** Primary agent / Git SSH environment.
- **Operation:** Fetch `origin/main` using the repository's configured SSH remote.
- **Expected result:** Confirm updated `main` before branch creation.
- **Actual result:** `git@github.com: Permission denied (publickey)`; no refs updated.
- **Affected paths/state:** No files or branches changed by failed fetch.
- **Impact:** Configured SSH credential unavailable in this environment; remote synchronization may also be affected.
- **Attempts:** (1) SSH fetch failed. (2) Read-only `git ls-remote https://github.com/vinnses/ibm.git refs/heads/main` returned `743ecb285b3a33fb806687b934afa616ab6cf434`, equal to local `main` and `origin/main`. (3) Created W046 branch from that verified local base.
- **Resolution/status:** Resolved for branch-base verification; remote push capability remains to be tested if needed.
- **Prevention/follow-up:** Keep HTTPS read-only comparison as fallback; do not embed credentials in Git URLs or logs.
- **Evidence:** W046 Git tool outputs and work specification.
