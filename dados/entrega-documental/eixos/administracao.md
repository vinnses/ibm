# Documentary axis: administrative history and data

## Scope and status

This axis joins preserved administrative acts, public indicators, historical series, applicant/vacancy records, evaluation material and bounded searches. It keeps annual snapshots separate from cumulative cohorts and keeps source-stated universes separate from derived summaries.

## Structured datasets and local registers

- [Administrative source index](../../../administracao/dados/fontes.csv) and [INEP source manifest](../../../administracao/dados/inep/fontes/manifesto-fontes-volumosas.csv) — source identity, provenance and hashes.
- [INEP trajectory rows](../../../administracao/dados/inep/trajetoria_informatica_biomedica_ufpr.csv), [cohort summary](../../../administracao/dados/inep/trajetoria_informatica_biomedica_ufpr_resumo_coortes_2011_2020.csv), and [annual series](../../../administracao/dados/inep/trajetoria_informatica_biomedica_ufpr_serie_anual_2011_2020.csv) — separate row-level, cohort and annual views.
- [UFPR applicant/occupancy records](../../../administracao/dados/ufpr/candidatos_ocupacao_nc.csv), [annual entrants/demand series](../../../administracao/dados/ufpr/serie_anual_ingressantes_procura_observatorio.csv), and [official vacancies](../../../administracao/dados/ufpr/vagas_oficiais_por_processo.csv) — source definitions and universes must be read with each row.
- [W026 historical applicant dataset](../../../dados/administracao/candidatos-historicos.csv), [manifest](../../../administracao/dados/ufpr/w026/manifesto.csv), and [bounded searches](../../../administracao/dados/ufpr/w026/buscas.csv) — located totals and category-specific records; missing years remain not located.
- [Historical transitions](../../../administracao/historico/transicoes.csv), [evaluations](../../../administracao/historico/avaliacoes.csv), [complementary series](../../../administracao/historico/series-complementares.csv), and [original-act register](../../../administracao/historico/atos-originais/registros.csv).
- [Historical negative-search register](../../../administracao/historico/buscas-negativas.csv) — bounded results and limits.

## Original sources, packages and manifests

- [Historical-source manifest](../../../administracao/historico/fontes/manifesto.csv) and [original-act manifest](../../../administracao/historico/atos-originais/manifesto.csv).
- [INEP official packages and extracted spreadsheets](../../../administracao/dados/inep/fontes/pacotes/) and [preserved official spreadsheets](../../../administracao/dados/inep/fontes/planilhas/) — preserved source families; extraction coverage is not equivalent to full workbook-field extraction.
- [UFPR administrative source directory](../../../administracao/dados/ufpr/fontes/) — notices, resolutions, reports, pages and candidate/vacancy material.
- [Preserved Portaria 44/2015 institutional reproduction](../../../administracao/historico/atos-originais/documentos/portaria-44-2015-reproducao-unifap.pdf) and [literal extracted annex data](../../../administracao/historico/atos-originais/dados-portaria-44.csv) — reproduction, not the original DOU facsimile.
- [CPA page](../../../administracao/historico/fontes/paginas/cpa-avaliacao-cursos-2022-2026-09-04.html) and [CPA workbook](../../../administracao/historico/fontes/documentos/cpa-avaliacao-curso-informatica-biomedica-2022.xlsx) — preserved but not fully extracted in the mandated spreadsheet runtime.

## Evidence boundaries

Applicant counts, vacancies, entrants, cohort indicators, evaluation records and acts cannot be combined without their documented universe, denominator, period and evidence class. The W026 file contains both course totals and category-specific counts; it does not create a complete annual series. Final occupancy cannot be derived from candidate lists and nominal vacancies. Creation/recognition originals, matched final occupancy/cutoff data and protected process records remain bounded gaps in [W011 human review](../../../governance/human-reviews/W011-p1-admin-procedure.md).

Use this axis for stable documentary data only. It does not establish current compliance, current offering, approval of the 2026 proposal or any later administrative state without the corresponding preserved act.

## Catalog entry points

- [Dataset access catalog](../../acesso/datasets.csv)
- [Source-record access catalog](../../acesso/source-records.csv)
- [Gap/search catalog](../../acesso/gaps.csv)
- [Coverage inventory](../../acesso/COBERTURA_DOCUMENTAL.md)
