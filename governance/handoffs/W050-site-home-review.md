# W050 handoff — site home and presentation review

- Branch: `work/w050-site-home-review`.
- Commit base: `a1ba2d51da7a4c7d3d6a0fbd2b509e9591775483`.
- Work commit: `c4b0662` (site changes, specification, and append-only error log). This handoff is committed separately.
- Primary-session model/effort: active primary Codex runtime; exact model variant and effort not exposed. No historical assignment inferred.
- Actors: primary agent only, orchestrator/implementer/reviewer/integrator, active runtime, effort not exposed; no subagents, reassignments, escalations, or tier mappings.
- Objective/verdict: completed implementation and premerge review; approved for integration. Publication and remote synchronization are integration follow-up, not yet asserted here.
- Deliverables: general homepage and grade chooser; coherent four-item Svelte/Dash menus; simplified Ficha copy; four-card direct-link document archive with source-grounded summaries; general home sharing metadata and year-specific grade metadata.
- Primary files: `site/src/routes/+page.svelte`, `site/src/routes/curriculos/+page.svelte`, `site/src/lib/components/CurriculumView.svelte`, `site/src/routes/documentos/+page.svelte`, `site/src/lib/server/public-documents.ts`, `site/src/routes/+layout.svelte`, `analises/app.py`.
- Sources added: none. Existing preserved resolutions and the 2026 proposal/claim matrix were used to check document summaries and the proposed course name; original evidence files were not changed.
- Coverage: both curriculum pages, home, documents archive, Dash menu and cited formal document links. Four formal document links followed to PDF with HTTP 200 in isolated container testing.
- Validations: Docker Svelte check/build and Dash image build passed; Dash test client returned 200; local HTTP checks returned 200 for home, chooser, both grades, and archive; four archive files returned `application/pdf` and 200 after redirect; `python scripts/validate_repository.py` checked 232 CSV, 132 hashes, and 282 links with zero warnings/errors; `git diff --check` passed.
- Gaps: no new documentary search; existing Ficha applicability gaps remain. No in-browser visual QA requested or performed.
- Divergences: user-supplied proposed course wording differed from the preserved 2026 proposal. Homepage uses the documented name “Inteligência Artificial Aplicada à Saúde” while explicitly describing it as a proposal, not an approved change.
- Provisional information: future course, labor-market, and research analyses and manifesto are marked as future scope on the homepage; not represented as current outputs.
- Explicitly unperformed: no new source collection, proposal evaluation, or curriculum comparison.
- Error log: `governance/errors/W050-site-home-review.md`; E-W050-001 through E-W050-006 resolved; open events none before integration.
- Human review: none newly required. Existing GitHub push-protection clearance remains an external gate; if still active, remote sync must be reported as incomplete.
- Recommended next bounded work: none automatically. User-directed data/analysis expansion can be specified separately.

## Integration record

Pending merge, publication, public HTTP verification, and non-forced GitHub sync attempt by the primary session.
