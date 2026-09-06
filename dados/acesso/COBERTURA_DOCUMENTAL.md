# Documentary coverage inventory

Generated mechanically by `scripts/build_w027_documentary_inventory.py` from the three access catalogs.

## Reading rules

- Counts below are catalog records. They are not counts of unique documents, unique sources, or completeness.
- Source-manifest rows are retained as recorded; duplicate identities, conflicting metadata, Ficha 1/Ficha 2 versions, and different statistical universes are not merged.
- A local path, URL, hash, or catalog row does not by itself establish applicability, approval, implementation, or historical completeness.
- `path exists` is checked against the current repository checkout; it describes accessibility, not evidentiary sufficiency.

## Current catalog totals

| Catalog | Record count | Meaning |
| --- | --- | --- |
| datasets.csv | 204 | dataset index records |
| source-records.csv | 191 | preserved/source-manifest records |
| gaps.csv | 33 | recorded gap or bounded-search records |
| datasets.csv declared rows | 1161 | rows declared by indexed datasets |

## Dataset records by scope

| Scope | Dataset records | Declared rows |
| --- | --- | --- |
| administrative data or historical series | 20 | 294 |
| curriculum inventory or formal structure | 12 | 384 |
| curated global source catalog | 1 | 10 |
| repository dataset | 171 | 473 |

## Dataset records by top-level documentary axis

| Axis | Dataset records | Declared rows |
| --- | --- | --- |
| Curricular | 183 | 852 |
| Administrative | 20 | 299 |
| Propositive | 0 | 0 |
| Cross-cutting | 1 | 10 |

### Axis interpretation

The axis is a deterministic path-based display grouping, not a claim that a record belongs exclusively to one historical question.

| Axis | Included path cues |
| --- | --- |
| Curricular | curriculum, Ficha, ementa |
| Administrative | administracao, INEP, UFPR, historico |
| Propositive | proposta, chamada, feasibility |
| Cross-cutting | remaining catalog paths |

## Source-record preservation and path availability

| Measure | Records |
| --- | --- |
| Source records | 191 |
| Local path recorded | 191 |
| Recorded local path exists | 191 |
| Source URL recorded | 178 |
| SHA-256 recorded | 191 |

### Source records by documentary axis

| Axis | Records |
| --- | --- |
| Curricular | 106 |
| Administrative | 82 |
| Propositive | 3 |
| Cross-cutting | 0 |

### Recorded source status

| Status | Records |
| --- | --- |
| downloaded | 40 |
| preservado | 12 |
| preserved | 62 |
| preserved_indeterminate | 1 |
| preserved_lfs | 22 |
| versionado | 30 |
| versionado_lfs | 22 |
| versionado_origem_fornecida | 2 |

### Recorded source document type

| Document type | Records |
| --- | --- |
| CEPE_chamber_minute | 1 |
| CPA_evaluation_workbook | 1 |
| Ficha 1 | 1 |
| HTML index | 1 |
| HTML index page | 1 |
| HTML page | 49 |
| PPC | 4 |
| Resolution | 1 |
| Resolução | 6 |
| admission_notice | 1 |
| derived_dataset | 1 |
| documento | 14 |
| ficha-1 | 23 |
| ficha-2 | 17 |
| institutional reproduction of act | 1 |
| internal call | 1 |
| md5_oficial | 11 |
| official_data_package | 11 |
| official_extracted_spreadsheet | 11 |
| pagina_html | 7 |
| planilha_dados_oficial | 11 |
| proposal form | 1 |
| proposal_form | 1 |
| report | 1 |
| resolution | 3 |
| zip_dados_oficial | 11 |

## Gap records

| Measure | Records |
| --- | --- |
| Gap records | 33 |

### Gap records by documentary axis

| Axis | Records |
| --- | --- |
| Curricular | 11 |
| Administrative | 22 |
| Propositive | 0 |
| Cross-cutting | 0 |

### Gap type

| Gap type | Records |
| --- | --- |
| institutional_access | 8 |
| public_documentary | 25 |

### Gap status

| Status | Records |
| --- | --- |
| pending human access decision. | 6 |
| pending human clarification; not a substitute for the agent correction. | 1 |
| pending human data-access decision. | 1 |
| recorded search; see original result and limits | 25 |

## Documentary-delivery lanes

- Repository-local extraction: use already preserved files and indexed datasets; do not alter the three input catalogs in this inventory task.
- Concrete public lead: pursue only a specific, bounded lead recorded in the gap/search material; preserve any newly used source before extraction.
- Institutional or user access: obtain records listed as institutional-access or requiring human clarification; the absence of a public record is not proof of nonexistence.
- Documentary freeze: after the data-delivery batches, validate manifests, hashes, paths, version separation, and reproducibility. This is a documentary gate, not curricular analysis.
- Comparative P3 and analytical P4 work remain future work requiring direct user participation and cannot begin implicitly from this inventory.

## Rebuild and check

```text
python scripts/build_w027_documentary_inventory.py
python scripts/build_w027_documentary_inventory.py --check
python scripts/validate_w027_documentary_inventory.py
```

The builder uses only Python's standard library, reads the three CSV inputs as UTF-8, sorts every displayed category deterministically, and writes the generated Markdown with a final newline. The validator compares a freshly rendered result byte-for-byte with the committed Markdown and checks the input record totals.
