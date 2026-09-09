# Linha editorial inicial para a discussão da nova grade

> **Status:** base argumentativa provisória de W035. Este texto inicia a
> discussão, mas não apresenta uma matriz curricular completa, distribuição de
> carga horária, parecer sobre aprovação nem conclusão definitiva sobre a
> proposta de 2026.

## Tese de abertura

**Se a proposta quer inteligência artificial no nome, precisa sustentar
inteligência artificial na formação.**

Uma graduação orientada a IA não pode ser construída apenas com ferramentas,
interfaces ou famílias de modelos atualmente populares. Ela precisa formar a
cadeia de competências que permite compreender por que um método funciona,
quando falha, quanto custa, como é implementado e como pode ser auditado em um
contexto de saúde.

Por isso, IA não substitui fundamentos: depende deles. Programação, algoritmos
e estruturas de dados, matemática discreta, álgebra linear, probabilidade e
estatística, otimização, arquitetura, sistemas, paralelismo, bancos de dados,
engenharia de software e segurança não são um passado a ser removido para abrir
espaço à IA. São parte da infraestrutura intelectual e técnica que torna uma
formação em IA mais do que treinamento de uso.

Essa é uma **proposta normativa** para orientar a discussão. A composição
exata, a profundidade e a carga de cada eixo ainda precisam ser demonstradas
por uma matriz, por objetivos de aprendizagem e pelas dependências entre
componentes.

## Correção factual de partida

O repositório permite afirmar duas coisas diferentes:

- **Fato documentado:** o currículo vigente preservado totaliza 3.200 horas.
- **Declaração da proposta:** o Apêndice B informa uma passagem de 3.200 para
  2.700 horas.

O repositório **não contém evidência de que 2.700 horas sejam um teto imposto
pelo MEC**. Também não contém a matriz proposta que explicaria como se chega a
esse total. Portanto, W035 trata 2.700 horas como uma intenção declarada pela
proposta, não como limite normativo provado.

Neste estágio, a carga total é uma restrição que a futura matriz terá de
demonstrar, e não um objetivo acadêmico capaz de justificar, por si só, a perda
de competências. Primeiro é preciso definir o que o egresso deve saber; depois,
avaliar quanto disso pode ser integrado ou comprimido sem falsificar o perfil
prometido.

## Estatuto das premissas

| Enunciado de trabalho | Estatuto em W035 | Uso permitido agora |
|---|---|---|
| O currículo vigente tem 3.200 horas | **Fato documentado** | Ponto de comparação factual |
| A proposta declara 2.700 horas | **Declaração de proposta** | Meta declarada, ainda sem matriz preservada |
| 2.700 horas seriam o máximo permitido pelo MEC | **Não localizado / não provado** | Questão documental, não premissa factual |
| Biológicas não abrirá novas disciplinas para o curso | **Testemunho da parte interessada** | Restrição estratégica para cenários, não posição institucional comprovada |
| Saúde admite diálogo, mas não redução de carga | **Testemunho da parte interessada** | Hipótese de negociação, não posição institucional comprovada |
| Componentes de Saúde são candidatos preferenciais à redução | **Interpretação estratégica da parte interessada** | Hipótese a testar por conteúdo, resultados de aprendizagem e evidência |
| A quarta edição de AIMA deve organizar a espinha de IA | **Proposta normativa** | Referência de coerência, não matriz pronta nem autoridade regulatória |
| Bases matemáticas e computacionais devem ser protegidas | **Proposta normativa apoiada por raciocínio curricular** | Critério de avaliação da futura matriz |

O registro completo dessas premissas e seus limites está em
[`governance/research-hypotheses/2026-09-09-editorial-premises.md`](../governance/research-hypotheses/2026-09-09-editorial-premises.md).

## AIMA como eixo de coerência, não como grade pronta

A página oficial preservada da Pearson identifica *Artificial Intelligence: A
Modern Approach*, de Stuart Russell e Peter Norvig, como quarta edição. A mesma
página combina metadados de variantes: publicação em 21 de dezembro de 2021,
copyright 2022 e um ISBN impresso listado como 2020. Por isso, este trabalho usa
“quarta edição” e preserva as datas sem reduzi-las à expressão ambígua “edição
de 2022”.

