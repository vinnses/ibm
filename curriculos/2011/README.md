# 2011 documentary inventory

This inventory reconstructs the 2011 curriculum as a historical unit. `inventario/componentes.csv` has exactly 41 targets: 37 coded components and four formal elective spaces. The normative structure, formal elective catalog, direct prerequisite edges, and Bloco A rule are transcribed from the preserved Resolução nº 34/2010-CEPE.

The current UFPR Ementário representation of course 96A is preserved separately. Its agreement with the resolution is useful for the portal's displayed offering units and for the fact that its ementa fields say `Não consta`; it is not treated as proof that an undated component record or later Ficha applied in 2011.

## Files

- `inventario/componentes.csv` — per-target status and formal attributes. `total_hours`, `weekly_total_hours` (the Anexo I `Tot.` column), and `credits` (the separate `Créd.` column) are distinct fields.
- `inventario/optativas.csv` — the 64 coded catalog entries in the resolution, not a record of actual offerings.
- `inventario/ementas.csv` — available ementa evidence and explicit non-location records.
- `inventario/dependencias.csv` — seven explicit edges plus the Article 2 §1 Bloco A rule. Its 26 targets are every inventory target outside the 15-member block: 22 coded components and four elective spaces. No block member is an endpoint. An elective-space row is conditional on a catalog discipline being selected and does not assert an offering.
- `inventario/divergencias.csv` — structured Article 1/Article 3 workload tension and the status of the review-reported calculation.
- `inventario/buscas-negativas.csv` — bounded public-search records.
- `fichas/manifesto.csv` — Ficha 1/Ficha 2 evidence without merging documents.
- `fontes/manifesto.csv` — provenance and SHA-256 records for all evidence used here.

## Interpretive limits

No Ficha 1 dated or versioned as applicable to the 2011 curriculum was located. The one located CI241 Ficha 1 is signed in 2025 and is retained only as `preserved_indeterminate`; its ementa is transcribed without assigning it to 2011. No term/class-specific Ficha 2 was located. These records establish only bounded public-search results, not nonexistence.

The resolution itself contains a graphic header inconsistency (`Resolução nº 39/09-CEPE` on later pages) while its title and repository provenance identify it as Resolução nº 34/2010-CEPE. This is preserved in the original and not silently corrected.

Article 1's Formação Profissional Geral heading says 840 hours, while Article 3 says 960 hours. Anexo I supports 840 for the 14 non-TCC 60-hour components and 960 when its 120-hour CI262 TCC is included. The act does not state whether the Article 1 heading excludes TCC; this is therefore classified as contradictory rather than resolved in `inventario/divergencias.csv`. The cross-review's reported 900-hour total is retained there as not reproduced from Anexo I, not as a source fact.
