# Repository Instructions for AI Agents

These instructions apply to the entire repository. Read this file before making changes, then read `governance/README.md`, `governance/PROJECT.md`, `governance/ROADMAP.md`, and `metodologia/criterios-documentais.md`.

## Non-negotiable rules

- Treat the repository as the source of truth. Do not substitute chat memory for repository evidence.
- Finish documentary reconstruction before curricular evaluation or proposal design.
- During research milestones, report what sources establish without arguing whether a change is desirable.
- Keep fact, inference, interpretation, and normative proposal explicitly separate.
- Do not project current structures onto historical curricula or silently fill gaps.
- Preserve conflicting versions and label uncertainty as proven, probable, contradictory, or not located.
- Preserve every public source used as evidence and record provenance and SHA-256. If a source cannot be committed, mark the preservation exception as unresolved; a URL and hash alone are not full compliance.
- A proposal proves that a proposal existed. Selection, approval, authorization, and implementation require separate evidence.
- Keep annual metrics separate from cumulative cohort indicators. Never infer final seat occupancy from entrants divided by nominal vacancies without matched universes.

## Git workflow

- Start from an updated `main` and create one branch per bounded work unit.
- Never edit `main` directly unless the user explicitly authorizes an integration step.
- Do not modify another active work branch.
- Prefer incremental, semantically scoped commits.
- Collection work keeps local manifests. Update global indexes only during an explicit integration milestone.
- Before a merge, run `python scripts/validate_repository.py` and the work-specific checks.
- End every work with the handoff contract in `governance/specs/HANDOFF.md`.

## Source handling

- Keep original binaries and captured pages unchanged.
- Record title, institution, source URL, access date, document date/version, document type, local path, SHA-256, and evidentiary purpose when applicable.
- Treat Ficha 1 and Ficha 2 as different document types. Do not merge multiple Ficha 2 versions.
- A matching code or title is insufficient to assign a Ficha to a curriculum; establish version or applicability.
- For negative searches, record the date, domains, terms, and limits. Absence from public search does not prove nonexistence.

## Scope control

- Use `governance/specs/WORK_UNIT.md` for every new milestone.
- Record newly discovered research fronts as backlog items unless they are required by the current acceptance criteria.
- Do not begin the next milestone automatically after completing the current one.
- Use the smallest capable model and effort. Mechanical capture, hashing, and simple extraction should not consume the strongest reasoning tier.

## Process auditability

- Record every agent, tool, validation, review, source-access, Git, environment, or orchestration error in the affected Work's append-only file under `governance/errors/`, following `governance/specs/ERROR_RECORD.md`.
- Preserve the failed attempt, affected paths/state, impact, ordered recovery attempts, final status, and verification. A later success does not erase the error history.
- Do not place secrets, credentials, private keys, session cookies, or passphrases in error records.
- Keep agent-correctable defects separate from questions that require protected access, institutional authority, value judgment, or human testimony. Record the latter under `governance/human-reviews/` with their gate consequence.
- Treat stakeholder statements as testimony or research hypotheses until independently supported. Preserve their provenance and do not silently convert them into institutional facts.

## Language and preservation

- Write technical agent documentation, code, comments, and identifiers in English.
- Preserve source titles, quotations, historical names, and documentary transcriptions in their original language.
- Existing Portuguese research documents may remain in Portuguese; do not translate them mechanically.
