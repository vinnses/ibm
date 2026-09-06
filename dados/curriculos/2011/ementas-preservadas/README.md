# Preserved 2011 ementa and Ficha 1 evidence

This directory exhausts the ementa and Ficha 1 information already preserved in the repository for the 41 W009 targets: 37 coded components and four elective spaces. It is a source-specific extraction, not a claim that the public record is complete.

## Outputs

- `evidencias.csv`: 38 version-separated evidence rows. Thirty-seven rows transcribe the current 96A Ementário component pages; one row transcribes the CI241 section of a 2025 multi-course Ficha 1 PDF.
- `cobertura.csv`: one mutually exclusive coverage status for every W009 target.
- `aplicabilidade.csv`: 40 applicability/version records: the 2010 resolution, the 2010 PPC, 37 current Ementário records, and the 2025 CI241 Ficha 1.
- `divergencias.md`: source-version metadata differences and the absence of competing ementa texts.
- `lacunas.md`: explicit documentary gaps and bounded next targets.
- `scripts/build_w017_ementas_2011.py`: reproducibly extracts the HTML fields and CI241 PDF ementa, then writes the three CSV files.
- `scripts/validate_w017_ementas_2011.py`: verifies target sets, status counts, source paths, stored-byte hashes, generated output, and the positive CI241 transcription.

## Preserved-source result

All 37 component HTML pages display `Não consta` in the `Ementa` field. They do preserve a literal displayed name, unit, nature, total workload, credits, and ideal course period. They do not display prerequisites or corequisites. The pages were captured on 2026-09-04, but neither the pages nor the source manifest state a historical version or validity date. Their applicability to the 2011 curriculum is therefore `indeterminada`; the records prove only what the preserved current 96A representation displayed at capture time.

The only preserved Ficha 1 for a W009 code is the CI241 section on PDF pages 24–25 of `curriculos/2011/fichas/ficha-1-indeterminada/CI241-ficha-1-2025-3-periodo.pdf`. It contains an ementa and permanent fields, but its electronic signature is dated 2025-05-14. Matching code and title do not establish continuity to 2011, so its applicability remains `indeterminada` and its ementa is not labeled as the 2011 ementa.

The 2010 PPC says in its final documentation section that Fichas 1 were annexed, but the preserved 32-page PDF ends without those annexes. The statement is retained as documentary context and does not supply missing Ficha contents.

## Coverage semantics

| Status | Count | Meaning in this dataset |
|---|---:|---|
| `evidencia_utilizavel` | 0 | An ementa/Ficha 1 is preserved and proven applicable to 2011. |
| `evidencia_parcial` | 36 | The formal target is proven and a current portal record is preserved, but it has no ementa and no applicable Ficha 1 is preserved. |
| `documento_aplicabilidade_indeterminada` | 1 | CI241 has a positive 2025 Ficha 1 whose applicability to 2011 is not established. |
| `documento_contraditorio` | 0 | Competing source versions establish contradictory ementa/Ficha content for 2011. |
| `nenhuma_evidencia_preservada_suficiente` | 4 | The target is an elective space; no selected coded component or component-level ementa/Ficha is identified. |

These categories are mutually exclusive and sum to 41. CI241's current portal row remains preserved as secondary partial evidence, but the positive later Ficha controls its coverage category under the priority rule: contradictory, indeterminate, usable, partial, insufficient.

## Transcription and normalization

`name_literal`, `ementa_literal`, `nature_literal`, and `unit_literal` preserve source wording and capitalization. For the CI241 ementa, layout line breaks are retained in `ementa_literal`; `ementa_normalized` only collapses whitespace. For Ementário rows, the literal field value `Não consta` is retained while `ementa_normalized` is empty so it cannot be mistaken for content. `unit_normalized` is separate from the literal unit string.

No source byte was changed, no new component was created, and documents of different dates were not merged. The formal resolution is used only as the 41-target context in `cobertura.csv` and `aplicabilidade.csv`; W009 remains the upstream target inventory.

## Reproduction and validation

```bash
python scripts/build_w017_ementas_2011.py --check
python scripts/validate_w017_ementas_2011.py
python scripts/validate_w009_curriculum_2011.py
python scripts/validate_governance_audit.py
python scripts/validate_repository.py
git diff --check
```

No external search was performed. The repository-wide Ficha manifests were checked for overlapping W009 codes. The only other match was MN129 Ficha 2 from 2022.1 under the 2023 curriculum tree; it is a different document type, has no established 2011 applicability, and is outside this Work.
