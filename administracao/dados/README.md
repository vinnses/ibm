# Dados administrativos históricos — Informática Biomédica/UFPR

Consulta e validação: **4 de setembro de 2026**.

Este diretório reúne a série administrativa disponível para o Bacharelado em Informática Biomédica da UFPR. Os dados anuais foram mantidos separados dos indicadores acumulados por coorte, porque respondem a perguntas diferentes e não podem ser somados ou comparados diretamente.

## Resultados principais

1. O Observatório da UFPR registra queda da relação candidato/vaga de **3,86 em 2015** para **2,20 em 2025**. A interface também exibiu **1,36 em 2026**, embora o seletor indicasse término em 2025; esse ponto permanece ressalvado.
2. O relatório institucional da UFPR informa **78,95%** como média das taxas de evasão das turmas/coortes de ingresso de 2009 a 2018 para o curso. Não é uma taxa anual e não é o indicador acumulado do INEP.
3. No INEP, as dez coortes de ingresso de 2011 a 2020 apresentam, na última observação disponível, desistência acumulada entre **53,33% e 94,74%**. As coortes mais recentes possuem acompanhamento menor, de modo que diferenças entre elas não devem ser interpretadas automaticamente como melhora ou piora causal.
4. As resoluções localizadas registram **30 vagas totais**, divididas em 24 no PS-UFPR e 6 no SiSU, nos processos documentados entre 2017/2018 e 2024/2025. O edital do PS-UFPR 2026 registra **24 vagas apenas para o processo próprio** e não informa o total anual nem a parcela SiSU.
5. Não foi localizada uma série pública comparável de ocupação final das vagas. Também não há série completa de candidatos absolutos: o NC confirma 65 concorrentes no PS 2016; o relatório de 2019/2020 expõe 37 na categoria Concorrência Geral, que não constitui total único do curso.

## O que cada indicador mede

| Tipo | Indicadores | Unidade e interpretação |
|---|---|---|
| Anual, UFPR/SIGA | ingressantes; relação candidato/vaga | fotografia de cada ano no filtro do curso/campus; a relação não fornece candidatos absolutos |
| Anual, INEP reconstruído | ingressantes, permanência ativa, concluintes, desistências | soma dos estoques e fluxos anuais das coortes disponíveis; série completa somente de 2011 a 2020 |
| Coorte, INEP | TAP | percentual da coorte original ainda em permanência no ano de referência |
| Coorte, INEP | TCA e TDA | percentuais **acumulados** de conclusão e desistência desde o ingresso até o ano de referência |
| Coorte, INEP | TCAN e TADA | percentuais da coorte original que concluíram ou desistiram **naquele ano** |
| Coortes/turmas, UFPR | média de evasão por curso | média das razões `evadidos ÷ integrantes da turma` para as turmas incluídas pelo relatório |

## Séries anuais

### Observatório UFPR/SIGA

| Ano | Ingressantes | Candidato/vaga |
|---:|---:|---:|
| 2015 | 36 | 3,86 |
| 2016 | 28 | 3,10 |
| 2017 | 33 | 2,33 |
| 2018 | 31 | 2,92 |
| 2019 | 36 | 2,71 |
| 2020 | 42 | 1,94 |
| 2021 | 27 | 2,88 |
| 2022 | 28 | 2,20 |
| 2023 | 34 | 2,64 |
| 2024 | 41 | 2,23 |
| 2025 | 36 | 2,20 |
| 2026* | 35 | 1,36 |

