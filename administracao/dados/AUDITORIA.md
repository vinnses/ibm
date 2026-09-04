# Auditoria integrada — dados, MEC/2026 e scripts

Data: 4 set. 2026. Escopo: arquivos textuais em `administracao/dados`, `administracao/mec/2026` e `scripts`; PDFs e demais binários não foram alterados.

## Testes executados

| Teste | Resultado |
|---|---|
| Estrutura dos CSVs | 7 CSVs verificados com `csv.reader`: cabeçalho presente e largura uniforme. |
| Série do Observatório | 12 linhas, anos contínuos 2015–2026; somente `candidatos_por_vaga`, sem candidatos absolutos. A observação de 2026 preserva a divergência da interface. |
| Links locais Markdown | 16 links em `administracao/dados` e `administracao/mec/2026` resolvidos; nenhum caminho quebrado. |
| Integridade INEP | Os 11 XLSX em `/workspace/scratch/caa386d9bd48/tmp/inep_xlsx` conferem com os MD5 preservados (11/11). |
| Integridade MEC/UFPR | SHA-256 dos dois PDFs e do HTML preservado conferem com os valores declarados nos READMEs/matriz. |
| Scripts INEP | Executados `extrair_indicadores_trajetoria.py` e `resumir_indicadores_trajetoria.py` com as 11 planilhas, coortes 2011–2020; a validação exige balanço coorte × ano e separa TCA/TDA acumuladas de TCAN/TADA anuais. |
| Complemento NC/UFPR | Os três arquivos locais têm SHA-256/tamanho conferidos e as URLs oficiais retornaram HTTP 200. O HTML de 2016 confirma 65 no campo “Total Geral de Inscritos” (1 treineiro separado). No PDF de 2019/2020 foram preservados somente os 37 da coluna “Concorrência Geral” e os 2 treineiros; categorias potencialmente sobrepostas não foram somadas. |

O caminho de scratch registrado para os XLSX documenta o ambiente original da auditoria e não é portátil. Os pacotes e planilhas brutos não estão presentes em um clone limpo; esta limitação foi formalizada como exceção de preservação no roadmap de governança.

## Reconciliações confirmadas

- A matriz passa a reconhecer a série pública do Observatório UFPR: ingressantes e relação candidato/vaga para 2015–2025; 2026 é preservado exclusivamente com a ressalva da interface.
- Não há candidatos absolutos na série, e não se calculou ocupação nem se multiplicou relação candidato/vaga por vagas de outro ato.
- Os **78,95%** são a média UFPR das taxas das turmas/coortes de 2009–2018; não são valor anual do INEP nem de uma única coorte.
- As 24 vagas de 2026 são exclusivamente do PS/UFPR; não representam SiSU ou total anual. A proposta registra 30 vagas, sem ato que explique a diferença.

## Pendências materiais

- A série do Observatório não define um limiar institucional de “baixa procura”, não mede demanda pelo curso proposto de IA e não resolve a divergência da interface em 2026.
- Seguem não localizados ato público de seleção/aprovação/implementação da proposta, discriminação SiSU/total de 2026 e método comparável para demanda/notas de corte de IA.
- Candidatos absolutos continuam incompletos: há total comparável somente para 2016. O campo de Concorrência Geral de 2019/2020 é parcial; não representa ocupação nem série histórica comparável.
