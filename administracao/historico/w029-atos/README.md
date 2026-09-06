# W029 historical-acts recovery lane

This directory records the W029 follow-up to the two exact-act gaps left by W016. It does not replace, amend, or reuse W016's originals or manifests.

## Scope and outcome

The targets were the original UFPR `Resolução 19/10-COUN` and the original *Diário Oficial da União* facsimile of `Portaria 44 de 22 de janeiro de 2015`. On 2026-09-06, three new, precise official-domain searches were made for each target. None returned a qualifying original document. The searches are bounded outcomes, not evidence that either act does not exist.

The UFPR queries returned the already preserved Ementário registry attribution rather than a copy of the COUN resolution. The official DOU/government queries returned no result identifying the target SERES recognition act or its 2015 DOU page. Existing W016 evidence remains unchanged: it includes an institutional UNIFAP reproduction of the Portaria, not an original DOU facsimile.

## Files

- `buscas.csv` records the six new search attempts and their limits.
- `registros.csv` records the exact status of each target after this lane.
- `validate_w029_historical_acts.py` checks the bounded log and status vocabulary.

Run `python administracao/historico/w029-atos/validate_w029_historical_acts.py` from the repository root.
