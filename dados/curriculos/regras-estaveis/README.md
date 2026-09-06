# W021 checkpoint D — stable TCC, internship, extension, and formative rules

Checkpoints B–C remain unchanged: 19 TCC and 35 Internship provisions. Checkpoint D appends 10 Formative and 11 Extension provisions, for 75 rows total. Each topic has source-stated provisions for both 2011 and 2023. The 2011 Extension row is the explicit “participação em atividades de extensão universitária oficial” category inside the 2011 PPC’s formative-activities list; no separate 2011 extension regulation is invented.

## Sources and method

- `curriculos/2011/fontes/ppc-2011.pdf`: TCC scope/workload/multidisciplinarity and the Monografia evaluation rule.
- `curriculos/2011/fontes/resolucao-34-2010-cepe.pdf`: formal CI262 matrix provision.
- `curriculos/2023/fontes/ppc-2023.pdf`: TCC evaluation rules, TCC description, and complete Anexo IV regulation (Arts. 1º–12º).
- `curriculos/2023/fontes/resolucao-75-22-cepe.pdf`: mandatory completion rule and formal matrix alternatives for CI1131/CI1133 and CI1132/CI1134.
- `curriculos/2023/fontes/ppc-2023.pdf`: curriculum-level internship distinction/workload/schedule and complete Anexo III regulation (Arts. 1º–31º).
- `curriculos/2023/fontes/resolucao-75-22-cepe.pdf`: formal 220-hour completion rule and CI1101 matrix workload/prerequisite.
- `curriculos/2011/fontes/resolucao-34-2010-cepe.pdf`: 480-hour formative-activity requirement and Colegiado validation by documentary proof.
- `curriculos/2011/fontes/ppc-2011.pdf`: complete 480-hour formative-activity list, limits, duplicate-use rule, and explicit official-extension category.
- `curriculos/2023/fontes/resolucao-75-22-cepe.pdf`: 320-hour ACE requirement and 80-hour formative requirement.
- `curriculos/2023/fontes/ppc-2023.pdf`: formative overview, complete Anexo II regulation/table, extension overview, and complete Anexo V regulation.

The dataset has one row per distinct provision/source, not one synthetic rule per curriculum. Conflicting or differently scoped provisions remain separate. `rule_text` is a complete normalized transcription of the source-stated provision; it is not a summary or pointer. Original Portuguese, numbering, order, and punctuation are retained. Normalization is limited to whitespace and line-break joining. Blank source table cells are recorded as `not stated`; this does not add a negative claim about the curriculum. PDFs remain authoritative.

## Schema

`provision_id`, `topic`, `curriculum_version`, `source_kind`, and `rule_type` identify the provision. `rule_text` is the complete text. `workload`, `eligibility`, `process`, and `approval_evaluation` contain the corresponding source-stated values, or exactly `not stated` when that field is absent from the provision. `evidence_status` and `uncertainty` keep documentary status separate from interpretation. `source_path`, `source_sha256`, `source_url`, and `locator` provide local provenance, stored-byte identity, and exact PDF page/section/article/annex location. `normalization_notes` records the permitted transformation.

The 2023 TCC provisions that mention extension remain classified as TCC because they are part of the TCC regulation; the 2023 standalone Extension rows separately capture the PPC/ACE rules. Internship rows include mandatory/nonmandatory distinctions, workload, eligibility, supervision, documentation, authorization, evaluation, validation, and process text when the source states them. Formative rows include workload, eligible categories/modalities, score/hour limits, documentation, validation, evaluation, deadlines, and double-counting rules. Extension rows include ACE categories, mandatory/optional distinctions, workloads, supervision, documentation, validation, process, evaluation linkage, and limits. No current practice, offering, applicability beyond the named curriculum version, conflict resolution, or normative conclusion is inferred.

## Validation

```bash
python scripts/validate_w021_rules.py
python scripts/validate_w020_fichas.py
python scripts/validate_w010_curriculum_2023.py
python scripts/validate_w009_curriculum_2011.py
python scripts/validate_repository.py
python scripts/validate_governance_audit.py
git diff --check
git lfs fsck
```

This checkpoint does not edit PDFs, manifests, global indexes, review, handoff, or `main`.
