# W009 handoff — 2011 curriculum documentary inventory

- **Branch:** `work/w009-p1-curriculum-2011`
- **Commit base:** `22b14805956fcece4e381dc089f7dbb06d2b0857`
- **Commits produced:** `829ac83 Build 2011 curriculum documentary inventory`; `9ab39b5 Record W009 curriculum inventory handoff`; `b7c998d Fix W009 formal curriculum records`; this correction-audit handoff commit.
- **Objective and completion verdict:** Corrected after cross-review; awaiting independent follow-up review and not approved or integrated. The 2011 inventory has exactly 41 targets (37 coded components and four elective spaces), a formal elective catalog, source-linked ementa states, and corrected formal dependency and workload records. The Ficha coverage acceptance condition is met through explicit bounded-search statuses, not through a claim that unavailable records do not exist.

## Deliverables and primary files

- `curriculos/2011/inventario/componentes.csv`
- `curriculos/2011/inventario/optativas.csv`
- `curriculos/2011/inventario/ementas.csv`
- `curriculos/2011/inventario/dependencias.csv`
- `curriculos/2011/inventario/divergencias.csv`
- `curriculos/2011/inventario/buscas-negativas.csv`
- `curriculos/2011/fichas/manifesto.csv` and preserved Ficha original
- `curriculos/2011/fontes/manifesto.csv` and preserved Ementário HTML captures
- `curriculos/2011/README.md`
- `scripts/validate_w009_curriculum_2011.py`

## Sources added

The local source manifest records the pre-existing preserved Resolução nº 34/2010-CEPE and 2010 PPC, plus 39 new UFPR Ementário HTML captures: course 96A, its curriculum representation, and the 37 coded-component records used for unit and ementa-field states. Every record has a repository-relative path, URL, access date, purpose, and SHA-256.

One official UFPR multi-course PDF signed on 2025-05-14 was preserved in `fichas/ficha-1-indeterminada/`. It contains a CI241 Ficha 1 section. It is not assigned to 2011 because the later signature and same code do not establish historical applicability.

## Coverage reached

- 37/37 coded components: formal curriculum attributes, unit state, explicit prerequisite/corequisite/equivalence state, hidden-requirement state, Ficha 1 status, Ficha 2 status, and gaps.
- 4/4 elective spaces: separately represented as slots, not merged into a synthetic component.
- 64/64 coded entries transcribed from the resolution's formal elective catalog.
- Seven explicit direct prerequisite edges and the Article 2 §1 Bloco A rule recorded separately. The rule targets all 22 coded components outside its 15 members and the four formal elective spaces; an elective-space edge only applies once a catalog discipline is selected and does not claim an offering.
- `total_hours`, `weekly_total_hours` (`Tot.`), and `credits` (`Créd.`) are distinct Anexo I transcriptions; they are not interchangeable measures.

## Validations executed and results

- `python scripts/validate_w009_curriculum_2011.py` — passed: 41 targets, 37 codes, 26 valid Bloco A targets, one structured workload divergence, and manifested paths/SHA-256 values valid.
- `python scripts/validate_governance_audit.py` — passed after the correction-audit documentation update.
- `python scripts/validate_repository.py` — passed after the correction-audit documentation update.
- `git diff --check` — passed after the correction-audit documentation update.

## Gaps

- No Ficha 1 dated/versioned as applicable to the 2011 curriculum was located in the bounded public official search.
- No Ficha 2 with a traceable term and class was located for any coded component or elective slot.
- The preserved Ementário component records display `Não consta` for their ementa fields; therefore no 2011 ementa is inferred from component names.
- Authenticated SIGA/SEI and non-public departmental archives were outside the accessible public surface. These absences are search results, not evidence of nonexistence.

## Divergences

- The preserved resolution’s later page header reads `Resolução nº 39/09-CEPE`, although its title and established repository provenance identify Resolução nº 34/2010-CEPE. The original is retained unchanged.
- The 2025 CI241 Ficha 1 has an ementa, but it is explicitly indeterminate for 2011 and must not be substituted for historical evidence.
- Article 1's Formação Profissional Geral heading says 840 hours and Article 3 says 960 hours. Anexo I calculates to 840 for 14 non-TCC 60-hour components and 960 when CI262's 120 hours is included. The act does not explicitly state whether the Article 1 heading excludes TCC, so `D-W009-001` classifies the tension as contradictory rather than selecting one category. The cross-review's 900-hour calculation is retained as a review claim but is not reproduced from Anexo I.

## Provisional information

Offering units come from the currently exposed 96A Ementário representation, which aligns with the formal 2011 structure but has no stated historical version date. They are recorded as a portal representation, not as independent proof of historical assignment. The 2010 PPC corroborates formal structure but contains pre-implementation placeholder codes in its internal matrix; the resolution controls coded structure.

## Error log and human-review gates

- **Error log:** `governance/errors/W009.md`. Resolved correction events: E-W009-001 (Bloco A endpoints), E-W009-002 (`Tot.`/`Créd.` separation), E-W009-003 (structured workload divergence), and E-W009-004 (review commit interruption). There are no open W009 agent-correctable error events in this handoff.
- **Human review:** `governance/human-reviews/W009-p1-curriculum-2011.md`. HR-W009-001 remains pending for authenticated/archive Ficha access; it does not block this bounded public inventory but materially limits P2/P3 content comparison. HR-W009-002 remains pending for a dated institutional offering-unit allocation; it blocks treating current Ementário units as proven 2011 facts.

## Explicitly unperformed work

No 2023 collection, administrative/procedural research, curriculum comparison, quality judgment, proposal analysis, global-index update, review, integration, or search of protected systems was performed.

## Recommended next bounded work unit

Independent follow-up cross-branch review of the three correction events against the preserved source, followed—only if authorized—by a dedicated protected/archive access request or review work unit for missing 2011 Ficha 1/Ficha 2 records. Do not begin the 2023 or comparative milestone from this branch.