\* O seletor temporal mostrava fim em 2025, mas o gráfico apresentava 2026. A transcrição integral, filtro, [URL do painel](https://app.powerbi.com/view?r=eyJrIjoiYjA2MTQ3ZDItOTIxZS00OGY2LTkzY2ItZDA0MmM0NjIyNjJmIiwidCI6ImMzN2IzN2EzLWU5ZTItNDJmOS1iYzY3LTRiOWI3MzhlMWRmMCJ9&pageName=88f6166f2c223b5ac6ac) e ressalvas estão em [`ufpr/serie_anual_ingressantes_procura_observatorio.csv`](ufpr/serie_anual_ingressantes_procura_observatorio.csv) e [`ufpr/NOTA_METODOLOGICA.md`](ufpr/NOTA_METODOLOGICA.md).

### INEP — reconstrução anual das coortes 2011–2020

| Ano | Novos ingressantes | Permanência ativa | Concluintes no ano | Desistências no ano |
|---:|---:|---:|---:|---:|
| 2011 | 31 | 27 | 0 | 4 |
| 2012 | 33 | 46 | 0 | 14 |
| 2013 | 31 | 68 | 0 | 9 |
| 2014 | 38 | 83 | 0 | 23 |
| 2015 | 37 | 89 | 1 | 30 |
| 2016 | 30 | 80 | 5 | 34 |
| 2017 | 30 | 83 | 3 | 24 |
| 2018 | 30 | 80 | 7 | 26 |
| 2019 | 37 | 85 | 4 | 28 |
| 2020 | 39 | 113 | 0 | 11 |

“Permanência ativa” é a soma de `QT_PERMANENCIA` das coortes observadas, não uma taxa. A série não foi estendida a 2021–2024 porque faltariam as coortes ingressantes nesses anos. O arquivo completo está em [`inep/trajetoria_informatica_biomedica_ufpr_serie_anual_2011_2020.csv`](inep/trajetoria_informatica_biomedica_ufpr_serie_anual_2011_2020.csv).

Os ingressantes UFPR/SIGA e INEP divergem no período comum — por exemplo, 36 versus 37 em 2015 e 42 versus 39 em 2020. Os valores foram preservados em paralelo, sem escolher arbitrariamente uma fonte, pois os sistemas possuem universos e datas de consolidação próprios.

## Trajetória acumulada por coorte

| Coorte | Ingressantes | Último ano | TAP | TCA acumulada | TDA acumulada |
|---:|---:|---:|---:|---:|---:|
| 2011 | 31 | 2020 | 0,00% | 25,81% | 74,19% |
| 2012 | 33 | 2021 | 3,03% | 3,03% | 93,94% |
| 2013 | 31 | 2022 | 0,00% | 16,13% | 83,87% |
| 2014 | 38 | 2023 | 0,00% | 5,26% | 94,74% |
| 2015 | 37 | 2024 | 0,00% | 13,51% | 86,49% |
| 2016 | 30 | 2024 | 6,67% | 6,67% | 86,67% |
| 2017 | 30 | 2024 | 6,67% | 40,00% | 53,33% |
| 2018 | 30 | 2024 | 6,67% | 16,67% | 76,67% |
| 2019 | 37 | 2024 | 10,81% | 18,92% | 70,27% |
| 2020 | 39 | 2024 | 12,82% | 5,13% | 82,05% |

A tabela usa a última observação de cada coorte, não um mesmo tempo de acompanhamento. O resumo também preserva a situação no ano esperado de integralização: [`inep/trajetoria_informatica_biomedica_ufpr_resumo_coortes_2011_2020.csv`](inep/trajetoria_informatica_biomedica_ufpr_resumo_coortes_2011_2020.csv).

## Vagas, candidatos e ocupação

As resoluções permitem reconstruir somente pontos documentados da oferta. Não houve interpolação para os processos 2018/2019 e 2023/2024.

| Processo | PS-UFPR | SiSU | Total | Estado |
|---|---:|---:|---:|---|
| 2017/2018 | 24 | 6 | 30 | confirmado |
| 2018/2019 | — | — | — | fonte não localizada |
| 2019/2020 | 24 | 6 | 30 | confirmado; o art. 1º contém referência interna divergente |
| 2020/2021 | 24 | 6 | 30 | confirmado |
| 2021/2022 | 24 | 6 | 30 | confirmado |
| 2022/2023 | 24 | 6 | 30 | confirmado |
| 2023/2024 | — | — | — | fonte não localizada |
| 2024/2025 | 24 | 6 | 30 | confirmado |
| 2026 | 24 | — | — | confirmado apenas para PS-UFPR |

Os detalhes estão em [`ufpr/vagas_oficiais_por_processo.csv`](ufpr/vagas_oficiais_por_processo.csv). Os dados absolutos parciais do NC estão em [`ufpr/candidatos_ocupacao_nc.csv`](ufpr/candidatos_ocupacao_nc.csv).

Não foi calculada uma “taxa de ocupação” por `ingressantes ÷ vagas`: ingressantes do SIGA podem incluir formas de ingresso e momentos de registro diferentes das vagas iniciais de uma resolução, fazendo a razão ultrapassar 100%. Uma ocupação defensável exige vagas ofertadas e preenchidas após todas as chamadas dentro do mesmo processo e universo; essa apuração consolidada não foi localizada.

## Relação com a proposta de reorganização

A [matriz de validação](../mec/2026/matriz-validacao-alegacoes.md) separa cada declaração do Apêndice B da evidência independente disponível.

- **Com suporte oficial delimitado:** existe baixa procura relativa segundo o PPC e a série do Observatório; há evasão histórica alta nas metodologias UFPR e INEP; o currículo de 2023 possui 3.200 horas; a proposta registra 2.700 horas e 30 vagas como intenções.
- **Parcial ou divergente:** resoluções anteriores registram 30 vagas totais, enquanto o edital do PS-UFPR 2026 registra 24 apenas nesse processo. Nenhum ato localizado explica a diferença.
- **Não validado:** que a nova denominação possua demanda local elevada, que a reorganização reduza evasão ou aumente permanência, que a infraestrutura seja suficiente, que dois docentes sejam contratados ou que exista o programa proposto no Complexo Hospital de Clínicas.
- **Estado administrativo:** não foram localizados resultado público do Edital nº 01/2026, memorando/Apêndice A, número de processo, aprovação colegiada/CEPE, ato do MEC, novo PPC ou edital de ingresso sob a nova denominação. A ausência em busca pública não prova inexistência.

O Planejamento Estratégico 2016–2020 do Setor de Ciências Exatas registra evasão e baixa procura como problemas setoriais, não como justificativa específica do curso. A ata do CEPE de 13 de dezembro de 2019 confirma a inclusão de prova específica de Matemática na segunda fase para Informática Biomédica a partir de 2020/2021, mas a ata não explicita a motivação.

## Proveniência, arquivos e reprodução

O inventário [`fontes.csv`](fontes.csv) registra URL, instituição, data de consulta, tamanho, SHA-256, caminho e estado de preservação. Os documentos UFPR efetivamente usados foram versionados. Os 11 pacotes nacionais do INEP foram baixados e verificados, mas somam aproximadamente **697 MiB** e não foram inseridos no histórico Git; o inventário conserva suas URLs e hashes, enquanto os manifestos MD5 oficiais, o dicionário, o recorte integral do curso e os scripts reprodutíveis foram versionados.

Reprodução:

```bash
python scripts/extrair_indicadores_trajetoria.py \
  /caminho/para/os/xlsx/*.xlsx \
  --ano-ingresso-min 2011 --ano-ingresso-max 2020 \
  --saida administracao/dados/inep/trajetoria_informatica_biomedica_ufpr.csv

python scripts/resumir_indicadores_trajetoria.py \
  --entrada administracao/dados/inep/trajetoria_informatica_biomedica_ufpr.csv \
  --diretorio-saida administracao/dados/inep
```

A auditoria executou 85 balanços de estoque por coorte/ano, validou as cinco taxas do INEP, conferiu os 11 MD5 das planilhas, os hashes dos documentos principais, os CSVs e os links locais. Consulte [`AUDITORIA.md`](AUDITORIA.md) para o registro dos testes.
