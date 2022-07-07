from dash import dcc, html, callback, Input, Output, State
import dash_bootstrap_components as dbc
import plotly.express as px

from components.kpiframe import kpibadge
from components.contract_state import contract_state
from components.contract_evo import contract_evo
from components.contract_sector import contract_sector
from dataframes.df_general import df_test

df1 = df_test.groupby(['DEPARTAMENTO','ESTADO']).agg({'CANTIDAD': ['sum'],'VALOR':['sum']}).reset_index()
df2 = df_test.groupby(['DEPARTAMENTO','ESTADO'])['CANTIDAD'].sum().reset_index()
df3 = df_test.groupby(['DEPARTAMENTO','FECHA'])['CANTIDAD'].sum().reset_index()
df4 = df_test.groupby(['DEPARTAMENTO','SECTOR'])['CANTIDAD'].sum().reset_index()
df_sort = df_test.groupby(['SECTOR'])['CANTIDAD'].sum().sort_values(ascending=False).reset_index()


pie_estado = contract_state('Number of contracts by state', 'row_pie_x',df2)

ser_evo = contract_evo('Evolution of contracts', 'row_evo_x',df3)

bar_sector = contract_sector('Contracts by sector', 'row_sec_x',df_sort)

a = df1['CANTIDAD'].sum()
b = round(df1['VALOR'].sum()/1000000,0)
c = round(b/a,2)

info = {}
content = [{"label": "All", "value": "All"}]
for iframe in df_test.DEPARTAMENTO.unique():
    info = { 'label': iframe , 'value': iframe}
    content.append(info) 

kpi1 = kpibadge(a, 'Total contracts', '')
kpi2 = kpibadge(b, 'Total value of contracts', 'Value in millions of pesos')
kpi3 = kpibadge(c, 'Average contract value', 'Value in millions of pesos')

layout=  dbc.Container(
    [
        dbc.Card(
            [dbc.CardBody([
                html.Div([
                    dbc.Row(
                            [
                                dbc.Col(
                                    [
                                        html.Div([
                                                    html.Div(['Select the departments'], className="mb-2  selector-label"),
                                                    dcc.Dropdown(
                                                    id="id_selector_depto",
                                                    options=content,
                                                    value=['All'],
                                                    multi = True
                                                )
                                        ]),
                                        html.Div([
                                            dbc.Button([
                                                'Filter'
                                            ],id="id_filtrar",className="btn-block mt-3")
                                        ], className="d-flex justify-content-end mb-3"),
                                    ]
                                )
                            ],
                    ),
                    dbc.Row([
                        dbc.Col([
                            html.Div([
                                        kpi1.display()
                                ],id="total_contratos") 
                        ], className='card_'),
                        dbc.Col([
                            html.Div([
                                        kpi2.display()
                                ],id="total_valor")
                        ], className='card_'),
                        dbc.Col([
                            html.Div([
                                        kpi3.display()
                                ],id="total_prom")
                        ], className='card_')
                    ]),
                    dbc.Row([
                        dbc.Col([
                            html.Div([
                                        pie_estado.display()
                                ],id="row_pie") 
                        ], className='card'), 
                        dbc.Col([
                            html.Div([
                                        ser_evo.display()
                                ],id="row_evo") 
                        ], className='card'), 
                    ]),
                    dbc.Row([
                        dbc.Col([
                            html.Div([
                                        bar_sector.display()
                                ],id="row_bar") 
                        ], className='card')
                    ])
                ])],className="mb-3")
            ])
    ]
)  


@callback(
        [Output("row_pie", 'children')], 
        [Output("total_contratos", 'children')],
        [Output("total_valor", 'children')],
        [Output("total_prom", 'children')],
        [Output("row_evo", 'children')],
        [Output("row_bar", 'children')],
        [State("id_selector_depto", "value"),
         Input("id_filtrar", "n_clicks"),
                
        ],prevent_initial_call=True
    )
def update_pie(selector_depto,nclicks):
        df_filtrado = df2[df2['DEPARTAMENTO'].isin(selector_depto)]
        df_filtrado_1 = df1[df1['DEPARTAMENTO'].isin(selector_depto)]
        df_filtrado_3 = df3[df3['DEPARTAMENTO'].isin(selector_depto)]
        df_filtrado_4 = df4[df4['DEPARTAMENTO'].isin(selector_depto)]
        #contract_state.df = df_filtrado
        pie_estado = contract_state('Number of contracts by state', 'row_pie_x',df_filtrado)
        ser_evo = contract_evo('Evolution of contracts', 'row_evo_x',df_filtrado_3)
        bar_sector = contract_sector('Contracts by sector', 'row_sec_x',df_filtrado_4)
        nuevo_pie = pie_estado.display()
        nuevo_evo = ser_evo.display()
        nuevo_bar = bar_sector.display()
        a = df_filtrado_1['CANTIDAD'].sum()
        b = round(df_filtrado_1['VALOR'].sum()/1000000,0)
        c = round(b/a,2)
        kpi1 = kpibadge(a, 'Total contracts', '')
        kpi2 = kpibadge(b, 'Total value of contracts', 'Value in millions of pesos')
        kpi3 = kpibadge(c, 'Average contract value', 'Value in millions of pesos')
        n_kpi1 = kpi1.display()
        n_kpi2 = kpi2.display()
        n_kpi3 = kpi3.display()
        return nuevo_pie, n_kpi1, n_kpi2, n_kpi3,nuevo_evo,nuevo_bar