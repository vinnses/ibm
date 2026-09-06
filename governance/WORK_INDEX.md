# Work Index

Status is assigned to the bounded milestone, not to the entire research axis.

| ID | Milestone | Status | Commits | Primary deliverables | Remaining boundary |
|---|---|---|---|---|---|
| W001 | Repository foundation and documentary method | Complete | `5a54eee`, `40f5ab6` | `README.md`, `metodologia/criterios-documentais.md` | Automation and governance were separate later work |
| W002 | 2011 formal curriculum reconstruction | Complete for formal structure | `3d93eba`, `80b438a` | `curriculos/2011/grade-curricular.md`, preserved resolution/PPC/pages | Electives, component inventory, Fichas, ementas, dependencies, and departmental validation remain |
| W003 | 2026 call and reorganization proposal capture | Complete for located initial documents | `c264a94`, `80b438a`, `5b5423d` | `administracao/mec/2026/`, validation matrix, preserved PDFs and official contextual page | Apêndice A, memorandum, deliberations, result, MEC act, new matrix/PPC/Fichas remain not located |
| W004 | 2023 formal curriculum reconstruction | Complete for formal structure | `f3b90fe`, `c019b6f`, `46fbeaf` | `curriculos/2023/grade-curricular.md`, primary acts, PPC, captured pages | Full electives, individual inventory, and regulatory documents remain |
| W005 | Initial 2023 Ficha capture and extraction | Complete for initial public set | `80b438a`, `8de7af8`, `6731c2a`, `ad1ce16` | 20 DInf Ficha 1, 16 DInf Ficha 2, 3 external Ficha 1, 1 external Ficha 2, manifests, extracted DInf ementas | Coverage and curriculum-specific validity remain incomplete |
| W006 | Administrative historical data | Complete for the bounded public-source search | `5b5423d`; merged by `c242270` | UFPR annual series, INEP cohorts 2011–2020, vacancy points, methods, scripts, audit, claim validation | Raw INEP packages are not repository-preserved; occupancy, complete applicant counts, evaluation data, and older acts remain |
| W007 | ChatGPT Work consolidation and local Codex governance | Complete | `4421965`, `af8437a`; merged by `d3ac930` | `AGENTS.md`, `governance/`, repository validator, corrected hashes | Future work must follow the new contracts |
| W008 | P0 preservation and consistency closure | Complete | `5b05d11`, `d8b0d06`, `d70bd4a`, `9b1dea5`, `989722c`; merged by `fdeef13` | 11 INEP packages and 11 exact XLSX inputs in Git LFS, stable manifests, reproducibility checks, updated assembly brief, D011 catalog decision | Git LFS is required to materialize large sources; P1 inventories remain separate work |
| W009 | 2011 documentary inventory | Complete with documented public-source exceptions | `70b129f`, `829ac83`, `9ab39b5`, `24fda02`, `b7c998d`, `50db1b9`, `c3ab97b`; merged by `267011f` | 41-target inventory, elective catalog, ementas, dependencies, bounded Ficha searches, workload-conflict record, validator, review, and handoff | Historical applicable Fichas and institutional confirmation of offering units remain human-review questions; absence is not asserted |
| W011 | Administrative and procedural history extension | Complete for the bounded public-source scope | `251cb46`, `8565b6d`, `b65d57f`, `41cd390`, `4fbc4fd`, `ae67c19`, `61e0c30`, `806a065`; merged by `92b3f4c` | Preserved 2022 CEPE minute, transition/evaluation datasets, negative-search log, validator, review, and handoff | Protected 2026 process records, original acts, and matched occupancy/cutoff evidence remain explicit human-review/public-source gaps |
| W012 | Auditable agent error and human-review trail | Complete | `88ded6d`, `fcd9aa8`, `f314806`, `d78ac14`, `2495074`, `2148744`; merged by `403ceac` | Error-record specification, W008-W012 event logs, separate human-review questions, stakeholder hypothesis record, audit validator | Later Works append their own events; W010 remains outside `main` pending final review |
| W013 | Binding model routing and primary-session authority | Complete | `eedbaae`, `8204236`, `3e37081`, `4ad0d41`, `7a16bc0`; merged by `a783dc3` | Sol-primary-session rule, Luna/Terra routing, mandatory assignment provenance, prospective validator, review, and handoff | Historical model assignments without provenance remain unknown and are not reconstructed |

