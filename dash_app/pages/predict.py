from dash import Dash, dcc, html, Input, Output, State, callback
import dash_bootstrap_components as dbc
from dataframes.data import df2

departamentos_options = []
for item in df2["Departamento"].unique():
    departamentos_options.append({"label": item, "value": item})
departamentos_select = html.Div(
    [
        dbc.Row(
            [
                dbc.Col(
                    dbc.Label("Departamento", html_for="departamento"), width=3
                ),
                dbc.Col(
                    dcc.Dropdown(
                        id="departamento",
                        options=departamentos_options,
                    )
                ),
            ],
        )
    ],
    className="mb-3",
)

orden_options = []
for item in df2["Orden"].unique():
    orden_options.append({"label": item, "value": item})    
orden_select = html.Div(
    [
        dbc.Row(
            [
                dbc.Col(
                    dbc.Label("Orden", html_for="orden"), width=3
                ),
                dbc.Col(
                    dcc.Dropdown(
                        id="orden",
                        options=orden_options,
                    )
                ),
            ],
        )
    ],
    className="mb-3",
)

sector_options = []
for item in df2["Sector"].unique():
    sector_options.append({"label": item, "value": item})
sector_select = html.Div(
    [
        dbc.Row(
            [
                dbc.Col(
                    dbc.Label("Sector", html_for="sector"), width=3
                ),
                dbc.Col(
                    dcc.Dropdown(
                        id="sector",
                        options=sector_options,
                    )
                ),
            ],
        )
    ],
    className="mb-3",
)

rama_options = []
for item in df2["Rama"].unique():
    rama_options.append({"label": item, "value": item})
rama_select = html.Div(
    [
        dbc.Row(
            [
                dbc.Col(
                    dbc.Label("Rama", html_for="rama"), width=3
                ),
                dbc.Col(
                    dcc.Dropdown(
                        id="rama",
                        options=rama_options,
                    )
                ),
            ],
        )
    ],
    className="mb-3",
)

entidad_centralizada_options = []
for item in df2["Entidad Centralizada"].unique():
    entidad_centralizada_options.append({"label": item, "value": item})
entidad_centralizada_select = html.Div(
    [
        dbc.Row(
            [
                dbc.Col(
                    dbc.Label("Entidad Centralizada", html_for="entidad_centralizada"), width=3
                ),
                dbc.Col(
                    dcc.Dropdown(
                        id="entidad_centralizada",
                        options=entidad_centralizada_options,
                    )
                ),
            ],
        )
    ],
    className="mb-3",
)

estado_contrato_options = []
for item in df2["Estado Contrato"].unique():
    estado_contrato_options.append({"label": item, "value": item})
estado_contrato_select = html.Div(
    [
        dbc.Row(
            [
                dbc.Col(
                    dbc.Label("Estado Contrato", html_for="estado_contrato"), width=3
                ),
                dbc.Col(
                    dcc.Dropdown(
                        id="estado_contrato",
                        options=estado_contrato_options,
                    )
                ),
            ],
        )
    ],
    className="mb-3",
)

tipo_contrato_options = []
for item in df2["Tipo de Contrato"].unique():
    tipo_contrato_options.append({"label": item, "value": item})
tipo_contrato_select = html.Div(
    [
        dbc.Row(
            [
                dbc.Col(
                    dbc.Label("Tipo de Contrato", html_for="tipo_contrato"), width=3
                ),
                dbc.Col(
                    dcc.Dropdown(
                        id="tipo_contrato",
                        options=tipo_contrato_options,
                    )
                ),
            ],
        )
    ],
    className="mb-3",
)

modalidad_contratacion_options = []
for item in df2["Modalidad de Contratacion"].unique():
    modalidad_contratacion_options.append({"label": item, "value": item})
modalidad_contratacion_select = html.Div(
    [
        dbc.Row(
            [
                dbc.Col(
                    dbc.Label("Modalidad de Contratación", html_for="modalidad_contratacion"), width=3
                ),
                dbc.Col(
                    dcc.Dropdown(
                        id="modalidad_contratacion",
                        options=modalidad_contratacion_options,
                    )
                ),
            ],
        )
    ],
    className="mb-3",
)

destino_gasto_options = []
for item in df2["Destino Gasto"].unique():
    destino_gasto_options.append({"label": item, "value": item})
destino_gasto_select = html.Div(
    [
        dbc.Row(
            [
                dbc.Col(
                    dbc.Label("Destino Gasto", html_for="destino_gasto"), width=3
                ),
                dbc.Col(
                    dcc.Dropdown(
                        id="destino_gasto",
                        options=destino_gasto_options,
                    )
                ),
            ],
        )
    ],
    className="mb-3",
)

valor_contrato_input = html.Div(
    [
        dbc.Row(
            [
                dbc.Col(
                    dbc.Label("Valor del Contrato", html_for="valor_contrato"), width=3
                ),
                dbc.Col(
                    dbc.Input(type="number", id="valor_contrato", value="0")
                )
            ],
        )
    ],
    className="mb-3",
)

