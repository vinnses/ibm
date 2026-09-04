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

Historical ChatGPT Work guidance used the following tiers:

- Luna/medium for mechanical capture, download, hashing, organization, and simple extraction.
- Terra/medium for documentary investigation and structured search.
- Terra/high for reconciliation, cross-validation, and divergence audits.
- Sol/high for complex integration, final audit, and genuinely global synthesis.

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
