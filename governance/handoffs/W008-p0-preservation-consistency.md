# Handoff — W008: P0 preservation and consistency closure

- Branch: `work/w008-p0-preservation`
- Commit base: `478dbe11a14ff2451f78b43f04794d79428492f6`
- Commits produced: `5b05d11` (specification); `d8b0d06` (INEP preservation and reproducibility); `d70bd4a` (factual brief and catalog decision); final blocked-review/handoff commit recorded by `HEAD`.
- Objective: close every P0 preservation and consistency exception or stop with the exact inaccessible dependency documented.
- Completion verdict: `blocked`; implementation is complete locally, but remote LFS preservation and remote clean-checkout reproduction are not established.
- Deliverables: W008 specification; Git LFS attributes; 11 INEP packages; 11 exact XLSX inputs; complete large-source manifest; stable paths in the administrative manifest; INEP and repository validators; pinned reproduction dependencies; updated preservation/audit documentation; refreshed factual assembly brief; D011 catalog-scope decision; this review and handoff.
- Primary files: `.gitattributes`; `administracao/dados/inep/fontes/manifesto-fontes-volumosas.csv`; `administracao/dados/fontes.csv`; `scripts/validate_inep_sources.py`; `scripts/validate_repository.py`; `assembleia/subsidio-factual-preliminar.md`; `governance/DECISIONS.md`; `governance/reviews/W008-p0-preservation-consistency.md`.
- Sources added: 11 exact official INEP ZIP packages (697 MiB) and their 11 exact XLSX members (401 MiB), all under `administracao/dados/inep/fontes/` and tracked by Git LFS.
- Coverage reached: all 11 W006 national input vintages from 2010-2019 through 2020-2024 have package and spreadsheet bytes, stable paths, SHA-256, official MD5 linkage, version range, provenance, purpose, and preservation status locally.
- Validation and result: package integrity/membership/MD5 passed 11/11; repository validator passed with 0 warnings and 0 errors; W006 regenerated 85 observations and three byte-identical outputs; clean local clone materialized all LFS objects and passed both validators; remote push failed before transfer due locked SSH authentication.
- Gaps: remote branch and LFS objects are not published; a remote clean clone cannot yet reproduce the evidence. The GitHub LFS quota/acceptance also remains unproven until authenticated upload succeeds.
- Divergences: no source-byte or extraction divergence. The INEP TLS chain was not trusted by the local client during recapture; exact prior SHA-256 and official MD5 identity checks passed and the limitation is recorded.
- Provisional information: the LFS endpoint is configured at the GitHub repository and the local clean-clone workflow works; remote capacity and download behavior are indeterminate until authenticated transfer.
- Explicitly not performed: no integration into `main`; no update of global roadmap/work indexes; no P1 work; no curricular evaluation, proposal design, or inference from documentary absence.
- Recommended next bounded work unit: resume W008 only after a human unlocks an authorized SSH key or configures authorized Git transport; push the existing branch, clone from `origin` with Git LFS enabled, rerun all validations, amend the review/handoff with the evidence, and integrate only if the verdict becomes approving.
