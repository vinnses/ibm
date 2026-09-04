# Preservação das fontes

Inventário em fontes.csv, com SHA-256, tamanho em bytes,
instituição, data de consulta (2026-09-04), tipo, caminho e URL oficial
quando disponível. O inventário cobre os arquivos já versionados em
administracao/dados/**/fontes, os 11 pacotes oficiais do INEP recebidos em
tmp/inep_zips e os TXT de MD5 extraídos de cada pacote.

Os 11 ZIPs somam aproximadamente 697 MiB e não foram copiados para o Git:
permanecem no caminho temporário indicado no CSV, com hash SHA-256 verificado.
Os ZIPs foram baixados de download.inep.gov.br; os links foram recuperados
das páginas oficiais salvas em tmp/inep_pages. Para permitir auditoria sem
versionar os dados tabulares volumosos, somente os manifestos MD5 oficiais e
o snapshot da página geral do INEP foram preservados neste repositório.
