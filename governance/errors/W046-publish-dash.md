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

## E-W046-002 — Host Python lacks pip for package-version inspection

- **Date/time:** 2026-09-24, America/Sao_Paulo.
- **Work / branch:** W046 / `work/w046-publish-dash`.
- **Actor:** Primary agent / host Python environment.
- **Operation:** Inspect available Dash, Gunicorn and pandas versions with `python -m pip index versions`.
- **Expected result:** Version list for reproducible Dash service dependencies.
- **Actual result:** `/usr/bin/python: No module named pip` for all three queries.
- **Affected paths/state:** No repository files or running services changed.
- **Impact:** Brief dependency-selection delay; no data or deployment impact.
- **Attempts:** (1) Host pip lookup failed. (2) Queried the public PyPI JSON metadata endpoints through HTTPS and confirmed Dash 4.4.1, Gunicorn 26.2.0 and pandas 3.0.6 as available. (3) Use a containerized Python build for installation/tests.
- **Resolution/status:** Resolved for version selection.
- **Prevention/follow-up:** Do not assume pip is installed in the host Python; use the pinned build container or isolated environment.
- **Evidence:** W046 package-metadata and host command outputs.

## E-W046-003 — Overly narrow 2023 formal-basis assertion

- **Date/time:** 2026-09-24, America/Sao_Paulo.
- **Work / branch:** W046 / `work/w046-publish-dash`.
- **Actor:** Primary agent / data generator.
- **Operation:** Generate the demo CSV from formal component inventories.
- **Expected result:** All 37 (2011) and 43 (2023) coded component rows with formal basis retained.
- **Actual result:** Initial assertion required the literal `Resolução 75/22-CEPE`; 14 of the 2023 rows instead state joint bases such as `Resoluções 75/22 e 80/22-CEPE`, so generation stopped before output.
- **Affected paths/state:** No output CSV/release was produced on failed run; original inventories unchanged.
- **Impact:** The first parser would have obscured source-specific creation acts if relaxed without review.
- **Attempts:** (1) Printed all distinct 2023 `formal_basis` strings and counts. (2) Confirmed 75/22 appears in every row, with five preserved additional 76–80 acts. (3) Retained literal per-row formal basis and listed all five additional-act hashes in release metadata; rerun and validate generation.
- **Resolution/status:** Recovery pending data regeneration.
- **Prevention/follow-up:** Preserve multi-act basis strings rather than requiring one spelling or silently reducing to the matrix resolution.
- **Evidence:** `curriculos/2023/inventario/componentes.csv`, formal source manifest and W046 generator run.

### Resolution update for E-W046-003

- **Attempts continued:** Regenerated 80 rows (37 for 2011, 43 for 2023); output retains each formal-basis string, lists hashes for Resoluções 76–80/22, and records the four TCC alternatives separately.
- **Resolution/status:** Resolved.
- **Verification:** `analises/data/formal_components.csv`, `analises/data/release.json`, focused W046 validation.

## E-W046-004 — Gunicorn control socket lacked a writable home

- **Date/time:** 2026-09-24, America/Sao_Paulo.
- **Work / branch:** W046 / `work/w046-publish-dash`.
- **Actor:** Primary agent / Dash preview runtime.
- **Operation:** Start the non-root Gunicorn Dash container and inspect health.
- **Expected result:** Clean production-server startup and responsive prefixed routes.
- **Actual result:** Routes returned HTTP 200, but Gunicorn logged `Control server error: [Errno 13] Permission denied: '/home/app'` because its default control socket targeted a nonexistent non-root home directory.
- **Affected paths/state:** Temporary Dash preview only; no public service or source data changed.
- **Impact:** Background control socket feature unavailable; request serving was functional, but a clean runtime is required before deployment.
- **Attempts:** (1) Inspected Gunicorn help/default `--control-socket` path and container identity/home. (2) Added the supported `--no-control-socket` option; rebuild and confirm startup without this error.
- **Resolution/status:** Recovery pending rebuild.
- **Prevention/follow-up:** Explicitly disable unused control socket in immutable non-root containers.
- **Evidence:** W046 preview logs and Dockerfile.

## E-W046-005 — Chart callback validator assumed JSON number array

