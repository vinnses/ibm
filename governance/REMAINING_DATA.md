# Remaining data: selectable batches and safe stopping points

Updated 2026-09-06 after W022. D01/D02 local extraction is complete; the first D03 search batch preserved eight official records for CI055-CI057 but did not prove curriculum-96A applicability. D09 was refreshed. Remaining gaps require further bounded code batches, protected institutional evidence, or separately selected administrative tables; no collection agent is active.

## What is already available

W009/W010 formal inventories, elective catalogs, dependencies and Ficha statuses; W011 public administrative records; W015 access package (36 datasets, 191 source records, 33 question/search records); W016 Portaria 44/2015 institutional reproduction and historical UFPR annex row. Start at `dados/acesso/README.md`. Record counts are not unique-document counts or a measure of completeness.

Do not repeat completed searches or transcriptions. For example, `curriculos/2023/inventario/ementas.csv` is a document/status index and points to normalized transcriptions already in `fichas/inventario-dinf.md`; use those first. The 2011 ementa inventory records absent portal ementas and cannot supply invented content. W016 recovered an institutional reproduction, not the original DOU facsimile.

## Recommended order for a short remaining session

1. **D01, one five-document batch:** the most predictable useful local output; no network needed.
2. If capacity remains, another D01 batch **or D02, one regulation**. Save and publish the first before starting the second.
3. **D09, package refresh:** update access paths/statuses for whatever actually finished. This may be the last step after any batch; it does not require completing the whole backlog.

If the user already has institutional files to provide, D07/D08 may take priority over local extraction. D03-D06 searches have uncertain yield and should not consume the last available capacity before a saved local output. No minutes/token estimate is promised.

## Batch menu

| ID / proposed priority | Exact small unit and starting inputs | Data output and acceptance | Planned smallest capable tier | Stop boundary / dependency |
|---|---|---|---|---|
| D01 / preserved Fichas | **Complete in W018-W020:** all 40 locally preserved PDFs | 23 separate Ficha 1 records and 17 separate Ficha 2 records under `dados/curriculos/2023/`, with complete normalized source fields, explicit absences, locators, paths and hashes | Luna/medium extraction; primary source review | Integrated through `35aa728`; no locally preserved Ficha remains unstructured. Applicability and unavailable-document gaps remain explicit |
| D02 / local stable rules | **Complete in W021:** TCC, internship, extension and formative activities from preserved 2011/2023 PPCs and formal acts | `dados/curriculos/regras-estaveis/regras.csv`: 75 separate source provisions with version, exact locator, workload/process fields and uncertainty | Luna/medium extraction; primary source review | Integrated by `257da0c`; no current-practice check or silent conflict reconciliation |
| D03 / historical curricular gaps | At most three 2011 component codes selected from W009 gap inventory; consult prior NS/HR-W009-001 before searching official historical public archives | Originals plus local manifesto and extracted fields if found; otherwise dated query log per code. Matching code alone never establishes 2011 applicability | Terra/medium; Luna only for identified-file capture | Maximum three targeted public attempts per code; commit each code's outcome. Stop at authentication/archive access; no repeated broad search |
| D04 / 2023 curricular gaps | At most three components with missing Ficha 1 or missing applicability evidence, chosen from W010 components and HR-W010-001 | Original approved Ficha/version evidence, manifesto and literal data, or explicit bounded retrieval/applicability gap | Terra/medium | Maximum three attempts per code; current webpage/offering is not applicability evidence. No requirement to establish present implementation |
| D05 / stable administrative data | One explicitly chosen historical indicator and one source/year or small already-preserved table: absolute applicants, official vacancies, dated evaluation results, or preserved CPA workbook metadata/raw cells | Work-local raw table plus source, year, universe, unit and denominator exactly as stated. Inspect existing datasets first; missing denominator is recorded, not invented. No interpretive aggregate | Luna/medium for preserved tables; Terra/medium for retrieval | One table or one source/year per commit. Annual and cohort records stay separate. Final occupancy/cutoff series needing unmatched data goes to HR-W011-003 |
| D06 / exact historical acts | One remaining target: original Resolução 19/10-COUN **or** original DOU facsimile for Portaria 44/2015 | Exact original plus manifesto and necessary source-stated fields, or a bounded search outcome; retain existing reproduction and earlier W016 searches | Terra/medium | At most three new targeted attempts based on a new lead. No repeat of W016's five COUN searches without new location evidence; stop if no new lead |
| D07 / institutional curricular inputs | One supplied institutional batch: historical applicable Ficha 1s, original departmental allocations, or archived teaching plans only if supplied and relevant | Preserve files separately; record custodian, received date, stated validity/disclosure limits; transcribe only factual document fields. Link HR-W009-001/002 and HR-W010-001/002 | Luna/medium capture; Terra/medium provenance/validity | Requires actual user/custodian files and access authority; no agent contact or access request is authorized. One received document per checkpoint. Active-offering Ficha 2 hunting is deferred |
| D08 / proposal and process inputs | One supplied or precisely located stable 2026 document: proposed matrix/component list/PPC/equivalences first; then Apêndice A, memorandum/process ID or dated deliberation/decision | Original and manifesto; literal matrix/act fields with document status. A proposal is not an approval; do not infer stages or staffing guarantees. Link HR-W011-001 | Terra/medium identification; Luna/medium capture/extraction | One document per commit; requires actual lead or supplied file. No open-ended search of today's process status and no institutional contact |
| D09 / deliver accumulated data | Any completed batch plus current access package; may run after D01 alone | Refresh access datasets/source records, data-only README and concise remaining gaps; validate deterministic outputs and publish saved version. No new analysis report | Luna/medium mechanical refresh; primary review/integration | End with committed and pushed usable data, even if most gaps remain. Do not call the release exhaustive |

