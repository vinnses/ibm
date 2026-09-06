# W019 D01 batch 2 — Ficha 1 ementas

This checkpoint publishes the second five-record D01 Ficha 1 batch: `CI1005`, `CI1007`, `CI1056`, `CI1057`, and `CI1062`.

## Method and scope

- Source PDFs are unchanged preserved files under `curriculos/2023/fichas/dinf/`.
- Existing normalized ementas from `curriculos/2023/fichas/inventario-dinf.md` were reused, then checked against `pdftotext -layout` output and a visual render of page 1 for every PDF.
- All title, ementa, total-hours, unit/department, and date locators identify the PDF page and field/section used.
- `source_total_hours` is the source-stated `CH Total`; it is not calculated from weekly hours or component metadata.
- `document_date` is `not stated` for all five records because the form has no separate document-date field. `signature_date` records the electronic-signature date shown in each PDF.
- `applicability_2023` remains `indeterminado` for every row. A located Ficha 1 and a matching code/title do not establish continuity into the 2023 curriculum.
- Normalization is limited to spaces and line breaks. Existing inventory spellings and ligatures are retained where applicable. The CI1005 PDF shows `Disciplina::` and `CI 1005`; the CSV uses the normalized inventory/manifest code `CI1005` and records the source form in its locator and normalization note. The CI1057 PDF title uses lowercase `estruturas de dados`; the CSV follows the existing inventory title capitalization and records that normalization.

The CSV includes the source URL, local path, SHA-256, and field-level PDF locators. The work-specific validator checks the five-row scope, required metadata, CSV values against the existing W010 Ficha inventory and DInf manifest, and hashes the stored PDFs.

## Validation

Run from the repository root:

```bash
python scripts/validate_w019_d01.py
python scripts/validate_w018_d01.py
python scripts/validate_w010_curriculum_2023.py
python scripts/validate_repository.py
python scripts/validate_governance_audit.py
git diff --check
```

This checkpoint does not modify PDFs, manifests, W010 inventory files, global indexes, applicability assessments, review, or handoff records.
