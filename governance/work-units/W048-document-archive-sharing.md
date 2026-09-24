# W048 — Streamline the document archive and share metadata

- **Objective:** Remove Ficha 1/Ficha 2 records from the general document archive while retaining their grade-page links, and improve page titles/descriptions/Open Graph metadata for link previews.
- **Branch:** `work/w048-document-archive-sharing`.
- **Commit base:** `ee6bbf77b376732dcdc6f53a8c60b3ebd565ca59`.
- **Primary-session assignment:** Exact model/effort not exposed by runtime; `unknown / unknown`, not inferred.
- **Agent assignments:** One primary session; site editor, integrator and release operator; model/effort unknown / unknown; actual. No subagents. Routing rationale: contained Svelte metadata and archive-filter changes plus integration.
- **Escalation rule:** No delegation; Sol subagents prohibited; any Sol-requiring task returns to primary.
- **Inputs:** `site/src/routes/documentos/+page.server.ts`, document archive page, route-level `<svelte:head>` metadata, Dash app metadata, existing Docker/Tailscale deployment.
- **In scope:** Exclude Ficha 1/2 from archive listing and its type filter; update archive explanatory copy; give the home, methodology, curriculum detail, document archive/detail, and Dash pages useful titles, descriptions and Open Graph text for sharing; build, integrate and deploy.
- **Out of scope:** Deleting or hiding source PDFs from curriculum records, content/data changes, new social image creation, research collection or curricular interpretation.
- **Deliverables:** Updated archive query/page metadata, route-level metadata and Dash metadata; this spec, per-work error log and handoff.
- **Method:** Filter only archive list records by public display type; preserve existing per-discipline Ficha 1 links and direct file routes. Put route-specific title/description and Open Graph tags in each route's head; keep wording concise and factual.
- **Acceptance criteria:** Archive no longer contains Ficha 1 or Ficha 2 types; grades continue linking available fichas; home/share tags describe the course and two grades; route previews have route-specific text; deployment is healthy.
- **Risks and uncertainty:** Link-preview services may cache older previews. No social-preview image currently exists; creation is outside this request.
- **Validation:** Svelte check/build, repository validator before merge, public HTML metadata and archive pages, service health after deployment.
- **Error log:** `governance/errors/W048-document-archive-sharing.md`.
- **Human review:** None anticipated.
