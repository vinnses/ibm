# Auditable Error Trail

This directory contains append-only error histories for bounded Works. The governing schema is [`../specs/ERROR_RECORD.md`](../specs/ERROR_RECORD.md).

An event remains recorded after correction. A `resolved` label means the stated failure was corrected and verified; it does not mean the historical event is deleted. Open or blocked events must appear in the corresponding handoff and review.

Per-work files avoid concurrent edits to a global log. Integration may update indexes, but must not collapse the event histories into an unauditable summary.
