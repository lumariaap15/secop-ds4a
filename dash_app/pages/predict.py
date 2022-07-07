from dash import Dash, dcc, html, Input, Output, State, callback
import dash_bootstrap_components as dbc
from dataframes.data import df2
from datetime import date
from datetime import datetime
import pandas as pd
import pickle

#colums to drop from dataframe to predict
drop = ['NormalizedDelay','Unnamed: 0', 'Nombre Entidad','Dias Adicionados', 
        'Fecha de Inicio del Contrato', 'Fecha de Fin del Contrato']

#Dataframe already loaded in dataframes.data
df = df2.drop(drop, axis=1)

#Categorization required in prediction model
cat_cols = ['Departamento', 'Orden', 'Sector', 'Rama','Entidad Centralizada', 'Estado Contrato', 
            'Tipo de Contrato', 'Modalidad de Contratacion', 'Es Grupo','Es Pyme', 'Destino Gasto', 'EsPostConflicto',
            'Obligaciones Postconsumo','Obligación Ambiental', 'Delay']
cat_values = {key:'category' for key in cat_cols}
df = df.astype(cat_values)

#Page elements (Combo boxes)
departamentos_options = []
for item in df["Departamento"].unique():
    departamentos_options.append({"label": item, "value": item})
departamentos_select = html.Div(
    [
        dbc.Row(
            [
                dbc.Col(
                    dcc.Dropdown(
                        id="departamento",
                        options=departamentos_options,
                        placeholder="Departamento"
                    )
                ),
            ],
        )
    ],
    className="mb-3",
)

orden_options = []
for item in df["Orden"].unique():
    orden_options.append({"label": item, "value": item})    
orden_select = html.Div(
    [
        dbc.Row(
            [
                dbc.Col(
                    dcc.Dropdown(
                        id="orden",
                        options=orden_options,
                        placeholder="Orden"
                    )
                ),
            ],
        )
    ],
    className="mb-3",
)

sector_options = []
for item in df["Sector"].unique():
    sector_options.append({"label": item, "value": item})
sector_select = html.Div(
    [
        dbc.Row(
            [
                dbc.Col(
                    dcc.Dropdown(
                        id="sector",
                        options=sector_options,
                        placeholder="Sector"
                    )
                ),
            ],
        )
    ],
    className="mb-3",
)

rama_options = []
for item in df["Rama"].unique():
    rama_options.append({"label": item, "value": item})
rama_select = html.Div(
    [
        dbc.Row(
            [
                dbc.Col(
                    dcc.Dropdown(
                        id="rama",
                        options=rama_options,
                        placeholder="Rama"
                    )
                ),
            ],
        )
    ],
    className="mb-3",
)

entidad_centralizada_options = []
for item in df["Entidad Centralizada"].unique():
    entidad_centralizada_options.append({"label": item, "value": item})
entidad_centralizada_select = html.Div(
    [
        dbc.Row(
            [
                dbc.Col(
                    dcc.Dropdown(
                        id="entidad_centralizada",
                        options=entidad_centralizada_options,
                        placeholder="Entidad Centralizada"
                    )
                ),
            ],
        )
    ],
    className="mb-3",
)

estado_contrato_options = []
for item in df["Estado Contrato"].unique():
    estado_contrato_options.append({"label": item, "value": item})
estado_contrato_select = html.Div(
    [
        dbc.Row(
            [
                dbc.Col(
                    dcc.Dropdown(
                        id="estado_contrato",
                        options=estado_contrato_options,
                        placeholder="Estado Contrato"
                    )
                ),
            ],
        )
    ],
    className="mb-3",
)

tipo_contrato_options = []
for item in df["Tipo de Contrato"].unique():
    tipo_contrato_options.append({"label": item, "value": item})
tipo_contrato_select = html.Div(
    [
        dbc.Row(
            [
                dbc.Col(
                    dcc.Dropdown(
                        id="tipo_contrato",
                        options=tipo_contrato_options,
                        placeholder="Tipo de Contrato"
                    )
                ),
            ],
        )
    ],
    className="mb-3",
)

