# Historical review UI

W034 turns the W032/W033 public model into a review interface for the 2011 and
2023 curricula. It does not analyze the 2026 proposal. Its editorial principle
is: **“O site protesta; os dados depõem.”**

## Visual separation

The editorial layer uses large condensed headings, black rules, red stamps,
highlight marks, slight rotations, and poster-like blocks. These devices frame
the investigation on the homepage and in section openings. They never encode
an epistemic state by themselves.

The documentary and analytical layer uses neutral paper/surface backgrounds,
system sans-serif text, stable spacing, conventional lists, textual labels,
and direct evidence links. Red is reserved for interventions, selection, and
conflict accents rather than filling the data interface.

## Visual grammar

Three independent dimensions remain visible:

| Dimension | Encoding | Rule |
|---|---|---|
| Change type | line pattern plus textual type | solid for `maintained`; double/intervention edge for `fragmented` and `merged`; dashed for `indeterminate`; every card prints the type |
| Evidence strength | line weight/opacity plus `StatusBadge` text | strength never inherits from change type; W033 relations display `indeterminate` explicitly |
| Review state | labelled badge | `proposed` means an inspectable analytical hypothesis, not an error |

Document coverage uses a symbol and text, never color alone:

- `● Cobertura suficiente`: an applicable Ficha is linked with documented or
  strongly supported applicability;
- `○ Documento não localizado`: an applicable content document was not
  located; this is not proof of nonexistence;
- `◐ Aplicabilidade indeterminada`: a Ficha exists, but its applicability to
  the historical curriculum is not established;
- `× Fonte contraditória`: a contradiction is recorded;
- `? Cobertura indeterminada`: the available records do not support another
  classification.

The W034 view derives coverage only from documents linked to component topic
occurrences plus the component's explicit gap note. It does not mutate W033
data or infer applicability from a code, title, or date.

## Interaction and responsive behavior

`/mapa-curricular` displays two periodized columns on desktop. Selecting a
component highlights shared topic IDs and candidate-relation endpoints, then
opens an inspection panel with workload, prerequisites, topics, counterparts,
relation caveats, and evidence. Selecting a topic switches to a side-by-side
occurrence comparison by curriculum.

On screens up to 700 px, the columns are not scaled down. A labelled 2011/2023
switch shows one full-width curriculum at a time; the inspection panel becomes
one column. All component cards are buttons, selection uses `aria-pressed`, the
panel announces updates through `aria-live`, and a skip link, visible focus,
non-color labels, and reduced-motion behavior support keyboard use.

## Visualization dependency decision

No graph library was added. The required layout is a periodized pair of
selectable lists with a small number of proposed relations, and Svelte state
plus CSS provides the filtering, highlighting, comparison, and responsive
behavior without a heavy client dependency. D3 or Cytoscape would add bundle
and interaction complexity without improving the current 12-candidate review
task. This decision should be revisited only if later evidence creates a graph
whose layout cannot remain legible as periodized lists.

## Future document ingestion

The existing boundary supports later Ficha ingestion without redesigning the
UI:

```text
new document
  → preserve original bytes + record provenance + SHA-256
  → create Evidence with page/section/excerpt and applicability
  → create or revise TopicOccurrence
  → rerun deterministic taxonomy/site builders
  → review generated analytical states
  → rebuild the interface
```

The new document must first enter the allowlisted public-document model. A
matching component code or date is never sufficient to set applicability.
Multiple Ficha 2 versions remain separate. Reprocessing changes displayed
coverage automatically because W034 derives it from the evidence graph rather
than maintaining a second manual coverage table.
