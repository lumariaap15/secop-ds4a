
from dash import html , dcc, callback, Input, Output, State
import dash_bootstrap_components as dbc

from components.mapcol_departamentos import mapcol_departamentos


from dataframes.contratos_departamento import df_maptest
from components.table_departamentos import table


mapa_colombia_departamentos = mapcol_departamentos('Cantidad de proyectos por departamento en Colombia', 'div_municipios_fig2',df_maptest)


params1 = {
            'title': '', 
            'description': 'Lista de departamentos  (Los valores de la columna TOTAL estan en miles de millones)',
            'columns': [ 'DEPARTAMENTO',  'CANTIDAD', 'TOTAL']
}
tabla_datos_departamentos = table(df_maptest,params1)


info = {}
content = [{"label": "TODOS", "value": "TODOS"}]
for iframe in df_maptest.DEPARTAMENTO:
    info = { 'label': iframe , 'value': iframe}
    content.append(info)      


layout= html.Div(
    [
        dbc.Card(
            [dbc.CardBody([
                html.Div([
                    mapa_colombia_departamentos.display()  
                ],id="row_map")   
            ])],className="mb-3"
        ),

        dbc.Card(
            dbc.CardBody([
                html.H3("Proyectos por departamento"),
                html.Div([
                    tabla_datos_departamentos.display()
                ],id="row_tabla")   
            ])
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
        df_filtrado = mapa_colombia_departamentos.df[mapa_colombia_departamentos.df['DEPARTAMENTO'].isin(selector_municipio)]
        #df_filtrado = df_filtrado[df_filtrado['COUNT']<(10**selector_year)]
        mapa_colombia_departamentos.df = df_filtrado
        nuevo_mapa = mapa_colombia_departamentos.display()
        #mapa_filtrado = mapcol_departamentos('Mapa Filtrado', 'id_filtrado', df_filtrado )
        #nuevo_mapa = mapa_filtrado.display()
        return [nuevo_mapa]
