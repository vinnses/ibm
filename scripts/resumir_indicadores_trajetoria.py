#!/usr/bin/env python3
"""Valida e resume a trajetória INEP de Informática Biomédica da UFPR.

O insumo é o CSV produzido por ``extrair_indicadores_trajetoria.py``. O
programa preserva a unidade da publicação do INEP (coorte x ano de referência)
e não confunde taxas acumuladas com fluxos anuais.
"""

from __future__ import annotations

import argparse
import csv
from collections import defaultdict
from pathlib import Path


COHORTES = range(2011, 2021)
TOLERANCIA_PERCENTUAL = 0.0002


def inteiro(valor: str) -> int:
    return int(float(valor))


def numero(valor: str) -> float:
    return float(valor)


def percentual(numerador: int, denominador: int) -> float:
    return 100 * numerador / denominador if denominador else 0.0


def escrever_csv(caminho: Path, campos: list[str], linhas: list[dict[str, object]]) -> None:
    with caminho.open("w", encoding="utf-8", newline="") as arquivo:
        escritor = csv.DictWriter(arquivo, fieldnames=campos)
        escritor.writeheader()
        escritor.writerows(linhas)


def validar(registros: list[dict[str, str]]) -> list[str]:
    erros: list[str] = []
    por_coorte: dict[int, list[dict[str, str]]] = defaultdict(list)
    for registro in registros:
        coorte = inteiro(registro["NU_ANO_INGRESSO"])
        referencia = inteiro(registro["NU_ANO_REFERENCIA"])
        por_coorte[coorte].append(registro)
        if inteiro(registro["CO_IES"]) != 571 or inteiro(registro["CO_CURSO"]) != 1126727:
            erros.append(f"identificador inesperado: coorte {coorte}, referência {referencia}")

    for coorte in COHORTES:
        linhas = sorted(por_coorte.get(coorte, []), key=lambda item: inteiro(item["NU_ANO_REFERENCIA"]))
        if not linhas:
            erros.append(f"coorte {coorte} ausente")
            continue
        anos = [inteiro(linha["NU_ANO_REFERENCIA"]) for linha in linhas]
        if anos != list(range(coorte, max(anos) + 1)):
            erros.append(f"anos não contíguos na coorte {coorte}: {anos}")
        ingressantes = inteiro(linhas[0]["QT_INGRESSANTE"])
        acumulado_concluintes = acumulado_desistencias = acumulado_falecidos = 0
        for linha in linhas:
            ano = inteiro(linha["NU_ANO_REFERENCIA"])
            acumulado_concluintes += inteiro(linha["QT_CONCLUINTE"])
            acumulado_desistencias += inteiro(linha["QT_DESISTENCIA"])
            acumulado_falecidos += inteiro(linha["QT_FALECIDO"])
            permanencia = inteiro(linha["QT_PERMANENCIA"])
            if permanencia + acumulado_concluintes + acumulado_desistencias + acumulado_falecidos != ingressantes:
                erros.append(f"balanço de estudantes falhou: coorte {coorte}, referência {ano}")
            esperados = {
                "TAP": percentual(permanencia, ingressantes),
                "TCA": percentual(acumulado_concluintes, ingressantes),
                "TDA": percentual(acumulado_desistencias, ingressantes),
                "TCAN": percentual(inteiro(linha["QT_CONCLUINTE"]), ingressantes),
                "TADA": percentual(inteiro(linha["QT_DESISTENCIA"]), ingressantes),
            }
            for campo, esperado in esperados.items():
                if abs(numero(linha[campo]) - esperado) > TOLERANCIA_PERCENTUAL:
                    erros.append(f"{campo} divergente: coorte {coorte}, referência {ano}")
    extras = sorted(set(por_coorte) - set(COHORTES))
    if extras:
        erros.append(f"coortes fora do escopo: {extras}")
    return erros


