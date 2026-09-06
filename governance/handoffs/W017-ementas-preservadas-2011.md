# W017 handoff — preserved 2011 ementa and Ficha 1 evidence

- Branch: `work/w017-ementas-preservadas-2011`.
- Commit base: `3530173f374d0c361e9f8829d3347c638b21a7db` (fetched `origin/main` before branch creation).
- Commits produced: `2605e59` specification and initial audit events; `7ffe196` 38-row evidence extraction and reproducible builder; `1a5a3a3` 41-target coverage, applicability, gaps, divergences, validator, and agent records; `da557eb` visual/source review and additional version/upstream findings; containing closure commit adds this handoff.
- Primary-session model and effort: GPT-5 family exposed by the Codex Work runtime; exact backend and active effort were not exposed. The primary acted as orchestrator, source/PDF reviewer, logical consolidator, committer, and handoff author.
- Agent assignments actually used: `/root/w017_extract` / subagent / mechanical repository inventory, HTML/PDF field extraction, hashing, and tabular cross-check / `gpt-5.6-luna` / medium / 37 HTML records, the CI241 Ficha section, repository Ficha overlap, and all relevant hashes; `/root/w017_reconcile` / subagent / independent applicability, version, and coverage assessment / `gpt-5.6-terra` / medium / recommended the mutually exclusive 41-target categories and verified that no later same-code source proves 2011 validity; primary / orchestrator, source reviewer, consolidator, and committer / GPT-5 family exposed by runtime / effort not exposed / direct scope decisions, visual PDF review, reconciliation, validation, and handoff.
- Reassignments, escalations, equivalent-tier mappings, and routing deviations: none. No Sol subagent was created; no Terra/high escalation was needed. Both subagents were activated after specification commit `2605e59`, operated read-only, and did not edit the branch.
- Objective and completion verdict: complete and approved for the bounded repository-preserved scope. All 41 W009 targets were examined; every recoverable ementa/Ficha 1 field is source-located and version-separated; applicability, gaps, and metadata differences are explicit. Completion does not mean applicable historical Fichas were found.

## Deliverables and primary files

- `dados/curriculos/2011/ementas-preservadas/evidencias.csv` — 38 evidence rows: 37 Ementário records plus one 2025 CI241 Ficha 1.
- `dados/curriculos/2011/ementas-preservadas/cobertura.csv` — exactly 41 target rows.
- `dados/curriculos/2011/ementas-preservadas/aplicabilidade.csv` — 40 version/applicability rows.
- `dados/curriculos/2011/ementas-preservadas/README.md`, `divergencias.md`, and `lacunas.md`.
- `scripts/build_w017_ementas_2011.py` and `scripts/validate_w017_ementas_2011.py`.
- `governance/work-units/W017-ementas-preservadas-2011.md`.
- `governance/reviews/W017-ementas-preservadas-2011.md`.
- `governance/errors/W017-ementas-preservadas-2011.md`.
- This handoff.

## Sources

- Sources added: none. All evidence was already preserved and source bytes were unchanged.
- Sources effectively used: Resolução nº 34/2010-CEPE; the 2010-07-30 PPC; all 37 individual HTML records under `curriculos/2011/fontes/ementario/disciplinas/`; the 2025 multi-course PDF containing the CI241 Ficha 1; the W009 source/Ficha manifests and structured target datasets; the W015 access indexes; W002 commit history and W009 specification, handoff, review, error, and human-review records.
- The repository-wide Ficha scan found only one other W009-code PDF, MN129 Ficha 2 from 2022.1. It was not used because it is the wrong document type, a later version with no 2011 applicability evidence, and Ficha 2 is outside scope.

## Coverage reached

- Evidence complete/usable and proven applicable to 2011: 0 targets.
- Partial evidence: 36 targets.
- Document with indeterminate applicability: 1 target, CI241.
- Contradictory ementa/Ficha evidence: 0 targets.
- No sufficient preserved component-level evidence: 4 targets, the elective spaces `OPT-07-01`, `OPT-08-01`, `OPT-08-02`, and `OPT-08-03`.

