# Agent Operations

## Functional roles

| Role | Typical tasks | Required output |
|---|---|---|
| Orchestrator | Define work units, dependencies, acceptance criteria, and assignments | Approved work spec and compact status updates |
| Collector | Locate, download, name, hash, and manifest sources | Preserved files, provenance records, gaps, and search log |
| Extractor | Produce literal or normalized structured data from preserved sources | Reproducible extraction, transformation notes, and validation counts |
| Reconciler | Compare versions, applicability, denominators, and contradictions | Evidence table with conflict and uncertainty states |
| Reviewer | Run independent checks against the work spec | Dated review with blockers, findings, and verdict |
| Integrator | Merge reviewed work and update shared indexes/governance | Merge record, repository validation, and final handoff |

One agent may perform several roles in a small milestone, but review criteria remain independent of the implementation narrative.

## Effort routing

The user controls the model and effort of the primary session. The primary agent is the orchestrator and is the only agent permitted to use Sol. Complex integration, final audit, and global synthesis are performed directly in that active primary session, using its current user-selected model and effort. The user may change that selection when the work demands it; agents must not silently assume or change it.

Subagents use the smallest capable non-Sol tier:

- Luna/medium for mechanical capture, download, hashing, organization, and simple extraction.
- Terra/medium for documentary investigation and structured search.
- Terra/high for reconciliation, cross-validation, and divergence audits.
- Terra/high for demanding independent review when Terra/medium is insufficient.

Sol is prohibited for subagents at every effort level. If a delegated task proves to require Sol, stop that delegation and return the task to the primary session. Do not create a Sol subagent as an escalation path.

The primary session does not have a fixed required effort. For example, when the active session is Sol/medium, integration remains in that Sol/medium session unless the user chooses to change it. Model names exposed by another runtime may differ; map an equivalent tier explicitly and record the mapping. Never infer a model from an agent display name.

### Required assignment record

Before substantive execution, every Work specification must record:

- the primary-session model and effort as selected by the user or exposed by the active runtime;
- each primary agent or subagent actor, functional role, exact model, effort, and routing rationale;
- whether the assignment is planned or actual;
- any equivalent-tier mapping when canonical Luna/Terra/Sol names are unavailable.

The handoff records what was actually used, including reassignments and escalations. A change of subagent tier must be recorded before continued execution. An unrecorded historical assignment remains `unknown`; names, cost, speed, and behavior are not substitutes for provenance.

Local Codex should apply the same principle even when model names differ: use the least expensive capable model and raise reasoning effort only for ambiguity, reconciliation, or cross-cutting decisions.

## Parallel work

Parallelize only independent work units with separate branches and local manifests. Avoid concurrent edits to `README.md`, `fontes/catalogo.csv`, `governance/ROADMAP.md`, and other global indexes. Integrate those files in a dedicated milestone.

## Compact agent result contract

Agents should report:

- result and completion verdict;
- sources added and their paths;
- structured outputs;
- divergences and uncertainty;
- unresolved gaps;
- validation executed;
- branch and commits.

Do not return long process narratives when these fields are sufficient.

## Failure and stop conditions

Stop and hand off when scope must materially expand, a required protected source is inaccessible, a destructive operation needs new authority, or evidence cannot distinguish materially different interpretations. Do not bypass permissions or convert uncertainty into a guess.

Every failure and recovery attempt must also be recorded under `governance/errors/` using `specs/ERROR_RECORD.md`. Review findings that identify incorrect data, provenance, logic, or a missing required deliverable are error events, even when corrected before integration. Human-only questions belong in `governance/human-reviews/`; agents should continue with permitted explicit gaps when the Work specification allows them.