def resumo_coortes(registros: list[dict[str, str]]) -> list[dict[str, object]]:
    por_coorte: dict[int, list[dict[str, str]]] = defaultdict(list)
    for registro in registros:
        por_coorte[inteiro(registro["NU_ANO_INGRESSO"])].append(registro)
    saida: list[dict[str, object]] = []
    for coorte in COHORTES:
        linhas = sorted(por_coorte[coorte], key=lambda item: inteiro(item["NU_ANO_REFERENCIA"]))
        esperado = inteiro(linhas[0]["NU_ANO_INTEGRALIZACAO"])
        no_esperado = next((linha for linha in linhas if inteiro(linha["NU_ANO_REFERENCIA"]) == esperado), None)
        ultima = linhas[-1]
        linha_saida: dict[str, object] = {
            "coorte_ingresso": coorte,
            "ingressantes": inteiro(linhas[0]["QT_INGRESSANTE"]),
            "prazo_integralizacao_anos": inteiro(linhas[0]["NU_PRAZO_INTEGRALIZACAO"]),
            "ano_esperado_integralizacao": esperado,
            "observacao_ano_esperado_disponivel": "sim" if no_esperado else "não",
            "ultima_observacao_ano": inteiro(ultima["NU_ANO_REFERENCIA"]),
        }
        for rotulo, linha in (("ano_esperado", no_esperado), ("ultima_observacao", ultima)):
            for origem, destino in (
                ("QT_PERMANENCIA", "permanencia"), ("QT_CONCLUINTE", "concluintes_ano"),
                ("QT_DESISTENCIA", "desistencias_ano"), ("TAP", "tap"),
                ("TCA", "tca_acumulada"), ("TDA", "tda_acumulada"),
                ("TCAN", "tcan_anual"), ("TADA", "tada_anual"),
            ):
                linha_saida[f"{rotulo}_{destino}"] = "" if linha is None else linha[origem]
        saida.append(linha_saida)
    return saida


def serie_anual(registros: list[dict[str, str]]) -> list[dict[str, object]]:
    por_ano: dict[int, list[dict[str, str]]] = defaultdict(list)
    for registro in registros:
        por_ano[inteiro(registro["NU_ANO_REFERENCIA"])].append(registro)
    saida: list[dict[str, object]] = []
    for ano in COHORTES:
        linhas = por_ano[ano]
        entradas = [linha for linha in linhas if inteiro(linha["NU_ANO_INGRESSO"]) == ano]
        saida.append({
            "ano_referencia": ano,
            "coortes_observadas": ";".join(str(inteiro(linha["NU_ANO_INGRESSO"])) for linha in sorted(linhas, key=lambda x: inteiro(x["NU_ANO_INGRESSO"]))),
            "ingressantes_novas_coortes": sum(inteiro(linha["QT_INGRESSANTE"]) for linha in entradas),
            "permanencia_ativa_nas_coortes": sum(inteiro(linha["QT_PERMANENCIA"]) for linha in linhas),
            "concluintes_anuais_nas_coortes": sum(inteiro(linha["QT_CONCLUINTE"]) for linha in linhas),
            "desistencias_anuais_nas_coortes": sum(inteiro(linha["QT_DESISTENCIA"]) for linha in linhas),
            "falecidos_anuais_nas_coortes": sum(inteiro(linha["QT_FALECIDO"]) for linha in linhas),
        })
    return saida


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--entrada", type=Path, required=True)
    parser.add_argument("--diretorio-saida", type=Path, required=True)
    args = parser.parse_args()
    with args.entrada.open(encoding="utf-8", newline="") as arquivo:
        registros = list(csv.DictReader(arquivo))
    erros = validar(registros)
    if erros:
        raise SystemExit("Validação falhou:\n- " + "\n- ".join(erros))
    args.diretorio_saida.mkdir(parents=True, exist_ok=True)
    coortes = resumo_coortes(registros)
    serie = serie_anual(registros)
    escrever_csv(args.diretorio_saida / "trajetoria_informatica_biomedica_ufpr_resumo_coortes_2011_2020.csv", list(coortes[0]), coortes)
    escrever_csv(args.diretorio_saida / "trajetoria_informatica_biomedica_ufpr_serie_anual_2011_2020.csv", list(serie[0]), serie)
    print(f"Validação aprovada: {len(registros)} observações, 10 coortes e 85 balanços/indicadores verificados.")


if __name__ == "__main__":
    main()
