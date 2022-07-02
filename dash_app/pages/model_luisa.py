from dash import dcc, html
import dash_bootstrap_components as dbc

from dataframes.data import df2


departamentos_options = []
for item in df2["Departamento"].unique():
    departamentos_options.append({"label": item, "value": item})
departamentos_select = html.Div(
    [
        dbc.Label("Departamento", html_for="departamento"),
        dcc.Dropdown(
            id="departamento",
            options=departamentos_options,
        ),
    ],
    className="mb-3",
)

orden_options = []
for item in df2["Orden"].unique():
    orden_options.append({"label": item, "value": item})
orden_select = html.Div(
    [
        dbc.Label("Orden", html_for="orden"),
        dcc.Dropdown(
            id="orden",
            options=orden_options,
        ),
    ],
    className="mb-3",
)

sector_options = []
for item in df2["Sector"].unique():
    sector_options.append({"label": item, "value": item})
sector_select = html.Div(
    [
        dbc.Label("Sector", html_for="sector"),
        dcc.Dropdown(
            id="sector",
            options=sector_options,
        ),
    ],
    className="mb-3",
)

rama_options = []
for item in df2["Rama"].unique():
    rama_options.append({"label": item, "value": item})
rama_select = html.Div(
    [
        dbc.Label("Rama", html_for="rama"),
        dcc.Dropdown(
            id="rama",
            options=sector_options,
        ),
    ],
    className="mb-3",
)



email_input = html.Div(
    [
        dbc.Label("Email", html_for="example-email"),
        dbc.Input(type="email", id="example-email", placeholder="Enter email")
    ],
    className="mb-3",
)

password_input = html.Div(
    [
        dbc.Label("Password", html_for="example-password"),
        dbc.Input(
            type="password",
            id="example-password",
            placeholder="Enter password",
        )
    ],
    className="mb-3",
)

form = dbc.Form([
    departamentos_select, 
    orden_select, 
    sector_select, 
    rama_select, 
    email_input, 
    password_input
])

layout = html.Div([
    html.H3("Contracts Delay Classificator"),
    dbc.Card([form], className="p-3"),
])