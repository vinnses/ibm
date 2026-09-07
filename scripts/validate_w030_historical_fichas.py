#!/usr/bin/env python3
"""Validate W030 historical Ficha extraction outputs and provenance."""
from __future__ import annotations
import csv, hashlib, json, subprocess, sys
from pathlib import Path
ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "dados/curriculos/2011/fichas-preservadas"
DOCS = OUT / "documents.csv"
FIELDS = OUT / "normalized-fields.csv"
EXPECTED = 12
EXPECTED_IDS = {
    "W022-CI055-F1-2011", "W022-CI055-OLDER-COMPONENT", "W022-CI055-F2-2011-1",
    "W022-CI056-F1-2011", "W022-CI056-F2-IBM-2010-1",
    "W022-CI057-F1-2011", "W022-CI057-F2-2011-1",
    "W023-CI244-F1-2011", "W023-CI244-F2-2011-1",
    "W024-BQ005-F1-2022", "W024-BQ054-F1-2022", "W024-CE003-F1-2022",
}
EXPECTED_EMENTA_IDS = {
    "W022-CI055-F1-2011", "W022-CI055-OLDER-COMPONENT", "W022-CI056-F1-2011",
    "W022-CI057-F1-2011", "W023-CI244-F1-2011", "W024-BQ005-F1-2022",
    "W024-BQ054-F1-2022", "W024-CE003-F1-2022",
}
def sha(path):
    h=hashlib.sha256()
    with path.open("rb") as f:
        for c in iter(lambda:f.read(1024*1024),b""): h.update(c)
    return h.hexdigest()
def main():
    errors=[]
    if not DOCS.is_file() or not FIELDS.is_file(): errors.append("expected CSV outputs absent")
    if errors: raise SystemExit("; ".join(errors))
    with DOCS.open(newline="", encoding="utf-8") as f: docs=list(csv.DictReader(f))
    with FIELDS.open(newline="", encoding="utf-8") as f: fields=list(csv.DictReader(f))
    if len(docs)!=EXPECTED or len(fields)!=EXPECTED: errors.append(f"expected {EXPECTED} rows, got documents={len(docs)} fields={len(fields)}")
    ids=[r["document_id"] for r in docs]
    if set(ids)!=EXPECTED_IDS: errors.append("unexpected or missing W022-W024 document IDs")
    if len(set(ids))!=len(ids): errors.append("duplicate document IDs")
    field_ids={r["document_id"] for r in fields}
    if set(ids)!=field_ids: errors.append("document/field IDs differ")
    for d in docs:
        source=ROOT/d["source_path"]; raw=OUT/d["raw_text_path"]
        if not source.is_file(): errors.append(f"missing source {d['source_path']}")
        elif sha(source)!=d["source_sha256"]: errors.append(f"source SHA mismatch {d['document_id']}")
        if not raw.is_file(): errors.append(f"missing raw text {d['document_id']}")
        else:
            obj=json.loads(raw.read_text(encoding="utf-8"))
            if obj.get("source_sha256")!=d["source_sha256"] or not obj.get("pages"): errors.append(f"raw provenance/page failure {d['document_id']}")
        if not d.get("source_path") or not d.get("manifest_path"): errors.append(f"missing provenance {d['document_id']}")
    for f in fields:
        if f.get("status")!="literal_extraction_only": errors.append(f"unexpected interpretation status {f['document_id']}")
        if f["document_id"] in EXPECTED_EMENTA_IDS and not f.get("ementa_literal"):
            errors.append(f"expected literal ementa is empty {f['document_id']}")
        if any(term.lower() in f.get("ementa_literal", "").lower() for term in ("Este plano de ensino", "Documento assinado", "Professor:")):
            errors.append(f"ementa crosses structural boundary {f['document_id']}")
        if any(term.lower() in f.get("program_literal", "").lower() for term in ("Este plano de ensino", "Documento assinado", "Atividade Curricular de Extensão")):
            errors.append(f"program crosses structural boundary {f['document_id']}")
        if any(term.lower() in f.get("evaluation_literal", "").lower() for term in ("Documento assinado", "licenciandos", "Estágio de Formação")):
            errors.append(f"evaluation crosses structural boundary {f['document_id']}")
        if f["document_id"].endswith("-F1-2011") and f.get("program_literal"):
            errors.append(f"unexpected program section in permanent 2011 Ficha 1 {f['document_id']}")
    if errors: raise SystemExit("\n".join(errors))
    print(f"validated {len(docs)} historical Ficha documents; hashes, raw pages, provenance, and normalized rows passed")
if __name__=="__main__": main()
