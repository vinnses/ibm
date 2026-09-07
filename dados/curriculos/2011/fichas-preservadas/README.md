# W030 historical Ficha extraction

This directory contains a reproducible, literal extraction of the twelve PDF
records preserved by W022-W024. The original PDFs remain under
`curriculos/2011/fichas/` and are not modified.

`documents.csv` carries document identity, manifest provenance, source URL,
source SHA-256, applicability status, and the raw-text locator. The exact
document type and status are copied from the work manifest; in particular,
`W022-CI055-OLDER-COMPONENT` remains an undesignated component document.

`raw-text/*.json` preserves page-numbered text produced with `pdftotext -layout`.
`normalized-fields.csv` contains only literal fields detected in that text,
with page locators. Empty fields mean that the field was not present in the
extracted source; no values, denominators, or curriculum applicability are
inferred. `extraction-inventory.json` records the twelve-document/page count.

Reproduce and validate with:

```text
python scripts/extract_w030_historical_fichas.py
python scripts/validate_w030_historical_fichas.py
```

The extractor reads the seven W022-W024 manifests listed in the script and
requires the manifest SHA-256 to match the preserved source before producing
outputs.
