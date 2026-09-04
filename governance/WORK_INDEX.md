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
| W012 | Auditable agent error and human-review trail | Complete | `88ded6d`, `fcd9aa8`, `f314806`, `d78ac14`, `2495074`, `2148744`; merged by `403ceac` | Error-record specification, W008-W012 event logs, separate human-review questions, stakeholder hypothesis record, audit validator | W009-W011 correction events remain open in their own P1 branches |

## Source and review indexes

- General source catalog: [`../fontes/catalogo.csv`](../fontes/catalogo.csv)
- Administrative source manifest: [`../administracao/dados/fontes.csv`](../administracao/dados/fontes.csv)
- DInf Ficha manifest: [`../curriculos/2023/fichas/manifesto-dinf.csv`](../curriculos/2023/fichas/manifesto-dinf.csv)
- Other-department Ficha manifest: [`../curriculos/2023/fichas/manifesto-outros-departamentos.csv`](../curriculos/2023/fichas/manifesto-outros-departamentos.csv)
- Administrative audit: [`../administracao/dados/AUDITORIA.md`](../administracao/dados/AUDITORIA.md)
- 2026 claim matrix: [`../administracao/mec/2026/matriz-validacao-alegacoes.md`](../administracao/mec/2026/matriz-validacao-alegacoes.md)

The general catalog is an initial global index, not a complete union of every local manifest.
