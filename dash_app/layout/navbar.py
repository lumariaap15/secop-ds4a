import dash_bootstrap_components as dbc
from dash import html

LOGO_INGES = "../assets/logo_inges.png"

navbar = dbc.Navbar(
    dbc.Container(
        [
            html.A(
                # Use row and col to control vertical alignment of logo / brand
                dbc.Row(
                    [
                        dbc.Col(html.Img(src=LOGO_INGES, width="150px")),
                    ],
                    align="center",
                    className="g-0",
                ),
                href="https://plotly.com",
                style={"textDecoration": "none"},
            ),
            html.Div(
                [
                    dbc.NavItem(dbc.NavLink("Dashboard", href="/")),
                    dbc.NavItem(dbc.NavLink("Predict", href="/predict")),
                    dbc.NavItem(dbc.NavLink("Model Luisa", href="/model-luisa"))
                ],
                style={"display": "flex"}
            ),
            
        ]
    ),
    color="white",
    dark=False,
)