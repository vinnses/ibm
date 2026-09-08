# W034 — Historical visualization and review UI handoff

- Branch: `work/w034-historical-visual-review`.
- Commit base: `64c0c0aade2f764ebef7a552610fd925d6a992bf`, fetched and synchronized between local `main` and `origin/main` before branch creation.
- Commits produced before the closure commit:
  - `01876ea` — define the W034 work unit;
  - `e1af6ae` — add the interactive 2011–2023 curriculum map;
  - `77acc58` — establish the editorial identity and evidence-first review pages;
  - `eed48b5` — document and validate historical review interactions;
  - `e72b9d3` — restore W031 identity invariants and normalize audit metadata.
- Primary-session model and effort: GPT-5 family as exposed by the active runtime; exact backend model and reasoning effort were not exposed and remain `unknown`, not inferred.
- Agent assignments actually used: primary session only, as detailed below.

| Actor | Primary/subagent | Functional role | Model | Effort | Routing rationale |
|---|---|---|---|---|---|
| primary | primary | orchestration, interaction and visual-system design, Svelte implementation, sample audit, security validation, acceptance review, and handoff | GPT-5 family; exact backend unknown | unknown | Cross-cutting UI integration and final audit remained under primary-session authority. |

- Reassignments, escalations, equivalent-tier mappings, and routing deviations: none. No subagent and no Sol subagent were created.
- Objective and completion verdict: W032/W033 are transformed into an evidence-first, responsive historical review interface with a first militant editorial identity. **W034 complete with accepted browser-availability exception E-W034-005.**

## Deliverables and routes

- New `/mapa-curricular`: periodized 2011/2023 explorer, selection, topic tracking, comparison, candidate review, coverage states, filters, mobile year switch, and evidence access.
- New `/metodologia`: public explanation of documentary/analytical separation, state grammar, preservation, and limits.
- Changed `/`: editorial investigation entry, historical call to action, explicit gaps, method access, and explicit 2026 boundary.
- Changed `/curriculos/[id]`: derived document coverage and map access.
- Changed `/disciplinas/[id]`: document state, topic excerpts, candidate counterparts, relations, dependencies, evidence, and map deep link.
- Changed `/conteudos` and `/conteudos/[id]`: map access and 2011/2023 occurrence comparison with aliases, applicability, excerpts, states, and evidence.
- Changed `/evidencias/[id]`: title, type, institution, date, SHA-256, URL, applicability, locator/excerpt, and preserved-file access near numeric PDF pages.
- Preserved `/curriculos`, `/documentos/[id]`, and `/documentos/[id]/arquivo`; all required W032 route families remain functional.

Primary components are `CoverageBadge.svelte`, `VisualLegend.svelte`, the
extended `EvidenceList.svelte`, and the server-only `review.ts` view-model
adapter. No graphics library was adopted: Svelte/CSS provide the current
periodized layout and 12-candidate interactions without a new dependency.

## Visual grammar, filters, and mobile

- Change type: textual label plus solid (`maintained`), double/intervention (`fragmented`/`merged`), or dashed (`indeterminate`) edge pattern.
- Evidence strength: independent textual `StatusBadge`; line weight/opacity is documented but never substitutes for its label.
- Review: independent badge; `proposed` reads “Proposto — não revisado” and means an inspectable analytical hypothesis.
- Document coverage: `●` sufficient, `○` not located, `◐` applicability indeterminate, `×` contradictory, `?` indeterminate, each with text and accessible detail.
- Filters: curriculum, period, domain, discipline, review state, evidence strength, document availability, topics in both curricula, proposed-only, and indeterminate-only.
- Mobile: ≤700 px shows one legible curriculum column at a time through a labelled 2011/2023 switch; panels and comparisons become one column. Desktop keeps both curricula visible.

## Evidence, gaps, and future ingestion

All selected components, occurrences, and relations offer “Ver evidência”
links. Evidence pages open the allowlisted preserved file and append a PDF page
fragment when the locator is numeric. Runtime download bytes matched the
recorded SHA-256.

Current derived coverage is 53 `not_located` and 31
`applicability_indeterminate` components. The grammar also supports future
`sufficient`, `contradictory`, and generic `indeterminate` records, but W034
does not fabricate examples absent from the current model. The ingestion flow
is documented as preservation/hash → Evidence → TopicOccurrence → deterministic
taxonomy rebuild → UI rebuild, with no code/date-only applicability inference.

## Inspection findings and corrections

The required maintained, fragmented, merged, new, indeterminate,
missing-Ficha, and applicability-indeterminate samples were inspected through
the running site's selected-component routes. No W033 data error was found and
no W033 analytical record was changed. One W034-created W031 regression—the
homepage's exact institutional identity string—was found by the baseline
validator and corrected (E-W034-008).

