# W033 lineage quality audit

Date: 2026-09-08  
Reviewer: `lineage-review` subagent — GPT-5.6 Terra, high effort.  
Role and routing rationale: independent cross-curriculum reconciliation, ambiguity review, and qualitative lineage audit; this is the demanding review role recorded in `governance/work-units/W033-first-content-taxonomy.md`.

- Reviewer assignment (primary/subagent, model, effort, routing rationale): subagent / independent lineage, ambiguity, split/merge, and qualitative sample audit / GPT-5.6 Terra / high / demanding cross-curriculum reconciliation required a higher-capability independent review.

## Scope and method

This independent audit read the W033 corpus, both source-proposal datasets and
their reviews, the reconciled taxonomy, the generated lineage output, and
`scripts/build_w033_taxonomy.py`. It checked the 13 generated relations against
the literal normalized excerpts and their locators in the corpus. It did not
use component code or name as evidence of continuity, did not assess the 2026
proposal, and did not alter datasets or builders.

The audit treats a relation as an analytical candidate, not a historical fact.
All source documents used by the candidates have `indeterminate` curriculum
applicability, all relations are `proposed`, and all have `indeterminate`
evidence strength. Those fields are necessary but do not cure a relation that
is contradicted by its available source text.

## Corpus, provenance, and applicability propagation

- The corpus declares 52 preserved source records: 12 attached to the 2011
  side and 40 attached to the 2023 side. All 40 2023 records are
  applicability-indeterminate. On the 2011 side, nine are indeterminate and
  three are explicitly `not_applicable` to Informática Biomédica/96A.
- The three not-applicable Ficha 2 records (`corpus-w022-ci055-f2-2011-1`,
  `corpus-w022-ci057-f2-2011-1`, and `corpus-w023-ci244-f2-2011-1`) are marked
  `occurrence_eligible: false`. Their 18 source-level proposals do not appear
  in the 242 generated occurrences. This is the correct treatment; they have
  not been silently reattached to curriculum 2011.
- The remaining 49 eligible source records are represented by at least one
  occurrence/evidence record. Each of the 242 occurrences has an evidence ID;
  its evidence points to a known W032 document and reproduces the corpus
  applicability note. No eligible occurrence was found with a changed
  applicability note or a missing document reference.
- The apparent 2011 side remains especially weak: some preserved documents
  are dated 2022 or are an undesignated older component document. They are
  correctly retained as indeterminate evidence, not evidence that their
  contents applied to curriculum 96A.

Conclusion: applicability and document provenance are propagated correctly in
the generated occurrence/evidence layer. The coverage limitation must remain
prominent in the site and in any future use of lineage candidates.

## Topic, domain, and alias audit

The reconciliation produces 18 proposed domains, 156 proposed topics, 242
occurrences, and three generated aliases. The domains are broad organizational
groups and the majority of topic labels have suitable intermediate granularity
(for example, `controle de concorrência e recuperação`, `análise filogenética`,
and `modelagem de casos de uso`). The labels do not create a substantive
curricular conclusion by themselves.

The generated aliases are safe and acyclic:

| Topic | Alias | Basis | Verdict |
|---|---|---|---|
| `estrutura de ácidos nucleicos` | `estrutura de ácidos nucléicos` | orthographic accent variation in source proposals | retain |
| `recursão` | `recursividade` | direct lexical/conceptual variation, recorded in CI056 proposals | retain as proposed |
| `sistemas gerenciadores de bancos de dados` | `SGBD` | abbreviation explicitly present in the relevant proposal/source context | retain |

The builder deliberately does **not** import the numerous looser source-agent
aliases. That avoids cycles and unsafe lexical fusion, but it also means that
the generic generated justification for a non-`SGBD` alias should not be read
as a document locator. This is nonblocking: future aliases should carry their
specific proposal/evidence ID and justification.

Two granularity cautions should remain visible for review rather than being
resolved automatically:

1. `programação estruturada` is inferred on the 2011 older CI055 document
   from `FOR`, `WHILE`, `REPEAT`, and `IF`, while the 2023 record uses the
   literal phrase. This is a defensible proposed analytical abstraction, but
   is not an exact textual overlap.
2. `estruturas de dados básicas` is intentionally broad. It cannot alone
   prove coverage of every linear structure named on the 2011 side; this
   directly constrains the merge candidate below.

## Relation-by-relation audit

All quoted text below is the normalized excerpt or program text from
`content-corpus.json`; preserved document bytes remain authoritative.

