# AI Governance Index

This directory is the durable operating context for AI-assisted work on the history of the UFPR Biomedical Informatics program. Repository evidence remains authoritative; chat history is not a source.

## Required reading order

1. [`../AGENTS.md`](../AGENTS.md) — repository-wide constraints.
2. [`PROJECT.md`](PROJECT.md) — purpose, scope, evidence model, and current baseline.
3. [`ROADMAP.md`](ROADMAP.md) — completed milestones, open work, dependencies, and gates.
4. [`WORK_INDEX.md`](WORK_INDEX.md) — map from past work to commits and deliverables.
5. [`../metodologia/criterios-documentais.md`](../metodologia/criterios-documentais.md) — documentary method.
6. [`AGENT_OPERATIONS.md`](AGENT_OPERATIONS.md) — functional roles, binding model routing, and primary-session authority.
7. The relevant specification in [`specs/`](specs/) before starting a branch.

## Directory map

| Path | Purpose |
|---|---|
| [`PROJECT.md`](PROJECT.md) | Stable project charter and evidence taxonomy |
| [`ROADMAP.md`](ROADMAP.md) | Current execution order and completion gates |
| [`WORK_INDEX.md`](WORK_INDEX.md) | Historical work and commit map |
| [`DECISIONS.md`](DECISIONS.md) | Durable methodological and workflow decisions |
| [`AGENT_OPERATIONS.md`](AGENT_OPERATIONS.md) | Agent roles, effort routing, and compact result contract |
| [`specs/WORK_UNIT.md`](specs/WORK_UNIT.md) | Required specification for a bounded work unit |
| [`specs/SOURCE_RECORD.md`](specs/SOURCE_RECORD.md) | Provenance and preservation schema |
| [`specs/ERROR_RECORD.md`](specs/ERROR_RECORD.md) | Append-only agent/process error and recovery schema |
| [`specs/REVIEW.md`](specs/REVIEW.md) | Review and integration criteria |
| [`specs/HANDOFF.md`](specs/HANDOFF.md) | Mandatory handoff contract |
| [`errors/`](errors/) | Per-work failed attempts, impacts, corrections, and open events |
| [`human-reviews/`](human-reviews/) | Questions requiring protected access, authority, testimony, or human judgment |
| [`research-hypotheses/`](research-hypotheses/) | Stakeholder testimony and research leads kept separate from facts |
| [`reviews/`](reviews/) | Dated repository and work reviews |
| [`handoffs/`](handoffs/) | Dated transfers between agents or environments |
| [`templates/`](templates/) | Copyable work, review, and handoff templates |

## Authority and updates

When documents conflict, use this order:

1. original official source;
2. repository-wide `AGENTS.md` and documentary methodology;
3. approved work specification;
4. dated review or handoff;
5. roadmap summary;
6. chat recollection.

Update `ROADMAP.md` and `WORK_INDEX.md` only during an explicit review or integration milestone. A completed work unit does not authorize the next one.

## Current transfer baseline

The ChatGPT Work phase was consolidated on 2026-09-04. The exact transfer record is [`handoffs/chatgpt-work-to-local-codex-2026-09-04.md`](handoffs/chatgpt-work-to-local-codex-2026-09-04.md), and the audit is [`reviews/consolidation-2026-09-04.md`](reviews/consolidation-2026-09-04.md).
