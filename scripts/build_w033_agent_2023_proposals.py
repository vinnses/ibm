#!/usr/bin/env python3
"""Generate the bounded W033 2023 source-level proposal dataset.

This is intentionally an intermediate source dataset, not the shared W033
builder.  It consumes only normalized, preserved Ficha CSVs and preserves the
document distinction and stated applicability of every row.
"""
import csv
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
INPUTS = [
    ROOT / "dados/curriculos/2023/fichas-1-lotes/D01/ementas.csv",
    ROOT / "dados/curriculos/2023/fichas-1-lotes/D01-batch2/ementas.csv",
    ROOT / "dados/curriculos/2023/fichas-preservadas/fichas-1-restantes.csv",
    ROOT / "dados/curriculos/2023/fichas-preservadas/fichas-2.csv",
]
OUT = ROOT / "site/data/source/w033/agent-2023-proposals.json"

# Labels are analytical proposals.  Quoted support is selected from each
# document's ementa, retaining Ficha 1/Ficha 2 as independent source records.
T = {
"CI1001": [("ferramentas de programação", "Programação e Desenvolvimento de Software", "Uso dirigido de ferramentas para programação."), ("estruturas de dados básicas", "Algoritmos e Estruturas de Dados", "Estudo de estruturas de dados básicas."), ("práticas de programação", "Programação e Desenvolvimento de Software", "Práticas de programação.")],
"CI1002": [("técnicas avançadas de desenvolvimento de software", "Programação e Desenvolvimento de Software", "Uso de técnicas avançadas para desenvolvimento de software."), ("projetos de programação de média e alta complexidade", "Programação e Desenvolvimento de Software", "Práticas de projetos de desenvolvimento de programas de média e alta complexidade.")],
"CI1003": [("história da computação", "Fundamentos da Computação", "História da Computação;"), ("impactos sociais da computação", "Computação, Sociedade e Ética", "Impactos da Computação na Ciência, Tecnologia e Sociedade;"), ("pensamento computacional", "Fundamentos da Computação", "Pensamento Computacional;"), ("ética em computação", "Computação, Sociedade e Ética", "Computação, Ética e Sociedade;")],
"CI1055": [("modelo de Von Neumann", "Fundamentos da Computação", "do modelo Von Neumann"), ("programação estruturada", "Programação e Desenvolvimento de Software", "programação estruturada"), ("estruturas de dados elementares", "Algoritmos e Estruturas de Dados", "estruturas de dados elementares"), ("tipos abstratos de dados simples", "Algoritmos e Estruturas de Dados", "Tipos abstratos de dados simples."), ("custo de programas", "Análise de Algoritmos", "Noções básicas de custo"), ("teste de programas", "Qualidade e Engenharia de Software", "teste de programas.")],
"CI1215": [("arquitetura básica de sistemas operacionais", "Sistemas Operacionais", "Estrutura básica de um sistema operacional"), ("comunicação e sincronização entre processos", "Sistemas Operacionais", "Mecanismos de comunicação e sincronização entre processos."), ("gerenciamento de processos", "Sistemas Operacionais", "gerenciamento de processos"), ("gerenciamento de memória", "Sistemas Operacionais", "memória"), ("sistemas de arquivos", "Sistemas Operacionais", "sistemas de arquivos"), ("entrada e saída", "Sistemas Operacionais", "entrada e saída.")],
"CI1005": [("qualidade de software", "Qualidade e Engenharia de Software", "Qualidade de software."), ("métricas de qualidade", "Qualidade e Engenharia de Software", "Métricas de qualidade."), ("gerenciamento de configuração", "Qualidade e Engenharia de Software", "Gerenciamento de Conﬁguração."), ("verificação e validação de software", "Qualidade e Engenharia de Software", "Veriﬁcação e Validação."), ("teste de software", "Qualidade e Engenharia de Software", "Teste de software."), ("qualidade de processo de software", "Qualidade e Engenharia de Software", "Qualidade de processo.")],
"CI1007": [("fundamentos de segurança computacional", "Segurança Computacional", "Conceitos básicos."), ("criptografia", "Segurança Computacional", "Introdução à criptograﬁa."), ("autenticação e controle de acesso", "Segurança Computacional", "Autenticação e controle de acesso."), ("segurança de sistemas e aplicações", "Segurança Computacional", "Segurança de sistemas e aplicações."), ("segurança de redes e internet", "Segurança Computacional", "Segurança em redes e na Internet."), ("auditoria e gestão de segurança", "Segurança Computacional", "Auditoria. Gestão da segurança.")],
"CI1056": [("recursão", "Algoritmos e Estruturas de Dados", "Recursão"), ("algoritmos de busca", "Algoritmos e Estruturas de Dados", "Busca"), ("algoritmos de ordenação", "Algoritmos e Estruturas de Dados", "Ordenação"), ("heaps", "Algoritmos e Estruturas de Dados", "Heaps"), ("contagem de recursos computacionais", "Análise de Algoritmos", "Contagem de recursos computacionais")],
"CI1057": [("acesso sequencial e indexado", "Algoritmos e Estruturas de Dados", "Acesso seqüêncial, indexado."), ("tipo abstrato de dados dicionário", "Algoritmos e Estruturas de Dados", "Tipo abstrato de dados dicionário."), ("ordenação externa", "Algoritmos e Estruturas de Dados", "Ordenação externa."), ("algoritmos gulosos", "Algoritmos e Estruturas de Dados", "Algoritmos gulosos.")],
"CI1062": [("paradigmas de programação", "Programação e Desenvolvimento de Software", "diferentes paradigmas de programação estruturados e não estruturados.")],
"CI1068": [("sistemas de numeração", "Arquitetura e Hardware", "Sistemas de numeração."), ("aritmética binária", "Arquitetura e Hardware", "Aritmética binária."), ("funções booleanas", "Arquitetura e Hardware", "Minimização e decomposição de funções booleanas."), ("circuitos combinacionais", "Arquitetura e Hardware", "Circuitos combinacionais"), ("circuitos sequenciais", "Arquitetura e Hardware", "Circuitos sequenciais."), ("máquinas de estados", "Arquitetura e Hardware", "Máquinas de estados.")],
"CI1162": [("requisitos funcionais e não funcionais", "Qualidade e Engenharia de Software", "Requisitos Funcionais e Não- Funcionais;"), ("processos de software", "Qualidade e Engenharia de Software", "Modelos de processos de software;"), ("análise de domínio", "Qualidade e Engenharia de Software", "Análise de domínio: do problema e da solução;"), ("elicitação e validação de requisitos", "Qualidade e Engenharia de Software", "elicitação, análise, especiﬁcação e validação de requisitos;"), ("documento de requisitos", "Qualidade e Engenharia de Software", "Documento de requisitos;"), ("modelagem de casos de uso", "Qualidade e Engenharia de Software", "Diagrama de Casos de Uso, Modelo Conceitual.")],
"CI1163": [("design de arquitetura de software", "Qualidade e Engenharia de Software", "Design da arquitetura de software."), ("design detalhado de software", "Qualidade e Engenharia de Software", "Design detalhado."), ("modelos de design de software", "Qualidade e Engenharia de Software", "Modelos de design de software."), ("padrões de design", "Qualidade e Engenharia de Software", "Padrões de design."), ("revisões e inspeções de design", "Qualidade e Engenharia de Software", "Revisões e inspeções."), ("correspondência entre design e codificação", "Qualidade e Engenharia de Software", "Correspondência entre design e codiﬁcação.")],
"CI1171": [("aprendizagem supervisionada", "Inteligência Artificial e Aprendizado de Máquina", "Aprendizagem supervisionada."), ("avaliação de classificadores", "Inteligência Artificial e Aprendizado de Máquina", "Avaliação de classiﬁcadores."), ("aprendizagem não supervisionada", "Inteligência Artificial e Aprendizado de Máquina", "Aprendizagem não supervisionada."), ("regressão em aprendizado de máquina", "Inteligência Artificial e Aprendizado de Máquina", "Regressão."), ("algoritmos genéticos", "Inteligência Artificial e Aprendizado de Máquina", "Algoritmos Genéticos"), ("otimização por enxame de partículas", "Inteligência Artificial e Aprendizado de Máquina", "PSO.")],
"CI1209": [("inteligência artificial simbólica", "Inteligência Artificial e Aprendizado de Máquina", "Inteligência Artiﬁcial simbólica e aplicações.")],
"CI1212": [("aritmética de inteiros e ponto flutuante", "Arquitetura e Hardware", "Aritmética de inteiros e ponto ﬂutuante"), ("avaliação de desempenho de computadores", "Arquitetura e Hardware", "avaliação de desempenho"), ("processador pipeline", "Arquitetura e Hardware", "processador pipeline"), ("sistemas de memória", "Arquitetura e Hardware", "sistemas de memória"), ("memória cache", "Arquitetura e Hardware", "memória cache"), ("memória virtual", "Arquitetura e Hardware", "memória virtual"), ("arquiteturas de alto desempenho", "Arquitetura e Hardware", "arquiteturas de alto desempenho.")],
"CI1218": [("sistemas gerenciadores de bancos de dados", "Banco de Dados", "sistema gerenciadores de bancos de dados (SGBD)"), ("modelos de dados", "Banco de Dados", "Modelos de dados"), ("linguagens de consulta", "Banco de Dados", "linguagens de consultas"), ("processamento e otimização de consultas", "Banco de Dados", "Processamento de consultas e otimização"), ("projeto de bancos de dados", "Banco de Dados", "Projeto de bancos de dados"), ("transações de banco de dados", "Banco de Dados", "Conceitos de transações"), ("controle de concorrência e recuperação", "Banco de Dados", "Controle de concorrência e recuperação.")],
"CI1221": [("processos de software", "Qualidade e Engenharia de Software", "Processos e modelos de processos de software."), ("gestão de projetos de software", "Qualidade e Engenharia de Software", "Gestão de projeto de software."), ("reuso de software", "Qualidade e Engenharia de Software", "Técnicas de Reuso."), ("manutenção e evolução de software", "Qualidade e Engenharia de Software", "Manutenção e evolução.")],
"CI1316": [("paralelismo", "Sistemas Distribuídos e Paralelos", "Introdução ao paralelismo."), ("análise de algoritmos paralelos", "Sistemas Distribuídos e Paralelos", "Análise de algoritmos paralelos."), ("avaliação de desempenho paralelo", "Sistemas Distribuídos e Paralelos", "Avaliação de desempenho."), ("programação multithreading e multiprocessos", "Sistemas Distribuídos e Paralelos", "Programação multithreading e multi-processos.")],
"CI1350": [("fundamentos de interação humano-computador", "Interação Humano-Computador", "Conceitos básicos em IHC;"), ("qualidade em interação humano-computador", "Interação Humano-Computador", "Qualidade em IHC;"), ("design participativo", "Interação Humano-Computador", "Design Participativo"), ("design universal", "Interação Humano-Computador", "Design Universal;"), ("modelagem e prototipação em IHC", "Interação Humano-Computador", "Especiﬁcação, Modelagem e Prototipação em IHC;"), ("avaliação em IHC", "Interação Humano-Computador", "Avaliação em IHC.")],
"BF114": [("homeostasia e fisiologia celular", "Biociências e Saúde", "atividade funcional da célula e dos diferentes sistemas que participam da homeostasia do meio interno."), ("transporte através de membranas", "Biociências e Saúde", "bases fisiológicas do transporte através de membranas."), ("fisiologia dos sistemas corporais", "Biociências e Saúde", "Fisiologia dos sistemas: Locomotor, cardiovascular, renal, respiratório e digestivo."), ("fisiologia endócrina", "Biociências e Saúde", "Fisiologia das Glândulas Endócrinas"), ("neurofisiologia", "Biociências e Saúde", "Neurofisiologia:"), ("simulações computacionais em fisiologia", "Informática Biomédica", "Fundamentos fisiológicos para elaboração de simulações de computador.")],
"BQ083": [("estrutura de ácidos nucléicos", "Biociências e Saúde", "Estrutura ácidos nucléicos;"), ("replicação, transcrição e tradução", "Biociências e Saúde", "replicação, transcrição, tradução, regulação da expressão gênica;"), ("manipulação gênica", "Biociências e Saúde", "princípios de manipulação gênica;"), ("bancos de dados biológicos", "Bioinformática", "Banco de dados biológicos;"), ("alinhamento de sequências e busca de genes", "Bioinformática", "algoritmos de alinhamento de sequências e busca de genes;"), ("análise filogenética", "Bioinformática", "análise filogenética;"), ("análises genômica, transcriptômica e proteômica", "Bioinformática", "análise Genômica, Transcriptômica e Proteômica;"), ("biologia de sistemas", "Bioinformática", "Biologia de Sistemas")],
"MN162": [("processo saúde-doença", "Saúde Coletiva e Sistema de Saúde", "Historicidade do processo saúde-doença"), ("indicadores ambientais e saúde", "Saúde Coletiva e Sistema de Saúde", "Indicadores ambientais e saúde."), ("políticas de saúde", "Saúde Coletiva e Sistema de Saúde", "Políticas de saúde."), ("organização do sistema de saúde brasileiro", "Saúde Coletiva e Sistema de Saúde", "organização do sistema de saúde brasileiro."), ("níveis de atenção à saúde", "Saúde Coletiva e Sistema de Saúde", "Níveis de atenção à saúde."), ("planejamento e avaliação em saúde", "Saúde Coletiva e Sistema de Saúde", "planejamento e avaliação em saúde.")],
"MN129": [("métodos e técnicas de pesquisa em saúde", "Metodologia Científica e Bioética", "A pesquisa em saúde, métodos e técnicas de pesquisa."), ("ética e bioética em pesquisa em saúde", "Metodologia Científica e Bioética", "A Ética e bioética na pesquisa em saúde.")],
}

