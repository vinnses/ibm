# W046 pre-integration review

Date: 2026-09-24. Reviewer: user-supervised primary session (exact model/effort
not exposed by runtime). This review covers the bounded example and public
routing, not curricular quality or completeness of the underlying research.

## Evidence and data

- The CSV is generated from the distinct 2011 and 2023 formal component
  inventories. It contains 37 and 43 coded rows respectively, with separate
  curriculum IDs, period, code, name, kind, hours and source basis.
- Release metadata records SHA-256 for both inventories, both matrix
  resolutions, additional 2023 creation acts 76–80/22 and the generated CSV.
- The demo excludes 2011 code-free elective spaces and the 2023 elective
  catalogue. Four 2023 TCC codes are explicitly marked as alternatives.
- Public copy asks a descriptive count question and does not make a curricular
  merit, equivalence or actual-offering claim.

## Site and access boundary

- W045 public-document catalogue and file routes remain intact. SvelteKit nav
  gains an analyses link only when the Dash route is deployed.
- The Dash service has no host-published port in Compose and joins only the
  `edge` network. The existing code-server remains solely on `dev`, with its
  existing loopback binding and password; no public router location points to
  it.
- NGINX longest-prefix routing sends only `/analises/` to Dash and all other
  paths to SvelteKit. `proxy_pass` without a URI preserves the path prefix.
  Tailscale Funnel retains one root handler, now targeting the router.

## Checks before merge

- W045 focused validator: 56 published document files and one Dash technical
  source hash verified.
- W046 focused validator: data/source hashes and row grains pass; through the
  isolated HTTP router, Dash root/health/layout/dependencies/CSS, both filter
  callbacks and both filtered CSV downloads pass.
- Local router smoke: `/`, `/documentos`, representative detail/PDF,
  `/curriculos/curriculum-2023`, `/health` and `/analises/health` all returned
  HTTP 200. The original PDF retained `application/pdf`.
- Pinned Node web build completed with Svelte check at zero errors/warnings;
  Dash image built; Compose config parsed; repository validation reported zero
  warnings/errors. Public-origin checks remain the release gate after merge.

## Release gate and rollback

Merge into `main` only after rerunning repository and focused checks. Build
and start Dash/router while leaving the current Funnel handler unchanged;
verify their health and local routed requests. Then recreate Tailscale with
the new root target. If public checks fail, restore the previous root target
`http://web:3000` and recreate only Tailscale; keep the code-server untouched.
Do not claim publication until public HTML, assets/callbacks, CSV download,
documents/PDF and root health all pass.
