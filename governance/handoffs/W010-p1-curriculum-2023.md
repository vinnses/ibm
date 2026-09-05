# W010 handoff — 2023 documentary inventory

- **Branch:** `work/w010-p1-curriculum-2023`
- **Commit base:** `22b14805956fcece4e381dc089f7dbb06d2b0857`
- **Commits produced:** `61be19b` — `Build 2023 curricular documentary inventory`; `9f576f7` — initial handoff; `838cd79` — correction of source/Ficha records and W010 validator; `bfd3eeb` — correction documentation; `82b7eb7` — Resolution 80 README/validator hash correction; `d8acf9f` — E-W010-005 and hash-correction handoff documentation; `7405e16` — clarification of hash-correction traceability. Subsequent resumption and integration records appear below.
- **Verdict:** Collection and structuring complete for the bounded public evidence reached; documentary completeness remains **not established** because many applicable Ficha 1/Ficha 2 versions were not publicly located. This is a handoff for cross-branch review, not approval or integration.

## Deliverables and coverage

- `curriculos/2023/inventario/componentes.csv`: exactly 43 unique targets (39 non-TCC and four separately-recorded TCC alternatives). Every record has formal basis, documentary status, Ficha status/path-or-gap, and 2023 applicability state.
- `curriculos/2023/inventario/optativas.csv`: formal elective catalog transcribed from Resolution 75/22-CEPE. It does not imply an actual offering.
- `curriculos/2023/inventario/ementas.csv`: 40 preserved Ficha records; Ficha 1 and each Ficha 2 remain separate. BQ083 is dated from its internal 2022 render/signatures and remains `indeterminado` for 2023 applicability. MN162 remains a documented chronology issue; MN129 2022.1 is not applicable to the 2023 matrix.
- `curriculos/2023/inventario/dependencias.csv`, `regulamentos.csv`, and `buscas-negativas.csv`: structured direct endpoints, PPC regulations, and bounded public-search limits.
- `curriculos/2023/fontes/manifesto.csv` and `curriculos/2023/inventario/README.md`: source provenance/hash record and interpretation limits, including the separately preserved Ementário response and 2025/2 schedule page.
- `scripts/validate_w010_curriculum_2023.py`: reproducible work-specific validation.

## Sources added or relied on

The preserved formal baseline is Resolution 75/22-CEPE, PPC 2023, and Resolutions 76–80/22-CEPE. The local source manifest records their stored-byte SHA-256 values and the preserved UFPR HTML captures. Existing DInf and other-department Ficha manifests retain source URLs, paths, and hashes for all located Fichas.

The corrected Ementário capture identifies itself as “Informática Biomédica - 2011 - Corrente” and displays 3,000 hours; Resolution 75/22 fixes the 3,200-hour structure for entrants from 2022/2023. The previously confused schedule page is retained under its correct 2025/2 provenance. No silent reconciliation was made.

## Gaps and divergences

- No current/public Ficha 1 was located for numerous cross-department components or the components created by Resolutions 76–80/22.
- No Ficha 2 with identified 2023–2026 term/class was located. The DInf Ficha 2 documents are preserved but have indeterminate term/class in this collection.
- MN162’s 2019 Ficha 1 remains a chronology issue and not applicability evidence. BQ083 is internally dated and signed in 2022; no act establishing its applicability to the 2023 matrix was located, so it remains indeterminate rather than contradictory.
- BF114’s preserved Ficha 1 is in a 2024 directory but has no established curriculum validity.

## Validations

- `python scripts/validate_w010_curriculum_2023.py`: passed — 43 targets, 21 dependencies, 12 source hashes, 40 Ficha hashes, 4 negative searches; 0 errors.
- `python scripts/validate_governance_audit.py`: passed — 5 error logs, 22 events, 3 human-review files, 8 questions; 0 errors.
- `python scripts/validate_repository.py`: passed — 18 CSV files, 126 preserved hashes, 93 Markdown links; 0 warnings, 0 errors.
- `git diff --check`: passed before commit.

## Provisional and unperformed work

No claim is made that an indeterminate Ficha applies to the 2023 curriculum. No content comparison, 2011 work, administrative-history expansion, proposal evaluation, global-index update, review, approval, or integration was performed.

## Error events and human-review questions

`E-W010-001` through `E-W010-005` remain in the append-only error log with dated correction updates; all five are resolved. E-W010-005 corrects a README-only Resolution 80 hash divergence and adds an automated README/manifest hash cross-check. `HR-W010-001` (current applicable Ficha 1), `HR-W010-002` (term/class-specific Ficha 2), and `HR-W010-003` (authoritative Ementário status) remain pending human-access/authority questions. They do not replace the completed agent corrections.

