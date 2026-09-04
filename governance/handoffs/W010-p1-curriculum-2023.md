# W010 handoff — 2023 documentary inventory

- **Branch:** `work/w010-p1-curriculum-2023`
- **Commit base:** `22b14805956fcece4e381dc089f7dbb06d2b0857`
- **Commits produced:** `61be19b` — `Build 2023 curricular documentary inventory`; `9f576f7` — initial handoff; `838cd79` — correction of source/Ficha records and W010 validator; follow-up documentation commit pending this amended handoff.
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

`E-W010-001` through `E-W010-004` remain in the append-only error log with dated correction updates; all four are resolved by the source/Ficha/validator correction recorded above. `HR-W010-001` (current applicable Ficha 1), `HR-W010-002` (term/class-specific Ficha 2), and `HR-W010-003` (authoritative Ementário status) remain pending human-access/authority questions. They do not replace the completed agent corrections.

## Recommended next bounded work unit

Cross-review W010 against the preserved PDFs and targeted retrieval from the responsible departments/UFPR systems for the missing current Ficha 1 and term/class-specific 2023–2026 Ficha 2 documents. Preserve any recovered originals before assigning applicability.
