#!/usr/bin/env python3
"""Focused regression checks for W010 documentary-inventory invariants."""

from __future__ import annotations

import csv
import os
import shutil
import subprocess
import tempfile
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
VALIDATOR = ROOT / "scripts/validate_w010_curriculum_2023.py"


class W010ValidatorRegressionTests(unittest.TestCase):
    def copied_root(self) -> tempfile.TemporaryDirectory[str]:
        directory = tempfile.TemporaryDirectory()
        fixture_root = Path(directory.name)
        shutil.copytree(ROOT / "curriculos/2023", fixture_root / "curriculos/2023")
        return directory

    def validate(self, fixture_root: Path) -> subprocess.CompletedProcess[str]:
        environment = os.environ | {"W010_VALIDATOR_ROOT": str(fixture_root)}
        return subprocess.run(
            ["python", str(VALIDATOR)], text=True, capture_output=True,
            env=environment, check=False,
        )

    def mutate_csv(self, path: Path, predicate, mutate) -> None:
        with path.open(encoding="utf-8", newline="") as stream:
            rows = list(csv.DictReader(stream))
            fields = list(rows[0])
        for row in rows:
            if predicate(row):
                mutate(row)
                break
        with path.open("w", encoding="utf-8", newline="") as stream:
            writer = csv.DictWriter(stream, fieldnames=fields)
            writer.writeheader()
            writer.writerows(rows)

    def test_baseline_passes(self) -> None:
        with self.copied_root() as directory:
            result = self.validate(Path(directory))
        self.assertEqual(result.returncode, 0, result.stderr)

    def test_rejects_omitted_elective(self) -> None:
        with self.copied_root() as directory:
            root = Path(directory)
            path = root / "curriculos/2023/inventario/optativas.csv"
            with path.open(encoding="utf-8", newline="") as stream:
                rows = list(csv.DictReader(stream))
                fields = list(rows[0])
            rows = [row for row in rows if row["code"] != "LIB038"]
            with path.open("w", encoding="utf-8", newline="") as stream:
                writer = csv.DictWriter(stream, fieldnames=fields)
                writer.writeheader()
                writer.writerows(rows)
            result = self.validate(root)
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("92 Resolution 75/22-CEPE", result.stderr)

    def test_rejects_altered_elective_title(self) -> None:
        with self.copied_root() as directory:
            root = Path(directory)
            self.mutate_csv(root / "curriculos/2023/inventario/optativas.csv", lambda row: row["code"] == "CMI104", lambda row: row.__setitem__("title", "APRENDIZAGEM DE MAQUINA"))
            result = self.validate(root)
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("92 Resolution 75/22-CEPE", result.stderr)

    def test_rejects_altered_elective_hours(self) -> None:
        with self.copied_root() as directory:
            root = Path(directory)
            self.mutate_csv(root / "curriculos/2023/inventario/optativas.csv", lambda row: row["code"] == "CMI071", lambda row: row.__setitem__("total_hours", "50"))
            result = self.validate(root)
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("92 Resolution 75/22-CEPE", result.stderr)

    def test_rejects_bad_component_hash(self) -> None:
        with self.copied_root() as directory:
            root = Path(directory)
            self.mutate_csv(root / "curriculos/2023/inventario/componentes.csv", lambda row: row["code"] == "CI1215", lambda row: row.__setitem__("ficha1_sha256", "0" * 64))
            result = self.validate(root)
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("component Ficha 1 claim differs from manifest: CI1215", result.stderr)

    def test_rejects_bad_ementa_hash(self) -> None:
        with self.copied_root() as directory:
            root = Path(directory)
            self.mutate_csv(root / "curriculos/2023/inventario/ementas.csv", lambda row: row["code"] == "CI1215" and row["document_kind"] == "Ficha 1", lambda row: row.__setitem__("sha256", "0" * 64))
            result = self.validate(root)
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("ementa Ficha claim differs from manifest: CI1215 Ficha 1", result.stderr)


if __name__ == "__main__":
    unittest.main(verbosity=2)
