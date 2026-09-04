# W010 handoff — 2023 documentary inventory

- **Branch:** `work/w010-p1-curriculum-2023`
- **Commit base:** `22b14805956fcece4e381dc089f7dbb06d2b0857`
- **Commit produced:** `61be19b` — `Build 2023 curricular documentary inventory`
- **Verdict:** Collection and structuring complete for the bounded public evidence reached; documentary completeness remains **not established** because many applicable Ficha 1/Ficha 2 versions were not publicly located. This is a handoff for cross-branch review, not approval or integration.

## Deliverables and coverage

- `curriculos/2023/inventario/componentes.csv`: exactly 43 unique targets (39 non-TCC and four separately-recorded TCC alternatives). Every record has formal basis, documentary status, Ficha status/path-or-gap, and 2023 applicability state.
- `curriculos/2023/inventario/optativas.csv`: formal elective catalog transcribed from Resolution 75/22-CEPE. It does not imply an actual offering.
- `curriculos/2023/inventario/ementas.csv`: 40 preserved Ficha records; Ficha 1 and each Ficha 2 remain separate. All pre-reform versions are `indeterminado`, except the explicitly contradictory MN162/BQ083 records and the 2022.1 MN129 Ficha 2, which is not applicable to the 2023 matrix.
- `curriculos/2023/inventario/dependencias.csv`, `regulamentos.csv`, and `buscas-negativas.csv`: structured direct endpoints, PPC regulations, and bounded public-search limits.
- `curriculos/2023/fontes/manifesto.csv` and `curriculos/2023/inventario/README.md`: source provenance/hash record and interpretation limits.

## Sources added or relied on

The preserved formal baseline is Resolution 75/22-CEPE, PPC 2023, and Resolutions 76–80/22-CEPE. The local source manifest records their stored-byte SHA-256 values and the preserved UFPR HTML captures. Existing DInf and other-department Ficha manifests retain source URLs, paths, and hashes for all located Fichas.

The Ementário capture is retained as a divergence: it shows a 3,000-hour older structure; Resolution 75/22 fixes the 3,200-hour structure for entrants from 2022/2023. No silent reconciliation was made.

## Gaps and divergences

- No current/public Ficha 1 was located for numerous cross-department components or the components created by Resolutions 76–80/22.
- No Ficha 2 with identified 2023–2026 term/class was located. The DInf Ficha 2 documents are preserved but have indeterminate term/class in this collection.
- MN162 and BQ083 Ficha 1 documents appear to predate their 2022 code-creation acts. This is recorded as contradictory, not as applicability evidence.
- BF114’s preserved Ficha 1 is in a 2024 directory but has no established curriculum validity.

## Validations

- Target/uniqueness/applicability/dependency check: passed (`43`, `39` non-TCC, `4` TCC alternatives, `40` Ficha records; all dependency endpoints valid).
- `python scripts/validate_repository.py`: passed — 18 CSV files, 126 preserved hashes, 88 Markdown links; 0 warnings, 0 errors.
- `git diff --check`: passed before commit.

## Provisional and unperformed work

No claim is made that an indeterminate Ficha applies to the 2023 curriculum. No content comparison, 2011 work, administrative-history expansion, proposal evaluation, global-index update, review, approval, or integration was performed.

## Recommended next bounded work unit

Cross-review W010 against the preserved PDFs and targeted retrieval from the responsible departments/UFPR systems for the missing current Ficha 1 and term/class-specific 2023–2026 Ficha 2 documents. Preserve any recovered originals before assigning applicability.