valor_pago_adelantado_input = html.Div(
    [
        dbc.Row(
            [
                dbc.Col(
                    dbc.Label("Valor del Pago Adelantado", html_for="valor_pago_adelantado"), width=3
                ),
                dbc.Col(
                    dbc.Input(type="number", id="valor_pago_adelantado", value="0")
                )
            ],
        )
    ],
    className="mb-3",
)

valor_facturado_input = html.Div(
    [
        dbc.Row(
            [
                dbc.Col(
                    dbc.Label("Valor Facturado", html_for="valor_facturado"), width=3
                ),
                dbc.Col(
                    dbc.Input(type="number", id="valor_facturado", value="0")
                )
            ],
        )
    ],
    className="mb-3",
)

valor_pendiente_pago_input = html.Div(
    [
        dbc.Row(
            [
                dbc.Col(
                    dbc.Label("Valor Pendiente de Pago", html_for="valor_pendiente_pago"), width=3
                ),
                dbc.Col(
                    dbc.Input(type="number", id="valor_pendiente_pago", value="0")
                )
            ],
        )
    ],
    className="mb-3",
)

valor_amortizado_input = html.Div(
    [
        dbc.Row(
            [
                dbc.Col(
                    dbc.Label("Valor Amortizado", html_for="valor_amortizado"), width=3
                ),
                dbc.Col(
                    dbc.Input(type="number", id="valor_amortizado", value="0")
                )
            ],
        )
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
                {"label": "Es Postconflicto", "value": "es_postconflicto"},
                {"label": "Presupuesto General de la Nación", "value": "es_pgn"},
                {"label": "Sistema General de Participaciones", "value": "es_sgp"},
                {"label": "Sistema Geenral de Regalías", "value": "es_sgr"},
                {"label": "Recursos Propios (Alcaldías Gobernaciones y Resguardos Indígenas)", "value": "es_rp_agr"},
                {"label": "Recursos Propios", "value": "es_rp_no_agr"},
                {"label": "Recursos de Crédito", "value": "es_rc"},
            ],
            #value=[1],
            id="switches_input",
            switch=True,
        ),
    ]
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
    destino_gasto_select,    
    valor_contrato_input,
    valor_pago_adelantado_input,
    valor_facturado_input,
    valor_pendiente_pago_input,
    valor_amortizado_input,
    switches_input,
])


layout = html.Div(
    [
        html.H3("Contracts Delay Prediction"),
        html.H6("Select the contract variables and press button below to see the prediction"),
        dbc.Card([form], className="p-3"),        
        #html.Br(),
        #html.Div(dcc.Input(id='input-on-submit', type='text')),
        dbc.Button(['Predict'],id="submit_val", className="btn-block mt-3", n_clicks=0),
        html.Br(),
        html.Br(),
        html.Div(id='container', children='')
    ]
)

@callback(
    Output('container', 'children'),
    [Input("submit_val", "n_clicks")],
    [State("departamento", "value"), 
     State("orden", "value"), 
     State("sector", "value"), 
     State("rama", "value"),
     State("entidad_centralizada", "value"),
     State("estado_contrato", "value"),
     State("tipo_contrato", "value"),
     State("modalidad_contratacion", "value"),
     State("destino_gasto", "value"),
     State("valor_contrato", "value"),
     State("valor_pago_adelantado", "value"),
     State("valor_facturado", "value"),
     State("valor_pendiente_pago", "value"),
     State("valor_amortizado", "value"),
     State("switches_input", "value")
    ]
    , prevent_initial_call=True
)
def update_output(n_clicks, departamento, orden, sector, rama, entidad_centralizada, estado_contrato, tipo_contrato, 
                 modalidad_contratacion, destino_gasto, valor_contrato, valor_pago_adelantado, valor_facturado,
                 valor_pendiente_pago, valor_amortizado, switches_input):
    variables = {}
    variables["Departamento"] = departamento
    variables["Orden"] = orden
    variables["Sector"] = sector
    variables["Rama"] = rama
    variables["Entidad Centralizada"] = entidad_centralizada
    variables["Estado Contrato"] = estado_contrato
    variables["Tipo de Contrato"] = tipo_contrato
    variables["Modalidad de Contratacion"] = modalidad_contratacion
    variables["Destino Gasto"] = destino_gasto
    variables["Valor del Contrato"] = valor_contrato
    variables["Valor del Pago Adelantado"] = valor_pago_adelantado
    variables["Valor Facturado"] = valor_facturado
    variables["Valor Pendiente de Pago"] = valor_pendiente_pago
    variables["Valor Amortizado"] = valor_amortizado
    variables["Switches"] = switches_input
    
    prediction = XGBoost_predict(n_clicks)
    return 'The delay prediction for {0} "{1}"'.format(variables, prediction['Delay prediction'])

def prepare_model_data(x_variables):
    return x_variables

def load_model():
    model = open('model.pkl', 'rb')
    return joblib.load(model)

def XGBoost_predict(x_variables):
    prepared_data = prepare_model_data(x_variables)
    #prediction = load_model().predict(prepared_data)
    return {'Delay prediction': 'No'}