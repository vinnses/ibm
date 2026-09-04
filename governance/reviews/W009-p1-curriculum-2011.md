# Cross-review — W009 2011 curriculum documentary inventory

- **Reviewed branch:** `work/w009-p1-curriculum-2011`
- **Reviewed base:** `22b14805956fcece4e381dc089f7dbb06d2b0857`
- **Reviewed commits:** `829ac83`, `9ab39b5`
- **Review date:** 2026-09-04
- **Verdict:** **changes required**

## Scope and evidence checks

The required local inventory, source manifests, bounded-search log, preserved Ementário captures, one indeterminate Ficha 1, validator, and handoff are present. Independent set checks confirm 41 inventory targets (37 coded components and four elective spaces), 64 elective-catalog entries, 37 matching component/ementa codes, and seven explicit prerequisite edges. The 2025 CI241 Ficha 1 is correctly preserved and kept indeterminate for 2011; source samples for CI241, CI056, CI171, and CI262 confirm the captured Ementário field `Não consta` for ementa.

The local manifests resolve and hash correctly. The source captures preserve the resolution’s header inconsistency and the inventory does not substitute the 2025 Ficha 1 for a 2011 document.

## Required corrections (integration blockers)

1. **Bloco A dependency endpoints are overinclusive.** Article 1 of the preserved Resolução nº 34/2010-CEPE places CI244, CI057, CI166, BQ054, and BC056 in Formação Básica (Bloco A). Article 2 §1 requires completion of Bloco A *to take any other discipline*. Yet `inventario/dependencias.csv` emits `BLOCK-A` hidden-requirement rows to each of those five Bloco A components (27 endpoints total). These five rows assert a condition on components that are part of the prerequisite block itself and are not supported by the wording. Correct the rule representation to exclude Bloco A components; also state separately whether and how the rule applies to the four elective spaces. **Consequence:** the structured dependency dataset cannot yet be relied upon for progression analysis. **Roadmap destination:** W009 correction before integration; reconcile again in P2.

2. **The `credits` field does not reproduce the primary act.** The Anexo I table distinguishes weekly total (`Tot.`) from `Créd.`. For example, CI241, CI055, BA040, CI243, CI056, and CI067 each display `Tot. 04` and `Créd. 03`; `componentes.csv` records `credits=4` for each. This appears to conflate weekly total with credits. Correct all component credit values against the original table, or rename/document the field if it intentionally means a different measure. **Consequence:** formal component attributes are materially inaccurate. **Roadmap destination:** W009 correction before integration; P2 should audit the corrected transcription.

3. **The resolution’s internal workload conflict needs an explicit inventory/audit note.** The code inventory totals 2,280 hours (37 coded components: 2,280) plus 240 elective-slot hours and 480 formative-activity hours, or 3,000. Article 3 nevertheless labels Formação Profissional Geral as 960 hours, while the 15 listed professional-general coded components total 900 hours and the category total implied by the other article-3 figures is 960. The existing `grade-curricular.md` repeats 960 without flagging the mismatch, and the W009 inventory/handoff records only the page-header inconsistency. **Consequence:** a reader can mistake the 960/900 discrepancy for resolved evidence. **Roadmap destination:** W009 correction before integration; preserve both values and classify the discrepancy for P2 reconciliation.

## Exceptions and non-blocking observations

- The absence of applicable 2011 Ficha 1/Ficha 2 documents is visibly bounded and does not block the specified inventory gate; it remains a P1 public-access gap and a P2 audit input, not evidence of nonexistence.
- The current Ementário department representation is consistently labeled as a current portal representation rather than independent historical proof. This is acceptable pending a historical unit act.
- `git diff --check` on the clean review worktree passes. A range check from the recorded base reports trailing whitespace on W009-added CRLF HTML captures and CSVs. The HTML issue is compatible with preserving source bytes unchanged; the CSV line endings should be normalized if the W009 correction reopens those files. This is not the basis for the blocking verdict.

## Validations and independent checks

- `python scripts/validate_w009_curriculum_2011.py` — passed: 41 targets, 37 codes, local manifests/hash checks; 0 errors.
- `python scripts/validate_repository.py` — passed: 18 CSV files, 126 preserved hashes, 88 local Markdown links; 0 warnings, 0 errors.
- `git diff --check` on the clean worktree — passed.
- Independent CSV audit — component and ementa code sets match (37/37); all ementa evidence paths exist; seven explicit prerequisite edges match the resolution sample; the five improper Bloco A endpoints and sampled credit mismatches above were reproduced directly from the preserved resolution.

No integration is authorized by this review.
