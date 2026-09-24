"""Small, source-linked Dash view of formal curriculum component placement."""

from __future__ import annotations

import hashlib
import json
from pathlib import Path

import pandas as pd
import plotly.graph_objects as go
from dash import Dash, Input, Output, State, dcc, html


HERE = Path(__file__).resolve().parent
DATA_PATH = HERE / "data/formal_components.csv"
RELEASE = json.loads((HERE / "data/release.json").read_text(encoding="utf-8"))
assert hashlib.sha256(DATA_PATH.read_bytes()).hexdigest() == RELEASE["csv_sha256"]
DATA = pd.read_csv(DATA_PATH, dtype=str, keep_default_na=False)
assert len(DATA) == RELEASE["row_count"]
YEARS = ("2011", "2023")
COLORS = {"2011": "#316e65", "2023": "#a06b3b"}


def selected_rows(year: str) -> pd.DataFrame:
    return DATA if year == "Todos" else DATA[DATA["curriculum_year"] == year]


def summary(year: str) -> pd.DataFrame:
    rows = selected_rows(year)
    counts = rows.groupby(["recommended_period", "curriculum_year"]).size()
    records = []
    for period in range(1, 9):
        record = {"Período": str(period)}
        for curriculum in YEARS:
            if year in ("Todos", curriculum):
                record[curriculum] = int(counts.get((str(period), curriculum), 0))
        records.append(record)
    return pd.DataFrame(records)


def figure(year: str) -> go.Figure:
    table = summary(year)
    fig = go.Figure()
    for curriculum in YEARS:
        if curriculum in table.columns:
            fig.add_bar(
                name=curriculum,
                x=table["Período"],
                y=table[curriculum],
                marker_color=COLORS[curriculum],
                hovertemplate="Período %{x}<br>Componentes: %{y}<extra>Grade " + curriculum + "</extra>",
            )
    fig.update_layout(
        barmode="group", title=None, margin=dict(l=38, r=12, t=15, b=42),
        paper_bgcolor="#ffffff", plot_bgcolor="#ffffff", font=dict(color="#1a302d"),
        legend_title_text="Grade", height=390,
    )
    fig.update_xaxes(title_text="Período recomendado", showgrid=False)
    fig.update_yaxes(title_text="Componentes com código", dtick=1, gridcolor="#e5ebe7", rangemode="tozero")
    return fig


def table_view(year: str) -> html.Table:
    table = summary(year)
    columns = list(table.columns)
    return html.Table([
        html.Thead(html.Tr([html.Th(column, scope="col") for column in columns])),
        html.Tbody([
            html.Tr([html.Th(row["Período"], scope="row")] +
                    [html.Td(row[column]) for column in columns[1:]])
            for _, row in table.iterrows()
        ]),
    ], className="summary-table")


app = Dash(
    __name__,
    routes_pathname_prefix="/analises/",
    requests_pathname_prefix="/analises/",
    title="Análises · Informática Biomédica",
    meta_tags=[
        {"name": "description", "content": "Explore uma análise descritiva das disciplinas codificadas nas grades curriculares de Informática Biomédica da UFPR, com dados e fontes para consulta."},
        {"property": "og:title", "content": "Análises curriculares · Informática Biomédica UFPR"},
        {"property": "og:description", "content": "Visualize e baixe dados das grades curriculares de Informática Biomédica da UFPR, com fontes e limites documentais."},
        {"property": "og:type", "content": "website"},
        {"property": "og:site_name", "content": "Dados, Documentos e Análises sobre IBM/UFPR"},
        {"property": "og:locale", "content": "pt_BR"},
        {"property": "og:url", "content": "https://ibm.tail6629d6.ts.net/analises/"},
    ],
    health_endpoint="health",
)
server = app.server
app.layout = html.Div([
    html.A("Pular para a análise", href="#analise", className="skip-link"),
    html.Header(html.Div([
        html.A("IB", href="/", className="mark", title="Voltar ao início"),
        html.Div([html.Strong("Informática Biomédica"), html.Small("Dados e análises · UFPR")], className="brand-name"),
        html.Nav([html.A("Início", href="/"), html.A("Grades", href="/curriculos"),
                  html.A("Documentos", href="/documentos"),
                  html.A("Análises", href="/analises/", **{"aria-current": "page"})]),
    ], className="header-inner")),
    html.Main([
        html.P("Análise demonstrativa", className="eyebrow"),
        html.H1("Componentes por período"),
        html.P("Como os componentes com código se distribuem pelos períodos recomendados nas matrizes formais de 2011 e 2023?", className="lead"),
        html.Div([
            html.Div([html.Label("Selecionar grade", htmlFor="grade"), dcc.Dropdown(
                id="grade", options=[{"label": "As duas grades", "value": "Todos"},
                                      {"label": "2011", "value": "2011"},
                                      {"label": "2023", "value": "2023"}],
                value="Todos", clearable=False,
            )], className="filter"),
            html.Button("Baixar dados filtrados (CSV)", id="download-button", className="download-button"),
            dcc.Download(id="download"),
        ], className="controls"),
        html.Div([
            html.Section([
                html.H2("Distribuição"),
                dcc.Graph(id="period-chart", figure=figure("Todos"), config={"displayModeBar": False},
                          responsive=True),
            ], className="panel chart-panel"),
            html.Section([
                html.H2("Valores"),
                html.P(id="row-count", className="count"),
                html.Div(id="period-table", children=table_view("Todos")),
            ], className="panel table-panel"),
        ], id="analise", className="results"),
        html.Section([
            html.H2("Recorte, fontes e limites"),
            html.P("Unidade: um componente com código em uma grade formal. O eixo horizontal mostra a periodização recomendada, não turmas efetivamente ofertadas."),
            html.P("A contagem de 2011 exclui quatro espaços optativos sem código; por isso o 8º período aparece com zero neste recorte. Em 2023, quatro códigos de TCC são alternativas, não quatro exigências simultâneas. O catálogo de optativas de 2023 não entra na contagem."),
            html.P(["Fontes: ", html.A("Resolução 34/2010-CEPE", href="/documentos/document-2011-resolution-34-2010/arquivo"),
                    " e ", html.A("Resolução 75/22-CEPE", href="/documentos/document-2023-resolution-75-22/arquivo"),
                    ". As criações de componentes da grade 2023 também constam das Resoluções 76–80/22-CEPE, registradas no conjunto de dados."]),
            html.P("O CSV inclui o código, o nome, a carga horária e a base formal de cada linha. Esta visualização descreve as matrizes; não avalia sua qualidade ou equivalência."),
            html.Small("Conjunto de dados: " + RELEASE["release_id"], className="release"),
        ], className="method"),
    ], className="main"),
    html.Footer("Consulta documental independente · Informática Biomédica / UFPR"),
])


@app.callback(
    Output("period-chart", "figure"),
    Output("period-table", "children"),
    Output("row-count", "children"),
    Input("grade", "value"),
)
def update_view(year: str):
    if year not in ("Todos", *YEARS):
        year = "Todos"
    rows = selected_rows(year)
    return figure(year), table_view(year), f"{len(rows)} componentes no recorte selecionado"


@app.callback(
    Output("download", "data"), Input("download-button", "n_clicks"), State("grade", "value"),
    prevent_initial_call=True,
)
def download_rows(_clicks: int, year: str):
    if year not in ("Todos", *YEARS):
        year = "Todos"
    return dcc.send_data_frame(selected_rows(year).to_csv, f"componentes-formais-{year.lower()}.csv", index=False)