Proposed output names above are local to the future Work; determine the exact directory in its specification before execution. D01-D09 are backlog IDs, not model assignments, elapsed-time estimates, active branches or claims of completion.

## Separate lanes that should not consume the short session

- **Human/protected:** the eight questions remain in `governance/human-reviews/W009-p1-curriculum-2011.md`, `W010-p1-curriculum-2023.md` and `W011-p1-admin-procedure.md`. W016 partly addresses HR-W011-002 through a reproduction; original-act gaps remain. Prepare/receive files only when the user chooses; do not send requests on their behalf.
- **Volatile or interpretive:** current offerings, teaching compliance, portal administrative explanation, comparison of Ficha 2 variations, curricular quality, proposal desirability, causal interpretation and P3/P4 analytical synthesis are deferred. Do not pursue them to mark a gap closed.
- **Editorial:** C-W010-003 through C-W010-006 stay in `governance/corrections/W010.md`; fix only if an actual material data-use problem depends on them. They do not block collecting data.

## Per-batch save contract

1. User selects batch and maximum extent, e.g. **D01: first five Ficha 1s only**. Read current main, create a Work/branch, and record actual model/effort and target files before delegation. Do not reserve several future Works merely to fill the backlog.
2. Commit a short Work specification and handoff with `active substep`, `last saved commit`, `next action` and `not performed`. If the lower-tier runtime remains unavailable, record any user-authorized primary takeover; never assume the quota reset.
3. For each document: preserve original plus local provenance/hash before reliance; extract needed data with exact locator; validate source identity/fields; commit. Existing source bytes and versions remain unchanged.
4. Publish the checkpoint branch after the material checks. Only then start the next document/batch. An interruption must leave the previous data usable, not only a plan or half-built script.
5. Primary reviews proportionately, integrates the selected completed batch, updates DATA_FIRST/WORK_INDEX and the access package, and pushes main. Keep source/validation defects separate from nonblocking editorial items. Do not launch a second review merely to polish process prose.
6. Stop at the user's chosen extent. Update the resume line to the next unstarted batch; do not enter another batch or any analysis phase automatically.

## Status to resume from now

W020 completed D01 for all locally preserved Fichas and refreshed D09. There is no third local extraction batch. Any further Ficha work requires retrieval or supply of documents not currently preserved, especially applicable historical versions and term/class-specific plans. D02 and the other non-Ficha data topics remain separate and unstarted.
