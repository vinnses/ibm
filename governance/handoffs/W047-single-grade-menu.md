# W047 handoff — single curriculum navigation item

- **Branch:** `work/w047-single-grade-menu`.
- **Commit base:** `954abe16ef261310b091ba20d4302a63dbbc6d2e`.
- **Commits produced:** `2d92d1f` (implementation and work records); integration merge commit recorded after integration.
- **Primary-session model and effort:** Unknown / unknown; not exposed by runtime.
- **Actors and routing:** One primary agent, implementation/integration/release; model and effort unknown / unknown. No subagents. No reassignment, escalation, equivalent-tier mapping or routing deviation.
- **Objective and verdict:** Replace duplicate global links to the 2011 and 2023 curriculum views with a single “Grades” link to `/`; keep the existing year tabs. Complete if integrated and deployed.
- **Deliverables:** `site/src/routes/+layout.svelte` and W047 governance records.
- **Sources:** No external or documentary research sources; this is a navigation-only change.
- **Coverage:** The global nav has one grade entry; root page's existing view has links for both 2011 and 2023.
- **Validations:** `python scripts/validate_repository.py` passed (231 CSVs, 132 hashes, 282 links; zero warnings/errors); inspected global navigation and year selector. Build and public page check remain release steps.
- **Gaps/divergences/provisional information:** None anticipated. Root page defaults to 2023; direct year routes remain available.
- **Explicitly unperformed:** No change to curriculum data, content, Dash, equivalence clues, other menu items or research conclusions.
- **Error log:** `governance/errors/W047-single-grade-menu.md`; no events recorded.
- **Human review:** None; no human-review file or gate consequence.
- **Integration:** Pending integration; update global index and record merge SHA.
- **Remote sync:** GitHub synchronization remains subject to the W046 authentication exception E-W046-011.
- **Next bounded work:** None recommended by this small UI adjustment.
