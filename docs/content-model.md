# Content and evidence architecture

W032 prepares a static, versioned data boundary for the SvelteKit site. It does
not define the substantive taxonomy or infer curricular lineage.

## Model and layer boundary

The factual layer contains `Curriculum`, curriculum-specific
`ComponentInstance`, `ComponentDependency`, and `PreservedDocument`. A code or
name is not a cross-curriculum discipline identity: `curriculum-2011-ci055` and
`curriculum-2023-ci1055` remain distinct records. The 2011 Bloco A rule is a
group dependency (`from_component_ids`), not an invented discipline.

The analytical layer contains `ContentDomain`, `ContentTopic`,
`TopicOccurrence`, and `EvolutionRelation`. Occurrences carry their own quoted
or normalized evidence text, locator, evidence strength, notes, and review
state. Relations keep `change_type` independent from `evidence_strength`; no
similarity score establishes a documentary fact. Analytical records only
reference factual IDs and never replace factual source fields.

Review states are `proposed`, `reviewed`, `contested`, and `indeterminate`.
Proposed records remain publishable and receive an explicit interface badge.
The sole W032 domain/topic pair starts with `fixture-`, has `is_fixture: true`,
has no real component occurrence, and exists only to exercise the review UI.

## Evidence and provenance

`Evidence` references one `PreservedDocument` and adds page, section,
cell/range, normalized excerpt, applicability note, documentary state, and
notes. Canonical title, institution, date, URL, repository path, hash, and type
stay on the document record instead of being silently duplicated.
`EvidenceLink` can attach evidence to any factual or analytical entity or to a
future typed `Claim`. Claims declare whether they belong to the factual or
analytical layer.

To add evidence later:

1. Preserve and manifest the original according to the repository method.
2. Add or generate its `PreservedDocument` record from that manifest.
3. Add an `Evidence` record with the exact locator and applicability.
4. Add typed `EvidenceLink` records and list the evidence ID on entities that
   have an `evidence_ids` field.
5. Rebuild and validate; never edit generated JSON directly.

## Deterministic generation

Inputs are the existing 2011/2023 component and dependency CSVs, their source
manifests, `site/data/source/public-documents.json`, and the explicitly
synthetic analytical fixture file. Run from the repository root:

```sh
python scripts/build_w032_site_data.py
python scripts/build_w032_site_data.py --check
python scripts/validate_w032_content_model.py
```

The builder sorts records and uses a source-as-of timestamp, producing
`site/src/lib/data/generated/content-model.json`. `--check` rebuilds in a
temporary directory and requires byte-identical JSON and public files. The
validator evaluates the committed JSON Schema with no third-party Python
dependency, then checks global ID uniqueness, references, states, evidence
origins, source/public hashes, the exact public file set, and negative mutated
cases for orphan IDs, invalid states, duplicates, missing origins, and path
traversal.

W033 replaces the synthetic analytical fixture at build time with a documented
corpus and taxonomy adapter. Its method, population counts, uncertainty rules,
and extension workflow are described in `docs/content-taxonomy.md`. The W032
builder itself still performs no content classification.

## Preserved public documents

Only entries in `site/data/source/public-documents.json` are copied to
`site/static/documents/`. Each entry must resolve to one existing manifest row,
remain under an allowed repository prefix, be a regular non-symlink file, and
match its recorded SHA-256. The generated tree now contains the four formal
curricular documents plus the 52 W033 Ficha source records selected through
the same allowlist and hash checks.

Users follow entity → evidence → document → `/documentos/[id]/arquivo`. The
endpoint accepts only a known document ID and redirects to its generated static
asset. Unknown IDs return 404. No request parameter becomes a filesystem path;
the repository, `.git`, `.env`, Tailscale state, code-server workspace, and
Docker socket are not copied into the web image. Adding another public document
requires a deliberate allowlist entry and successful hash/safety validation.

## Site routes

- `/curriculos` and `/curriculos/[id]` list historical curriculum units and
  their component instances;
- `/disciplinas/[id]` shows factual attributes, dependencies, analytical
  occurrences when present, and evidence;
- `/conteudos` and `/conteudos/[id]` expose analytical state and fixtures;
- `/evidencias/[id]` resolves the locator and source document;
- `/documentos/[id]` shows provenance and provides the preserved copy.

The interface is intentionally plain. It is an inspection surface, not the
project's final narrative or visual identity.