## Validation

- W033 corpus, taxonomy, and W032 downstream builders in `--check`: deterministic and current.
- W031: 16 preserved sources; Compose/application/secret checks; zero errors.
- W032: 84 components, 54 dependencies, 56 documents, 18 domains, 156 topics, 242 occurrences, 12 relations, 246 evidence records, and 658 links; negative invariants passed.
- W033: 52 corpus sources, 260 proposals, 242 occurrences, 3 aliases, and 12 relations; provenance/uncertainty passed.
- W034: filters/state/mobile/source assertions; all required sample classes; live routes; preserved SHA-256; invalid IDs and encoded traversal returned 404.
- Docker production build: Svelte check 0 errors/0 warnings, adapter-node build passed, production audit 0 vulnerabilities.
- Runtime health and all route families: HTTP 200; sample and deep-link routes rendered expected caveats/states.
- Repository: 223 CSVs, 126 preserved hashes, 277 local Markdown links, zero warnings/errors.
- Governance: 27 logs, 171 events before closure, 4 human-review files, routing metadata valid, zero errors.
- Compose config, Git LFS fsck, `git diff --check`, and contrast checks: pass.
- Visual inspection limitation: in-app browser selection and prescribed troubleshooting found zero browser instances. Pixel/screenshot desktop and mobile inspection was not performed; responsive behavior is supported by zero-warning compilation, explicit breakpoint/source checks, and runtime DOM output only.

## Limits, exclusions, and audit closure

- Sources added: none; W034 uses the existing preserved W032/W033 evidence graph.
- Provisional information: all 18 domains, 156 topics, 242 occurrences, and 12 lineage candidates remain proposed; all occurrence/relation strength remains indeterminate.
- Gaps/divergences: uneven 2011/2023 coverage and applicability limits remain unchanged; no contradiction or sufficient-content component currently appears in the derived display distribution.
- Explicitly unperformed: 2026 proposal analysis, 2023→2026 comparison, final manifesto, public campaign, full political argument, Ficha ingestion, institutional request, complete review of 156 topics, taxonomy reconstruction, W033 data revision, screenshot capture, merge, deployment/publication, global-index update, W035, or any later Work.
- Error log: `governance/errors/W034.md`.
- Resolved events: E-W034-001 through E-W034-004 and E-W034-006 through E-W034-010.
- Accepted exception: E-W034-005 (no browser instance for rendered visual QA).
- Open event IDs: none.
- Human-review question path and gate consequence: no W034 human-review file; existing documentary applicability/access questions remain visible nonblocking gaps.
- Recommended next bounded work unit: a browser-based visual QA correction pass may close E-W034-005 when a browser is available; do not start it automatically. W035 and 2026 analysis remain unauthorized.

## Editorial/data balance

The militant identity is perceptible through poster scale, paper texture,
black rules, red intervention, stamps, highlights, and annotated-document
language. Data remain legible because documentary panels use neutral surfaces,
plain typography, spacing, textual state labels, and direct evidence access.
If candidate volume grows, a later Work should reassess relation overview and
line routing; no heavier graph layer is warranted now.

HISTORICAL REVIEW UI READY — 2011–2023 content lineage is visually explorable and evidence-accessible.

## Integration update — 2026-09-08

- Merged branch: `work/w034-historical-visual-review` into local `main` after explicit user authorization.
- Merge commit: `b3bbf0001a6c2afe9c42d47b84d33f50220f632e` (`Merge W034 historical visual review`).
- Conflict resolution: none; the `ort` merge completed cleanly.
- Global indexes updated: none; W034 did not add documentary sources or authorize a global-index milestone.
- Post-merge validation: W031/W032/W033/W034, deterministic builders, runtime routes, preserved-file hash, invalid IDs, traversal, repository, governance, Compose configuration/build, Git LFS, and diff checks passed.
- Local service update: `ibm-web:dev` was rebuilt, the web container was force-recreated after E-W034-011 detected a same-tag stale container, exact image IDs matched, and `/health`, `/`, `/mapa-curricular`, and `/metodologia` passed. The Tailscale service remained healthy.
- Remote synchronization state: `main` through integration record `790459a` was pushed successfully to `origin/main`; the final publication-record commit follows this verified push.
- Public verification: Tailscale Funnel reported `https://ibm.tail6629d6.ts.net` proxying `/` to `http://web:3000`; external HTTPS checks for `/health`, `/`, and `/mapa-curricular` returned the expected updated W034 content.
