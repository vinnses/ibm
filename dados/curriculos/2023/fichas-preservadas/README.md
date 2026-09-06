# W020 — Remaining preserved Ficha 1 records

This checkpoint publishes the 13 preserved Ficha 1 PDFs not represented by W018 or W019:

`CI1068`, `CI1162`, `CI1163`, `CI1171`, `CI1209`, `CI1212`, `CI1218`, `CI1221`, `CI1316`, `CI1350`, `BF114`, `BQ083`, and `MN162`.

## Method and scope

- The records use the W018/W019 field structure and are one row per distinct preserved Ficha 1 PDF.
- Only local preserved PDFs, local manifests, `curriculos/2023/fichas/inventario-dinf.md`, and the W010 inventory were used. No web retrieval or new source was used.
- Existing normalized DInf ementas were reused and checked against `pdftotext -layout` plus visual renders. External-department ementas were transcribed directly from the preserved PDFs because no normalized external transcription exists in the DInf inventory.
- Title, ementa, total-hours, unit/department, and date locators identify the exact PDF page and field/section. Missing document dates are explicitly `not stated`.
- Multiple electronic-signature dates are retained in `signature_date` separated by `; `. PDF footer/header timestamps that identify rendering/export time are not treated as document dates.
- `source_total_hours` records the source-stated total; BF114's source `60h` is represented as numeric `60` to match the W018/W019 schema.
- `applicability_2023` is `indeterminado` for every row. The MN162 record is explicitly not upgraded despite the existing note that its 2019 Ficha predates formal code creation; that is a gap/conflict, not evidence of 2023 applicability.
- Source spellings, ligatures, capitalization differences, and external department labels are preserved or described in `normalization_notes`; the original PDFs remain authoritative.

W020 checkpoint B intentionally creates no Ficha 2 dataset. The validator combines this CSV with the W018 and W019 Ficha 1 CSVs and checks all 23 Ficha 1 records for schema, unique identity/path/URL, manifest agreement, and stored-byte hashes.

## Validation

Run from the repository root:

```bash
python scripts/validate_w020_fichas.py
python scripts/validate_w019_d01.py
python scripts/validate_w018_d01.py
python scripts/validate_w010_curriculum_2023.py
python scripts/validate_repository.py
python scripts/validate_governance_audit.py
git diff --check
git lfs fsck
```

This checkpoint does not modify PDFs, manifests, W010 data, review, handoff, global indexes, or `main`.
