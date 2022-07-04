from dash import Input, Output, dcc, html
import dash_bootstrap_components as dbc

from dataframes.contratos_departamento import df_maptest

# the style arguments for the sidebar. We use position:fixed and a fixed width

SIDEBAR_STYLE = {
    "position": "fixed",
    "top": 0,
    "left": 0,
    "bottom": 0,
    "width": "300px",
    "padding": "2rem 1rem",
    "backgroundColor": "#F8F9F9",
    "marginTop": "50px"
}

sidebarTitle = html.Div(
    [
        html.P(
            "Public contracts delay classificator", className="sidebar-subtitle"
        ),
        html.H1("Colombian Public Contracting Analytics Dashboard")
    ]
)

sidebar = html.Div(
    [
        sidebarTitle,
        html.Hr()
    ],
    style=SIDEBAR_STYLE,
)

sidebar2 = html.Div(
    [
        sidebarTitle
    ],
    style=SIDEBAR_STYLE,
)