A fonte oferece uma sequência pública de 27 capítulos. W035 deriva dessa
sequência uma leitura curricular em seis blocos. Essa divisão é uma
**interpretação curricular**, não uma determinação editorial da Pearson e não
prova que a UFPR deva adotar determinado número de disciplinas.

| Bloco curricular derivado | Capítulos de referência | Função formativa | Possíveis unidades curriculares — todas **propostas** |
|---|---:|---|---|
| 1. Fundamentos e agentes | 1–2 | Delimitar IA, agentes e critérios de racionalidade | Introdução à IA; pode ser integrada ao bloco 2 |
| 2. Resolução de problemas, busca e otimização | 3–6 | Busca, problemas complexos, competição e restrições | Fundamentos de IA e Resolução de Problemas; ou Busca e Otimização Inteligente |
| 3. Conhecimento, raciocínio e planejamento | 7–11 | Lógica, representação, inferência e planejamento | Representação do Conhecimento, Raciocínio e Planejamento |
| 4. Incerteza e decisão | 12–18 | Modelagem probabilística, decisões e ambientes multiagentes | IA Probabilística e Tomada de Decisão |
| 5. Aprendizagem | 19–22 | Aprendizagem por exemplos, modelos probabilísticos, redes profundas e reforço | Aprendizado de Máquina; Aprendizado Profundo; reforço em unidade própria ou avançada conforme a futura matriz |
| 6. Comunicação, percepção e ação | 23–25 | Linguagem, percepção visual e ação robótica | Processamento de Linguagem Natural; Visão Computacional; Sistemas Inteligentes ou Robótica quando houver suporte curricular |
| Eixo transversal | 26–27 | Filosofia, ética, segurança e futuro da IA | Governança e ética em todos os componentes e em projeto integrador, não como item isolado de conformidade |

O original preservado, seu hash e a finalidade probatória estão registrados no
[`manifesto de fontes de W035`](fontes/manifest.csv). O livro oferece cobertura
conceitual ampla; ele não resolve sozinho carga horária, pré-requisitos,
recursos docentes, aderência às diretrizes brasileiras nem integração com o
domínio da saúde.

## Arquitetura curricular candidata

Esta arquitetura é um mapa de competências para discussão, não uma lista
aprovada de disciplinas.

### Fundamentos a preservar e demonstrar

- matemática discreta, cálculo, álgebra linear, probabilidade, estatística e
  otimização/métodos numéricos;
- programação, algoritmos, estruturas de dados e análise de complexidade;
- arquitetura de computadores, sistemas operacionais, redes e processamento
  paralelo ou distribuído;
- bancos de dados e engenharia de dados;
- engenharia de software, reprodutibilidade, testes e segurança.

Preservar não significa necessariamente manter cada nome, fronteira ou carga
atual. Significa que qualquer fusão, redução ou deslocamento deve mostrar onde
ficou cada competência, com que profundidade e quais pré-requisitos continuam
válidos.

### Espinha candidata de IA

1. Fundamentos de IA e Resolução de Problemas;
2. Representação do Conhecimento, Raciocínio e Planejamento;
3. IA Probabilística e Tomada de Decisão;
4. Aprendizado de Máquina;
5. Aprendizado Profundo;
6. Processamento de Linguagem Natural;
7. Visão Computacional;
8. integração aplicada à saúde, com projeto, governança, ética, segurança e
   avaliação de impacto.

Separar aprendizado de máquina de aprendizado profundo, assim como linguagem
de visão, é uma **hipótese curricular plausível**, não uma decisão fechada. A
separação só se sustenta se cada componente tiver objetivos próprios,
pré-requisitos coerentes, profundidade suficiente e docentes disponíveis. Um
currículo “recheado de IA” não deve multiplicar nomes sem multiplicar
competências.

## Saúde e restrições setoriais

