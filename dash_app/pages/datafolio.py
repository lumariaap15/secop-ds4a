from dash import dcc, html, callback, Input, Output, State
import dash_bootstrap_components as dbc


layout=  dbc.Container(
    [
        dbc.Card(
            [
                dbc.Row(
                    [
                        dbc.Col([
                            html.Div([
                                dbc.CardImg(
                                src='assets/DS4A_DATAFOLIO.jpg',
                            )
                            ])
                        ], align="center")
                    ])
            ])
    ])