#!/usr/bin/env python3
"""Deterministically extract the twelve W022-W024 historical Ficha PDFs.

The preserved PDFs and their per-work manifests are authoritative.  This script
does not assign curriculum applicability and does not rewrite source files.
"""
from __future__ import annotations

import csv
import hashlib
import json
import re
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "dados/curriculos/2011/fichas-preservadas"
RAW = OUT / "raw-text"
MANIFESTS = [
    ROOT / "curriculos/2011/fichas/w022-ci055/manifesto.csv",
    ROOT / "curriculos/2011/fichas/w022-ci056/manifesto.csv",
    ROOT / "curriculos/2011/fichas/w022-ci057/manifesto.csv",
    ROOT / "curriculos/2011/fichas/w023-ci244/manifesto.csv",
    ROOT / "curriculos/2011/fichas/w024-bq005/manifesto.csv",
    ROOT / "curriculos/2011/fichas/w024-bq054/manifesto.csv",
    ROOT / "curriculos/2011/fichas/w024-ce003/manifesto.csv",
]
EXPECTED_IDS = {
    "W022-CI055-F1-2011", "W022-CI055-OLDER-COMPONENT", "W022-CI055-F2-2011-1",
    "W022-CI056-F1-2011", "W022-CI056-F2-IBM-2010-1",
    "W022-CI057-F1-2011", "W022-CI057-F2-2011-1",
    "W023-CI244-F1-2011", "W023-CI244-F2-2011-1",
    "W024-BQ005-F1-2022", "W024-BQ054-F1-2022", "W024-CE003-F1-2022",
}

