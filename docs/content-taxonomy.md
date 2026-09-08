# First content taxonomy, 2011–2023

W033 populates the W032 analytical model for review. It is a first,
source-grounded taxonomy, not a completed historical conclusion. Every domain,
topic, occurrence, and lineage relation is `proposed`; every occurrence and
relation has `indeterminate` evidence strength because the available Fichas do
not by themselves establish application to the named curriculum.

## Corpus and generation flow

The consolidated corpus contains 52 preserved source records: 12 associated
with the 2011 investigation and 40 associated with the 2023 investigation.
Forty-nine are eligible for occurrence extraction. Three historical Ficha 2
records are retained for audit but excluded because their own evidence assigns
them to another course. The builder never changes source files.

Run the pipeline from the repository root in this order:

```sh
python scripts/build_w033_content_corpus.py
python scripts/build_w033_taxonomy.py
python scripts/build_w032_site_data.py
python scripts/validate_w033_taxonomy.py
```

The first builder adapts manifests and normalized documentary inventories into
`site/data/source/w033/content-corpus.json`. The second reconciles the two
source-grounded proposal files into `site/data/source/w033/taxonomy.json` and
the split machine-readable files under `site/data/generated/w033/`. The W032
builder then produces the SvelteKit model and copies only allowlisted,
hash-verified documents. Each builder supports `--check` for byte-identical
determinism.

The resulting analytical set has 18 domains, 156 topics, 242 occurrences,
three justified aliases, and 12 lineage candidates. There are no fixtures,
claims, `removed` candidates, or numerical similarity scores.

## Topic and occurrence method

Topics use intermediate granularity: broader than a literal clause and more
specific than a domain. Each topic has one primary domain. Conflicting domain
suggestions remain in identification provenance instead of being silently
erased. Aliases are limited to explicit abbreviations or documented lexical
normalizations and do not form a second topic graph.

An occurrence exists only when an eligible corpus source contains an exact
supporting excerpt. It links a curriculum-specific component instance to a
topic, evidence record, source document, locator, applicability note,
epistemic strength, and review state. Documentary text and component facts
remain in the factual layer; topic assignment remains analytical.

## Lineage candidates

Lineage uses arrays of source and target occurrences, so fragmentation and
merging do not require a one-to-one discipline mapping. Candidate type and
evidence strength are independent. Codes and discipline names are context,
not proof. No embeddings were used, and `similarity_score` is null for every
candidate.

The independent qualitative audit accepted 12 records only as proposed
candidates: eight maintained, one fragmented, one merged, one new relative to
the explicitly sparse corpus, and one indeterminate coverage case. It rejected
an initial reduction candidate because target program text contradicted the
classification. The rejected case remains in the audit trail, not in generated
data. No content is classified as removed.

## Extending and reviewing

To add taxonomy material, add a source-grounded proposal to the appropriate
versioned input, including exact excerpt, locator, source record, proposed
label/domain, aliases, notes, and applicability. Reconcile canonical labels and
domains in the builder, regenerate all downstream layers, and run validation.
Never edit generated JSON directly.

To add an evidence source, first preserve and manifest the original with its
hash and provenance, then add it to the corpus adapter. Public access also
requires a deliberate allowlist entry. The builder rejects missing files,
hash mismatches, symlinks, unapproved repository prefixes, and unexpected
public-tree files.

The review interface supports domain navigation, curriculum filtering,
topic-to-component occurrences, evidence, document metadata and preserved
downloads, review states, and lineage candidates. It deliberately exposes
proposed and indeterminate analysis instead of treating publication as human
approval.

W033 does not evaluate the 2026 proposal, complete the taxonomy, establish
formal continuity, or provide final visual design or narrative.
