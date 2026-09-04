# Decision Log

| ID | Decision | Rationale | Consequence |
|---|---|---|---|
| D001 | Evidence collection precedes curricular judgment. | Early evaluation risks selecting facts to support a preferred conclusion. | Research milestones remain descriptive unless analysis is explicitly authorized. |
| D002 | Each curriculum is an independent historical unit. | Codes, names, departments, and requirements can persist while content or applicability changes. | No silent projection between 2011, 2023, and proposed structures. |
| D003 | Sources used as evidence must be preserved with provenance and SHA-256. | External links can change or disappear. | Unpreserved sources are unresolved exceptions and cannot silently support final conclusions. |
| D004 | Ficha 1 and Ficha 2 are separate evidence types. | Ficha 1 is permanent curricular evidence; Ficha 2 records a specific offering. | Multiple Ficha 2 versions remain separate and applicability must be established. |
| D005 | Proposal status is staged. | A feasibility form does not prove institutional or federal approval. | Use proposal, selected, approved, authorized, and implemented only with separate acts. |
| D006 | Annual and cohort metrics remain separate. | Their denominators and time bases differ. | No direct summing or causal comparison; methods travel with every series. |
| D007 | One bounded work unit uses one branch and a mandatory handoff. | Long unbounded sessions exhausted limits and obscured completion. | Branch, acceptance criteria, review, and handoff are defined before execution. |
| D008 | Use the smallest capable model and effort. | Capture and hashing do not require global reasoning. | Reserve high-reasoning models for reconciliation, audit, and synthesis. |
| D009 | The repository replaces chat as durable project memory. | Work is moving from ChatGPT Work to local Codex. | New agents recover state from `AGENTS.md`, governance, manifests, commits, and handoffs. |
| D010 | Global catalogs change only during explicit integration. | Concurrent collectors can conflict on shared indexes. | Collection branches maintain local manifests; integration reviews decide global updates. |
| D011 | `fontes/catalogo.csv` is a curated global index rather than a complete union. | Local manifests are authoritative for bounded collections; duplicating every record in a global CSV creates drift and merge conflicts without adding evidence. | Every collection maintains a complete local manifest. The global catalog may point to major source sets but completeness claims and validation use the local manifests. |
| D012 | Agent and process errors have append-only per-work audit trails. | Failed attempts, false negatives, provenance mistakes, and validation defects affect confidence even when later corrected. | Every Work logs the full error/recovery path under `governance/errors/`; handoffs identify open events and reviews verify closure. |
| D013 | Stakeholder testimony and hypotheses remain separate from documentary facts. | Lived experience and institutional interpretations can identify high-value research questions but do not independently establish motive, causality, approval, or implementation. | Preserve provenance and wording, derive explicit evidence questions, and defer argumentative use until the documentary/analytical roadmap gates permit it. |
| D014 | Sol is exclusive to the user-supervised primary session; subagents use Luna or Terra. | The user controls the primary model/effort, while task-appropriate delegation preserves capacity and makes costs predictable. Agent display names do not establish model identity. | Integration, final audit, and global synthesis stay in the active primary session. Every Work records actual model, effort, role, rationale, and escalation; no Sol subagent may be created. |

Add decisions only when they change future work. Do not use this file as a narrative activity log.
