from dash import Input, Output, dcc, html
import dash_bootstrap_components as dbc

from components.sampledf.model import df_maptest

# the style arguments for the sidebar. We use position:fixed and a fixed width

SIDEBAR_STYLE = {
    "position": "fixed",
    "top": 0,
    "left": 0,
    "bottom": 0,
    "width": "300px",
    "padding": "2rem 1rem",
    "backgroundColor": "#F8F9F9",
    "marginTop": "50px"
}

info = {}
content = [{"label": "TODOS", "value": "TODOS"}]
for iframe in df_maptest.DEPARTAMENTO:
    info = { 'label': iframe , 'value': iframe}
    content.append(info)  

sidebar = html.Div(
    [
        html.P(
            "Public contracts delay classificator", className="sidebar-subtitle"
        ),
        html.H1("Colombian Public Contracting Analytics Dashboard"),
        html.Hr(),
        html.Div([
                    html.Div(['Seleccione los departamentos'], className="mb-2  selector-label"),
                    dcc.Dropdown(
                    id="id_selector_municipio",
                    options=content,
                    value=['TODOS'],
                    multi = True
                )
        ]),
        html.Div([
                    html.Div(['Seleccione el rango de valores'], className="mb-2 mt-2 selector-label"),
                        dcc.Slider(0, 6, 0.01,
                        id='slider-updatemode',
                        marks={i: '{}'.format(10 ** i) for i in range(7)},
                        value=6,
                        updatemode='drag'
                    ),
        ]),
        dbc.Button([
                    'Filtrar'
                ],id="id_filtrar",className="btn-block mt-3")
    ],
    style=SIDEBAR_STYLE,
)