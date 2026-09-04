# Project Roadmap

Baseline: 2026-09-04 after integration of `research/admin-data-2026`.

## Completed foundation

- Documentary method, source hierarchy, preservation rules, historical-version rules, and fact/inference separation are established.
- The 2011 formal curriculum is reconstructed from the Resolução nº 34/2010-CEPE and the 2010 PPC: 37 coded components, four elective spaces, eight semesters, and 3,000 hours.
- The 2023 formal curriculum is reconstructed from the Resolução nº 75/22-CEPE, the 2023 PPC, and related component-creation resolutions: periodization, workloads, prerequisites, TCC alternatives, internship, extension, and 3,200-hour total.
- An initial 2023 Ficha collection is preserved: 20 DInf Ficha 1 documents, 16 DInf Ficha 2 documents, three external Ficha 1 documents, and one external Ficha 2 document.
- The UFPR 2026 internal call and the Biomedical Informatics feasibility form are preserved and described. The form is classified as a proposal, not evidence of approval or implementation.
- Administrative data are consolidated for the public scope reached: UFPR entrants and candidate/vacancy ratio for 2015–2026, official vacancy points, partial absolute applicant data, the UFPR historical dropout measure, and INEP cohort indicators for entry cohorts 2011–2020.
- Annual metrics are separated from cumulative cohort indicators, and the 2026 proposal claims have an evidence-status matrix.
- The administrative research branch is merged into `main`; repository governance, transfer documentation, and automated validation are now present.

## Execution order

### P0 — Close preservation and consistency exceptions

1. Preserve the 11 INEP source packages and the exact extracted spreadsheets used by W006 in a repository-backed mechanism, preferably Git LFS. Replace temporary absolute paths in `administracao/dados/fontes.csv` with stable repository paths and verify the recorded hashes.
2. Update `assembleia/subsidio-factual-preliminar.md` from the consolidated administrative data and validation matrix. The current file is explicitly marked preliminary and partially superseded.
3. Decide whether `fontes/catalogo.csv` becomes a complete global catalog or remains an intentionally small index. If complete, generate it from local manifests rather than maintaining duplicates manually.

Acceptance gate: a clean checkout can reproduce every source lookup used by existing conclusions, `python scripts/validate_repository.py` has no errors, and every preservation exception is either resolved or explicitly approved and documented.

### P1 — Complete the 2011 documentary inventory

1. Transcribe the formal elective catalog.
2. Create an inventory for all 37 coded components and four elective spaces.
3. Locate and preserve the applicable Ficha 1 for every component, or record a bounded unsuccessful search.
4. Transcribe ementas with source version and applicability.
5. Locate Ficha 2 documents by term and class without merging versions.
6. Validate departments, prerequisites, correquisites, equivalences, and hidden requirements.
7. Create a structured representation of components and dependencies.

Acceptance gate: every component has a status, evidence path, source hash, version/applicability assessment, and explicit gaps or conflicts.

### P1 — Complete the 2023 documentary inventory

1. Transcribe and structure the formal elective catalog in the resolution.
2. Inventory the 39 non-TCC components and four alternative TCC codes individually.
3. Complete Ficha 1 and prioritized 2023–2026 Ficha 2 collection across all departments.
4. Confirm whether pre-2023 Fichas apply to the 2023 curriculum; do not infer continuity from code alone.
5. Catalog internship, TCC, extension, and formative-activity regulations.
6. Resolve or document the stale Portal do Ementário representation.
7. Create a structured component and dependency dataset.

Acceptance gate: the same per-component evidence standard used for 2011 is met, and every pre-reform Ficha has an applicability judgment or remains explicitly indeterminate.

### P1 — Extend administrative and procedural history

1. Preserve acts creating and recognizing the course.
2. Preserve minutes and opinions supporting the reform approved in 2022.
3. Add official institutional evaluations, Enade, CPA reports, and e-MEC records with comparable definitions.
4. Continue the bounded search for complete applicant counts, final occupancy after all calls, and comparable cutoff scores.
5. Preserve Apêndice A, forwarding memorandum, SEI identifier, NDE/Colegiado/Setor decisions, PROGRAP/PROPLAD result, UFPR submission, and MEC decision if they become available.
6. Obtain the proposed 2,700-hour matrix, component list, equivalences, PPC/minutes, and staffing guarantees.

Acceptance gate: each administrative transition is tied to a primary act or remains explicitly not located; quantitative series state universe, denominator, time basis, and comparability.

### P2 — Documentary reconciliation and audit

1. Audit every manifest, link, hash, extraction, and version assignment.
2. Reconcile conflicts between resolutions, PPCs, institutional pages, Ementário, and Fichas without silently selecting one.
3. Produce coverage matrices for 2011, 2023, administrative history, and the 2026 proposal.
4. Freeze a documented evidence baseline for comparison.

Acceptance gate: no required component or claim lacks a status, and all material contradictions have an audit note.

### P3 — Comparative curricular analysis

Begin only after both curriculum inventory gates and the P2 audit pass.

1. Compare 2011 and 2023 by ementa, program, workload, progression, and dependencies rather than names alone.
2. Compare Computing, Biosciences, Health, and interdisciplinary integration.
3. Analyze continuity, redundancy, gaps, and changes in prerequisite chains.
4. Evaluate the 2026 proposal against reconstructed curricula and verified administrative evidence.
5. Keep direct facts, inferences, interpretations, and normative recommendations visibly separate.

### P4 — Final synthesis and reproducible release

1. Produce the final evidence-backed report and machine-readable datasets.
2. Include source catalogs, methodology, limitations, conflicts, and reproducibility instructions.
3. Tag the evidence baseline and archive large source artifacts through the chosen repository-backed mechanism.

## Explicitly deferred

- Judging whether the 2026 change is desirable.
- Designing a new curriculum or renaming components.
- Inferring content from course or discipline names.
- Treating expected funding or two requested faculty positions as guaranteed.
- Calling the proposed course selected, approved, authorized, or implemented without the corresponding act.
