# Handoff — W008: P0 preservation and consistency closure

- Branch: `work/w008-p0-preservation`
- Commit base: `478dbe11a14ff2451f78b43f04794d79428492f6`
- Commits produced: `5b05d11` (specification); `d8b0d06` (INEP preservation and reproducibility); `d70bd4a` (factual brief and catalog decision); final blocked-review/handoff commit recorded by `HEAD`.
- Objective: close every P0 preservation and consistency exception or stop with the exact inaccessible dependency documented.
- Completion verdict: `approved for integration`; remote LFS preservation and clean-checkout reproduction are established.
- Deliverables: W008 specification; Git LFS attributes; 11 INEP packages; 11 exact XLSX inputs; complete large-source manifest; stable paths in the administrative manifest; INEP and repository validators; pinned reproduction dependencies; updated preservation/audit documentation; refreshed factual assembly brief; D011 catalog-scope decision; this review and handoff.
- Primary files: `.gitattributes`; `administracao/dados/inep/fontes/manifesto-fontes-volumosas.csv`; `administracao/dados/fontes.csv`; `scripts/validate_inep_sources.py`; `scripts/validate_repository.py`; `assembleia/subsidio-factual-preliminar.md`; `governance/DECISIONS.md`; `governance/reviews/W008-p0-preservation-consistency.md`.
- Sources added: 11 exact official INEP ZIP packages (697 MiB) and their 11 exact XLSX members (401 MiB), all under `administracao/dados/inep/fontes/` and tracked by Git LFS.
- Coverage reached: all 11 W006 national input vintages from 2010-2019 through 2020-2024 have package and spreadsheet bytes, stable paths, SHA-256, official MD5 linkage, version range, provenance, purpose, and preservation status locally.
- Validation and result: package integrity/membership/MD5 passed 11/11; repository validator passed with 0 warnings and 0 errors; W006 regenerated 85 observations and three byte-identical outputs; clean local and GitHub clones each materialized all 22 LFS objects and passed both validators; remote branch and 1.2 GB of LFS objects uploaded successfully.
- Gaps: no unresolved P0 preservation exception. Git LFS remains an explicit checkout prerequisite.
- Divergences: no source-byte or extraction divergence. The INEP TLS chain was not trusted by the local client during recapture; exact prior SHA-256 and official MD5 identity checks passed and the limitation is recorded.
- Provisional information: none affecting the P0 gate. The recorded INEP transport limitation remains part of provenance.
- Explicitly not performed: no integration into `main`; no update of global roadmap/work indexes; no P1 work; no curricular evaluation, proposal design, or inference from documentary absence.
- Recommended next bounded work unit: decompose P1 into independent curricular-2011, curricular-2023, and administrative/procedural work units with separate branches, worktrees, local manifests, reviews, and handoffs; do not start P2 until every P1 gate passes.

## Integration record

- Merged branch: `work/w008-p0-preservation` at `989722c`.
- Merge commit: `fdeef13` (`Merge approved W008 P0 preservation`).
- Conflict resolutions: none.
- Global indexes updated: `governance/WORK_INDEX.md` and `governance/ROADMAP.md` in the integration metadata commit at `HEAD`.
- Final validation: `scripts/validate_inep_sources.py` passed 11 packages, 11 spreadsheets, and 11 official MD5 entries with zero errors; `scripts/validate_repository.py` passed 11 CSV files, 126 hashes, and 88 local Markdown links with zero warnings and zero errors; Python compilation and `git diff --check` passed.
- Remote synchronization state: work branch and all 22 LFS objects are synchronized; `main` push follows this integration metadata commit.
