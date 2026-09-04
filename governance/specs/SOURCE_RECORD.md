# Source Preservation Specification

## Required record

Record these fields when applicable:

| Field | Meaning |
|---|---|
| `id` | Stable repository identifier |
| `title` | Documentary title as published |
| `institution` | Issuing institution or body |
| `source_url` | Original URL or explicit user-provided origin |
| `accessed_at` | ISO date of retrieval |
| `document_date` | Date printed in or assigned by the source |
| `document_type` | Resolution, PPC, Ficha 1, Ficha 2, dataset, HTML page, etc. |
| `local_path` | Stable repository-relative path |
| `sha256` | Lowercase 64-character digest of preserved bytes |
| `version_or_validity` | Version, curriculum applicability, term, or unknown state |
| `purpose` | Claim or extraction supported by the source |
| `status` | Preserved, incomplete, conflicting, not located, or approved exception |
| `notes` | Normalization, capture, access, or authenticity limits |

## Capture rules

- Preserve downloadable originals without modifying bytes.
- Capture evidentiary web pages as HTML or another documented representation.
- Preserve the exact file used by an extraction, not only a later equivalent.
- Store normalized extracts separately from originals and describe transformations.
- Use repository-relative paths. Temporary absolute paths are invalid for preserved records.
- For large files, prefer Git LFS or another repository-backed, versioned mechanism. A URL plus digest is a discovery record, not full preservation.

## Negative search record

Record query terms, official domains, date, result, and limits. Do not transform a negative public search into proof that a document does not exist.

## Validation

Run `python scripts/validate_repository.py`. Any malformed or mismatched SHA-256 is a blocker. Unpreserved records may remain warnings only when the roadmap and handoff call them out explicitly.