## Recommended next bounded work unit

Cross-review W010 against the preserved PDFs and targeted retrieval from the responsible departments/UFPR systems for the missing current Ficha 1 and term/class-specific 2023–2026 Ficha 2 documents. Preserve any recovered originals before assigning applicability.

## Resumption record — 2026-09-05

- Primary-session model and effort: GPT-6 (runtime-exposed family after the user model switch; exact backend identifier not exposed); medium requested in the user's resumption plan, runtime effort not independently exposed.
- Agent assignments actually used: resumption primary / primary / orchestrator, process-reference corrector, integrator and final auditor / GPT-6 / medium requested, runtime value not exposed / user-supervised integration role. Historical W010 collector, correction-agent and reviewer model/effort assignments remain unknown where unrecorded. Resumption reviewer / subagent / independent documentary reviewer / gpt-5.6-terra (Terra) / high / demanding cross-validation of source evidence and three prior reviews; assigned 2026-09-05 before activation. Conditional Luna/medium and Terra/medium correctors are not activated.
- Reassignments, escalations, equivalent-tier mappings, and routing deviations: the runtime-exposed GPT-6 primary maps to the repository's primary-only Sol role; the model change came from the user/session, not agent orchestration. No Sol subagent was created. The late durable primary-assignment record is logged as E-W010-009; there is no subagent escalation.
- Resumption baseline: clean W010 at `7405e16`; clean `main` and fetched `origin/main` at `1edcb35f582da966169406f3dab46215bfca959d`; incorporated by merge `6483fa0389018a86dc57a59c6861094452785afd`, with no conflicts or changes to W010 source bytes/data.
- Pre-merge validation: W009, W011, governance and repository validators on `main`; W010 and repository validators on the W010 branch; whitespace and LFS integrity checks on both worktrees passed. Full combined validation and independent review follow before integration.
- Error-log path: `governance/errors/W010.md`. E-W010-006 records the prior interrupted review (open until a new verdict); E-W010-007 (incorrect discovery path), E-W010-008 (residual handoff reference), and E-W010-009 (late assignment record) are resolved. E-W010-001 through E-W010-005 retain their original records and resolution updates.
- Human-review path: `governance/human-reviews/W010-p1-curriculum-2023.md`; HR-W010-001 through HR-W010-003 remain pending. P2 must retain version/applicability and portal-status gaps; P3 may compare only source-supported content and cannot infer missing term/class plans or institutional portal status. Bounded inventory acceptance does not certify exhaustive Ficha recovery.
- Current verdict: resumed and awaiting independent review. The historical collection and prior-review statements above describe their dated stages; the final operative verdict will be appended after review.
- Explicitly unperformed: new public-source collection, protected access, source/CSV changes, P2-P4 work. Recommended next Work after approved integration: P2 documentary reconciliation, manifest audit, coverage matrices, and evidence-baseline freeze, requiring separate authorization.

### Review findings and correction assignment — 2026-09-05

Review `0392c8c` returned `changes required`, identifying E-W010-010 (14 missing formal elective rows; 78/92 transcribed) and E-W010-011 (CI1215 hash typo in component/ementa records). E-W010-006 is resolved because the interrupted review has now completed; approval remains pending correction and independent re-review. The historical no-CSV-change statement above applies only to the initial resumption stage.

Actual additional assignment, recorded before activation: documentary corrector / subagent / source-to-table and derived-hash correction with targeted validator coverage / `gpt-5.6-terra` (Terra) / medium / bounded documentary reconciliation of the two findings. Conditional Luna/medium remains not activated. No primary-session model change or subagent escalation occurs. Sources and CSV schemas are unchanged; only the evidenced derived records and validator may be corrected. The same Terra/high reviewer will independently re-review the resulting commits.

### Corrections complete; expedited final review — 2026-09-05

Correction commit `75b4ee4` completes 92 formal elective records, fixes both CI1215 hash fields, adds complete catalog and derived-Ficha checks, and passes six focused regression cases plus W010/governance/repository/whitespace checks. Corrector actor: `01a07330-c14e-7881-9b87-532c5e9565f3`, Terra/medium; reviewer actor: `01a0732b-44ac-7390-a52b-af30504f85bb`, Terra/high. E-W010-010/E-W010-011 are corrected awaiting independent verification; E-W010-012/E-W010-013 are resolved local process errors. E-W010-014 is a nonblocking accepted process-documentation exception under the user's explicit instruction. All secondary corrections are consolidated in `governance/corrections/W010.md`; they do not delay P1. Final review is limited to material defects and regressions, using the prior completed checks.
