# História curricular da Informática Biomédica — UFPR

Este repositório reúne a reconstrução documental e os dados históricos do Bacharelado em Informática Biomédica da Universidade Federal do Paraná (UFPR), vinculado ao Departamento de Informática.

## Objetivo

Entregar o acervo documental e de dados mais completo, rastreável e reutilizável razoavelmente obtenível, preservando versões, universos estatísticos, incertezas e lacunas. A comparação curricular e a avaliação da proposta dependem de um objetivo futuro com participação direta do usuário.

Comece pela [entrega documental](dados/entrega-documental/README.md).

## Regra de preservação

Todo arquivo utilizado como evidência deve ser copiado para este repositório e referenciado pelo caminho local e pela URL de procedência. Isso inclui PDFs, planilhas, páginas HTML, imagens e arquivos auxiliares. Uma URL sem cópia preservada pode ser registrada como pista de pesquisa, mas não sustenta uma conclusão documental do projeto.

Cada fonte preservada deve possuir, quando tecnicamente possível:

- nome local estável;
- URL de origem;
- data de consulta;
- código da disciplina ou processo relacionado;
- tipo documental e vigência observável;
- hash SHA-256;
- indicação de autenticidade, incompletude ou divergência.

## Eixos

1. **Currículo de 2011:** matriz, Fichas 1, Fichas 2, optativas, atividades formativas e documentação normativa.
2. **Currículo de 2023:** matriz vigente, Fichas 1, Fichas 2, estágio, extensão, TCC, optativas e documentação normativa.
3. **História administrativa:** criação do curso, reformulações, procura, ingresso, evasão, conclusão, avaliações e decisões colegiadas.
4. **Proposta de 2026:** tramitação, justificativas, matriz proposta, recursos associados e consequências institucionais.
5. **Comparação:** realizada somente depois da reconstrução suficiente dos documentos anteriores.

## Ficha 1 e Ficha 2

- A **Ficha 1 permanente** é a referência principal da ementa, natureza, carga horária e requisitos formalmente aprovados.
- A **Ficha 2 variável** registra a concretização de uma oferta: programa, objetivos, procedimentos, avaliação, bibliografia, docente, turma e período.
- Diferentes Fichas 2 do mesmo código não serão fundidas. A variação entre elas é um objeto da pesquisa.
- Uma Ficha 1 genérica será descrita como tal; sua relação com inconsistências entre ofertas só será avaliada após a comparação das Fichas 2.

## Estrutura

- `metodologia/`: critérios documentais e regras de transcrição;
- `governance/`: operating rules, work specifications, reviews, handoffs and roadmap for AI-assisted work;
- `curriculos/2011/`: reconstrução do currículo original;
- `curriculos/2023/`: reconstrução do currículo vigente;
- `administracao/`: editais, indicadores, atas, pareceres e demais registros administrativos;
- `propostas/`: documentos e análise futura da reorganização;
- `assembleia/`: sínteses factuais temporárias para discussão;
- `scripts/`: coleta e validação reproduzíveis.

AI agents and local Codex sessions must start with [`AGENTS.md`](AGENTS.md) and the [governance index](governance/README.md).

## Estado e plano completo

Atualização de 06/09/2026: P0/P1 e o programa documental N1-N6 estão concluídos no alcance aprovado. A entrega indexa 204 datasets, 191 registros de fontes e 33 lacunas/buscas, mantendo exceções explícitas. As listas detalhadas abaixo preservam o histórico e não substituem o [roadmap](governance/ROADMAP.md) nem a [entrega](dados/entrega-documental/README.md).

### 0. Infraestrutura documental

- [x] Repositório e critérios iniciais criados.
- [x] Separação entre documento original, extração e interpretação.
- [x] Regra de preservação local de todo arquivo utilizado.
- [x] Criar catálogo global inicial de fontes com URL, caminho, data, tipo, vigência e SHA-256.
- [x] Adicionar rotina automatizada para estrutura dos CSVs, hashes manifestados e links Markdown locais.
- [ ] Resolver a exceção de preservação dos 11 pacotes brutos do INEP usados na extração administrativa.
- [x] Preservar cópias das páginas HTML utilizadas nesta etapa.

### 1. Currículo de 2011

- [x] Grade e periodização identificadas na Resolução nº 34/2010-CEPE.
- [x] Preservar a Resolução nº 34/2010-CEPE no diretório do currículo.
- [x] Localizar e preservar o PPC original de 30 de julho de 2010.
- [ ] Transcrever o elenco formal de optativas.
- [ ] Criar inventário dos 37 componentes codificados.
- [ ] Localizar e preservar a Ficha 1 correspondente à vigência de cada componente.
- [ ] Transcrever literalmente cada ementa e registrar versão/vigência.
- [ ] Localizar e preservar Fichas 2 por turma e período letivo.
- [ ] Registrar Fichas 1 ou 2 genéricas, ausentes, contraditórias ou posteriores.
- [ ] Documentar departamentos, correquisitos e requisitos não visíveis na tabela resumida.
- [ ] Representar a estrutura e as dependências em formato estruturado.

