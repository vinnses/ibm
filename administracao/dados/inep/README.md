# Indicadores de trajetória — Informática Biomédica/UFPR

Recorte dos **Indicadores de Trajetória da Educação Superior** do INEP para a
UFPR (`CO_IES=571`) e o curso Informática Biomédica (`CO_CURSO=1126727`). O
arquivo-base `trajetoria_informatica_biomedica_ufpr.csv` contém uma linha por
coorte de ingresso e ano de referência; abrange as coortes 2011–2020 e 85
observações (até 2024, conforme a coorte).

## Produtos

- `trajetoria_informatica_biomedica_ufpr_resumo_coortes_2011_2020.csv`: a
  situação de cada coorte no ano previsto de integralização e na última
  observação disponível.
- `trajetoria_informatica_biomedica_ufpr_serie_anual_2011_2020.csv`: série
  reconstruída que soma, em cada ano, as coortes observadas: ingressantes da
  nova coorte, permanência ativa, concluintes anuais, desistências anuais e
  falecidos anuais.

`TAP` é a taxa de permanência no ano de referência. `TCA` e `TDA` são,
respectivamente, taxas **acumuladas** de conclusão e desistência até o ano de
referência. Já `TCAN` e `TADA` são taxas **anuais**, calculadas apenas com os
concluintes e desistentes daquele ano. Portanto, não se devem somar TCA/TDA
entre anos nem tratar TAP como uma taxa anual de ingresso.

A série anual publicada termina em 2020 porque foi solicitada para as coortes
2011–2020. Mesmo que as planilhas tragam observações até 2024, qualquer série
posterior a 2020 construída com este recorte é incompleta: faltam as coortes
de ingresso 2021 em diante.

## Reprodução e validação

Com os XLSX oficiais já extraídos em `tmp/inep_xlsx`, gere o CSV-base (o filtro
descarta a coorte 2010) e depois os resumos:

```bash
python scripts/extrair_indicadores_trajetoria.py \
  /workspace/scratch/caa386d9bd48/tmp/inep_xlsx/*.xlsx \
  --ano-ingresso-min 2011 --ano-ingresso-max 2020 \
  --saida administracao/dados/inep/trajetoria_informatica_biomedica_ufpr.csv
python scripts/resumir_indicadores_trajetoria.py \
  --entrada administracao/dados/inep/trajetoria_informatica_biomedica_ufpr.csv \
  --diretorio-saida administracao/dados/inep
```

O segundo comando falha se faltar coorte, se os anos de uma coorte não forem
contíguos, se os códigos da IES/curso divergirem, ou se falhar qualquer uma
das 85 identidades: `permanência + concluintes acumulados + desistências
acumuladas + falecidos acumulados = ingressantes`; ele também confere as cinco
taxas divulgadas contra seus numeradores e denominadores.

## Fontes e versões verificadas

Fonte institucional: microdados/planilhas **Indicadores de Trajetória da
Educação Superior (INEP)**. Foram usados os recortes de coorte 2011–2020:
`indicadores_trajetoria_educacao_superior_2011_2020.xlsx` até
`indicadores_trajetoria_educacao_superior_2020_2024.xlsx`, disponíveis nesta
execução em `/workspace/scratch/caa386d9bd48/tmp/inep_xlsx`; os ZIPs originais
correspondentes estão em `/workspace/scratch/caa386d9bd48/tmp/inep_zips`.
Também foi usado o dicionário oficial local
`fontes/dicionario-acompanhamento-trajetoria.docx`.

| Arquivo XLSX | SHA-256 |
| --- | --- |
| 2011_2020 | `f9c221a075aee4511d10fba33f9080c81a027a9ac661f7ae08547d0c3244be97` |
| 2012_2021 | `3738aa6d3c9479695eb1a547684bf9185cdc368de77c0d53cbcd4e77b800dd23` |
| 2013_2022 | `d1c49714ba21a5791766a87e9f2c45624b1361769bf346bfdd5ae3c8b42419f5` |
| 2014_2023 | `7e7b963517b27580a2b43b951b65eebb45404daab02df4014167a4e77ab743d7` |
| 2015_2024 | `831fa6adeac46f8610a8715b4df1493784e1b21b5ca2f77eb837ac9f59d573d9` |
| 2016_2024 | `b9776a782d1a909e75b4eb42fd1d840a42dac4e0e8ae87dbada451f39f347b6a` |
| 2017_2024 | `b77ac3e2cc951dfd314bbe7a2fc141f3f2ec39470558674e198f567f8f43dbf1` |
| 2018_2024 | `e710299b0196ed9f87d631295b05cbb6c3381061d6e0693c6917dab83c241009` |
| 2019_2024 | `9ef61488ac66604368dd29e03f33831924cd8f8d980137da60527a1d195c9cc3` |
| 2020_2024 | `214a7dacd77875c440ffa0551be11008080d017104ffdd65fce0e362bac22f53` |
