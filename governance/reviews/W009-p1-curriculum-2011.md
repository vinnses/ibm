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

## Post-correction follow-up — 2026-09-04

- **Corrective commits reviewed:** `b7c998d`, `50db1b9`
- **Post-correction verdict:** **approved with documented exceptions**

The preceding `changes required` verdict is retained as the record of the
pre-correction review. The three integration blockers have been corrected and
rechecked; this follow-up is the operative verdict for the corrected branch.

### Corrected Bloco A rule and component measures

The Article 1 Formação Básica set is now represented as its 15 members:
`CI241`, `CI055`, `CM201`, `CM045`, `BA040`, `CI243`, `CI056`, `CI067`,
`CM005`, `BQ005`, `CI244`, `CI057`, `CI166`, `BQ054`, and `BC056`.
The Article 2 §1 hidden-requirement rows now have 26 endpoints: 22 coded
components outside that set and the four elective spaces (`OPT-07-01`,
`OPT-08-01`, `OPT-08-02`, and `OPT-08-03`). The four space rows expressly
condition a later catalog selection and do not assert an offering. No Bloco A
member is an endpoint of its own completion rule.

Independent cross-checking of every Anexo I row confirms the fields are now
kept distinct: `weekly_total_hours` transcribes `Tot.`, and `credits`
transcribes `Créd.`. The 37 coded components comprise 26 rows of
`60/4/3`, 10 rows of `60/4/4`, and CI262 at `120/8/6`
(`total_hours/weekly_total_hours/credits`); each of the four elective spaces
is `60/4/4`. The calculated `total_hours` values are consistent with the
15-week structure and the act's category totals; they are not a relabeling of
the Anexo's weekly `Tot.` field.

### Workload contradiction and prior-review calculation

The preserved act remains contradictory in its category presentation. Article
1 labels Formação Profissional Geral as 840 hours, while Article 3 labels it
as 960 hours. Anexo I independently recomputes to 840 hours for its 14
non-TCC 60-hour components; adding CI262 Trabalho de Conclusão de Curso
(120 hours) produces 960 hours. This arithmetic supports neither an assertion
that the act explicitly classifies TCC inside Formação Profissional Geral nor
an assertion that it excludes it: Article 1 displays TCC separately, and the
classification treatment is not stated expressly. `D-W009-001` correctly
preserves this as contradictory evidence rather than resolving it by
inference.

The earlier review's 900-hour statement is also retained as a review claim,
but is not reproducible from Anexo I: the apparent fifteenth item, CI262, is
120 rather than 60 hours. Its correction does not erase the 840/960 source
contradiction.

### Remaining documented exceptions and checks

- The bounded public-search/Ficha gaps and the current-portal Ementário
  limitation remain documented research limits, not findings of nonexistence.
- Error-log and human-review records preserve the original defects and their
  corrections; no new unrecorded exception was found in this recheck.
- `python scripts/validate_w009_curriculum_2011.py` — passed (41 targets, 37
  codes, 26 Bloco A targets, one workload divergence; 0 errors).
- `python scripts/validate_governance_audit.py` — passed (0 errors).
- `python scripts/validate_repository.py` — passed (19 CSV files, 126
  preserved hashes, 93 local Markdown links; 0 warnings, 0 errors).
- `git diff --check` — passed.

This review approves the corrected W009 branch with the stated documentary
exceptions. It does not integrate the branch or resolve the source's 840/960
classification conflict.
