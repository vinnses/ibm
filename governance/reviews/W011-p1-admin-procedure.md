# Cross-review — W011 administrative and procedural history

- **Reviewed branch:** `work/w011-p1-admin-procedure`
- **Reviewed commits:** `8565b6d`, `b65d57f`, `41cd390`
- **Review date:** 2026-09-04
- **Verdict:** **changes required**

## Scope and positive checks

The work is within W011 scope. The transition register keeps the five 2026 states (`proposal`, `selected`, `approved`, `authorized`, `implemented`) separate. Only `proposal` is marked proven; the other four are explicitly bounded not-located records. The registry-derived authorization/recognition rows identify their evidence class and do not claim to preserve the underlying acts.

The quantitative rows keep their universes and denominators visible. The 2016 applicant observation, PS/UFPR-2026 vacancies, historical cohort dropout measure, and INEP cohort trajectory front are not combined to infer occupancy, demand, or a cross-series rate. The CPA workbook is retained as unaggregated response-level material and its missing denominator/aggregation metadata is visible.

All nine manifest records have present stable paths and matching SHA-256 values. Independent samples confirm the preserved Ementário capture contains the named authorization/recognition attribution and undated `Conceito MEC 4`; the 2026 notice has 24 PS-specific places for Informática Biomédica; and the historical-dropout report displays 78.95 for the course. CSV widths are consistent.

## Required correction / blocker to integration

`HN003` states that the 2022 reform minutes and opinions were not publicly located. This is contradicted by a repository-held official source pointer in `curriculos/2023/fontes/README.md`: it names the 1st CEPE Chamber minute of 2 December 2022 and its canonical SOC URL. Independent retrieval at that URL on 2026-09-04 succeeded: the two-page official PDF states for process `061269/2022-16` (Informática Biomédica) that the rapporteur read a favorable opinion and that the matter was approved unanimously. Retrieved-byte SHA-256: `461fd8121be84c13d53c6d77a0dcc0d11500ee84a295b08a3e8c86df914b8faf`.

This review does not add that binary because its authorization is limited to this review file. Its use is therefore an **unresolved preservation exception** in this review record, not a replacement for a repository-preserved source. The W011 correction must preserve the original under the local W011 source tree, add a complete manifest record, replace or narrow `HN003`, and add the minute/opinion evidence to the transition/evidence register. Until then, the claimed “every target has evidence or bounded not-located record” acceptance criterion is not met. Destination: a corrective W011 commit and repeat cross-review before the P1 administrative-history gate can advance.

The original authorization and recognition acts, other 2026 procedural artifacts, detailed e-MEC/Enade records, final occupancy, and comparable cutoff-score data remain documented gaps rather than blockers; their stated public-search limits are appropriate and do not establish nonexistence.

## Validation performed

- `python scripts/validate_w011_admin_procedure.py` — passed: 9 source hashes, 8 transitions, 11 negative searches; 0 errors.
- `python scripts/validate_repository.py` — passed: 16 CSV files, 126 preserved hashes, 88 Markdown links; 0 warnings, 0 errors.
- Independent CSV-width audit — passed for all five W011 CSV files.
- Independent SHA-256 recomputation for all nine W011 manifest paths — matched.
- `git diff --check` — passed before this review commit.

No integration, approval, or research-deliverable mutation was performed.
