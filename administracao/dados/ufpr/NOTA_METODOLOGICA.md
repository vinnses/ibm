# Dados UFPR — Informática Biomédica

## Escopo e fontes

Os arquivos desta pasta consolidam exclusivamente informações oficiais da UFPR para o curso de **Informática Biomédica**, no Campus Centro Politécnico quando essa dimensão é informada. As fontes primárias arquivadas estão em `fontes/`: resoluções CEPE de vagas, Edital n.º 28/2025-NC/PROGRAP (PS/UFPR 2026), o relatório institucional de evasão e cópias HTML do portal do Observatório.

`serie_anual_ingressantes_procura_observatorio.csv` é a transcrição da [consulta ao painel Power BI institucional](https://app.powerbi.com/view?r=eyJrIjoiYjA2MTQ3ZDItOTIxZS00OGY2LTkzY2ItZDA0MmM0NjIyNjJmIiwidCI6ImMzN2IzN2EzLWU5ZTItNDJmOS1iYzY3LTRiOWI3MzhlMWRmMCJ9&pageName=88f6166f2c223b5ac6ac) com o filtro “Informática Biomédica - Campus Centro Politécnico”. Ela contém ingressantes e a razão candidato/vaga, não candidatos em número absoluto. Portanto, **não se deve multiplicar a razão por vagas de outra fonte para estimar candidatos**: o painel e as resoluções podem usar universos, momentos de extração e regras de contabilização distintos.

Há uma divergência registrada na interface consultada: o seletor temporal indicava fim em 2025, mas o gráfico mostrava também 2026 (35 ingressantes; 1,36 candidato/vaga). A linha de 2026 foi preservada com essa ressalva e não recebeu validação independente.

## Vagas por processo

`vagas_oficiais_por_processo.csv` separa as vagas anuais do **PS-UFPR**, do **SiSU/PS-SISU** e o **total** quando a própria resolução apresenta as três colunas. As resoluções disponíveis confirmam 24 vagas no PS-UFPR, 6 no SiSU e 30 no total para 2017/2018, 2019/2020, 2020/2021, 2021/2022, 2022/2023 e 2024/2025. Não foram localizadas no acervo resoluções para 2018/2019 e 2023/2024; essas lacunas são explícitas, sem imputação. O Edital PS/UFPR 2026 confirma 24 vagas no processo próprio, mas não informa a parcela SiSU ou o total, que permanecem vazios.

O título da Resolução n.º 04/19-CEPE identifica o processo 2019/2020; seu art. 1º menciona 2018/2019. O CSV preserva o identificador do título e registra a inconsistência.

## Comparabilidade e uso de indicadores

Ingressantes do painel não são automaticamente vagas ofertadas em uma resolução: podem refletir matrícula/ingresso efetivado, chamadas posteriores, remanejamentos, vagas adicionais ou regra temporal diferente. Por isso, este acervo não calcula ocupação. Caso venha a ser calculada a razão `ingressantes ÷ vagas oficiais`, ela deverá ser chamada de **proxy de ingresso/vaga**, nunca de taxa de ocupação; pode superar 100% justamente por esses universos e mecanismos de preenchimento não coincidirem.

Também não se equipara candidato/vaga do painel ao conjunto de vagas das resoluções nem se infere candidatos absolutos. A relação pode ter denominador específico do processo/curso e não informa, por si só, inscrições únicas ou pessoas candidatas.

## Candidatos e ocupação final — disponibilidade NC/UFPR

`candidatos_ocupacao_nc.csv` acrescenta somente valores absolutos efetivamente publicados pelo Núcleo de Concursos (NC/UFPR), com a definição de cada campo. Para o PS 2016, o NC publicou 65 inscritos concorrentes no total do curso (e 1 treineiro, excluído da relação). Para o PS 2019/2020, a fonte organiza os candidatos por categorias potencialmente sobrepostas; por isso o CSV preserva apenas os 37 da coluna **Concorrência Geral**, sem apresentá-los como total de inscritos. Os arquivos usados foram arquivados em `fontes/nc/`.

| Período/processo | Candidatos absolutos utilizáveis | Ocupação final de vagas | Situação |
| --- | --- | --- | --- |
| 2015 | Não localizado na busca delimitada | Não localizada | Lacuna |
| PS 2016 | 65 inscritos concorrentes | Não localizada | Parcial; fonte NC |
| PS 2017/2018 | Página NC mostra candidatos convocados à 2ª fase por categoria; não total de inscritos únicos | Não localizada | Não comparável com o total de 2016 |
| PS 2018/2019 | Não localizado na busca delimitada | Não localizada | Lacuna |
| PS 2019/2020 | 37 na coluna Concorrência Geral; não é total único do curso | Não localizada | Parcial; categorias não devem ser somadas |
| 2020/2021 a 2026 | Não localizado na busca delimitada | Não localizada | Lacuna para esta consolidação |

“Ocupação final” exigiria uma fonte que apurasse, após chamadas e registros acadêmicos, vagas preenchidas e vagas ofertadas no mesmo universo. Listas de aprovados/registro acadêmico não foram tratadas como ocupação final, pois não fornecem essa apuração consolidada e podem incluir chamadas posteriores ou processos distintos.

## Evasão

O `relatorio-evasao-analise-modelagem-ufpr-2026.pdf` informa para Informática Biomédica — Campus Centro Politécnico a **taxa média de evasão de 78,95%**. Esse valor deve ser citado apenas segundo a metodologia do relatório: para a análise por curso, consideram-se turmas com ano de início de **2009 a 2018**; para cada turma, a taxa é `total de alunos evadidos / total de alunos da turma`; a taxa publicada é a média das taxas anuais do período. O relatório inclui abandono, cancelamentos, decisão administrativa, desistência, desligamento com penalidades, jubilamento, mudanças de campus/habilitação, novo vestibular, reopção e transferências entre as formas consideradas. Não é indicador da série de ingressantes 2015–2026, nem uma taxa de evasão de uma única coorte.