def sha256(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()

def load_sources() -> list[dict[str, str]]:
    rows = []
    for manifest in MANIFESTS:
        with manifest.open(newline="", encoding="utf-8-sig") as f:
            for row in csv.DictReader(f):
                if row.get("record_id") in EXPECTED_IDS:
                    row["manifest_path"] = manifest.relative_to(ROOT).as_posix()
                    rows.append(row)
    if {r["record_id"] for r in rows} != EXPECTED_IDS or len(rows) != 12:
        raise RuntimeError("expected exactly twelve unique W022-W024 source rows")
    return sorted(rows, key=lambda r: r["record_id"])

def page_text(pdf: Path, page: int) -> str:
    proc = subprocess.run(
        ["pdftotext", "-layout", "-f", str(page), "-l", str(page), str(pdf), "-"],
        check=True, capture_output=True,
    )
    return proc.stdout.decode("utf-8", errors="replace").replace("\r\n", "\n").replace("\r", "\n")

def pdf_pages(pdf: Path) -> list[str]:
    info = subprocess.run(["pdfinfo", str(pdf)], check=True, capture_output=True, text=True).stdout
    match = re.search(r"^Pages:\s+(\d+)$", info, re.MULTILINE)
    if not match:
        raise RuntimeError(f"pdfinfo did not report page count: {pdf}")
    return [page_text(pdf, n) for n in range(1, int(match.group(1)) + 1)]

def first_match(text: str, patterns: list[str]) -> tuple[str, str]:
    for pat in patterns:
        m = re.search(pat, text, re.IGNORECASE | re.MULTILINE)
        if m:
            return m.group(1).strip(), m.group(0).strip()
    return "", ""

def section(text: str, start: list[str], stop: list[str]) -> str:
    # Headings must occupy their own line (possibly followed by an inline
    # value, as in Ficha 2 ``Programa: ...``). This prevents matching words
    # such as ``programação`` or ``extensão`` in ordinary prose.
    start_re = r"(?:" + "|".join(start) + r")"
    stop_re = r"(?:" + "|".join(stop) + r")"
    m = re.search(r"(?im)^[ \t]*" + start_re + r"[ \t]*(?::[ \t]*(?P<inline>[^\n]*))?[ \t]*$", text)
    if not m:
        return ""
    end = re.search(r"(?im)^\s*" + stop_re + r"\b", text[m.end():])
    body = (m.group("inline") or "") + ("\n" + text[m.end():m.end() + end.start()] if end else "\n" + text[m.end():])
    return re.sub(r"\s+", " ", body).strip(" :-")

def locator(texts: list[str], patterns: list[str]) -> str:
    return ";".join(f"page:{i}" for i, t in enumerate(texts, 1) if any(re.search(p, t, re.I | re.M) for p in patterns))

def normalized_fields(texts: list[str]) -> dict[str, str]:
    full = "\n\n".join(texts)
    # Keep literal content after normalization of whitespace only. Empty means
    # the field was not present in the extracted source, not zero or unknown.
    workload, _ = first_match(full, [r"Carga hor[áa]ria:\s*([^\n]+)", r"CH Total:\s*([^\n]+)"])
    prereq, _ = first_match(full, [r"Pr[ée]-requisito:[ \t]*?(.*?)(?=[ \t]+Co-requisito:|\n|$)"])
    coreq, _ = first_match(full, [r"Co-requisito:[ \t]*([^\n]*)"])
    course, _ = first_match(full, [r"Curso:\s*([^\n]+)"])
    term, _ = first_match(full, [r"validade a partir do ano e semestre letivo de\s*([^\n]+)", r"validade a partir do ano e semestre letivo de\s*([^\n]+)"])
    ementa = section(full, [r"EMENTA\s*\(Unidades? did[áa]ticas?\)", r"EMENTA"], [r"Este plano de ensino", r"Professor", r"Aprovado", r"Programa", r"Objetivos", r"Procedimentos did[áa]ticos", r"Documento assinado", r"Art\. 9"])
    program = section(full, [r"Programa"], [r"Procedimentos did[áa]ticos", r"Objetivos", r"Avalia[çc][ãa]o", r"Bibliografia", r"Professor respons[áa]vel", r"Documento assinado"])
    objectives = section(full, [r"Objetivos"], [r"Avalia[çc][ãa]o", r"Bibliografia", r"Professor respons[áa]vel", r"Documento assinado"])
    evaluation = section(full, [r"Avalia[çc][ãa]o"], [r"Bibliografia", r"Professor respons[áa]vel", r"Documento assinado", r"Art\. 9"])
    return {
        "course": course, "term_or_period": term, "workload_literal": workload,
        "prerequisites_literal": prereq, "corequisites_literal": coreq,
        "ementa_literal": ementa, "program_literal": program,
        "objectives_literal": objectives, "evaluation_literal": evaluation,
        "course_locator": locator(texts, [r"Curso:"]),
        "term_locator": locator(texts, [r"validade a partir", r"validity"]),
        "workload_locator": locator(texts, [r"Carga hor[áa]ria", r"CH Total"]),
        "prerequisites_locator": locator(texts, [r"Pr[ée]-requisito"]),
        "corequisites_locator": locator(texts, [r"Co-requisito"]),
        "ementa_locator": locator(texts, [r"EMENTA"]),
        "program_locator": locator(texts, [r"Programa"]),
        "objectives_locator": locator(texts, [r"Objetivos"]),
        "evaluation_locator": locator(texts, [r"Avalia[çc][ãa]o"]),
    }

def main() -> int:
    OUT.mkdir(parents=True, exist_ok=True); RAW.mkdir(parents=True, exist_ok=True)
    rows = load_sources()
    docs, fields, inventory = [], [], {"source": "W022-W024 manifest rows", "documents": []}
    for row in rows:
        pdf = ROOT / row["local_path"]
        if not pdf.is_file(): raise RuntimeError(f"missing source: {pdf}")
        actual_hash = sha256(pdf)
        if actual_hash != row["sha256"]: raise RuntimeError(f"SHA mismatch for {pdf}: {actual_hash} != {row['sha256']}")
        texts = pdf_pages(pdf)
        document_id = row["record_id"]
        raw_rel = Path("raw-text") / (document_id + ".json")
        raw_payload = {"document_id": document_id, "source_path": row["local_path"], "source_sha256": actual_hash, "pages": [{"page": i, "text": t} for i, t in enumerate(texts, 1)]}
        (OUT / raw_rel).write_text(json.dumps(raw_payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
        nf = normalized_fields(texts)
        docs.append({"document_id": document_id, "document_kind": row["document_type"], "source_title": row["title"], "source_path": row["local_path"], "source_url": row["source_url"], "source_sha256": actual_hash, "manifest_path": row["manifest_path"], "document_date": row["document_date"], "applicability": row["status"], "notes": row["notes"], "raw_text_path": raw_rel.as_posix(), "page_count": str(len(texts))})
        fields.append({"document_id": document_id, **nf, "source_path": row["local_path"], "source_sha256": actual_hash, "status": "literal_extraction_only"})
        inventory["documents"].append({"document_id": document_id, "page_count": len(texts), "filled_page_count": sum(bool(t.strip()) for t in texts), "raw_text_path": raw_rel.as_posix()})
    with (OUT / "documents.csv").open("w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=list(docs[0])); w.writeheader(); w.writerows(docs)
    with (OUT / "normalized-fields.csv").open("w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=list(fields[0])); w.writeheader(); w.writerows(fields)
    inventory["document_count"] = len(docs); inventory["extraction_method"] = "pdftotext -layout per page; whitespace normalization only"
    (OUT / "extraction-inventory.json").write_text(json.dumps(inventory, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    return 0

if __name__ == "__main__":
    try: raise SystemExit(main())
    except Exception as exc:
        print(f"ERROR: {exc}", file=sys.stderr); raise SystemExit(1)