| Relation | Quoted support checked | Verdict |
|---|---|---|
| `relation-maintained-access` | 2011 CI057 Ficha 1: `Acesso seqüêncial, indexado.` 2023 CI1057 Ficha 1/Ficha 2: `Acesso seqüêncial, indexado.` | Retain as a proposed exact-wording candidate. It is not proof of curricular continuity because both applications are indeterminate. |
| `relation-maintained-search` | 2011 CI056 Ficha 1: `Busca.` 2023 CI1056 Ficha 1/Ficha 2: `Busca`. | Retain only as a broad proposed overlap. The analytical label `algoritmos de busca` is a reasonable expansion of the noun, but neither excerpt establishes scope or continuity. |
| `relation-maintained-sequence-alignment` | 2011 BQ054: `algoritmos de alinhamento de sequências e busca de genes`; 2023 BQ083: the same wording. | Retain as a proposed exact-wording candidate, with the 2022-source/2011-applicability limitation retained. |
| `relation-maintained-phylogeny` | 2011 BQ054: `análise filogenética`; 2023 BQ083: `análise filogenética`. | Retain as a proposed exact-wording candidate under the same applicability limitation. |
| `relation-maintained-omics` | 2011 BQ054: `análise Genômica, Transcriptômica e Proteômica`; 2023 BQ083: `análise Genômica, Transcriptômica e Proteômica`. | Retain as a proposed exact-wording candidate; not a documented historical link. |
| `relation-maintained-biological-databases` | 2011 BQ054: `Banco de dados biológicos`; 2023 BQ083: `Banco de dados biológicos`. | Retain as a proposed exact-wording candidate. It remains separate from general database-system content, appropriately. |
| `relation-maintained-external-sorting` | 2011 CI057 Ficha 1: `Ordenação externa.` 2023 CI1057 Ficha 1/Ficha 2: `Ordenação externa.` | Retain as a proposed exact-wording candidate with indeterminate applicability. |
| `relation-maintained-structured-programming` | 2011 older CI055 program: `Comandos de repetição com FOR`; `WHILE e REPEAT`; `Comando de desvio com IF`. 2023 CI1055 Ficha 1/Ficha 2: `programação estruturada`. | Retain only with the granularity caution above. The 2011 source supports control structures, not its exact label; the relation must remain `proposed`/`indeterminate` and must not be described as textual continuity. |
| `relation-fragmented-order-search` | 2011 CI056 Ficha 2: `Algoritmos fundamentais para pesquisa e ordenação ... em memória principal.` 2023 CI1056 Ficha 1/Ficha 2 separately list `Busca` and `Ordenação`. | Retain as a proposed split/fragmentation representation. It captures a change in analytical segmentation, not a documented organizational split. |
| `relation-merged-linear-structures` | 2011 CI056 Ficha 1: `Tipos abstratos de dados: listas, pilhas, filas.` CI056 Ficha 2: `listas ... filas e pilhas.` 2023 CI1001 Ficha 1/Ficha 2: `Estudo de estruturas de dados básicas.` | Retain only as a `hypothesis`-level proposed merge. The broad target does not explicitly enumerate the source structures; no stronger reading is supported. |
| `relation-new-security-access-control` | 2023 CI1007 Ficha 1/Ficha 2: `Autenticação e controle de acesso.` No matching record is in the declared usable 2011 corpus. | Retain only as a corpus-relative proposed `new` candidate. It must continue to say that sparse 2011 coverage does not establish absence from the 2011 curriculum. |
| `relation-indeterminate-networks` | 2011 CI244 Ficha 1: `Modelos OSI e TCP/IP.` No matching 2023 topic is located in the declared usable Ficha corpus. | Retain. `indeterminate`, rather than `removed`, is the correct classification given incomplete 2023 coverage. |
| `relation-reduced-recursion` | 2011 CI056 Ficha 2 names `Uso de relações de recorrência ... Resolução de relações de recorrência simples.` The target CI1056 Ficha 2 program itself says `relações de recorrência (sem notação assintótica)` and its objective says `Resolver relações de recorrência simples`. | **Reject as `reduced`; blocking correction required.** The target source contradicts the stated basis that recurrence relations are absent/narrowed. Add a source-grounded CI1056 Ficha 2 occurrence for this content and replace the relation with a proposed `maintained` candidate, or remove the candidate until that occurrence is modeled. |

## Required qualitative sample

The sample covers each requested class and confirms that all claims remain
analytical candidates.

| Class | Sample | Result |
|---|---|---|
| Simple continuity | `relation-maintained-access` | Exact wording occurs on both sides, but source applicability prevents a factual continuity conclusion. Retain proposed. |
| New candidate | `relation-new-security-access-control` | 2023 evidence is direct; the negative side is only the sparse usable 2011 corpus. Retain only with its corpus-relative caveat. |
| Possible reduction | `relation-reduced-recursion` | Fails: target CI1056 Ficha 2 explicitly includes recurrence relations. Correct/remove before release. |
| Split | `relation-fragmented-order-search` | Evidence supports a proposed analytical segmentation from one combined unit to two labels; no formal split is established. |
| Merge | `relation-merged-linear-structures` | Source names lists/queues/stacks; target is broad. A hypothesis is representable, but it cannot carry stronger evidence. |
| Indeterminate | `relation-indeterminate-networks` | Correctly avoids a removal claim when later coverage is insufficient. |

## Systematic findings and recommendations

### Blocking before W033 handoff

1. Correct `relation-reduced-recursion`. Its available target Ficha 2 evidence
   positively contains recurrence relations. The correct repair is to generate
   a CI1056 Ficha 2 occurrence grounded in the cited program/objectives and
   then make a proposed, indeterminate-strength `maintained` candidate, or to
   remove the relation. Do not retain `reduced`.

### Nonblocking recommendations

1. Keep every lineage relation visibly labeled as a proposed candidate with
   indeterminate applicability and evidence strength. Do not summarize the
   seven `maintained` records as established historical continuity.
2. Surface the corpus-relative nature of `new` in the site candidate view;
   sparse 2011 coverage prevents a claim of historical absence.
3. For future generated aliases, preserve the proposal/evidence ID that
   justifies the normalization instead of relying on a generic generated note.
4. Add a builder-level regression check that scans the full source sections,
   including Ficha 2 program/objectives, before emitting a `reduced` relation.
   The missed CI1056 recurrence wording shows that comparing only extracted
   topic labels can create a false change candidate.
5. Present the 2022-dated BQ/CE documents attached to the 2011 analytical
   side with their indeterminate applicability note next to the occurrence,
   not only on the evidence detail page.

## Audit conclusion

The source/evidence chain, applicability propagation, proposed review states,
and conservative `indeterminate` network candidate are sound. The taxonomy is
usable for site-based review with the documented granularity cautions. One
material lineage error was found: `relation-reduced-recursion` conflicts with
the target Ficha 2 program and must be corrected or removed before W033 is
handed off. No `removed` relation is present, and this audit contains no 2026
analysis.
