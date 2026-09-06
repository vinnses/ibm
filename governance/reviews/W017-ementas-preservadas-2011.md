# W017 preserved 2011 ementa evidence review — 2026-09-06

- Reviewer assignment (primary/subagent, model, effort, routing rationale): primary / GPT-5 family exposed by the Codex Work runtime / active effort not exposed / final source review and logical consolidation remain primary-session duties. Read-only supporting checks were performed by `/root/w017_extract` (`gpt-5.6-luna`, medium) for mechanical extraction/hashes and `/root/w017_reconcile` (`gpt-5.6-terra`, medium) for independent applicability/version assessment.
- Reviewed branch: `work/w017-ementas-preservadas-2011`.
- Reviewed base: `3530173f374d0c361e9f8829d3347c638b21a7db`.
- Reviewed commits: `2605e59`, `7ffe196`, `1a5a3a3`.
- Verdict: approved for the requested preserved-material extraction, with two open upstream W009 correction events that do not alter W017 evidence or coverage.

## Scope and source review

The output matches the exact W009 universe of 37 coded components and four elective spaces; no component was added from a later document. Repository-wide Ficha manifests and filenames were checked for target-code overlap. The only in-scope Ficha 1 is CI241 in the preserved 2025 multi-course PDF. MN129 Ficha 2 from 2022.1 was correctly excluded by document type and scope.

All 37 Ementário component pages were parsed from preserved HTML. Each output path and SHA-256 agrees with `curriculos/2011/fontes/manifesto.csv`. Every page has a source-literal name, unit, type, workload, credits, and ideal-period value; every `Ementa` and `Objetivos` field displays `Não consta`; prerequisites and corequisites are not displayed. Their 2011 applicability remains `indeterminada` because the current portal representation has no historical validity date.

The CI241 PDF pages 24–25 were rendered and visually reviewed under the PDF procedure. Code/title, checked nature/modalities, CH total 60, weekly 04, PD 60, prerequisite `Não`, corequisite `Não`, ementa wording, unit header, and electronic signature date 2025-05-14 agree with `evidencias.csv`. No credit value is stated on the Ficha. Its applicability was not upgraded from `indeterminada`.

Resolução nº 34/2010-CEPE Anexo I pages 5–6 were also rendered and visually checked for the recorded metadata differences. The current portal's differing credit, nature, ideal-period, and displayed-name values are preserved separately and do not override the act. Visual review found three additional upstream W009 label defects, recorded as E-W017-106 and D-W017-012 through D-W017-014.

The 2010 PPC is correctly limited to context: it says Fichas 1 were annexed, but the preserved 32-page PDF ends without the annexes. No missing content was synthesized.

## Coverage and applicability

- 0 `evidencia_utilizavel`/complete targets.
- 36 `evidencia_parcial` coded targets.
- 1 `documento_aplicabilidade_indeterminada`: CI241.
- 0 `documento_contraditorio` targets for ementa/Ficha content.
- 4 `nenhuma_evidencia_preservada_suficiente` elective spaces.

The 40-row applicability register keeps two proven contextual/formal documents separate from 38 indeterminate content/portal records. No document of a different date or type is merged.

## Validation

- `python scripts/build_w017_ementas_2011.py --check` — passed.
- `python scripts/validate_w017_ementas_2011.py` — passed: 41 targets, 38 evidence rows, required coverage distribution.
- `python scripts/validate_w009_curriculum_2011.py` — passed as a regression check; its current expectations do not detect open E-W017-104/E-W017-106.
- `python scripts/validate_governance_audit.py` — passed after resolved E-W017-105 documented the first status-format failure.
- `python scripts/validate_repository.py` — passed with zero warnings/errors.
- `git diff --check` — passed.

## Exceptions and errors

Resolved events: E-W017-101 (identifier collision contained by unique slugs), E-W017-102 (clone yield/recovery), E-W017-103 (optional parser dependency replaced), and E-W017-105 (governance status formatting corrected). Open E-W017-104 and E-W017-106 concern inaccurate pre-existing W009 CI262 period/name and three additional W009 labels. W017 identifies targets by the accepted code set and explicitly labels carried names as `w009_target_label`, so these issues do not block the new source-specific extraction.

No external search, source modification, Ficha 2 extraction, curricular comparison, quality analysis, or integration was performed.
