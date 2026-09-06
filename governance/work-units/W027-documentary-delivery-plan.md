# W027 — Documentary delivery objective and consolidated inventory

- **Objective:** replace the deferred P2-P4 execution sequence with an explicit documentary-delivery program and publish a reproducible inventory of what is already available, what remains locally extractable, what requires a concrete public lead, and what requires institutional/user access.
- **Branch:** `work/w027-documentary-delivery-plan`.
- **Commit base:** `2d6c14378b42ae36ffa3b657795a78ecf96e349d`.
- **Primary-session assignment:** GPT-5 exposed family; exact backend and effort are not exposed; actual orchestrator, scope authority, reviewer and integrator.
- **Agent assignments:**

| Actor | Primary/subagent | Functional role | Model | Effort | Planned/actual | Routing rationale |
|---|---|---|---|---|---|---|
| Primary session | primary | orchestrator, scope authority, reviewer, integrator | GPT-5 exposed family | unavailable | actual | Objective reformulation, cross-cutting governance and integration remain primary-session duties |
| W027 inventory agent | subagent | mechanical inventory builder | `gpt-5.6-luna` | medium | planned | Read existing access CSVs and generate a deterministic Markdown coverage view; canonical Luna/medium routing for mechanical organization and simple extraction |

- **Escalation rule:** ambiguity about project objectives, category boundaries or gate consequences returns to the primary session. No Sol subagent may be created; work genuinely requiring Sol remains with the user-supervised primary session.
- **Inputs:** `governance/PROJECT.md`, `governance/ROADMAP.md`, `governance/DATA_FIRST.md`, `governance/REMAINING_DATA.md`, `governance/WORK_INDEX.md`, `dados/acesso/datasets.csv`, `dados/acesso/source-records.csv`, `dados/acesso/gaps.csv`, and existing W009-W026 records.
- **In scope:** (1) state the documentary-delivery objective as the active project objective; (2) retain P3/P4 analysis as future work requiring direct user participation; (3) define bounded N1-N6 stages and gates; (4) generate a consolidated, reproducible Markdown inventory from existing access catalogs; (5) classify next work by repository-local extraction, concrete-lead retrieval, institutional/user input, or final documentary freeze; (6) update roadmap/restart records during integration.
- **Out of scope:** new source searches, source downloads, CPA workbook extraction, new CSV/XLSX authorship, Ficha applicability adjudication, current compliance/offering, curricular comparison, proposal evaluation, recommendations, institutional contact, or starting N2/N3 collection work.
- **Deliverables:** `governance/DOCUMENTARY_DELIVERY_PLAN.md`; `dados/acesso/COBERTURA_DOCUMENTAL.md`; `scripts/build_w027_documentary_inventory.py`; `scripts/validate_w027_documentary_inventory.py`; `governance/reviews/W027-documentary-delivery-plan.md`; `governance/handoffs/W027-documentary-delivery-plan.md`; `governance/errors/W027.md`; integration updates to `governance/PROJECT.md`, `governance/ROADMAP.md`, `governance/DATA_FIRST.md`, `governance/REMAINING_DATA.md`, `governance/WORK_INDEX.md`, and `dados/acesso/README.md`.
- **Method:** treat repository records as authoritative; derive counts from existing access CSVs without changing them; keep record counts distinct from unique-document and completeness claims; classify gaps without converting `not located` into nonexistence; expose exact input paths and deterministic rebuild/check commands.
- **Acceptance criteria:** active objective and exclusions are unambiguous; N1-N6 have stop boundaries and observable outputs; inventory rebuild is deterministic and agrees with all three access catalogs; every next lane states its access dependency; P3/P4 cannot begin implicitly; no open agent-correctable defect; branch is reviewed, validated, committed and published before integration.
- **Risks and uncertainty:** existing access records are heterogeneous and may duplicate source identities; a coverage inventory measures repository accessibility, not completeness; spreadsheet tooling is unavailable in this runtime, so W027 authors no spreadsheet and CPA remains deferred.
- **Validation:** `python scripts/build_w015_data_access.py --check`; W027 validator; governance audit; repository validator; `git diff --check`; `git lfs fsck`; manual comparison of generated totals with the input catalogs.
- **Error log:** `governance/errors/W027.md`.
- **Human review:** existing records under `governance/human-reviews/` remain authoritative. W027 creates no new human question unless its inventory identifies a genuinely new access dependency.
- **Checkpoint contract:** specification commit first; deterministic inventory checkpoint second; objective/roadmap checkpoint third; closure/review checkpoint fourth. Each checkpoint is pushed before the next. Integration is authorized by the user's instruction to begin and carry out this reformulation; no subsequent collection Work is authorized.
