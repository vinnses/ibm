# Preservação das fontes administrativas

O inventário geral desta frente está em [`fontes.csv`](fontes.csv). Os 11 pacotes oficiais do INEP e as 11 planilhas XLSX exatas usadas por W006 também possuem registros completos em [`inep/fontes/manifesto-fontes-volumosas.csv`](inep/fontes/manifesto-fontes-volumosas.csv).

## Arquivos volumosos do INEP

- Pacotes originais: `administracao/dados/inep/fontes/pacotes/*.zip`.
- Planilhas extraídas sem alteração: `administracao/dados/inep/fontes/planilhas/*.xlsx`.
- Armazenamento: Git LFS, configurado em `.gitattributes`.
- Integridade: SHA-256 no manifesto; para cada XLSX, o MD5 oficial também está registrado nas notas e preservado em `administracao/dados/inep/fontes/md5/`.
- Uso: os XLSX são as entradas integrais de `scripts/extrair_indicadores_trajetoria.py`; os ZIPs preservam os pacotes oficiais dos quais foram extraídos.

Durante a recaptura de W008, o cliente local não reconheceu a cadeia TLS apresentada por `download.inep.gov.br`. O download foi aceito somente porque os 11 SHA-256 coincidiram exatamente com os valores previamente verificados em W006 e os 11 XLSX coincidiram com os MD5 oficiais. Essa limitação de transporte não foi tratada como prova de autenticidade por si só.

## Checkout e verificação

Instale Git LFS antes do checkout ou execute `git lfs pull` depois de instalá-lo. Confirme que os caminhos contêm os binários reais, não arquivos-ponteiro, e então rode:

```bash
python scripts/validate_repository.py
```

A reprodução completa das extrações está documentada em [`README.md`](README.md). O catálogo global `fontes/catalogo.csv` é seletivo; os manifestos locais são os inventários completos de cada frente.
