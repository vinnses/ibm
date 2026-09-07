# Extraction status register

Checkpoint N3 of W028. This register reports the state of source families already present in the repository. A `structured` row means that a repository dataset or explicit register exists for the named factual scope; it does not mean that every field in every original source has been extracted. `partially_structured` means that only a bounded subset, transcription, index or source metadata is structured. `deferred_access` requires an authorized document or custodian. `deferred_tooling` requires the mandated runtime/tooling. `not_applicable` is used only where the family is outside the axis.

No source was contacted, downloaded or re-searched in N3. Exact source identity and preservation remain in the linked manifests/catalogs.

## Curriculum 2011

| Source family | Status | Repository evidence | Next action |
| --- | --- | --- | --- |
| Formal resolution and PPC | `structured` | [resolution](../..//curriculos/2011/fontes/resolucao-34-2010-cepe.pdf), [PPC](../..//curriculos/2011/fontes/ppc-2011.pdf), [components](../..//curriculos/2011/inventario/componentes.csv), [dependencies](../..//curriculos/2011/inventario/dependencias.csv), [electives](../..//curriculos/2011/inventario/optativas.csv) | Use these structured fields as the formal baseline; retain originals for any field-level verification. |
| Formal ementas and divergence notes | `structured` | [ementas](../..//curriculos/2011/inventario/ementas.csv), [divergences](../..//curriculos/2011/inventario/divergencias.csv) | Preserve source locator and version when consuming a row; do not resolve divergences in N3. |
| Ementário HTML representations | `partially_structured` | [preserved pages](../..//curriculos/2011/fontes/ementario/), [source manifest](../..//curriculos/2011/fontes/manifesto.csv) | Extract only a specifically selected field with its page locator; applicability and historical offering unit remain open. |
| Ficha 1 public search and preserved indeterminate record | `partially_structured` | [Ficha manifest](../..//curriculos/2011/fichas/manifesto.csv), [search register](../..//curriculos/2011/inventario/buscas-negativas.csv), [W022–W024 registers](../..//curriculos/2011/fichas/) | Keep search evidence and applicability separate; do not assign the located later/indeterminate Ficha to 2011. |
| Historical Ficha 2 by term/class | `deferred_access` | [bounded search record](../..//curriculos/2011/inventario/buscas-negativas.csv), [W009 human review](../..//governance/human-reviews/W009-p1-curriculum-2011.md) | Request authorized term/class-specific originals and validity metadata if this data is later required. |

## Curriculum 2023

| Source family | Status | Repository evidence | Next action |
| --- | --- | --- | --- |
| Formal resolutions and PPC | `structured` | [Resolução 75/22](../..//curriculos/2023/fontes/resolucao-75-22-cepe.pdf), [2023 PPC](../..//curriculos/2023/fontes/ppc-2023.pdf), [components](../..//curriculos/2023/inventario/componentes.csv), [dependencies](../..//curriculos/2023/inventario/dependencias.csv) | Use the formal inventories and originals as the matrix baseline; retain each resolution separately. |
| Electives and regulations | `structured` | [electives](../..//curriculos/2023/inventario/optativas.csv), [regulations](../..//curriculos/2023/inventario/regulamentos.csv), [ementas](../..//curriculos/2023/inventario/ementas.csv) | Consume only recorded fields and source versions; no curricular comparison is part of N3. |
| Preserved Ficha 1/Ficha 2 PDFs and derived indexes | `partially_structured` | [original Fichas](../..//curriculos/2023/fichas/), [preserved Ficha tables](../..//dados/curriculos/2023/fichas-preservadas/), [DInf manifest](../..//curriculos/2023/fichas/manifesto-dinf.csv), [other-department manifest](../..//curriculos/2023/fichas/manifesto-outros-departamentos.csv) | Treat Ficha 1 and Ficha 2 separately; record document date/term/class before using any field. |
| Ementário and departmental HTML representations | `partially_structured` | [preserved pages](../..//curriculos/2023/fontes/), [applicability/search register](../..//curriculos/2023/inventario/buscas-negativas.csv) | Keep the portal representation as a source with uncertain/stale applicability; do not use it to overwrite the formal resolution/PPC. |
| Applicable Ficha 1 and term/class Ficha 2 not publicly established | `deferred_access` | [W010 human review](../..//governance/human-reviews/W010-p1-curriculum-2023.md) | Obtain authorized version/applicability and term/class records if a later documentary need requires them. |

## Administrative history and data

| Source family | Status | Repository evidence | Next action |
| --- | --- | --- | --- |
| UFPR applicant, entrant, vacancy and demand datasets | `structured` | [UFPR datasets](../..//administracao/dados/ufpr/), [W026 applicants](../..//dados/administracao/candidatos-historicos.csv), [W026 manifest](../..//administracao/dados/ufpr/w026/manifesto.csv) | Keep course totals, category-specific counts, vacancies and entrants as separate universes. |
| INEP trajectory row/cohort/annual datasets | `structured` | [trajectory rows](../..//administracao/dados/inep/trajetoria_informatica_biomedica_ufpr.csv), [cohort summary](../..//administracao/dados/inep/trajetoria_informatica_biomedica_ufpr_resumo_coortes_2011_2020.csv), [annual series](../..//administracao/dados/inep/trajetoria_informatica_biomedica_ufpr_serie_anual_2011_2020.csv) | Use the existing schema and keep annual and cumulative indicators separate. |
| INEP official packages and workbooks | `partially_structured` | [official packages](../..//administracao/dados/inep/fontes/pacotes/), [official workbooks](../..//administracao/dados/inep/fontes/planilhas/), [INEP manifest](../..//administracao/dados/inep/fontes/manifesto-fontes-volumosas.csv) | If a specific field is needed, cite workbook/package, sheet or file locator and extraction method; do not claim full workbook extraction. |
| Historical acts, transitions and evaluations | `partially_structured` | [transitions](../..//administracao/historico/transicoes.csv), [evaluations](../..//administracao/historico/avaliacoes.csv), [source manifest](../..//administracao/historico/fontes/manifesto.csv), [act register](../..//administracao/historico/atos-originais/registros.csv) | Keep evidence class and primary-act status visible; do not promote registry summaries to original acts. |
| Bounded public searches | `structured` | [historical negative searches](../..//administracao/historico/buscas-negativas.csv), [W026 searches](../..//administracao/dados/ufpr/w026/buscas.csv), [act searches](../..//administracao/historico/atos-originais/buscas.csv) | Use as limits and leads only; do not repeat without a new concrete lead. |
| CPA evaluation workbook | `deferred_tooling` | [CPA page](../..//administracao/historico/fontes/paginas/cpa-avaliacao-cursos-2022-2026-09-04.html), [CPA workbook](../..//administracao/historico/fontes/documentos/cpa-avaliacao-curso-informatica-biomedica-2022.xlsx) | Extract only after the mandated spreadsheet runtime is available; do not substitute another authoring/extraction stack. |
| Final occupancy and comparable cutoff data | `deferred_access` | [W011 human review](../..//governance/human-reviews/W011-p1-admin-procedure.md), [bounded search](../..//administracao/historico/buscas-negativas.csv) | Request matched process/category/call universes and definitions; never derive occupancy from mismatched public fragments. |

## 2026 proposal

| Source family | Status | Repository evidence | Next action |
| --- | --- | --- | --- |
| Internal call and proposal form | `partially_structured` | [Edital](../..//administracao/mec/2026/edital-01-2026-prograp-proplad.pdf), [proposal form](../..//administracao/mec/2026/apendice-b-proposta-informatica-biomedica.pdf), [source records](../..//administracao/historico/fontes/manifesto.csv) | Preserve proposal claims as claims and extract a field only with an explicit document locator; no later state is inferred. |
| Public contextual page | `partially_structured` | [UFPR context page](../..//administracao/mec/2026/fontes-complementares/ufpr-dialogo-edital-01-2026.html) | Use only for the page's documented context and preserve its date/URL; it is not proof of approval or implementation. |
| Proposed matrix, PPC, equivalences and staffing acts | `deferred_access` | [W011 human review](../..//governance/human-reviews/W011-p1-admin-procedure.md), [bounded search](../..//administracao/historico/buscas-negativas.csv) | Request the named originals and process linkage from an authorized custodian. |
| Later selection, approval, authorization and implementation acts | `deferred_access` | [transition register](../..//administracao/historico/transicoes.csv), [W011 human review](../..//governance/human-reviews/W011-p1-admin-procedure.md) | Preserve the corresponding act before changing the administrative state; proposal text alone is insufficient. |

## Counts and interpretation

The W027 snapshot contains 204 indexed dataset records, 191 source-manifest records and 33 gap/search records. These are catalog-record counts, not counts of unique documents, unique sources or completeness. This register adds no CSV rows and does not assert that every field of any original source has been extracted.

## W029 closure update

W029 reviewed all eight formerly `partially_structured` families. Six are closed for further agent-only extraction because useful stable fields are already represented or, for the 2026 call/proposal, were added in `dados/extracoes-w029/proposal-2026.json`. The 2023 Ementário/departmental family remains partial pending authoritative applicability evidence. INEP packages remain partial for unspecified future fields, while CPA remains `deferred_tooling`. These states do not imply source exhaustiveness.
