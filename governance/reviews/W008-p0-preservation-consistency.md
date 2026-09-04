# Review — W008: P0 preservation and consistency closure

- Date: 2026-09-04
- Reviewer role: independent criteria-based review by the orchestrator
- Branch and commits: `work/w008-p0-preservation`; `5b05d11`, `d8b0d06`, `d70bd4a`, `9b1dea5`, and the approval update at branch `HEAD`
- Verdict: `approved for integration`

## Findings

### Blocking

- None. The prior SSH authentication blocker was resolved on retry. GitHub accepted all 22 LFS objects and the branch, and a subsequent clean clone from `origin` materialized and validated the source bytes.

### Non-blocking

- The W008 recapture could not validate the TLS chain presented by `download.inep.gov.br` in this environment. Every downloaded package nevertheless matched the exact SHA-256 recorded by W006, and every extracted XLSX matched both its package member and the preserved official MD5. This transport limitation is disclosed in the source documentation and does not create a byte-identity conflict.
- Git LFS was not installed system-wide. Review used the official Git LFS 3.8.0 Linux AMD64 release in a temporary path; its archive SHA-256 matched the digest published by the GitHub release API. Reproducible users still need Git LFS installed in their environment.

### Preservation and provenance

- Eleven official ZIP packages and eleven exact XLSX members are tracked by Git LFS under stable repository-relative paths.
- `administracao/dados/fontes.csv` no longer contains the eleven absolute scratch paths and records byte sizes and SHA-256 values for all 22 large inputs.
- `administracao/dados/inep/fontes/manifesto-fontes-volumosas.csv` records stable identifiers, titles, institution, URLs, access date, type, version range, purpose, status, SHA-256, and capture notes.
- Original package and spreadsheet bytes were not normalized or modified.

### Reproducibility

- All 11 ZIP integrity checks passed; every ZIP contained exactly one XLSX; every extracted XLSX equaled its ZIP member and matched the official MD5.
- W006 regenerated 85 source observations and both summaries. The extracted course CSV and both derived CSVs were byte-identical to the committed outputs.
- A clean clone from the local Git object/LFS stores and a separate clean clone from the GitHub remote each materialized all 22 binaries and passed both validators.
- The remote clone regenerated the 85 W006 observations and both summaries; all three resulting CSVs were byte-identical to the committed outputs.

### Scope and historical validity

- The refreshed assembly brief distinguishes direct facts, proposal content, evidentiary limits, divergence, and not-located records; it adds no curricular judgment.
- D011 establishes `fontes/catalogo.csv` as a curated global index and local manifests as authoritative complete inventories. The catalog itself was not duplicated or mechanically expanded.
- No P1 research or curricular comparison was started.

## Validation executed

- `python scripts/validate_inep_sources.py` — 11 packages, 11 spreadsheets, 11 official MD5 entries; 0 errors.
- `python scripts/validate_repository.py` — 11 CSV files, 126 preserved hashes, 88 local Markdown links; 0 warnings, 0 errors.
- Python compilation for the four relevant scripts — passed.
- W006 extraction and summary regeneration — 85 observations and 85 balance/indicator checks; all three outputs byte-identical.
- `git diff --check` — passed.
- Clean local clone with LFS smudge — all 22 objects materialized; both validators passed.
- `git push --set-upstream origin work/w008-p0-preservation` — passed on retry; 22 LFS objects (reported as 1.2 GB) and the branch were uploaded.
- Clean clone from `git@github.com:vinnses/ibm.git`, branch `work/w008-p0-preservation` — 22 LFS objects materialized; both validators passed; W006 regenerated 85 observations and all three outputs were byte-identical.

## Exceptions and roadmap destination

- The INEP TLS-chain limitation remains documented as a capture condition, with exact W006 SHA-256 and official MD5 matches establishing byte identity. It does not block integration.
- P0 acceptance criteria are met. W008 may be integrated under the user's standing authorization to integrate only approved work.