modalidad_contratacion_options = []
for item in df["Modalidad de Contratacion"].unique():
    modalidad_contratacion_options.append({"label": item, "value": item})
modalidad_contratacion_select = html.Div(
    [
        dbc.Row(
            [
                dbc.Col(
                    dcc.Dropdown(
                        id="modalidad_contratacion",
                        options=modalidad_contratacion_options,
                        placeholder="Modalidad de Contratación"
                    )
                ),
            ],
        )
    ],
    className="mb-3",
)

destino_gasto_options = []
for item in df["Destino Gasto"].unique():
    destino_gasto_options.append({"label": item, "value": item})
destino_gasto_select = html.Div(
    [
        dbc.Row(
            [
                dbc.Col(
                    dcc.Dropdown(
                        id="destino_gasto",
                        options=destino_gasto_options,
                        placeholder="Destino Gasto"
                    )
                ),
            ],
        )
    ],
    className="mb-3",
)

#Page elements (Inputs)
valor_contrato_input = html.Div(
    [
        dbc.Row(
            [
                dbc.Col(
                    dbc.Input(type="number", id="valor_contrato", placeholder="Valor del Contrato")
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
                    dbc.Input(type="number", id="valor_pago_adelantado", placeholder="Valor del Pago Adelantado")
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
                    dbc.Input(type="number", id="valor_facturado", placeholder="Valor Facturado")
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
                    dbc.Input(type="number", id="valor_pendiente_pago", placeholder="Valor Pendiente de Pago")
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
                    dbc.Input(type="number", id="valor_amortizado", placeholder="Valor Amortizado")
                )
            ],
        )
    ],
    className="mb-3",
)

#Page elements (Switches = yes or no)
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

#Main div to render the page
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

#Form distributed in two columns using all the elements created before
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


#Layout page integrating all the components above
layout = html.Div(
    [
        html.H3(["Contracts Delay Prediction"],className="text-white"),
        html.H6(["Select the contract variables and press button below to see the prediction"],className="text-white"),
        dbc.Card([
            form,
            html.Div([
                dbc.Button(['Predict'],id="submit_val", className="mt-3", n_clicks=0),
            ],className="d-flex justify-content-center"),
            html.Div(id='container', children='')   
        ], className="p-3"),        
    ]
)

#Callback receiving all the user data provided in the form elements
#Output: a div to show prediction result
#Input: button click
#State: all form elements values provided by user
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

    predict_df = prepare_model_data(departamento, orden, sector, rama, entidad_centralizada, estado_contrato, tipo_contrato, 
                 modalidad_contratacion, destino_gasto, valor_contrato, valor_pago_adelantado, valor_facturado,
                 valor_pendiente_pago, valor_amortizado, fecha_fin_contrato, switches_input)
    
    prediction = XGBoost_predict(predict_df)
    return 'The delay prediction for this contract is {0}'.format(prediction)
    #return str(variables)

#Invoke prediction model using a pickle file
def XGBoost_predict(predict_df):    
    prediction = load_model().predict(predict_df)[0]
    return normalize_prediction(prediction)

