from dash import Input, Output, dcc, html
import dash_bootstrap_components as dbc

from dataframes.contratos_departamento import df_maptest

LOGO_DS4A = "../assets/Asset 5.svg"

# the style arguments for the sidebar. We use position:fixed and a fixed width

SIDEBAR_STYLE = {
    "position": "fixed",
    "top": 0,
    "left": 0,
    "bottom": 0,
    "width": "300px",
    "padding": "2rem 1rem",
    "backgroundColor": "#F8F9F9",
    "marginTop": "50px",
    "display":"flex",
    "flexDirection":"column",
    "justifyContent": "space-between",
    "alignItems": "center",
    "boxShadow": "5px 5px 10px rgba(0,0,0,.05)"
}

sidebarTitle = html.Div(
    [
        html.P(
            "Team 219", className="sidebar-subtitle"
        ),
        html.H1(["Public Contracts Delay Classificator"],style={"fontSize":"30px"})
    ]
)

sidebar = html.Div(
    [
        html.Div([
            sidebarTitle,
            html.Hr(),
            dbc.Nav(
                [
                    dbc.NavLink("Dashboard", href="/", active="exact"),
                    dbc.NavLink("Maps", href="/map1", active="exact"),
                    dbc.NavLink("Predict", href="/predict", active="exact")
                ],
                vertical=True,
                pills=True,
            ),
        ]),
        html.Div([html.Img(src=LOGO_DS4A, width="150px")])
    ],
    id="sidebar",
    style=SIDEBAR_STYLE,
)
