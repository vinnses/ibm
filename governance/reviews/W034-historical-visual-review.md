# W034 — Historical visual review acceptance audit

- Reviewer assignment (primary/subagent, model, effort, routing rationale): primary session / final interface, data-boundary, regression, security, and acceptance audit / GPT-5 family, exact backend unknown / effort unknown / final audit and cross-cutting integration remain under primary-session authority; no subagent was used.

## Verdict

**Approved for bounded W034 completion with one accepted visual-tooling
exception.** The 2011→2023 curriculum is explorable by period, component, and
content; proposed relations, source limitations, and preserved evidence remain
explicit. The production build, runtime routes, responsive implementation, and
data/security invariants pass. The in-app browser exposed no browser instance,
so rendered-pixel screenshot inspection at desktop/mobile widths remains an
accepted environment exception (E-W034-005), not a claimed completed check.

## Acceptance review

| Criterion | Observed evidence | Result |
|---|---|---|
| Historical map | `/mapa-curricular` renders 2011 and 2023 as separate eight-period columns with 84 selectable components | pass |
| Discipline exploration | selection exposes workload, period, prerequisites/conditions, extracted topics, proposed counterparts, lineage caveats, coverage, and evidence | pass |
| Content following | topic selection and `/conteudos/[id]` show domain, aliases, 2011/2023 occurrences, excerpts, review/strength, applicability, candidates, and evidence | pass |
| Side-by-side comparison | selected components show shared and both-side exclusive topic sets; topic records render curriculum columns | pass |
| Epistemic separation | change type uses pattern/text, evidence strength uses an independent labelled badge, and review state remains separately labelled | pass |
| Proposed state | all 12 W033 candidates remain `proposed` and `indeterminate`; no UI element upgrades them to fact | pass |
| Documentary gaps | derived display states classify 53 components as document not located and 31 as Ficha applicability indeterminate; no empty region implies absence | pass |
| Evidence access | component, topic, relation, evidence, and document views resolve to records; preserved file opens from an ID-only allowlisted route, with `#page=` when numeric | pass |
| Filters | curriculum, period, domain, discipline, review state, evidence strength, document availability, cross-curriculum topics, proposed-only, and indeterminate-only controls are present and reactive | pass |
| Responsive contract | desktop retains two columns; ≤700 px uses one full-width curriculum with a 2011/2023 switch and single-column drawers/comparisons rather than scaled cards | pass by build/source/runtime; pixel inspection exception |
| Accessibility | semantic buttons, `aria-pressed`, `aria-live`, labelled controls, skip link, visible 3 px focus, reduced-motion handling, text/symbol/pattern redundancy, and zero Svelte warnings | pass |
| Contrast | primary tested pairs range from 5.57:1 to 15.59:1, including white/red action text, link/surface, body/paper, and focus/surface | pass |
| Editorial identity | paper, black rules, red intervention, stamps, marker, poster typography, and annotated-document references are concentrated in editorial framing | pass |
| Data readability | data panels use neutral surfaces, system text, restrained borders, textual states, and direct provenance links | pass |
| Library decision | no D3/Cytoscape/chart dependency; Svelte state and CSS fit 12 current relations and the periodized task | pass |
| W031/W032/W033 safety | builders deterministic; model/provenance checks, ID resolution, preserved SHA-256, unknown IDs, traversal, public-tree, secrets, Compose segmentation, and non-root/read-only controls pass | pass |
| 2026 boundary | homepage explicitly states that this stage does not analyze 2026; no 2023→2026 comparison or substantive conclusion was added | pass |

## Interface-based sample audit

The production route was loaded with a selected component query for each
sample, and its rendered server output was checked for the relation caveat,
review state, evidence strength, coverage, and links:

| Requested class | Sample | Review result |
|---|---|---|
| simple continuity | `relation-maintained-access`, CI057→CI1057 | clearly proposed; exact-label overlap does not appear as formal equivalence |
| split | `relation-fragmented-order-search`, CI056→CI1056 | multi-target candidate and “not a formal equivalence” caveat visible |
| merge | `relation-merged-linear-structures`, CI056→CI1001 | broader target and hypothesis caveat visible |
| new | `relation-new-security-access-control`, CI1007 | bounded sparse-corpus limitation visible; no historical absence claim |
| indeterminate | `relation-indeterminate-networks`, CI244 | incomplete 2023 coverage blocks a removal reading |
| missing Ficha | `curriculum-2011-ba040` | “Documento não localizado” plus nonexistence warning visible |
| applicability indeterminate | `curriculum-2011-bq005`; `document-bf114-ficha-1` | preserved Ficha and curriculum applicability remain visibly separate |

No evident W033 data defect was found. No taxonomy, occurrence, relation,
review state, evidence strength, or applicability value was corrected in W034.
The audit did expose a W031 homepage identity regression introduced by W034;
it was restored and recorded as E-W034-008.

## Visual balance and limits

The militant identity is perceptible in the homepage, map opening, stamps,
annotations, rules, and red intervention accents. Data remain more legible than
ornamentation because analytical cards use neutral surfaces and labels. A later
Work may refine line routing or add a compact relation overview if the number
of reviewed candidates grows substantially; adding a graph library is not
justified at the current scale.

Rendered screenshot inspection should be repeated when a browser instance is
available. No screenshots were committed because no repository convention was
found and the required browser surface was unavailable.