#Receive input data to create a dataframe from it
def prepare_model_data(departamento, orden, sector, rama, entidad_centralizada, estado_contrato, tipo_contrato, 
                 modalidad_contratacion, destino_gasto, valor_contrato, valor_pago_adelantado, valor_facturado,
                 valor_pendiente_pago, valor_amortizado, fecha_fin_contrato, switches_input):
    
    #Used to conver True and False as Yes or No
    bools = ("No", "Si")
    
    #Create an additional feature based on fecha_fin_contrato and december 31 for that year.
    #Difference in days is added as a new attribute to the model
    fecha_fin_contrato = datetime.strptime(fecha_fin_contrato, '%Y-%m-%d').date()
    fecha_fin_ano_contrato = datetime.strptime(str(fecha_fin_contrato.year) + '-12-31', '%Y-%m-%d').date()

    #Load a record from the dataframe to create the record to predict
    cols = ['Departamento', 'Orden', 'Sector', 'Rama', 'Entidad Centralizada',
           'Estado Contrato', 'Tipo de Contrato', 'Modalidad de Contratacion',
           'Es Grupo', 'Es Pyme', 'Obligación Ambiental',
           'Obligaciones Postconsumo', 'Valor del Contrato',
           'Valor de pago adelantado', 'Valor Facturado',
           'Valor Pendiente de Pago', 'Valor Amortizado', 'EsPostConflicto',
           'Destino Gasto', 'PGN', 'SGP', 'SGR', 'RP_AGR', 'RP_NO_AGR', 'RC', 'Days_to_end_of_year']
    new_df = df[df["Delay"] == 0][cols].head(1)

    #Replaces all the values in the dataframe row with the values provided by the user
    #It was the only way to invoke prediction without receiving and error from model
    index = new_df.iloc[[0]].index
    new_df.loc[index, "Departamento"] = departamento
    new_df.loc[index, "Orden"] = orden
    new_df.loc[index, "Sector"] = sector
    new_df.loc[index, "Rama"] = rama
    new_df.loc[index, "Entidad Centralizada"] = entidad_centralizada
    new_df.loc[index, "Estado Contrato"] = estado_contrato
    new_df.loc[index, "Tipo de Contrato"] = tipo_contrato
    new_df.loc[index, "Modalidad de Contratacion"] = modalidad_contratacion
    
    new_df.loc[index, "Es Grupo"] = bools['es_grupo' in switches_input] if switches_input != None else "No"
    new_df.loc[index, "Es Pyme"] = bools['es_pyme' in switches_input] if switches_input != None else "No"
    new_df.loc[index, "Obligación Ambiental"] = bools['obligacion_ambiental' in switches_input] if switches_input != None else "No"
    new_df.loc[index, "Obligaciones Postconsumo"] = bools['obligaciones_postconsumo' in switches_input] if switches_input != None else "No"
    new_df.loc[index, "Valor del Contrato"] = float(valor_contrato) if valor_contrato != None else 0
    new_df.loc[index, "Valor de pago adelantado"] = float(valor_pago_adelantado) if valor_pago_adelantado != None else 0
    new_df.loc[index, "Valor Facturado"] = float(valor_facturado) if valor_facturado != None else 0
    new_df.loc[index, "Valor Pendiente de Pago"] = float(valor_pendiente_pago) if valor_pendiente_pago != None else 0
    new_df.loc[index, "Valor Amortizado"] = float(valor_amortizado) if valor_amortizado != None else 0
    new_df.loc[index, "EsPostConflicto"] = bools['es_postconflicto' in switches_input] if switches_input != None else "No"
    new_df.loc[index, "Destino Gasto"] = destino_gasto
    new_df.loc[index, "PGN"] = int('es_pgn' in switches_input) if switches_input != None else 0
    new_df.loc[index, "SGP"] = int('es_sgp' in switches_input) if switches_input != None else 0
    new_df.loc[index, "SGR"] = int('es_sgr' in switches_input) if switches_input != None else 0
    new_df.loc[index, "RP_AGR"] = int('es_rp_agr' in switches_input) if switches_input != None else 0
    new_df.loc[index, "RP_NO_AGR"] = int('es_rp_no_agr' in switches_input) if switches_input != None else 0
    new_df.loc[index, "RC"] = int('es_rc' in switches_input) if switches_input != None else 0
    new_df.loc[index, "Days_to_end_of_year"] = (fecha_fin_ano_contrato-fecha_fin_contrato).days

    return new_df

#Load the pickle file
def load_model():
    return pickle.load(open('assets/model/model_downsampling.pkl', 'rb'))

#Transforms the prediction to show the result
def normalize_prediction(prediction):
    possible_results = {0: "None", 1: "Low", 2: "Medium", 3: "High"}
    return possible_results[prediction]