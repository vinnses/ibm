# W029 — preserved-source extraction closure

This directory records the final review of the eight `partially_structured` source
families listed in `dados/entrega-documental/STATUS_EXTRACAO.md`.

The review was documentary only. It did not assign Ficha applicability, compare
curricula, infer equivalences, promote the 2026 proposal beyond `proposal`, or
alter an original source, CSV, XLSX, or existing manifest. The mandated
spreadsheet runtime was unavailable, so no workbook extraction was attempted.

## Result

One new machine-readable factual output was warranted:

- [`proposal-2026.json`](proposal-2026.json) records explicit identification,
  procedure, and proposal fields from the preserved Edital 01/2026 and Apêndice
  B, with page locators and source hashes. Proposal claims remain claims of the
  proposal; the JSON does not establish selection, approval, authorization, or
  implementation.

No new source was located or downloaded. Consequently, no new source manifest
was required. All inputs below were already preserved and manifested elsewhere.

## Family-by-family review

| Family | Inspected inputs | Existing structured outputs | New output | Status after review | Rationale |
| --- | --- | --- | --- | --- | --- |
| 2011 Ementário HTML representations | `curriculos/2011/fontes/ementario/`; its source manifest; 37 component pages | `curriculos/2011/inventario/componentes.csv`; `ementas.csv`; `divergencias.csv` | None | closed for agent extraction | The component pages state the already-recorded portal result (`Não consta`) or metadata already represented in the inventories. No additional stable field was found that would not duplicate those tables. Historical offering-unit and applicability questions remain open. |
| 2011 Ficha 1 public search and indeterminate record | `curriculos/2011/fichas/manifesto.csv`; W022–W024 search registers; `ficha-1-indeterminada/CI241-ficha-1-2025-3-periodo.pdf` | `curriculos/2011/inventario/componentes.csv`; `ementas.csv`; W022–W024 manifests and negative-search logs | None | closed for agent extraction; applicability remains indeterminate | The only preserved Ficha 1 is already indexed with its 2025 signature and indeterminate 2011 applicability. Search logs already record the bounded negative results. No term/version evidence permits a new 2011 fact. |
| 2023 preserved Ficha 1/Ficha 2 PDFs and derived indexes | `curriculos/2023/fichas/`; `dados/curriculos/2023/fichas-preservadas/`; DInf and other-department manifests; derived index | `curriculos/2023/inventario/ementas.csv`; `componentes.csv`; `dados/curriculos/2023/fichas-preservadas/fichas-1-restantes.csv`; `fichas-2.csv`; `inventario-dinf.md` | None | closed for agent extraction; applicability remains indeterminate where recorded | The 40 preserved documents, document type, dates, hashes, normalized ementas, and applicability limits are already represented. No new extraction can establish 2023 applicability from a code/title match. |
| 2023 Ementário and departmental HTML representations | `curriculos/2023/fontes/`; preserved departmental pages; `curriculos/2023/inventario/buscas-negativas.csv` | `curriculos/2023/inventario/ementas.csv`; component inventory; search register | None | remains partial | The pages provide portal representation and search context, but no authoritative version/applicability fact beyond the existing records. The authoritative formal baseline remains the resolution/PPC. |
| INEP official packages and workbooks | `administracao/dados/inep/fontes/pacotes/`; `planilhas/`; volumous-source manifest; existing trajectory outputs | `trajetoria_informatica_biomedica_ufpr.csv`; cohort summary; annual series; source manifest | None | remains partial / tooling-sensitive | Existing row, cohort, and annual outputs cover the stable fields already used. Full workbook/package extraction would require a specific field and mandated tooling; no materially useful unstructured field was identified in this closure. No alternate spreadsheet stack was used. |
| Historical acts, transitions and evaluations | `administracao/historico/transicoes.csv`; `avaliacoes.csv`; `series-complementares.csv`; source manifests; W029 act registers | those three registers, original-act registers, W029 act/evaluation records | None | closed for agent extraction; original-act gaps remain | Dates, stages, source classes, the 2022 CEPE minute, the registry concept, CPA provenance, and applicant/vacancy observations are already structured. Missing originals remain `not located`, not reconstructed from registry summaries. |
| 2026 internal call and proposal form | preserved Edital 01/2026 and Apêndice B PDFs | prose README, validation matrix, transition register | [`proposal-2026.json`](proposal-2026.json) | closed for agent extraction | Explicit document fields were useful in machine-readable form and were not represented as a dedicated factual JSON. Proposal assertions are labelled as proposal-stated and retain page locators. |
| 2026 public contextual page | `administracao/mec/2026/fontes-complementares/ufpr-dialogo-edital-01-2026.html`; source manifest; validation matrix | proposal axis README; claim-validation matrix; source manifest | None | closed for agent extraction; contextual only | The page's date, URL, provenance and limited contextual role are already recorded. It does not add course-specific selection, approval, authorization, implementation, matrix, or staffing facts. |

## Evidence boundary

The new JSON contains direct transcriptions of preserved documents only. It is
not a curricular comparison or an equivalence map. The absent proposed matrix,
equivalence table, SEI process, institutional decisions and later acts remain
protected or not-located gaps documented in the release.

Validation command:

```text
python scripts/validate_w029_preserved_extractions.py
```
