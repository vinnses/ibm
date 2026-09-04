# Consolidation Review — 2026-09-04

## Verdict

`approved with documented exceptions`

The completed administrative branch was suitable for integration after reproducibility checks. Governance consolidation corrected three pre-existing manifest errors and exposed one material preservation exception.

## Branch audit

- Remote default branch before integration: `origin/main` at `ad1ce16`.
- Only unmerged remote work branch found: `origin/research/admin-data-2026` at `5b5423d`.
- The branch was one commit ahead and zero commits behind `main`.
- Remote merge commit: `c242270` (`Merge administrative data research`).
- The earlier 2011 and 2023 work was already present in `main`.

The governance changes were committed as `4421965` and `af8437a`, then merged into remote `main` by `d3ac930`.

## Validation performed

- Compiled `scripts/extrair_indicadores_trajetoria.py` and `scripts/resumir_indicadores_trajetoria.py`.
- Regenerated both INEP summary CSVs from the preserved course extract; byte comparison passed.
- Validated 85 INEP observations, 10 cohorts, and 85 balance/indicator identities.
- Checked uniform row width in all CSV files present at review time.
- Verified that the two user-supplied PDFs match the repository copies exactly:
  - edital: `dc8b4a809155f4995224ecc25c71ad873357ff605e04ceb92aaa25b659897a11`
  - Apêndice B: `994b17a9b1915a8d0dfc3104d01e7cc4d49b7f85e4002102687ee2e543109052`
- Rechecked hashes in the configured source manifests.

## Corrections made

1. Updated the global catalog hash for the complete `resolucao-75-22-cepe.pdf`; the catalog still contained the digest of an earlier incomplete binary.
2. Restored the missing final hexadecimal character in the BF114 Ficha 1 hash.
3. Restored the missing final hexadecimal character in the MN129 Ficha 2 hash.
4. Added `scripts/validate_repository.py` so these conditions are checked from a clean checkout.
5. Marked the assembly brief as preliminary and partially superseded after administrative data consolidation.

## Documented exceptions and follow-up

### INEP source packages are not preserved in Git

Eleven official packages used to obtain the national source spreadsheets were verified during W006 but not committed because the collection was approximately 697 MiB. Their manifest paths point to the former Work scratch directory and do not exist in a clean checkout. URLs and hashes remain, but this does not satisfy the repository's strict preservation rule.

Consequence: the committed course extract and scripts are auditable, but full extraction from the exact raw national files is not reproducible from the repository alone.

Required follow-up: roadmap P0 must preserve the exact packages and extracted spreadsheets through Git LFS or another explicitly approved repository-backed mechanism, then replace temporary paths with stable repository paths.

### Global catalog is intentionally incomplete

`fontes/catalogo.csv` contains the initial central records, while administrative and Ficha sources use local manifests. This is documented in `WORK_INDEX.md`; an integration decision remains open on whether to generate a complete global catalog.

### Assembly brief requires refresh

`assembleia/subsidio-factual-preliminar.md` predates the administrative evidence review. It now carries a warning and must not be treated as the current validation summary.

## Whitespace findings

`git diff --check` reports trailing whitespace in captured official HTML pages and official MD5 text files. These are preserved source bytes, not authored code. They were not normalized because preservation takes priority over stylistic cleanup.