## W010 integration — 2026-09-05

| ID | Milestone | Status | Commits | Primary deliverables | Remaining boundary |
|---|---|---|---|---|---|
| W010 | 2023 documentary inventory and P1 closure | Complete with documented exceptions | `61be19b`, `838cd79`, `82b7eb7`, `7405e16`; resumed through `6483fa0`, `6411ecd`, `94415ae`, `0392c8c`, `6ae22e5`, `75b4ee4`, `6c07a5d`, `0518f67`, `ee2a240`; merged by `750df8b` | 43-target inventory, 92 formal electives, 21 dependencies, 40 separate Ficha records, regulations, source manifests, validator and six regression tests, independent review and final handoff | HR-W010-001/002/003 limit P2 reconciliation and P3 source-supported comparison; C-W010-003 through C-W010-006 are nonblocking deferred corrections; P2 not started |

The W012 row's statement that W010 was outside `main` describes the W012 integration stage; it is superseded by this W010 integration record. P1 is now complete only for the approved bounded documentary scope of W009, W010 and W011. See `governance/corrections/W010.md` for consolidated nonessential follow-ups.

## Source and review indexes

## Data-first checkpoints — 2026-09-05

| ID | Status | Saved commits | Output / remaining boundary |
|---|---|---|---|
| W014 | Complete; integrated | `478268c`, `1db440e`; merge `20fa763` | Data-first direction and per-step restart plan in `governance/DATA_FIRST.md`; analytical P2-P4 execution deferred |
| W015 | Complete with documented access-snapshot limits; integrated | `b174421`, `feaaf0c`, `03f129c`; merge `90929c0` | Existing-data index; integration refresh covers 36 datasets, 191 source records and 33 recorded gaps/searches; no claim of exhaustive underlying data |
| W016 | Complete bounded batch with documentary exceptions; integrated | `91bdd4c`, `6501723`, `9f94e37`, `6fef8d5`; merge `241204b` | Portaria 44/2015 institutional reproduction plus one annex record; COUN original not located; original DOU facsimile remains pending |

## Source access links

W018 D01 first Ficha 1 batch: complete with documented applicability/date gaps and integrated on 2026-09-05. Commits `4c428d8`, `5dbce54`, `edbf444`; merge `d94900e`. Deliverable: five source-located records for CI1001, CI1002, CI1003, CI1055 and CI1215 plus validator. All 2023 applicability values remain indeterminate; HR-W010-001 remains. Access package refreshed afterward; no second batch started.

W017 remaining-data planning: complete and integrated on 2026-09-05, plan `61702d3`, merge `f3f9d4e`. Deliverable: `governance/REMAINING_DATA.md`, with D01-D09 selectable batch boundaries. All batches remain unstarted pending the user's choice; no new collection or analysis was performed.

- General source catalog: [`../fontes/catalogo.csv`](../fontes/catalogo.csv)
- Administrative source manifest: [`../administracao/dados/fontes.csv`](../administracao/dados/fontes.csv)
- DInf Ficha manifest: [`../curriculos/2023/fichas/manifesto-dinf.csv`](../curriculos/2023/fichas/manifesto-dinf.csv)
- Other-department Ficha manifest: [`../curriculos/2023/fichas/manifesto-outros-departamentos.csv`](../curriculos/2023/fichas/manifesto-outros-departamentos.csv)
- Administrative audit: [`../administracao/dados/AUDITORIA.md`](../administracao/dados/AUDITORIA.md)
- 2026 claim matrix: [`../administracao/mec/2026/matriz-validacao-alegacoes.md`](../administracao/mec/2026/matriz-validacao-alegacoes.md)

The general catalog is an initial global index, not a complete union of every local manifest.
