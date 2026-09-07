# W029 evaluation and admissions recovery lane

This directory records a bounded follow-up on five stable public-data targets: a detailed public e-MEC course record, a dated course-specific Enade result, and source-stated absolute applicant counts for the 2018, 2025, and 2026 UFPR admission processes.

On 2026-09-06, three genuinely new targeted official-public attempts were made for every target. None produced a qualifying source. The e-MEC public entry point returned an access challenge and was not bypassed. The INEP indicator entry point returned an access denial and was not bypassed. The NC results located for the admission years were result/list surfaces without a source-stated absolute applicant total; no named list, category sum, ratio, cutoff, or vacancy value was converted into a count.

The results are bounded outcomes, not assertions that the records do not exist. Existing W011, W026, and human-review records remain unchanged.

## Files

- `buscas.csv` records the 15 distinct attempts and their limits.
- `registros.csv` records the post-search status for each target.
- `manifesto.csv` is deliberately header-only because no new qualifying source was preserved in this lane.
- `validate_w029_evaluations_admissions.py` checks target coverage, attempt limits, and the absence of unsupported extraction.

Run `python administracao/historico/w029-avaliacoes-admissoes/validate_w029_evaluations_admissions.py` from the repository root.
