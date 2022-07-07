
from dash import html , dcc, callback, Input, Output, State
import dash_bootstrap_components as dbc

from components.mapcol_departamentos import mapcol_departamentos


from dataframes.contratos_departamento import df_maptest
from components.table_departamentos import table
from components.contract_type_graphs import contract_type_count_pie_chart


mapa_colombia_departamentos = mapcol_departamentos('Number of projects by department in Colombia', 'div_municipios_fig2',df_maptest)


params1 = {
            'title': '', 
            'description': 'List of departments (The values ​​of the TOTAL column are in billions)',
            'columns': [ 'DEPARTAMENTO',  'CANTIDAD', 'TOTAL']
}
tabla_datos_departamentos = table(df_maptest,params1)


info = {}
content = [{"label": "All", "value": "All"}]
for iframe in df_maptest.DEPARTAMENTO:
    info = { 'label': iframe , 'value': iframe}
    content.append(info)      


layout= html.Div(
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
                                                    id="id_selector_municipio",
                                                    options=content,
                                                    value=['All'],
                                                    multi = True
                                                )
                                        ]),
                                    ]
                                ),
                                dbc.Col(
                                    [ 
                                        html.Div([
                                                    html.Div(['Select the range of values'], className="mb-2 mt-2 selector-label"),
                                                        dcc.Slider(0, 6, 0.01,
                                                        id='slider-updatemode',
                                                        marks={i: '{}'.format(10 ** i) for i in range(7)},
                                                        value=6,
                                                        updatemode='drag'
                                                    ),
                                        ]),
                                    ]
                                )
                            ],
                    )
                ]),
                html.Div([
                    dbc.Button([
                        'Filter'
                    ],id="id_filtrar",className="btn-block mt-3")
                ], className="d-flex justify-content-end mb-3"),
                html.Div([
                    mapa_colombia_departamentos.display()  
                ],id="row_map")   
            ])],className="mb-3"
        ),

        

        dbc.Row(
            [dbc.Col([
                dbc.Card(
                    dbc.CardBody([
                        html.H3("Projects by department"),
                        html.Div([
                            tabla_datos_departamentos.display()
                        ],id="row_tabla")   
                    ])
                ),
            ]),
            dbc.Col([
                dbc.Card(
                    dbc.CardBody([
                        html.H3("Contract Types"),
                        dcc.Graph(
                            figure=contract_type_count_pie_chart
                        )
                    ])
                ),
            ])]
        ),
    ]
)  


@callback(
        [Output("row_map", 'children')], 
        [State("id_selector_municipio", "value"), 
         State("slider-updatemode","value"),
         Input("id_filtrar", "n_clicks"),
                
        ],prevent_initial_call=True
    )
def update_map(selector_municipio,selector_year,nclicks):
        mapa_colombia_departamentos = mapcol_departamentos('Number of projects by department in Colombia', 'div_municipios_fig2',df_maptest)
        df_filtrado = mapa_colombia_departamentos.df[mapa_colombia_departamentos.df['DEPARTAMENTO'].isin(selector_municipio)]
        #df_filtrado = df_filtrado[df_filtrado['COUNT']<(10**selector_year)]
        mapa_colombia_departamentos.df = df_filtrado
        nuevo_mapa = mapa_colombia_departamentos.display()
        #mapa_filtrado = mapcol_departamentos('Mapa Filtrado', 'id_filtrado', df_filtrado )
        #nuevo_mapa = mapa_filtrado.display()
        return [nuevo_mapa]
