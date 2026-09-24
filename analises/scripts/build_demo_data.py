"""Build the first public analytical slice from formal curriculum inventories."""

from __future__ import annotations

import csv
import hashlib
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
OUTPUT = ROOT / "analises/data"
RELEASE_ID = "formal-coded-components-2011-2023-v1"
SOURCES = {
    2011: ("curriculos/2011/fontes/resolucao-34-2010-cepe.pdf", "document-2011-resolution-34-2010"),
    2023: ("curriculos/2023/fontes/resolucao-75-22-cepe.pdf", "document-2023-resolution-75-22"),
}
FIELDS = [
    "curriculum_year", "recommended_period", "component_code", "component_name",
    "component_kind", "workload_hours", "formal_basis", "source_document_id", "source_sha256",
]


def digest(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def rows() -> list[dict[str, str]]:
    result = []
    for year in (2011, 2023):
        inventory = ROOT / f"curriculos/{year}/inventario/componentes.csv"
        source_path, source_id = SOURCES[year]
        source_hash = digest(ROOT / source_path)
        with inventory.open(encoding="utf-8", newline="") as handle:
            for item in csv.DictReader(handle):
                if year == 2011:
                    if item["target_type"] != "coded_component":
                        continue
                    assert item["formal_evidence_path"] == source_path
                    assert item["formal_evidence_sha256"] == source_hash
                    period = item["recommended_term"]
                    kind = "componente codificado"
                    formal_basis = "Resolução 34/2010-CEPE"
                else:
                    if not item["code"]:
                        continue
                    assert "75/22" in item["formal_basis"]
                    period = item["recommended_period"]
                    kind = item["nature"]
                    formal_basis = item["formal_basis"]
                assert period in {str(i) for i in range(1, 9)}
                assert item["code"]
                result.append({
                    "curriculum_year": str(year),
                    "recommended_period": period,
                    "component_code": item["code"],
                    "component_name": item["title"],
                    "component_kind": kind,
                    "workload_hours": item["total_hours"],
                    "formal_basis": formal_basis,
                    "source_document_id": source_id,
                    "source_sha256": source_hash,
                })
    return sorted(result, key=lambda row: (row["curriculum_year"], int(row["recommended_period"]), row["component_code"]))


def main() -> None:
    OUTPUT.mkdir(parents=True, exist_ok=True)
    data = rows()
    assert len(data) == 80
    assert sum(row["curriculum_year"] == "2011" for row in data) == 37
    assert sum(row["curriculum_year"] == "2023" for row in data) == 43
    assert sum(row["component_kind"] == "TCC alternativa" for row in data) == 4
    csv_path = OUTPUT / "formal_components.csv"
    with csv_path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=FIELDS, lineterminator="\n")
        writer.writeheader()
        writer.writerows(data)
    metadata = {
        "release_id": RELEASE_ID,
        "generated_from": [
            {"inventory": f"curriculos/{year}/inventario/componentes.csv",
             "inventory_sha256": digest(ROOT / f"curriculos/{year}/inventario/componentes.csv"),
             "formal_source": SOURCES[year][0], "formal_source_sha256": digest(ROOT / SOURCES[year][0]),
             "public_document_id": SOURCES[year][1]}
            for year in (2011, 2023)
        ],
        "additional_2023_creation_acts": [
            {"path": f"curriculos/2023/fontes/resolucao-{number}-22-cepe.pdf",
             "sha256": digest(ROOT / f"curriculos/2023/fontes/resolucao-{number}-22-cepe.pdf")}
            for number in range(76, 81)
        ],
        "csv_sha256": digest(csv_path),
        "row_count": len(data),
        "row_count_by_curriculum": {"2011": 37, "2023": 43},
        "observation_unit": "one coded component listed in one formal curriculum",
        "exclusions": "2011 elective spaces without codes; 2023 formal elective catalogue and non-coded spaces",
        "important_limit": "The four 2023 TCC codes are alternatives, not four simultaneous completion requirements.",
    }
    (OUTPUT / "release.json").write_text(json.dumps(metadata, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"{RELEASE_ID}: {len(data)} rows; CSV SHA-256 {metadata['csv_sha256']}")


if __name__ == "__main__":
    main()
