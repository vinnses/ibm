# W050 — Site home and presentation review

- Objective: make the agreed general homepage and sharing metadata live, remove redundant Ficha notices, simplify document access, and align navigation across Svelte and Dash.
- Branch: `work/w050-site-home-review`.
- Commit base: `a1ba2d51da7a4c7d3d6a0fbd2b509e9591775483` (`main`).
- Primary-session assignment: active primary Codex session; exact model variant and effort are not exposed by this runtime. No historical model assignment is inferred.
- Agent assignments: primary agent, orchestrator/reviewer/implementer/integrator, active primary runtime, effort not exposed, actual; cross-route review and integration remain with the user-supervised primary. No subagents assigned.
- Escalation: Sol subagents are prohibited. Any Sol-requiring work returns to the primary session; no delegation is planned.
- Inputs: existing SvelteKit site, Dash app, preserved curriculum/document model, W047–W049 handoffs, and the user's approved Portuguese copy and UI requests. No new external research source is needed.
- In scope: homepage, metadata, menus, Ficha card/detail copy, public document archive cards and direct file links, Dash navigation/source links, focused review, validation, publication, and non-forced remote sync attempt.
- Out of scope: documentary reconstruction, new comparative claims, new analytics datasets, removal of preserved source documents, and unrelated routes.
- Deliverables: updated `site/src/` and `analises/app.py`; this specification, `governance/errors/W050-site-home-review.md`, and `governance/handoffs/W050-site-home-review.md`.
- Method: edit only presentation/navigation using existing evidence; preserve source files and evidence caveats; review all affected routes and file links; validate before integration.
- Acceptance: agreed title and description in home head/OG; home is a general index; both grades reachable; positive Ficha location labels removed while missing labels remain; archive shows only four relevant formal documents with accurate summaries and direct files; no methodology menu or explanatory 'how to read' block; Dash menu includes Análises; Svelte and Dash build/check; repository validator passes; deployed routes work.
- Risks: historical Ficha applicability remains unresolved; GitHub push protection may still reject a preserved public-page token from W044. Do not alter that source or force push.
- Validation: `npm run check`, `npm run build`, Dash Python import/health and link checks, `python scripts/validate_repository.py`, Docker health and public HTTP checks.
- Error log: `governance/errors/W050-site-home-review.md`.
- Human review: none anticipated for this presentation-only work. Existing GitHub false-positive clearance remains an external gate if push protection persists.
