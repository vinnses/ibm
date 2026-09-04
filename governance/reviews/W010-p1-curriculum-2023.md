# Cross-review — W010 P1 2023 curriculum inventory

- **Review date:** 2026-09-04
- **Branch reviewed:** `work/w010-p1-curriculum-2023`
- **Reviewed commits:** `61be19b`, `9f576f7`
- **Verdict:** **changes required**

## Scope and structural checks

The delivered files match the intended W010 surface and do not expand into comparison or proposal work. Independent CSV checks found exactly 43 unique component targets: 39 non-TCC components and four TCC alternatives. All 21 dependency endpoints are targets. The formal resolution and PPC samples support the 3,200-hour baseline, the four TCC alternatives, 320 ACE hours, 80 formative-activity hours, and the documented 17-component conjunctive barrier.

The Ficha records remain distinct by type and version. The collection does not improperly assign the pre-reform DInf Fichas to the 2023 curriculum: their applicability is `indeterminado`. The bounded public Ficha 1/Ficha 2 gaps are visible in every relevant component and negative-search records; on their own, those gaps satisfy the work unit's status-and-gap acceptance condition. They remain a P1 recovery front, not evidence of nonexistence.

## Required corrections

1. **The claimed stale Ementário source is not preserved at the manifested path.** `curriculos/2023/fontes/manifesto.csv` record `2023-EMENTARIO` claims URL `https://ementario.ufpr.br/ementario/curriculo.action?v=1225`, purpose “registro da divergência 3000h”, and local path `curriculos/2023/fontes/pagina-grade-semestral.html`. The preserved file instead identifies itself as “Grade Semestral 2025/2” and contains current codes such as CI1003, CI1068, and CI1055; it is not a capture of the cited Ementário page and does not establish a 3,000-hour representation. The accompanying README and handoff repeat the unsupported claim. This violates the required URL/path/provenance relation and leaves the stale-portal requirement unverified. Capture the actual Ementário response unchanged, manifest it with its own hash and correct path, then revise only source-supported descriptions. If it cannot be captured, record an unresolved preservation exception rather than asserting it is preserved.

2. **BQ083 is incorrectly dated and classified.** The `ementas.csv`, component inventory, and external-Ficha manifest describe BQ083 as a 2021-directory record that is contradictory because it predates the December 2022 creation act. The preserved PDF itself is a SEI Ficha 1 rendered 2022-06-09 and signed 2022-04-05. A URL directory is not the document date. The record needs its actual document date and a defensible applicability judgment. The preserved evidence establishes neither 2023 applicability nor a documentary contradiction solely from the date; `indeterminado` is the supported default unless a conflict is shown from content or an act.

3. **No reproducible W010 work-specific validator is delivered.** The handoff reports a target/uniqueness/applicability/dependency check, but the repository has no `validate_w010_*` script or documented command that independently executes those checks. W010 acceptance requires work-specific validation. Add a scoped validator (including manifest hashes, 43/39/4 counts, applicability states for pre-reform Fichas, dependency endpoints and cycles, and regulation coverage), or provide a committed reproducible equivalent.

## Other findings and exceptions

- The source sampling confirms CI1055’s preserved Ficha 1 says “Algoritmos e **Estruturas** de Dados 1”; `componentes.csv` says “Algoritmos e Estrutura de Dados 1”. Correct the transcription against the formal resolution/Ficha.
- BF114’s 2024 Ficha 1 is correctly retained as indeterminate rather than assigned to 2023, despite its matching code and title.
- MN162’s 2019 Ficha 1 is correctly not used as 2023 applicability evidence. Its chronology with the later code-creation act remains a documented issue.
- The public Ficha deficits and lack of 2023–2026 term/class-specific Ficha 2 records do not block this review by themselves because they are explicitly bounded, per-target, and not converted into claims of nonexistence. Their consequence is that the P1 documentary-completeness gate remains open. Roadmap destination: P1 2023 targeted recovery, then P2 reconciliation.

## Validation performed

- `python scripts/validate_repository.py` — passed: 18 CSV files, 126 preserved hashes, 88 local Markdown links; zero warnings and errors.
- Independent CSV/hash check — passed: 43 unique targets, 39 non-TCC plus four TCC alternatives, 21 valid dependency endpoints, 53 valid source/Ficha-manifest hashes, and complete per-component status fields.
- Source samples — checked Resolução nº 75/22-CEPE, PPC 2023, CI1055 Ficha 1, MN162 Ficha 1, BQ083 Ficha 1, BF114 Ficha 1, MN129 Ficha 2, and the purported Ementário capture.
- `git diff --check` — passed before this review file was added.

## Review boundary

This review changes no research deliverable, global index, roadmap, or integration state. After the three required corrections, rerun the repository validator and the new work-specific validator, then request a follow-up cross-review. No integration is authorized by this review.
