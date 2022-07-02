from dash import Dash, dcc, html, Input, Output, State, callback
import dash_bootstrap_components as dbc

layout = html.Div(
    [
        html.Div(dcc.Input(id='input-on-submit', type='text')),
        dbc.Button(['Predict'],id="submit-val", className="btn-block mt-3", n_clicks=0),
        html.Br(),
        html.Br(),
        html.Div(id='container-button-basic', children='')
    ]
)

@callback(
    Output('container-button-basic', 'children'),
    Input('submit-val', 'n_clicks'),
    [State('input-on-submit', 'value')], prevent_initial_call=True
)
def update_output(n_clicks, value):
    return 'The delay prediction is "{}" day(s)'.format(value)