# Ficha 2 retains its own transcription; these punctuation/spelling variants
# must not silently be represented as if they were the Ficha 1 wording.
EXCERPT_OVERRIDES = {
    ("CI1171-ficha-2", "otimização por enxame de partículas"): "PSO",
    ("CI1221-ficha-2", "manutenção e evolução de software"): "Manutenção e evolução",
    ("CI1316-ficha-2", "programação multithreading e multiprocessos"): "Programação multi-threading e multi-processos.",
}

def rows():
    for path in INPUTS:
        with path.open(encoding="utf-8", newline="") as f:
            yield from csv.DictReader(f)

def main():
    sources=[]
    for r in rows():
        proposals=[]
        for label, domain, excerpt in T[r["code"]]:
            excerpt = EXCERPT_OVERRIDES.get((r["document_id"], label), excerpt)
            proposals.append({
                "proposed_label_pt": label,
                "suggested_domain_label_pt": domain,
                "aliases": (["SGBD"] if label == "sistemas gerenciadores de bancos de dados" else []),
                "alias_justification": ("The source explicitly supplies the abbreviation in parentheses." if label == "sistemas gerenciadores de bancos de dados" else None),
                "supporting_excerpt": excerpt,
                "epistemic_state": "indeterminate",
                "review_state": "proposed",
                "notes": "Analytical proposal grounded in the quoted source text; it does not establish 2023 curriculum applicability."
            })
        locator = r.get("ementa_locator") or r.get("source_locators")
        sources.append({
            "source_document_id": r["document_id"], "curriculum_id": "curriculum-2023",
            "component_code": r["code"], "component_name": r["source_title"],
            "document_type": r["document_kind"], "source_path": r["source_path"],
            "source_sha256": r["source_sha256"], "source_url": r["source_url"],
            "locator": locator, "applicability_2023": r["applicability_2023"],
            "documentary_status": "preserved; applicability indeterminate",
            "topic_proposals": proposals
        })
    payload={
      "dataset_id":"w033-agent-2023-proposals-v1", "dataset_kind":"intermediate-agent-proposals",
      "scope":"All 23 preserved Ficha 1 and 17 preserved Ficha 2 records in the declared 2023 corpus.",
      "generation_method":"Deterministic mapping of manually reviewed, exact excerpts from normalized preserved-source fields. No title-only proposals and no cross-curriculum inference.",
      "source_count":len(sources), "all_applicability_2023":"indeterminado",
      "sources":sources
    }
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps(payload, ensure_ascii=False, indent=2)+"\n", encoding="utf-8")

if __name__ == "__main__": main()
