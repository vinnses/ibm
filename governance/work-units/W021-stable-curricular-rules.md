# W021 — Stable curricular rule data

- Objective: transcribe source-stated rules for TCC, internship, extension and formative activities from preserved 2011/2023 PPCs and formal acts into a machine-readable dataset.
- Branch/base: `work/w021-stable-curricular-rules`; `35366e350a306cfd813fadd273b61b9851959cf7`.
- Primary-session assignment: GPT-5 exposed family; exact backend/effort unavailable; actual orchestrator, source reviewer and integrator.
- Agent assignments: `01a07485-ece4-7091-8840-b30978c79bf3` / subagent / extractor / `gpt-5.6-luna` / medium / planned reuse / literal extraction from identified local PDFs. Primary / primary / reviewer-integrator / GPT-5 exposed family / effort unknown / actual / cross-document review and integration.
- Escalation rule: ambiguity returns to primary; no Sol subagent. Terra is activated only for material reconciliation and recorded before use.
- Inputs: preserved 2011 and 2023 PPCs, CEPE resolutions and current structured curriculum inventories/manifests; no web.
- In scope: TCC, mandatory/nonmandatory internship, curricular extension and formative/complementary activities; one row per distinct source provision; curriculum/version, requirement, workload, eligibility/process/approval/evaluation rules, exact page/article/annex locator, path/URL/hash, and uncertainty.
- Out of scope: current compliance/offering, desirability, comparative analysis, unsupported interpretation, new sources and unrelated regulations.
- Deliverables: `dados/curriculos/regras-estaveis/regras.csv`, README, `scripts/validate_w021_rules.py`, W021 error/review/handoff.
- Method: literal normalized transcription with each source provision separate; preserve conflicts and explicit absence; no silent reconciliation. PDFs remain unchanged and authoritative.
- Acceptance: all four topics and both curriculum versions receive explicit sourced rows or explicit not-stated status; source path/URL/hash match manifests and stored bytes; locators are exact; deterministic checks pass.
- Risks: rules may be split between act and PPC or differ by version; record separate rows and uncertainty.
- Validation: W021, W020, W010, W009, governance, repository, access check after integration, whitespace and LFS; render/review cited pages.
- Error log: `governance/errors/W021.md`.
- Human review: existing W009/W010 human-review files; no new human question anticipated for literal extraction.
- Checkpoints: A spec; B TCC; C internship; D extension/formative activities; E review/integration/D09. Each checkpoint is committed and pushed before the next.

