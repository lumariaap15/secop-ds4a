from dash import Dash, dcc, html, Input, Output, State, callback
import dash_bootstrap_components as dbc
from dataframes.data import df2
from datetime import date
from datetime import datetime
import pandas as pd
import pickle

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
                {"label": "Tiene Obligación Ambiental", "value": "obligacion_ambiental"},
                {"label": "Tiene Obligaciones Postconsumo", "value": "obligaciones_postconsumo"},
                {"label": "Es Postconflicto", "value": "es_postconflicto"},
                {"label": "Tiene Presupuesto General de la Nación", "value": "es_pgn"},
                {"label": "Tiene Presupuesto Sistema General de Participaciones", "value": "es_sgp"},
                {"label": "Tiene Presupuesto Sistema General de Regalías", "value": "es_sgr"},
                {"label": "Tiene Recursos Propios (Alcaldías Gobernaciones y Resguardos Indígenas)", "value": "es_rp_agr"},
                {"label": "Tiene Recursos Propios", "value": "es_rp_no_agr"},
                {"label": "Tiene Recursos de Crédito", "value": "es_rc"},
            ],
            #value=[1],
            id="switches_input",
            switch=True,
        ),
    ]
)

fecha_fin_contrato_input = html.Div(
    [
        dbc.Row(
            [
                dbc.Col(
                    dbc.Label("Fecha de Fin del Contrato", html_for="fecha_fin_contrato"), width=3
                ),
                dbc.Col(
                    dcc.DatePickerSingle(
                        id='fecha_fin_contrato',
                        min_date_allowed=df2["Fecha de Fin del Contrato"].min(), #date(2018, 1, 31),
                        max_date_allowed=df2["Fecha de Fin del Contrato"].max(), #date(2022, 12, 31),
                        initial_visible_month=date.today(), #date(2022, 7, 4),
                        date=date.today() #date(2022, 7, 4)
                    )
                )
            ],
        )
    ],
    className="mb-3",
)

"""
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
"""

form = dbc.Form([
    dbc.Row(
            [
                dbc.Col(
                    [
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
                    ]
                ),
                dbc.Col(
                    [ 
                        valor_facturado_input,
                        valor_pendiente_pago_input,
                        valor_amortizado_input,
                        fecha_fin_contrato_input,
                        switches_input,
                    ]
                )
            ],
    )
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
     State("fecha_fin_contrato", "date"),
     State("switches_input", "value")
    ]
    , prevent_initial_call=True
)
def update_output(n_clicks, departamento, orden, sector, rama, entidad_centralizada, estado_contrato, tipo_contrato, 
                 modalidad_contratacion, destino_gasto, valor_contrato, valor_pago_adelantado, valor_facturado,
                 valor_pendiente_pago, valor_amortizado, fecha_fin_contrato, switches_input):
    variables = {}
    variables["Departamento"] = departamento
    variables["Orden"] = orden
    variables["Sector"] = sector
    variables["Rama"] = rama
    variables["Entidad Centralizada"] = entidad_centralizada
    variables["Estado Contrato"] = estado_contrato
    variables["Tipo de Contrato"] = tipo_contrato
    variables["Modalidad de Contratacion"] = modalidad_contratacion
    variables["Es Grupo"] = int('es_grupo' in switches_input) if switches_input != None else 0
    variables["Es Pyme"] = int('es_pyme' in switches_input) if switches_input != None else 0
    variables["Obligación Ambiental"] = int('obligacion_ambiental' in switches_input) if switches_input != None else 0
    variables["Obligaciones Postconsumo"] = int('obligaciones_postconsumo' in switches_input) if switches_input != None else 0
    variables["Valor del Contrato"] = int(valor_contrato)
    variables["Valor del Pago Adelantado"] = int(valor_pago_adelantado)
    variables["Valor Facturado"] = int(valor_facturado)
    variables["Valor Pendiente de Pago"] = int(valor_pendiente_pago)
    variables["Valor Amortizado"] = int(valor_amortizado)
    variables["EsPostConflicto"] = int('es_postconflicto' in switches_input) if switches_input != None else 0
    variables["Destino Gasto"] = destino_gasto
    variables["PGN"] = int('es_pgn' in switches_input) if switches_input != None else 0
    variables["SGP"] = int('es_sgp' in switches_input) if switches_input != None else 0
    variables["SGR"] = int('es_sgr' in switches_input) if switches_input != None else 0
    variables["RP_AGR"] = int('es_rp_agr' in switches_input) if switches_input != None else 0
    variables["RP_NO_AGR"] = int('es_rp_no_agr' in switches_input) if switches_input != None else 0
    variables["RC"] = int('es_rc' in switches_input) if switches_input != None else 0
    
    fecha_fin_contrato = datetime.strptime(fecha_fin_contrato, '%Y-%m-%d').date()
    fecha_fin_ano_contrato = datetime.strptime(str(fecha_fin_contrato.year) + '-12-31', '%Y-%m-%d').date()
    variables["Days_to_end_of_year"] = (fecha_fin_ano_contrato-fecha_fin_contrato).days
    
    prediction = XGBoost_predict(variables)
    return 'The delay prediction for this contract is {0}'.format(prediction)
    #return str(variables)

def XGBoost_predict(variables):
    df_input = prepare_model_data(variables)
    prediction = load_model().predict(df_input)[0]
    return normalize_prediction(prediction)

def prepare_model_data(variables):
    df_input = pd.DataFrame.from_dict(variables, orient='index').T

    cat_cols = ['Departamento', 'Orden', 'Sector', 'Rama', 'Entidad Centralizada', 'Estado Contrato', 
                'Tipo de Contrato', 'Modalidad de Contratacion', 'Es Grupo','Es Pyme', 'Destino Gasto', 
                'EsPostConflicto', 'Obligaciones Postconsumo', 'Obligación Ambiental']

    cat_values = {key:'category' for key in cat_cols}
    df_input = df_input.astype(cat_values)

    cols = df_input.select_dtypes(include='object').columns
    df_input[cols] = df_input[cols].astype('int')    
    
    return df_input

def load_model():
    return pickle.load(open('assets/model/clf_model.pkl', 'rb'))

def normalize_prediction(prediction):
    possible_results = {0: "None", 1: "Low", 2: "Medium", 3: "High"}
    return possible_results[prediction]