A identidade “IA aplicada à saúde” exige competência no domínio de aplicação.
Dados clínicos, processos assistenciais, incerteza, vieses, privacidade,
governança, segurança e consequências de erro não podem aparecer apenas como
exemplos decorativos em disciplinas genéricas.

Ao mesmo tempo, W035 não assume como fato que o Setor de Ciências Biológicas
recusará novos componentes nem que o Setor de Ciências da Saúde recusará
reduções. São expectativas relatadas pela parte interessada. Para elaborar
cenários sem ocultá-las, adotam-se provisoriamente estas regras:

- **Biológicas:** não depender da criação de uma nova disciplina pelo setor no
  cenário de referência. Isso não autoriza remover competências biológicas já
  necessárias; integração em componentes existentes ou conduzidos pelo curso
  precisa de suporte acadêmico e institucional.
- **Saúde:** não antecipar uma redução como acordo obtido. Componentes podem ser
  examinados quanto a sobreposição, integração e resultados de aprendizagem,
  mas “candidato à redução” continua sendo posição de negociação, não conclusão
  documental.
- **Informática/Exatas:** qualquer ampliação de IA deve explicitar os
  fundamentos e a capacidade docente que a sustentam. A proposta preservada
  solicita dois docentes adicionais, mas solicitação não prova concessão nem
  disponibilidade.

As Fichas que vierem da Secretaria poderão alterar esse diagnóstico. Até sua
ingestão e validação, ausência de Ficha não prova ausência de conteúdo, e código
ou data não bastam para definir aplicabilidade curricular.

## Testes para qualquer futura matriz

Uma matriz candidata só deve avançar se permitir responder, com evidência:

1. Para cada componente removido, reduzido ou fundido, quais conteúdos e
   resultados de aprendizagem existiam e onde reaparecem?
2. Cada disciplina de IA possui objetivos distintos e pré-requisitos
   matemáticos e computacionais verificáveis?
3. Alguma base está sendo perdida apenas para atingir 2.700 horas?
4. O total proposto inclui corretamente todos os tipos de carga e atende à
   norma aplicável, ainda a localizar e interpretar?
5. Há capacidade docente e departamental separada da ambição declarada na
   proposta?
6. A aplicação à saúde envolve domínio, dados, governança e risco, em vez de
   somente exemplos temáticos?
7. Fusões evitam duplicação sem transformar conteúdos profundos em menções
   superficiais?
8. Há plano de transição, pré-requisitos e equivalências para estudantes já
   matriculados?

## Vocabulário editorial inicial

As formulações abaixo são **propostas normativas de comunicação**, não fatos:

> IA não substitui fundamentos; depende deles.

> Uma grade de IA não se mede pelo número de disciplinas com “IA” no nome, mas
> pela cadeia de competências que torna seus modelos compreensíveis, auditáveis
> e eficientes.

> Reduzir carga não pode significar ocultar perda formativa.

> Primeiro definimos o que o egresso precisa saber; depois discutimos quanto
> pode ser comprimido sem falsificar esse perfil.

O tom pode ser firme sem apagar incerteza, testemunho ou falta documental. A
argumentação pública futura deve continuar distinguindo o que os documentos
estabelecem, o que inferimos deles e o que defendemos como projeto de curso.

## Evidências ainda necessárias

- matriz completa que totaliza as 2.700 horas e sua tabela de equivalências;
- ato normativo usado para sustentar eventual mínimo, máximo ou parâmetro de
  carga horária;
- Fichas aplicáveis dos componentes atuais e dos cenários propostos;
- manifestações formais dos departamentos e setores sobre oferta e carga;
- disponibilidade docente, infraestrutura e sequência de implantação;
- objetivos de aprendizagem e pré-requisitos de cada novo componente;
- documentação de transição dos estudantes e tratamento das versões
  curriculares.

## Adiamentos explícitos

W035 não escolhe disciplinas a remover, não fixa horas, não fecha uma matriz,
não recomenda aprovação ou rejeição da proposta, não converte expectativas
setoriais em fatos, não executa a comparação sistemática 2023→2026 e não inicia
campanha ou manifesto final.
