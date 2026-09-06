#!/usr/bin/env python3
"""Validate contiguous W024 per-code official-public Ficha search checkpoints."""
from __future__ import annotations
import csv, hashlib, sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
BASE = ROOT / "curriculos/2011/fichas"
LOTS = (("L1", ("CM201", "CM045", "BA040")), ("L2", ("CI067", "CM005", "BQ005")), ("L3", ("CI166", "BQ054", "BC056")), ("L4", ("CI215", "CI062", "CE003")), ("L5", ("CI164", "BF075", "BG054")), ("L6", ("CI162", "CI065", "CI171")), ("L7", ("CI316", "MN127", "CI167")), ("L8", ("CI209", "CI218", "CI394")), ("L9", ("MN128", "CI220", "CI221")), ("L10", ("CI169", "CI172", "MN129")), ("L11", ("CI262",)))
FIELDS = ("accessed_at", "domains", "terms", "result", "limits", "applicability_consequence")
def rows(path: Path):
    with path.open(encoding="utf-8", newline="") as f: return list(csv.DictReader(f))
def digest(path: Path):
    h=hashlib.sha256()
    with path.open("rb") as f:
        for b in iter(lambda:f.read(1024*1024),b""): h.update(b)
    return h.hexdigest()
def main():
    errors=[]; completed=[]; sources=0; missing_seen=False
    for lot,codes in LOTS:
        dirs=[BASE/f"w024-{c.lower()}" for c in codes]
        present=[d.is_dir() for d in dirs]
        if any(present) and not all(present): errors.append(f"{lot}: partial lot directories")
        if all(present):
            if missing_seen: errors.append(f"{lot}: completed after a missing earlier lot")
            completed.append(lot)
        else: missing_seen=True
        for code,d in zip(codes,dirs):
            if not d.is_dir(): continue
            for name in ("README.md","manifesto.csv","buscas-negativas.csv"):
                if not (d/name).is_file(): errors.append(f"{code}: missing {name}")
            if not (d/"manifesto.csv").is_file() or not (d/"buscas-negativas.csv").is_file(): continue
            manifest=rows(d/"manifesto.csv"); sources+=len(manifest)
            for r in manifest:
                p=ROOT/r.get("local_path","")
                if not p.is_file(): errors.append(f"{code}: missing manifested {r.get('local_path')}")
                elif digest(p)!=r.get("sha256"): errors.append(f"{code}: hash mismatch {r.get('local_path')}")
                if r.get("document_type") not in {"Ficha 1","Ficha 2"}: errors.append(f"{code}: unsupported document type")
                if r.get("status")!="preserved_indeterminate": errors.append(f"{code}: applicability status must be preserved_indeterminate")
                if ".ufpr.br/" not in r.get("source_url",""): errors.append(f"{code}: non-UFPR source URL")
            searches=rows(d/"buscas-negativas.csv")
            expected={f"W024-{code}-{n:02d}" for n in range(1,4)}
            if len(searches)!=3 or {r.get("search_id") for r in searches}!=expected: errors.append(f"{code}: exactly three attempts required")
            for r in searches:
                if r.get("targets")!=code: errors.append(f"{code}: out-of-scope target")
                for field in FIELDS:
                    if not r.get(field): errors.append(f"{code}: missing {field}")
    if errors:
        for e in errors: print(f"ERROR: {e}",file=sys.stderr)
        return 1
    print(f"W024 validation passed: completed lots={','.join(completed) or 'none'}; codes={sum(len(c) for l,c in LOTS if l in completed)}; preserved sources={sources}; three attempts per completed code.")
if __name__=="__main__": raise SystemExit(main())
