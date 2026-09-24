"""Validate W045 source preservation and public-document route assumptions."""

from __future__ import annotations

import csv
import hashlib
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SITE = ROOT / "site"


def main() -> None:
    model = json.loads((SITE / "src/lib/data/generated/content-model.json").read_text())
    documents = model["factual"]["documents"]
    ids = [document["id"] for document in documents]
    assert len(ids) == len(set(ids)), "Duplicate public document ID"
    for document in documents:
        assert document["public_path"] == f"/documentos/{document['id']}/arquivo"
        assert (SITE / "static" / document["asset_path"].lstrip("/")).is_file(), document["id"]
        assert document["media_type"] == "application/pdf", document["id"]
    with (SITE / "architecture/sources/manifest.csv").open(newline="", encoding="utf-8") as handle:
        sources = list(csv.DictReader(handle))
    for source in sources:
        original = ROOT / source["local_path"]
        assert original.is_file(), source["source_id"]
        assert hashlib.sha256(original.read_bytes()).hexdigest() == source["sha256"]
    print(f"W045 passed: {len(documents)} public documents, {len(sources)} technical source capture")


if __name__ == "__main__":
    main()
