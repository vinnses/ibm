# W047 — Simplify the grade navigation

- **Objective:** Replace the two curriculum links in the global menu with one “Grades” link to the grade page, leaving the 2011/2023 selector within that page.
- **Branch:** `work/w047-single-grade-menu`.
- **Commit base:** `954abe16ef261310b091ba20d4302a63dbbc6d2e`.
- **Primary-session assignment:** Exact model and effort are not exposed by runtime; `unknown / unknown`, not inferred.
- **Agent assignments:** Primary session only; implementer, integrator and release operator; model/effort unknown / unknown; actual. No subagents. Routing rationale: one-file navigation change with existing selector.
- **Escalation rule:** No delegation. Sol subagents prohibited; Sol-requiring work stays with the primary session.
- **Inputs:** `site/src/routes/+layout.svelte`, `site/src/lib/components/CurriculumView.svelte`, existing W046 deployed site.
- **In scope:** Consolidate the global menu curriculum entries while retaining year selection inside the curriculum view; build/release this small UI change.
- **Out of scope:** Changes to curriculum data, page content, Dash, other navigation items or documentary interpretation.
- **Deliverables:** Updated site layout, work spec, error log and handoff.
- **Method:** Link “Grades” to `/`, whose existing curriculum view defaults to 2023 and contains 2011/2023 tabs.
- **Acceptance criteria:** Global nav contains one grade link; the grade view still exposes both years; deployed page responds with the new nav.
- **Risks and uncertainty:** The root page defaults to 2023; direct curriculum URLs remain available and year tabs remain the in-page selector.
- **Validation:** Build and public route check after deployment; inspect the nav source for a single grade entry.
- **Error log:** `governance/errors/W047-single-grade-menu.md`.
- **Human review:** None anticipated.
