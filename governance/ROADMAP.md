# Project Roadmap

Baseline: 2026-09-05, data-first redirection after W010/P1 bounded closure.

## Active direction — data delivery before analysis

Latest execution checkpoint: W026 completed the selected historical-applicant batch in five intermediate pushed lots. Ten process-years received bounded searches, seven official sources were preserved, and the output keeps total-course and category-only counts separate. Absolute counts remain not located for 2018, 2025 and 2026; no named list, ratio or unmatched vacancy count was converted into a total.

The user's latest instruction supersedes the immediate P2-P4 sequence below. Prioritize relevant stable data and original documents, not curricular analysis or verification of current compliance/offering. The executable overall plan and per-step restart state are in [`DATA_FIRST.md`](DATA_FIRST.md).

- W014: commit and integrate the new direction and checkpoint contract.
- W015: index existing datasets and preserved source records, with a queue of already documented gaps; Luna/medium.
- W016: recover two original historical acts in separately committed batches, or record bounded retrieval gaps; Terra/medium.

Execution result: W014/W015/W016 are integrated (`20fa763`, `90929c0`, `241204b`). Lower-tier usage limits required a recorded primary takeover. The access package now indexes 36 datasets, 191 source records and 33 existing gap/search records. W016 preserved a Portaria 44/2015 institutional reproduction and literal UFPR annex data; the COUN original and original DOU facsimile remain gaps. See DATA_FIRST for the next bounded data batch and current restart point.

These three small steps are explicitly covered by the user's execution request. Each output is committed before the next batch, reviewed proportionately, and integrated separately by the primary. Cosmetic corrections stay deferred. Later data batches are selected from observed gaps and specified before activation; comparative P3 and analytical P4 are not authorized by this instruction.

## Completed foundation

- Documentary method, source hierarchy, preservation rules, historical-version rules, and fact/inference separation are established.
- The 2011 formal curriculum is reconstructed from the Resolução nº 34/2010-CEPE and the 2010 PPC: 37 coded components, four elective spaces, eight semesters, and 3,000 hours.
- The 2023 formal curriculum is reconstructed from the Resolução nº 75/22-CEPE, the 2023 PPC, and related component-creation resolutions: periodization, workloads, prerequisites, TCC alternatives, internship, extension, and 3,200-hour total.
- An initial 2023 Ficha collection is preserved: 20 DInf Ficha 1 documents, 16 DInf Ficha 2 documents, three external Ficha 1 documents, and one external Ficha 2 document.
- The UFPR 2026 internal call and the Biomedical Informatics feasibility form are preserved and described. The form is classified as a proposal, not evidence of approval or implementation.
- Administrative data are consolidated for the public scope reached: UFPR entrants and candidate/vacancy ratio for 2015–2026, official vacancy points, source-stated applicant records with explicit universes, the UFPR historical dropout measure, and INEP cohort indicators for entry cohorts 2011–2020.
- Annual metrics are separated from cumulative cohort indicators, and the 2026 proposal claims have an evidence-status matrix.
- The administrative research branch is merged into `main`; repository governance, transfer documentation, and automated validation are now present.
- P0 preservation exceptions are closed: the 11 exact INEP packages and 11 XLSX inputs used by W006 are stored through Git LFS, remote clean-checkout reproduction passed, the assembly brief is current with the consolidated evidence, and the global catalog is explicitly a curated index backed by complete local manifests.
- Agent/process failures, recovery attempts, review defects, and human-only questions now have append-only per-work audit trails. Stakeholder testimony and research hypotheses are preserved separately from documentary facts.
- Sol is reserved to the user-supervised primary session. Subagents use Luna or Terra according to task complexity, while model, effort, role, rationale, and escalation are mandatory prospective Work records. Integration, final audit, and global synthesis remain direct duties of the active primary session at its user-selected model/effort.

## Execution order

### P0 — Close preservation and consistency exceptions — complete

1. Preserve the 11 INEP source packages and the exact extracted spreadsheets used by W006 in a repository-backed mechanism, preferably Git LFS. Replace temporary absolute paths in `administracao/dados/fontes.csv` with stable repository paths and verify the recorded hashes.
2. Update `assembleia/subsidio-factual-preliminar.md` from the consolidated administrative data and validation matrix. The current file is explicitly marked preliminary and partially superseded.
3. Decide whether `fontes/catalogo.csv` becomes a complete global catalog or remains an intentionally small index. If complete, generate it from local manifests rather than maintaining duplicates manually.

Acceptance gate: a clean checkout can reproduce every source lookup used by existing conclusions, `python scripts/validate_repository.py` has no errors, and every preservation exception is either resolved or explicitly approved and documented.

Gate result: passed by W008 on 2026-09-04. A clean clone from the GitHub remote materialized all 22 LFS objects, both source/repository validators passed with zero errors and zero warnings, and W006 regenerated 85 observations plus three byte-identical outputs. See `governance/reviews/W008-p0-preservation-consistency.md`.

### P1 — Complete the 2011 documentary inventory

1. Transcribe the formal elective catalog.
2. Create an inventory for all 37 coded components and four elective spaces.
3. Locate and preserve the applicable Ficha 1 for every component, or record a bounded unsuccessful search.
4. Transcribe ementas with source version and applicability.
5. Locate Ficha 2 documents by term and class without merging versions.
6. Validate departments, prerequisites, correquisites, equivalences, and hidden requirements.
7. Create a structured representation of components and dependencies.

