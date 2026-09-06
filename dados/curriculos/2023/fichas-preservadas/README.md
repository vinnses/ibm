# W020 — Preserved Ficha 1 and Ficha 2 records

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

W020 checkpoint B intentionally created no Ficha 2 dataset. Its 13 Ficha 1 rows remain in this directory, and checkpoint C adds the separate Ficha 2 dataset below.

## Checkpoint C — Ficha 2

`fichas-2.csv` contains exactly one row for each of the 17 preserved Ficha 2 PDFs: 16 DInf records and the external-department `MN129` record. Ficha 2 versions are not merged with Ficha 1 or with one another. The row schema is:

- identity: `document_id`, `document_kind`, `code`, `source_title`;
- version/context: `term_or_period`, `class_identifier`, `plan_version`, `document_date`, `applicability_2023`;
- source-stated content: `unit_department`, `permanent_fields`, `ementa`, `program`, `objectives`, `method`, `evaluation`, `bibliography`, and `teacher_fields`;
- provenance: `source_path`, `source_sha256`, `source_url`, `source_locators`, and `normalization_notes`.

`permanent_fields` records the source table's hours, prerequisite/corequisite, modality, and period nature. `not stated` is used where the source does not state a value; `indeterminado` is retained for curriculum applicability. `source_locators` identifies the PDF page and section for every field group. Long bibliographic sections are represented by source-stated title groups or an explicit source-stated presence statement plus page locator; the preserved PDF remains authoritative for the complete list. The external MN129 row retains the source's `2022.1` term, Nursing department, 45 total hours, and responsible teacher without treating it as a 2023 offering.

Checkpoint C extends validation to all 40 preserved PDFs exactly once: 23 Ficha 1 rows from W018/W019/W020 and these 17 Ficha 2 rows. It checks cross-kind source-path/URL/identity uniqueness, manifest agreement, SHA-256 values, and stored PDF bytes for both DInf and external manifests.

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
