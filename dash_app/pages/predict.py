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
    prediction = XGBoost_predict(value)
    return 'The delay prediction for {} is "{}"'.format(value, prediction['Delay prediction'])

def prepare_model_data(x_variables):
    return x_variables

def load_model():
    model = open('model.pkl', 'rb')
    return joblib.load(model)

def XGBoost_predict(x_variables):

    prepared_data = prepare_model_data(x_variables)
    #prediction = load_model().predict(prepared_data)
    return {'Delay prediction': 'No'}