# Documentary data release

This directory is the stable entry point for the documentary and data collection about the UFPR Bachelor of Biomedical Informatics. It delivers evidence and access paths; it does not compare curricula, evaluate the 2026 proposal or recommend decisions.

## Start here

1. Choose an axis: [2011 curriculum](eixos/curriculo-2011.md), [2023 curriculum](eixos/curriculo-2023.md), [administrative history](eixos/administracao.md), or [2026 proposal](eixos/proposta-2026.md).
2. Check [extraction status](STATUS_EXTRACAO.md) before assuming a preserved source is fully structured.
3. Use [requests and gaps](SOLICITACOES_E_LACUNAS.md) for evidence that needs a new precise lead, institutional access or user-supplied files.
4. Read the [audit and freeze](AUDITORIA_E_CONGELAMENTO.md) for verified coverage and accepted exceptions.
5. Verify this checkout with [validation instructions](VALIDACAO.md) and `MANIFEST.sha256`.

The machine-readable access catalogs remain in [`dados/acesso/`](../acesso/): 204 dataset records, 191 source-manifest records and 33 gap/search records at this release. These counts are records, not unique documents or a completeness percentage.

## Evidence boundaries

- Original files remain at their repository paths and are not copied or normalized here.
- Ficha 1 and every Ficha 2 version remain separate.
- Historical versions and applicability are not inferred from matching codes or titles.
- Annual, cohort, course-total, category-specific, vacancy, entrant and occupancy universes remain distinct.
- A proposal establishes a proposal; later administrative states require separate acts.
- `Not located` and access-dependent are documented outcomes, not nonexistence.

## Reproduce and verify

From the repository root:

```text
python scripts/build_w015_data_access.py --check
python scripts/build_w027_documentary_inventory.py --check
python scripts/build_w028_release_manifest.py --check
python scripts/validate_w028_documentary_release.py
python scripts/validate_governance_audit.py
python scripts/validate_repository.py
git diff --check
git lfs fsck
```

The release manifest lists each included dataset, preserved source and release-control file with its checkout SHA-256. Git LFS objects must be materialized before checksum validation.

## Deferred future program

Curricular comparison, interpretation, evaluation and recommendations are outside this release. They require a new user-supervised objective and must keep direct fact, inference, interpretation and normative proposal separate.