### 2. Currículo de 2023 — vigente

- [x] Resolução nº 75/22-CEPE e PPC 2023 preservados.
- [x] Resoluções departamentais nº 76 a 80/22-CEPE preservadas.
- [x] Grade, periodização, cargas e pré-requisitos reconstruídos.
- [ ] Transcrever e estruturar o catálogo formal de optativas da resolução.
- [ ] Criar inventário individual dos 39 componentes não-TCC e quatro códigos alternativos de TCC.
- [ ] Localizar e preservar a Ficha 1 vigente de cada componente (20 Fichas 1 do DInf e três de outros departamentos preservadas nesta etapa; cobertura e vigência ainda incompletas).
- [ ] Transcrever literalmente cada ementa e registrar versão/vigência.
- [ ] Localizar e preservar Fichas 2 por turma e período letivo, priorizando 2023–2026 (16 documentos do índice do DInf e uma oferta de `MN129` em 2022.1 preservados; período de parte do conjunto ainda indeterminado).
- [ ] Comparar Fichas 2 do mesmo código para medir variação entre ofertas.
- [ ] Classificar o grau de especificidade das Fichas 1 sem inferir conteúdo ausente.
- [ ] Catalogar regulamentos próprios de estágio, TCC, extensão e atividades formativas.
- [ ] Resolver a divergência do Portal do Ementário, que ainda expõe a matriz anterior.
- [ ] Representar a estrutura e as dependências em formato estruturado.

### 3. História administrativa e indicadores

- [ ] Preservar atos de criação e reconhecimento do curso.
- [ ] Preservar atas e pareceres da reforma aprovada em 2022.
- [x] Obter e documentar a série disponível de vagas e concorrência, mantendo explícitas as lacunas de candidatos absolutos, ocupação final e notas de corte.
- [x] Obter séries oficiais de ingresso, permanência, evasão e conclusão nos recortes disponíveis da UFPR e do INEP.
- [x] Identificar metodologia, denominadores e recortes temporais de cada indicador, separando medidas anuais de acumulados por coorte.
- [ ] Obter avaliações institucionais, Enade, relatórios da CPA e dados do e-MEC.
- [x] Separar indicadores específicos do curso de diagnósticos gerais do Setor de Ciências Exatas.

Síntese, dados e auditoria: [`administracao/dados/`](administracao/dados/).

### 4. Edital e proposta de reorganização de 2026

- [x] Edital nº 01/2026-PROGRAP/PROPLAD preservado.
- [x] Apêndice B preenchido preservado e descrito.
- [ ] Localizar e preservar o Apêndice A e o memorando de encaminhamento.
- [ ] Localizar atas e deliberações do NDE, Colegiado e Conselho Setorial.
- [ ] Localizar resultado final e pareceres da PROGRAP/PROPLAD.
- [ ] Localizar submissão institucional e decisão do MEC.
- [ ] Obter a matriz proposta de Inteligência Artificial Aplicada à Saúde.
- [ ] Obter ementas, Fichas 1, PPC ou minutas dos novos componentes propostos.
- [ ] Identificar precisamente componentes mantidos, removidos, reduzidos, substituídos e compartilhados.
- [x] Classificar documentalmente as alegações de baixa procura, evasão, demanda por IA e suficiência de infraestrutura, registrando confirmações, suporte parcial e itens não validados.
- [ ] Identificar condições e garantias relativas às duas vagas docentes solicitadas.
- [ ] Determinar o estágio correto: proposta, selecionada, aprovada, autorizada ou implementada.

### 5. Comparação e análise

- [ ] Comparar 2011 e 2023 somente após completar seus inventários documentais.
- [ ] Comparar ementas e programas, não apenas códigos e nomes.
- [ ] Analisar progressão, pré-requisitos, continuidade e redundância dos conteúdos.
- [ ] Comparar a formação em Computação, Biociências, Saúde e integração interdisciplinar.
- [ ] Avaliar a proposta de 2026 contra os currículos reconstruídos e os indicadores verificados.
- [ ] Produzir análise final distinguindo fatos, alegações institucionais e interpretação.

## Prioridade imediata

Direção atual: a entrega documental N1-N6 está concluída com exceções documentadas. Novas evidências podem entrar por Work limitado quando forem fornecidas ou surgir uma pista concreta. Comparações e síntese analítica continuam adiadas.

O roteiro autoritativo e seus critérios de conclusão estão em [`governance/ROADMAP.md`](governance/ROADMAP.md). Em resumo:

1. autorizar um novo Work de P2 para reconciliar documentos, auditar manifestos e congelar a base documental;
2. manter explícitas as lacunas públicas e humanas herdadas de P1;
3. após o gate P2, autorizar P3 para comparação curricular limitada às evidências disponíveis;
4. após P3, autorizar P4 para síntese e versão reproduzível.

O antigo P2 foi substituído pelo congelamento documental N5, concluído. P3 e a parte analítica de P4 não foram iniciados.