All 37 current Ementário pages display `Não consta` for Ementa. CI241 is the sole positive Ficha/ementa extraction; its 2025 date prevents assignment to 2011. The four elective targets are spaces, not synthetic components.

## Validation executed

- `python scripts/build_w017_ementas_2011.py --check` — passed.
- `python scripts/validate_w017_ementas_2011.py` — passed: 41 targets, 38 evidence rows, complete=0, partial=36, indeterminate=1, contradictory=0, insufficient=4.
- `python scripts/validate_w009_curriculum_2011.py` — passed regression check.
- `python scripts/validate_governance_audit.py` — passed after the first failed run was recorded as E-W017-105.
- `python scripts/validate_repository.py` — passed with zero warnings and zero errors.
- `git diff --check` — passed.
- Manual PDF review — CI241 Ficha pages 24–25 and resolution Anexo I pages 5–6 rendered and visually checked; fields and transcriptions agree with the structured records.

## Gaps, divergences, and provisional information

- Gaps: no Ficha 1 or ementa is proven applicable to 2011 for any coded component; the 2010 PPC references annexed Fichas that are absent from the preserved 32-page file; no selected component/Ficha is identified for the four elective spaces; dated historical offering-unit evidence remains unavailable.
- Divergences: no competing ementa texts are proven applicable to 2011. `divergencias.md` preserves 14 versioned metadata/display differences between the 2010 resolution and the current portal, without using the undated portal to override the act. W009's pre-existing Article 1/Article 3 workload conflict remains separate.
- Provisional information: all department, nature, credit, and ideal-period values extracted from the Ementário are facts about the current 96A representation captured on 2026-09-04, not proven 2011 assignments. The CI241 Ficha fields are facts about the signed 2025 document only.
- Open upstream defects: W009 CI262 has an incorrect carried period and truncated title (E-W017-104); W009 labels for CI171, CI218, and CI172 reproduce portal variants rather than the cited resolution strings (E-W017-106). These do not affect W017 code identity or source-specific evidence.

## Searches, errors, and human-review gate

- External searches: none, broad or punctual.
- Error log: `governance/errors/W017-ementas-preservadas-2011.md`.
- Resolved events: E-W017-101, E-W017-102, E-W017-103, and E-W017-105.
- Open events: E-W017-104 and E-W017-106, both bounded upstream W009 corrections contained for this Work.
- Human-review question path: `governance/human-reviews/W009-p1-curriculum-2011.md`. HR-W009-001 remains the access gate for historical Ficha archives; HR-W009-002 remains the gate for treating current portal units as proven historical facts. Neither blocks completion of this bounded preserved-material extraction, but both limit any later content comparison or historical unit assertion.

## Explicitly unperformed work

No external document discovery, new source capture, Ficha 2 extraction, new component creation, offering-semester reconstruction, current-offering/compliance check, 2011–2023/2026 comparison, curricular evaluation, proposal analysis, source-byte modification, manifest/global-index update, W009 correction, merge, or next batch was performed. The two user-attached 2026 call/proposal PDFs were not used because no repository evidence made them relevant to 2011 ementa/Ficha identity.

## Recommended next bounded work

Recover and preserve the original Fichas 1 referenced as annexes to the 2010 PPC, or a small custodian-supplied batch whose approval/version metadata explicitly links each Ficha to the curriculum effective in 2011. Keep the separate W009 CI171/CI172/CI218/CI262 correction as a small data-quality Work. Start neither without explicit authorization.

## Remote synchronization

The local HTTPS push failed before writing because the runtime had no GitHub CLI credentials; E-W017-107 records the complete recovery. The authenticated GitHub connector created `work/w017-ementas-preservadas-2011` from the exact base and published commit `4ed8a129e34ed00248fad07446033e4892bd8790`. Its tree `2db0554cd3fa3b49b04ceba4262ce8c73c6f3164` was byte-identical to local closure `a99fa67`. A following connector commit adds this synchronization/error record; final ref/tree equality is verified after that containing update. The remote publication history is connector-generated rather than the five local commit objects, whose semantic sequence and hashes remain listed above. `main` was not changed or merged.
