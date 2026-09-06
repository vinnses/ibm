# Version and divergence register

## Ementa/Ficha content

No two preserved sources provide competing ementa texts proven applicable to 2011. The current CI241 Ementário page displays `Não consta`, while the separate 2025 Ficha 1 contains an ementa. This is a version/applicability coexistence, not a resolved historical contradiction: the portal does not provide an alternative text and neither source establishes the Ficha's validity in 2011.

## Current portal metadata versus the 2010 act

The following values differ between Resolução nº 34/2010-CEPE and the current 96A Ementário pages captured on 2026-09-04. Both values are retained. The portal has no stated validity date, so these differences do not override the act and do not make the corresponding 2011 coverage status `documento_contraditorio`.

| ID | Code | Field | Resolução nº 34/2010-CEPE | Current Ementário representation | Source locators | Status |
|---|---|---|---|---|---|---|
| D-W017-001 | CI241 | Credits | 3 | 4 | Resolution, Anexo I p. 5; `161246.html`, Informações Gerais | Versioned mismatch; portal applicability indeterminate |
| D-W017-002 | CM201 | Nature | Fixed 1st-semester component | `Optativa` | Resolution, Anexo I p. 5; `161248.html`, Tipo | Versioned mismatch; portal applicability indeterminate |
| D-W017-003 | CM045 | Nature | Fixed 1st-semester component | `Optativa` | Resolution, Anexo I p. 5; `161249.html`, Tipo | Versioned mismatch; portal applicability indeterminate |
| D-W017-004 | CM005 | Nature | Fixed 2nd-semester component | `Optativa` | Resolution, Anexo I p. 5; `161254.html`, Tipo | Versioned mismatch; portal applicability indeterminate |
| D-W017-005 | BQ005 | Credits | 4 | 3 | Resolution, Anexo I p. 5; `161255.html`, Informações Gerais | Versioned mismatch; portal applicability indeterminate |
| D-W017-006 | BQ054 | Credits | 4 | 3 | Resolution, Anexo I p. 5; `161259.html`, Informações Gerais | Versioned mismatch; portal applicability indeterminate |
| D-W017-007 | CI171 | Ideal period | 5th semester | 6 | Resolution, Anexo I p. 5; `161269.html`, Período Ideal no Curso | Versioned mismatch; portal applicability indeterminate |
| D-W017-008 | CI394 | Ideal period | 6th semester | 5 | Resolution, Anexo I p. 5; `161276.html`, Período Ideal no Curso | Versioned mismatch; portal applicability indeterminate |
| D-W017-009 | MN128 | Credits | 4 | 3 | Resolution, Anexo I p. 5; `161277.html`, Informações Gerais | Versioned mismatch; portal applicability indeterminate |
| D-W017-010 | CI262 | Credits | 6 | 8 | Resolution, Anexo I p. 6; `161283.html`, Informações Gerais | Versioned mismatch; portal applicability indeterminate |
| D-W017-011 | CI262 | Displayed name | `Trabalho de Conclusão de Curso em Informática Biomédica` | `Trabalho de Conclusão de Curso em Informática` | Resolution, Anexo I p. 6; `161283.html`, Disciplina | Truncation/different displayed name; portal applicability indeterminate |
| D-W017-012 | CI171 | Displayed name | `Aprendizado de Máquina` | `APRENDIZADO DE MÁQUINAS` | Resolution, Anexo I p. 5; `161269.html`, Disciplina | Singular/plural difference; portal applicability indeterminate |
| D-W017-013 | CI218 | Displayed name | `Sistemas de Banco de Dados` | `SISTEMAS DE BANCOS DE DADOS` | Resolution, Anexo I p. 5; `161275.html`, Disciplina | Singular/plural difference; portal applicability indeterminate |
| D-W017-014 | CI172 | Displayed name | `Processamento de Imagens Biomédicas` | `Processamento de Imagnes Biomédicas` | Resolution, Anexo I p. 5; `161281.html`, Disciplina | Source spelling difference; portal applicability indeterminate |

Capitalization and diacritic differences in other displayed names remain source-literal in `evidencias.csv`; they are not silently normalized or interpreted as distinct components.

## Upstream processing defect discovered

W009 `componentes.csv` records CI262 with the truncated label and `recommended_term=7`, although the cited resolution places the full name under the 8th semester. This is logged as open event `E-W017-104`. Its labels for CI171, CI218, and CI172 also reproduce the current portal variants instead of the cited resolution strings; the additional source-review finding is `E-W017-106`. The W017 coverage column is explicitly named `w009_target_label` so it cannot be mistaken for a new literal transcription. Correcting the accepted W009 dataset and validator is outside this Work.

The pre-existing W009 Article 1/Article 3 840/960-hour conflict and the resolution's later-page `39/09-CEPE` header are not new W017 findings and remain in their original W009 records.