- **Date/time:** 2026-09-24, America/Sao_Paulo.
- **Work / branch:** W046 / `work/w046-publish-dash`.
- **Actor:** Primary agent / HTTP validator.
- **Operation:** Validate Dash's chart callback for the 2011 filter.
- **Expected result:** Sum eight numeric `y` values to 37.
- **Actual result:** Dash/Plotly serialized the chart's pandas-derived numeric series as a typed-array object (`dtype=i1`, base64 `bdata`); `sum` over the dictionary raised a `TypeError`.
- **Affected paths/state:** Validator only; Dash callback itself returned HTTP 200 and a valid figure.
- **Impact:** False validation failure, no published or source-data impact.
- **Attempts:** (1) Printed the callback's figure data. (2) Updated validator to decode the documented wire representation when present and sum the eight values. (3) Rerun callback and CSV-download checks.
- **Resolution/status:** Recovery pending rerun.
- **Prevention/follow-up:** Validate Plotly's JSON serialization variants rather than assuming a plain list.
- **Evidence:** W046 local callback response and validator.

### Resolution update for E-W046-004 and E-W046-005

- **Attempts continued:** Rebuilt the Dash image with `--no-control-socket`; startup logs were clean. The prefixed root, health, layout, dependencies and CSS returned HTTP 200. The revised validator decoded Plotly's typed-array value and confirmed the 2011 filter yields 37 records; the CSV callback downloaded exactly those 37 records.
- **Resolution/status:** Both resolved.
- **Verification:** `python scripts/validate_w046_dashboard.py --base-url http://127.0.0.1:5186` passed.

## E-W046-006 — Incorrect preserved Tailscale source filename

- **Date/time:** 2026-09-24, America/Sao_Paulo.
- **Work / branch:** W046 / `work/w046-publish-dash`.
- **Actor:** Primary agent / source inspection.
- **Operation:** Inspect preserved Tailscale proxy-path handling before choosing deployment routing.
- **Expected result:** Find whether a mounted path is stripped before proxying.
- **Actual result:** Initial `rg` targeted nonexistent `tailscale-v1.102.3-serve.go.source` and reported a file error.
- **Affected paths/state:** No source or service changed.
- **Impact:** Brief inspection delay. Choosing Tailscale's path handler without checking would have broken Dash's prefix.
- **Attempts:** (1) Listed preserved source filenames. (2) Read `tailscale-v1.102.3-ipnlocal-serve.go.source` and found `http.StripPrefix` for non-root mounts. (3) Chose a same-origin NGINX router behind Tailscale's root mount, then validated Dash assets/callbacks through it.
- **Resolution/status:** Resolved.
- **Prevention/follow-up:** Resolve file paths from the local source catalog before targeted search.
- **Evidence:** W046 source-inspection output, NGINX config and local routed callback tests.

## E-W046-007 — Production-status formatting command failed

- **Date/time:** 2026-09-24, America/Sao_Paulo.
- **Work / branch:** W046 / `work/w046-publish-dash` integration.
- **Actor:** Primary agent / shell diagnostic.
- **Operation:** Format `docker compose ps --format json` through a short Python one-liner while checking pre-cutover state.
- **Expected result:** Concise service status.
- **Actual result:** The f-string quoting in the command raised `SyntaxError`; the preceding read-only Funnel status and Compose config checks had succeeded.
- **Affected paths/state:** None; no running service changed.
- **Impact:** Diagnostic display only.
- **Attempts:** (1) Failed custom formatter. (2) Reran plain `docker compose ps`, which displayed all services and ports correctly.
- **Resolution/status:** Resolved.
- **Prevention/follow-up:** Prefer plain Compose output over shell-embedded formatters for small status checks.
- **Evidence:** W046 tool output.

## E-W046-008 — Router restart loop under dropped CHOWN capability

- **Date/time:** 2026-09-24, America/Sao_Paulo.
- **Work / branch:** W046 / `work/w046-publish-dash` staged deployment.
- **Actor:** Primary agent / NGINX container runtime.
- **Operation:** Start Dash and internal router before switching public Funnel.
- **Expected result:** Both healthy while public traffic remains on old web target.
- **Actual result:** Dash became healthy; router entered a restart loop with `chown("/var/cache/nginx/client_temp", 101) failed (1: Operation not permitted)` because root NGINX attempted ownership changes after all capabilities were dropped.
- **Affected paths/state:** Only new `ibm-router-1`; public Funnel still pointed directly to healthy `ibm-web-1`, and code-server was unchanged.
- **Impact:** Public cutover halted until router startup is corrected; no public outage.
- **Attempts:** (1) HTTP validation failed with connection refused. (2) Inspected Compose status and router logs. (3) Changed router to run as NGINX UID/GID 101 with writable tmpfs, avoiding startup chown; rebuild/recreate and revalidate before cutover.
- **Resolution/status:** Recovery pending router retest.
- **Prevention/follow-up:** Test the exact non-root and capability profile in isolated preview, not just read-only behavior.
- **Evidence:** Production Compose status/logs and amended Compose file.
