# W018 D01 — Ficha 1 ementas

This checkpoint publishes five source-located Ficha 1 records only: `CI1001`, `CI1002`, `CI1003`, `CI1055`, and `CI1215`.

## Method and scope

- Source PDFs are unchanged preserved files under `curriculos/2023/fichas/dinf/`.
- Existing normalized ementas from `curriculos/2023/fichas/inventario-dinf.md` were reused, then checked against `pdftotext -layout` output and a visual render of page 1 for every PDF.
- All title, ementa, total-hours, unit/department, and date locators identify the PDF page and field/section used.
- `source_total_hours` is the source-stated `CH Total`; it is not calculated from weekly hours or component metadata.
- `document_date` is `not stated` for all five records because the form has no separate document-date field. `signature_date` records the electronic-signature date when present. For `CI1003` and `CI1215`, the signature date is `not stated`; the page-footer timestamps are rendering timestamps and are not treated as document dates.
- `applicability_2023` remains `indeterminado` for every row. A located Ficha 1 and a matching code/title do not establish continuity into the 2023 curriculum.
- Normalization is limited to spaces and line breaks, except that the existing inventory transcription's literal `proﬁssional` ligature and `Politicas` spelling are retained in `CI1003`; the PDFs remain authoritative.

The CSV includes the source URL, local path, SHA-256, and field-level PDF locators. The work-specific validator checks the five-row scope, required metadata, CSV values against the existing W010 Ficha inventory and DInf manifest, and hashes the stored PDFs.

## Validation

Run from the repository root:

```bash
python scripts/validate_w018_d01.py
git diff --check
```

Checkpoint B does not modify PDFs, manifests, W010 inventory files, global indexes, or applicability assessments.
