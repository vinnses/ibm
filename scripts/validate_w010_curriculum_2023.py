#!/usr/bin/env python3
"""Validate W010 2023 curriculum-inventory invariants and local manifests."""

from __future__ import annotations

import csv
import hashlib
import os
import re
import sys
from pathlib import Path


ROOT = Path(os.environ.get("W010_VALIDATOR_ROOT", Path(__file__).resolve().parents[1])).resolve()
BASE = ROOT / "curriculos/2023"
INVENTORY = BASE / "inventario"


# Resolution 75/22-CEPE, Annex I. Titles retain the inventory's established
# Title Case transcription normalization; spelling, diacritics, punctuation,
# and the Annex I total-hours field are source-derived.
EXPECTED_ELECTIVES = {
    ('BC012', 'TECNICAS HISTOLOGICAS', 60), ('BC043', 'BIOLOGIA CELULAR AVANÇADA', 90),
    ('BC061', 'PROCESSOS CELULARES', 60), ('BG020', 'GENETICA MEDICA', 40),
    ('BG030', 'IMUNOGENETICA BASICA', 60), ('BG048', 'GENÉTICA DE POPULAÇÕES HUMANAS', 60),
    ('BG049', 'TEMAS ATUAIS EM GENÉTICA', 30), ('BG055', 'CITOGENÉTICA HUMANA', 45),
    ('BG066', 'EPIGENÉTICA', 45), ('CI1008', 'INTRODUÇÃO A SISTEMAS EMBARCADOS', 60),
    ('CI1009', 'COMPUTAÇÃO PARALELA COM GPUS', 60), ('CI1010', 'PROGRAMAÇÃO WEB', 60),
    ('CI1011', 'RECONHECIMENTO DE PADRÕES', 60), ('CI1013', 'GRANDES IDEIAS DA COMPUTAÇÃO TEÓRICA', 60),
    ('CI1014', 'REDES SOCIAIS E ECONÔMICAS', 60), ('CI1015', 'TESTE DE SOFTWARE', 60),
    ('CI1016', 'TÉCNICAS EM MODELAGEM DE APLICAÇÕES', 60), ('CI1017', 'CRIPTOGRAFIA', 60),
    ('CI1018', 'TÓPICOS EM INTELIGÊNCIA ARTIFICIAL', 60), ('CI1019', 'TÓPICOS EM INTELIGÊNCIA COMPUTACIONAL', 60),
    ('CI1020', 'ROBÓTICA MÓVEL', 60), ('CI1021', 'PROGRAMAÇÃO DE DISPOSITIVOS MÓVEIS', 60),
    ('CI1022', 'PROJETO DE SISTEMAS DIGITAIS', 60), ('CI1023', 'PROJETO DE SISTEMAS EMBARCADOS', 60),
    ('CI1024', 'TÓPICOS EM ARQUITETURA DE COMPUTADORES', 60), ('CI1025', 'DISPOSITIVOS REPROGRAMÁVEIS', 60),
    ('CI1026', 'VISÃO COMPUTACIONAL E PERCEPÇÃO', 60), ('CI1027', 'INTRODUÇÃO À PESQUISA EM CIÊNCIA DA COMPUTAÇÃO', 60),
    ('CI1028', 'BIOMETRIA E VIGILÂNCIA POR VISÃO COMPUTACIONAL', 60), ('CI1029', 'TÓPICOS EM SEGURANÇA COMPUTACIONAL', 60),
    ('CI1030', 'CIÊNCIA DE DADOS PARA SEGURANÇA', 60), ('CI1031', 'DESAFIOS DE PROGRAMAÇÃO', 60),
    ('CI1032', 'TÓPICOS EM COMPLEXIDADE COMPUTACIONAL', 60), ('CI1033', 'COMPUTAÇÃO QUÂNTICA', 60),
    ('CI1034', 'TÓPICOS EM OTIMIZAÇÃO', 60), ('CI1035', 'TÓPICOS EM COMPUTAÇÃO CIENTÍFICA', 60),
    ('CI1036', 'TÓPICOS EM PROGRAMAÇÃO PARALELA', 60), ('CI1037', 'TÓPICOS EM SISTEMAS OPERACIONAIS', 60),
    ('CI1038', 'TÓPICOS EM PROGRAMAÇÃO DE COMPUTADORES', 60), ('CI1040', 'FUNDAMENTOS DA EXTENSÃO UNIVERSITÁRIA', 30),
    ('CI1059', 'INTRODUÇÃO À TEORIA DA COMPUTAÇÃO', 60), ('CI1084', 'TÓPICOS EM TEORIA DOS GRAFOS', 60),
    ('CI1086', 'ARQUITETURAS DE ALTO DESEMPENHO', 60), ('CI1087', 'TÓPICOS EM BANCO DE DADOS', 60),
    ('CI1088', 'SISTEMAS DISTRIBUÍDOS', 60), ('CI1090', 'TÓPICOS EM ENGENHARIA DE SOFTWARE', 60),
    ('CI1091', 'AVALIAÇÃO DE DESEMPENHO', 60), ('CI1170', 'TÓPICOS EM COMPUTAÇÃO BIOINSPIRADA', 60),
    ('CI1173', 'COMPUTAÇÃO GRÁFICA', 60), ('CI1174', 'TÓPICOS EM APRENDIZADO DE MÁQUINA', 60),
    ('CI1175', 'OFICINA DE COMPUTAÇÃO DE IMAGENS', 60), ('CI1176', 'TÓPICOS EM VISÃO COMPUTACIONAL', 60),
    ('CI1177', 'TÓPICOS EM COMPUTAÇÃO GRÁFICA', 60), ('CI1178', 'TEORIA DO APRENDIZADO DE MÁQUINA', 60),
    ('CI1204', 'INOVAÇÃO TECNOLÓGICA E GESTÃO DE PROJETOS', 60), ('CI1211', 'CONSTRUÇÃO DE COMPILADORES', 60),
    ('CI1219', 'SISTEMAS AVANÇADOS DE BANCO DE DADOS', 60), ('CI1220', 'TEORIA DE SISTEMAS', 60),
    ('CI1311', 'FUNDAMENTOS LÓGICOS DA INTELIGÊNCIA ARTIFICIAL', 60), ('CI1315', 'PROJETO DE SISTEMAS OPERACIONAIS', 60),
    ('CI1338', 'GEOMETRIA COMPUTACIONAL', 60), ('CI1339', 'COMPLEXIDADE COMPUTACIONAL', 60),
    ('CI1351', 'TÓPICOS EM INTERAÇÃO HUMANO-COMPUTADOR', 60), ('CI1352', 'DESIGN DE SISTEMAS SOCIOTÉCNICOS', 60),
    ('CI1353', 'PRÁTICA EM DESENVOLVIMENTO DE SOFTWARE', 60), ('CI1355', 'TÓPICOS EM ALGORITMOS', 60),
    ('CI1360', 'REDES MÓVEIS', 60), ('CI1365', 'TÓPICOS EM REDES DE COMPUTADORES', 60),
    ('CI1366', 'GERENCIAMENTO DE REDES DE COMPUTADORES', 60), ('CI1367', 'TÓPICOS EM SIMULAÇÃO DE SISTEMAS COMPUTACIONAIS', 60),
    ('CI1394', 'PROCESSAMENTO DE IMAGENS', 60), ('CI1397', 'SISTEMAS TUTORES INTELIGENTES', 60),
    ('CM314', 'CÁLCULO 4', 60), ('CMI071', 'MÉTODOS DE MATEMÁTICA APLICADA', 60),
    ('CMI103', 'MÉTODOS COMPUTACIONAIS DE OTIMIZAÇÃO', 60), ('CMI104', 'APRENDIZAGEM DE MÁQUINA', 60),
    ('CMM031', 'ÁLGEBRA LINEAR I', 60), ('CMM041', 'TEORIA DE NÚMEROS', 60),
    ('CMM051', 'ANEIS E CORPOS', 60), ('CMM201', 'TEORIA DE GRUPOS', 60),
    ('CMM202', 'ANÁLISE I', 60), ('CMM211', 'ÁLGEBRA LINEAR II', 60),
    ('CMM212', 'ANÁLISE II', 60), ('CMM213', 'TOPOLOGIA DE SUPERFÍCIES', 60),
    ('CMM222', 'ANÁLISE III', 60), ('CMM242', 'ESPAÇOS MÉTRICOS', 60),
    ('LIB038', 'COMUNICAÇÃO EM LÍNGUA BRASILEIRA DE SINAIS-LIBRAS: FUNDAMENTOS DA EDUCAÇÃO BILÍNGUE PARA SURDOS', 60),
    ('MN150', 'EPIDEMIOLOGIA CRÍTICA', 30), ('MN152', 'GESTÃO DA QUALIDADE EM SAÚDE', 30),
    ('MN155', 'SAÚDE DO TRABALHO', 30), ('MN156', 'GÊNERO E SAÚDE COLETIVA', 30),
    ('MN159', 'PRIMEIROS SOCORROS', 15),
}
ELECTIVE_METADATA = {
    'formal_source': 'Resolução 75/22-CEPE Anexo I',
    'status': 'comprovada',
    'notes': 'catálogo formal; não indica oferta',
}


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as stream:
        for block in iter(lambda: stream.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


def read_csv(path: Path, errors: list[str]) -> list[dict[str, str]]:
    with path.open(encoding="utf-8", newline="") as stream:
        raw_rows = list(csv.reader(stream))
    if not raw_rows or len({len(row) for row in raw_rows}) != 1:
        errors.append(f"invalid CSV width: {path.relative_to(ROOT)}")
        return []
    with path.open(encoding="utf-8", newline="") as stream:
        return list(csv.DictReader(stream))


def check_hash_records(
    rows: list[dict[str, str]], path_field: str, hash_field: str, status_field: str,
    accepted: set[str], errors: list[str], label: str,
) -> int:
    checked = 0
    for row in rows:
        if row[status_field] not in accepted:
            continue
        path = ROOT / row[path_field]
        expected = row[hash_field].lower()
        if not path.is_file():
            errors.append(f"{label}: missing {row[path_field]}")
        elif len(expected) != 64 or sha256(path) != expected:
            errors.append(f"{label}: hash mismatch {row[path_field]}")
        else:
            checked += 1
    return checked


def check_derived_ficha_claims(
    components: list[dict[str, str]], ementas: list[dict[str, str]],
    manifests: list[dict[str, str]], errors: list[str],
) -> None:
    manifest_records = {
        (row['code'], row.get('kind', row.get('kind_in_index', '')), row['local_path'], row['sha256'])
        for row in manifests if row['status'] == 'downloaded'
    }
    for row in components:
        if not row['ficha1_path'] and not row['ficha1_sha256']:
            continue
        claim = (row['code'], 'ficha-1', row['ficha1_path'], row['ficha1_sha256'])
        if claim not in manifest_records:
            errors.append(f"component Ficha 1 claim differs from manifest: {row['code']}")
    for row in ementas:
        kind = row['document_kind'].lower().replace(' ', '-')
        claim = (row['code'], kind, row['document_path'], row['sha256'])
        if claim not in manifest_records:
            errors.append(
                f"ementa Ficha claim differs from manifest: {row['code']} {row['document_kind']} {row['document_path']}"
            )


def main() -> int:
    errors: list[str] = []
    components = read_csv(INVENTORY / "componentes.csv", errors)
    electives = read_csv(INVENTORY / "optativas.csv", errors)
    ementas = read_csv(INVENTORY / "ementas.csv", errors)
    dependencies = read_csv(INVENTORY / "dependencias.csv", errors)
    regulations = read_csv(INVENTORY / "regulamentos.csv", errors)
    searches = read_csv(INVENTORY / "buscas-negativas.csv", errors)
    sources = read_csv(BASE / "fontes/manifesto.csv", errors)
    dinf = read_csv(BASE / "fichas/manifesto-dinf.csv", errors)
    external = read_csv(BASE / "fichas/manifesto-outros-departamentos.csv", errors)

    actual_electives = {
        (row['code'], row['title'], int(row['total_hours']))
        for row in electives if row['total_hours'].isdigit()
    }
    if actual_electives != EXPECTED_ELECTIVES or len(electives) != 92:
        errors.append("electives must contain exactly the 92 Resolution 75/22-CEPE Annex I code/title/hours rows")
    for row in electives:
        for field, expected in ELECTIVE_METADATA.items():
            if row[field] != expected:
                errors.append(f"elective {field} differs from formal catalog record: {row['code']}")
    check_derived_ficha_claims(components, ementas, dinf + external, errors)

    codes = {row["code"] for row in components}
    if len(components) != 43 or len(codes) != 43:
        errors.append("components must contain exactly 43 unique targets")
    if sum(row["nature"] == "TCC alternativa" for row in components) != 4:
        errors.append("components must contain exactly four TCC alternatives")
    if sum(row["nature"] != "TCC alternativa" for row in components) != 39:
        errors.append("components must contain exactly 39 non-TCC targets")
    for row in components:
        if not row["evidence_status"] or not row["applicability_2023"]:
            errors.append(f"component lacks status/applicability: {row['code']}")

    ci1055 = next((row for row in components if row["code"] == "CI1055"), None)
    if not ci1055 or ci1055["title"] != "Algoritmos e Estruturas de Dados 1":
        errors.append("CI1055 title does not match the preserved Ficha 1 transcription")
    bq083 = next((row for row in components if row["code"] == "BQ083"), None)
    if not bq083 or bq083["applicability_2023"] != "indeterminado":
        errors.append("BQ083 applicability must remain indeterminate without an applicability act")
    bq083_ficha = next((row for row in ementas if row["code"] == "BQ083" and row["document_kind"] == "Ficha 1"), None)
    if not bq083_ficha or "2022" not in bq083_ficha["document_version_or_term"] or bq083_ficha["applicability_2023"] != "indeterminado":
        errors.append("BQ083 Ficha 1 date/applicability is not source-supported")
    for row in ementas:
        if not row["applicability_2023"]:
            errors.append(f"Ficha record lacks applicability: {row['code']} {row['document_kind']}")

    graph: dict[str, set[str]] = {code: set() for code in codes}
    for row in dependencies:
        if row["dependent_code"] not in codes or row["prerequisite_code"] not in codes:
            errors.append(f"dependency endpoint absent from inventory: {row}")
        else:
            graph[row["dependent_code"]].add(row["prerequisite_code"])
    visiting: set[str] = set()
    visited: set[str] = set()
    def visit(node: str) -> None:
        if node in visiting:
            errors.append(f"dependency cycle includes {node}")
            return
        if node in visited:
            return
        visiting.add(node)
        for next_node in graph[node]:
            visit(next_node)
        visiting.remove(node)
        visited.add(node)
    for code in graph:
        visit(code)

    required_regulations = {"Atividades Formativas", "Estágio obrigatório e não obrigatório", "Trabalho de Conclusão de Curso", "Atividades Curriculares de Extensão"}
    if not required_regulations <= {row["subject"] for row in regulations}:
        errors.append("required regulation coverage is incomplete")
    if not searches or any(not row["accessed_at"] or not row["official_domains"] or not row["limits"] for row in searches):
        errors.append("negative-search records lack required scope fields")

    source_count = check_hash_records(sources, "local_path", "sha256", "status", {"preservado"}, errors, "source manifest")
    ficha_count = check_hash_records(dinf, "local_path", "sha256", "status", {"downloaded"}, errors, "DInf Ficha manifest")
    ficha_count += check_hash_records(external, "local_path", "sha256", "status", {"downloaded"}, errors, "external Ficha manifest")
    portal = next((row for row in sources if row["id"] == "2023-EMENTARIO"), None)
    if not portal or portal["local_path"] != "curriculos/2023/fontes/pagina-ementario-curriculo-96a-2026-09-04.html":
        errors.append("Ementário manifest does not identify the preserved curriculum response")
    elif "3000" not in (ROOT / portal["local_path"]).read_text(encoding="utf-8"):
        errors.append("Ementário curriculum capture does not contain the recorded 3000-hour value")

    readme = (BASE / "fontes/README.md").read_text(encoding="utf-8")
    for row in sources:
        source_path = Path(row["local_path"])
        if source_path.parent != Path("curriculos/2023/fontes") or source_path.suffix.lower() != ".pdf":
            continue
        pattern = re.compile(
            rf"^\| `{re.escape(source_path.name)}` \|.*\| `([0-9a-f]{{64}})` \|$",
            re.MULTILINE,
        )
        match = pattern.search(readme)
        if not match:
            errors.append(f"source README lacks hash row for {source_path.name}")
        elif match.group(1) != row["sha256"]:
            errors.append(f"source README hash differs from manifest for {source_path.name}")

    for error in errors:
        print(f"ERROR: {error}", file=sys.stderr)
    print(f"Checked {len(components)} targets, {len(dependencies)} dependencies, {source_count} source hashes, {ficha_count} Ficha hashes, and {len(searches)} negative searches; errors={len(errors)}.")
    return 1 if errors else 0


if __name__ == "__main__":
    raise SystemExit(main())
