# W020 — Complete structured data for all preserved Fichas

- Objective: publish structured records for every preserved Ficha not already represented in the two D01 datasets, keeping Ficha 1 and each Ficha 2 version separate.
- Branch: `work/w020-complete-preserved-fichas`.
- Commit base: `98b540029e820ef7e792c2f3f2035c4626f54bf8`.
- Primary-session assignment: GPT-5 exposed family; exact backend and effort unavailable; primary orchestrator, source reviewer and integrator; actual.
- Agent assignments: `01a07485-ece4-7091-8840-b30978c79bf3` / subagent / mechanical extractor / `gpt-5.6-luna` / medium / planned reuse / smallest capable recorded tier for preserved-PDF extraction. Primary / primary / reviewer-integrator / GPT-5 exposed family / effort unknown / actual / global review and integration cannot be delegated.
- Escalation rule: ambiguous documentary identity returns to the primary; no Sol subagent may be created. Terra is used only if reconciliation beyond literal extraction becomes necessary and is recorded before activation.
- Inputs: all 40 unchanged PDFs under `curriculos/2023/fichas/`, both local manifests, existing DInf inventory/transcriptions, W010 inventory, and W018/W019 datasets and validators.
- In scope: the 13 preserved Ficha 1 documents not already in W018/W019; all 17 preserved Ficha 2 documents; literal identity, permanent/plan fields available from each source, dates/term/class or explicit absence, path, URL, SHA-256, locators and normalization notes; one deterministic validator.
- Out of scope: new retrieval, claims of 2023 applicability, merging Ficha 1 with Ficha 2, merging Ficha 2 versions, current offering/compliance, curricular comparison or proposals, and documents not preserved locally.
- Deliverables: `dados/curriculos/2023/fichas-preservadas/fichas-1-restantes.csv`, `dados/curriculos/2023/fichas-preservadas/fichas-2.csv`, `dados/curriculos/2023/fichas-preservadas/README.md`, `scripts/validate_w020_fichas.py`, W020 error/review/handoff files.
- Method: preserve source bytes; one row per distinct PDF; copy source text without silent modernization; identify missing values explicitly; retain `indeterminado` where term, class, version or 2023 applicability is not established; verify every row against manifest path/URL/hash and visually inspect page layout.
- Acceptance criteria: all 40 preserved PDFs are represented exactly once across W018, W019 and W020 by document identity; 23 Ficha 1 rows total and 17 distinct Ficha 2 rows total; no duplicate source path; schemas document each field; hashes match stored bytes and manifests; all required checks pass.
- Risks and uncertainty: older PDFs and unsigned plans may omit document date, term, class or applicability; these remain explicit rather than inferred.
- Validation: W020, W019, W018, W010, governance, repository, access-package check, `git diff --check`, and `git lfs fsck`; primary visual/source sampling of every remaining document.
- Error log: `governance/errors/W020.md` (append-only).
- Human review: `governance/human-reviews/W010-p1-curriculum-2023.md`; HR-W010-001/002 remain and are not resolved by extraction alone.
- Checkpoints: A specification committed/pushed; B remaining Ficha 1 data committed/pushed; C all Ficha 2 data committed/pushed; D review, integration, access refresh and final remote synchronization. If interrupted, the latest published checkpoint is the restart point.

