### Import Packages ###
from dash import dcc, html
from dataframes.data import fig, df2
import dash_bootstrap_components as dbc

### Import Dash Instance ###
#from app import app

### Page 1 Layout and Callback ###
graph = dcc.Graph(
        id='example-graph',
        figure=fig
    )

columns = []
for col in df2.columns:
    columns.append(html.P(col))

layout = html.Div([
    dbc.Card(
        dbc.CardBody([
            dbc.Row([
                dbc.Col(columns, width=3),
                dbc.Col([
                    graph
                ], width=12),
                dbc.Col([
                    graph
                ], width=6),
                dbc.Col([
                    graph
                ], width=6),
            ], align='center'), 
            html.Br(),
            dbc.Row([
                dbc.Col([
                    graph
                ], width=3),
                dbc.Col([
                    graph
                ], width=3),
                dbc.Col([
                    graph
                ], width=6),
            ], align='center'), 
            html.Br(),
            dbc.Row([
                dbc.Col([
                    graph
                ], width=9),
                dbc.Col([
                    graph
                ], width=3),
            ], align='center'),      
        ]), color = 'light'
    )
])