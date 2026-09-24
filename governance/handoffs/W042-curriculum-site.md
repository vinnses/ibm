# W042 handoff — two-curriculum public site

- **Branch:** `work/w042-curriculum-site`.
- **Commit base:** `fdada2dd65aed5e6a24dd496c122ad2af7101af6` (updated `main`).
- **Commits produced:** `27d3943` (site redesign); this handoff commit follows separately.
- **Primary-session model and effort actually used:** Not exposed by the runtime; `unknown / unknown`, not inferred.
- **Agents:** Primary agent only; primary; orchestration, implementation, data mapping, and final audit; model/effort `unknown / unknown`; actual. Routing rationale: integrated site and documentary-state changes. No subagents.
- **Reassignments, escalations, mappings, deviations:** None. Sol subagents were not created.
- **Objective and verdict:** Completed the bounded redesign: the public site now opens on the 2023 grade and provides a matching 2011 view, component cards, source-linked Ficha 1 states, and cautious cross-grade navigation. No main integration or deployment was attempted.
- **Deliverables:** `site/src/lib/components/CurriculumView.svelte`; `site/src/lib/server/curriculum.ts`; redesigned route shell, grade pages, discipline detail and source-explanation page; `site/data/source/w042-static-fichas.csv`; six published PDF copies; narrow repository-validator exclusion for installed dependencies.
- **Sources added:** No new original research sources. Six already-preserved W036 Ficha 1 PDFs were copied byte-for-byte into site static assets; SHA-256 matches both the W036 manifest and the new site copy manifest. The Biomedicina grade and public GitHub repository were consulted only as a design reference; no repository code was copied because no license was declared.
- **Coverage:** 41 components shown for 2011 and 43 for 2023. The 2023 view shows 29 Ficha 1 versions located, 10 non-TCC components without a located Ficha 1, and four TCC alternatives outside the Ficha request queue. The 2011 view shows seven located Ficha 1 versions and 29 coded non-TCC components without a located Ficha 1; the historical TCC and four optative spaces are separately marked not applicable. Twenty-one curated pairs connect same-code or similar-name disciplines without asserting formal equivalence.
- **Validation:** `npm run check` in pinned Node container: 0 errors, 0 warnings. `npm run build`: pass. Runtime HTTP checks: grade, detail, source page and new PDF return 200; legacy map redirects to the grade. `python scripts/validate_repository.py`: 227 CSVs, 132 hashes, 282 local links, 0 warnings/errors. `git diff --check`: pass. All six published PDF hashes match originals.
- **Gaps:** Most located Ficha 1 versions still lack established applicability to the corresponding IBM curriculum. The pair links are navigational clues, not formal equivalences. The website was not browser-screenshot tested because the in-app browser was unavailable and no browser QA was requested.
- **Divergences:** The reference repository had no declared license; its architecture and interaction pattern informed an original Svelte implementation rather than a source-code copy.
- **Provisional information:** The 2011/2023 counterpart list is curated from code/title similarity and needs separate documentary evidence before any official equivalence claim.
- **Explicitly unperformed:** No new Ficha search, no Ficha 2 display, no course-quality evaluation, no assembly argument, no remote push, no deployment, no merge to `main`.
- **Error log:** `governance/errors/W042-curriculum-site.md`; resolved E-W042-001, E-W042-002, E-W042-003; open events: none.
- **Human-review questions:** None opened for this implementation. Curricular applicability and institutional equivalence remain documentary gaps, not resolved by the UI.
- **Recommended next bounded work unit:** User review of the two grade views, followed by authorized integration/deployment if accepted. Do not start automatically.