Acceptance gate: every component has a status, evidence path, source hash, version/applicability assessment, and explicit gaps or conflicts.

Gate result: passed with documented public-source exceptions by W009 on 2026-09-04 and integrated by `267011f`. Historical applicable Fichas and offering-unit confirmation remain explicitly separated human-review questions; no nonexistence is inferred.

### P1 — Complete the 2023 documentary inventory

1. Transcribe and structure the formal elective catalog in the resolution.
2. Inventory the 39 non-TCC components and four alternative TCC codes individually.
3. Complete Ficha 1 and prioritized 2023–2026 Ficha 2 collection across all departments.
4. Confirm whether pre-2023 Fichas apply to the 2023 curriculum; do not infer continuity from code alone.
5. Catalog internship, TCC, extension, and formative-activity regulations.
6. Resolve or document the stale Portal do Ementário representation.
7. Create a structured component and dependency dataset.

Acceptance gate: the same per-component evidence standard used for 2011 is met, and every pre-reform Ficha has an applicability judgment or remains explicitly indeterminate.

Gate result: passed with documented exceptions by W010 on 2026-09-05, independently approved in `0518f67` and integrated by `750df8b`. Coverage: 43 unique targets (39 non-TCC and four alternative TCC codes), 92 formal electives, 21 direct dependency rows, five regulatory subjects and 40 separately preserved Ficha records. The missing electives and CI1215 derived-hash defects were corrected in `75b4ee4` and independently verified.

Accepted exceptions: HR-W010-001 (applicable Ficha 1), HR-W010-002 (term/class-specific 2023–2026 Ficha 2), and HR-W010-003 (authoritative Ementário status) remain pending. P2 must retain these gaps in version/applicability and conflict reconciliation; P3 must limit content and offering comparisons to supported evidence. Indeterminate applicability is not continuity or nonexistence. Nonmaterial editorial/process corrections C-W010-003 through C-W010-006 are deferred under the user's explicit direction in `governance/corrections/W010.md`; E-W010-014 is an accepted process-documentation exception with no research-data impact.

### P1 — Extend administrative and procedural history

1. Preserve acts creating and recognizing the course.
2. Preserve minutes and opinions supporting the reform approved in 2022.
3. Add official institutional evaluations, Enade, CPA reports, and e-MEC records with comparable definitions.
4. Preserve source-stated applicant counts and retain unresolved complete-count, final-occupancy and comparable-cutoff gaps without deriving values from mismatched universes. W026 completed a bounded 2015–2026 applicant search; 2018, 2025 and 2026 remain not located.
5. Preserve Apêndice A, forwarding memorandum, SEI identifier, NDE/Colegiado/Setor decisions, PROGRAP/PROPLAD result, UFPR submission, and MEC decision if they become available.
6. Obtain the proposed 2,700-hour matrix, component list, equivalences, PPC/minutes, and staffing guarantees.

Acceptance gate: each administrative transition is tied to a primary act or remains explicitly not located; quantitative series state universe, denominator, time basis, and comparability.

Gate result: passed for the bounded public-source scope by W011 on 2026-09-04 and integrated by `92b3f4c`. Protected and not-located records remain explicit gaps and do not establish nonexistence.

### Historical P2 plan — broad reconciliation deferred; essential data checks retained

P1 closure: W009, W010 and W011 are integrated and their bounded documentary gates have passed with recorded exceptions. This does not certify exhaustive data recovery. W014-W016 now take priority; only source identity, accurate transcription, version separation and preservation checks needed for trustworthy data delivery are immediate. The former broader P2 plan below is retained for later authorization.

1. Audit every manifest, link, hash, extraction, and version assignment.
2. Reconcile conflicts between resolutions, PPCs, institutional pages, Ementário, and Fichas without silently selecting one.
3. Produce coverage matrices for 2011, 2023, administrative history, and the 2026 proposal.
4. Freeze a documented evidence baseline for comparison.

Acceptance gate: no required component or claim lacks a status, and all material contradictions have an audit note.

### Historical P3 plan — comparative curricular analysis deferred

Begin only after both curriculum inventory gates and the P2 audit pass.

1. Compare 2011 and 2023 by ementa, program, workload, progression, and dependencies rather than names alone.
2. Compare Computing, Biosciences, Health, and interdisciplinary integration.
3. Analyze continuity, redundancy, gaps, and changes in prerequisite chains.
4. Evaluate the 2026 proposal against reconstructed curricula and verified administrative evidence.
5. Keep direct facts, inferences, interpretations, and normative recommendations visibly separate.

### Historical P4 plan — analytical synthesis deferred; data release remains a priority

1. Produce the final evidence-backed report and machine-readable datasets.
2. Include source catalogs, methodology, limitations, conflicts, and reproducibility instructions.
3. Tag the evidence baseline and archive large source artifacts through the chosen repository-backed mechanism.

## Explicitly deferred

- Judging whether the 2026 change is desirable.
- Designing a new curriculum or renaming components.
- Inferring content from course or discipline names.
- Treating expected funding or two requested faculty positions as guaranteed.
- Calling the proposed course selected, approved, authorized, or implemented without the corresponding act.
