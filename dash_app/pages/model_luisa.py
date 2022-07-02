from dash import dcc, html
import dash_bootstrap_components as dbc

from dataframes.data import df2


departamentos_options = []
for item in df2["Departamento"].unique():
    departamentos_options.append({"label": item, "value": item})
departamentos_select = html.Div(
    [
        dbc.Label("Departamento", html_for="departamento"),
        dcc.Dropdown(
            id="departamento",
            options=departamentos_options,
        ),
    ],
    className="mb-3",
)

orden_options = []
for item in df2["Orden"].unique():
    orden_options.append({"label": item, "value": item})
orden_select = html.Div(
    [
        dbc.Label("Orden", html_for="orden"),
        dcc.Dropdown(
            id="orden",
            options=orden_options,
        ),
    ],
    className="mb-3",
)

sector_options = []
for item in df2["Sector"].unique():
    sector_options.append({"label": item, "value": item})
sector_select = html.Div(
    [
        dbc.Label("Sector", html_for="sector"),
        dcc.Dropdown(
            id="sector",
            options=sector_options,
        ),
    ],
    className="mb-3",
)

rama_options = []
for item in df2["Rama"].unique():
    rama_options.append({"label": item, "value": item})
rama_select = html.Div(
    [
        dbc.Label("Rama", html_for="rama"),
        dcc.Dropdown(
            id="rama",
            options=sector_options,
        ),
    ],
    className="mb-3",
)

entidad_centralizada_options = []
for item in df2["Entidad Centralizada"].unique():
    entidad_centralizada_options.append({"label": item, "value": item})
entidad_centralizada_select = html.Div(
    [
        dbc.Label("Entidad Centralizada", html_for="entidad_centralizada"),
        dcc.Dropdown(
            id="entidad_centralizada",
            options=entidad_centralizada_options,
        ),
    ],
    className="mb-3",
)

estado_contrato_options = []
for item in df2["Estado Contrato"].unique():
    estado_contrato_options.append({"label": item, "value": item})
estado_contrato_select = html.Div(
    [
        dbc.Label("Estado de Contrato", html_for="estado_contrato"),
        dcc.Dropdown(
            id="estado_contrato",
            options=estado_contrato_options,
        ),
    ],
    className="mb-3",
)

tipo_contrato_options = []
for item in df2["Tipo de Contrato"].unique():
    tipo_contrato_options.append({"label": item, "value": item})
tipo_contrato_select = html.Div(
    [
        dbc.Label("Tipo de Contrato", html_for="tipo_contrato"),
        dcc.Dropdown(
            id="tipo_contrato",
            options=tipo_contrato_options,
        ),
    ],
    className="mb-3",
)

modalidad_contratacion_options = []
for item in df2["Modalidad de Contratacion"].unique():
    modalidad_contratacion_options.append({"label": item, "value": item})
modalidad_contratacion_select = html.Div(
    [
        dbc.Label("Modalidad de Contratación", html_for="modalidad_contratacion"),
        dcc.Dropdown(
            id="modalidad_contratacion",
            options=modalidad_contratacion_options,
        ),
    ],
    className="mb-3",
)

switches_input = html.Div(
    [
        dbc.Checklist(
            options=[
                {"label": "Es Grupo", "value": "es_grupo"},
                {"label": "Es Pyme", "value": "es_pyme"},
                {"label": "Obligación Ambiental", "value": "obligacion_ambiental"},
                {"label": "Obligaciones Postconsumo", "value": "obligaciones_postconsumo"},
            ],
            value=[1],
            id="switches-input",
            switch=True,
        ),
    ]
)

valor_contrato_input = html.Div(
    [
        dbc.Label("Valor del Contrato", html_for="valor_contrato"),
        dbc.Input(type="number", id="valor_contrato", value="0")
    ],
    className="mb-3",
)

valor_pago_adelantado_input = html.Div(
    [
        dbc.Label("Valor del Pago Adelantado", html_for="valor_pago_adelantado"),
        dbc.Input(type="number", id="valor_pago_adelantado", value="0")
    ],
    className="mb-3",
)

form = dbc.Form([
    departamentos_select, 
    orden_select, 
    sector_select, 
    rama_select, 
    entidad_centralizada_select,
    estado_contrato_select,
    tipo_contrato_select,
    modalidad_contratacion_select,
    switches_input,
    valor_contrato_input,
    valor_pago_adelantado_input
])

layout = html.Div([
    html.H3("Contracts Delay Classificator"),
    dbc.Card([form], className="p-3"),
])