import dash_bootstrap_components as dbc
from dash import html

LOGO_INGES = "../assets/logo_inges.png"
LOGO_DS4A = "../assets/COLOMBIA MAIN SANS TAG.svg"

navbar = dbc.Navbar(
    dbc.Container(
        [
            html.A(
                # Use row and col to control vertical alignment of logo / brand
                dbc.Row(
                    [
                        dbc.Col([
                            html.Img(src=LOGO_INGES, width="200px"),
                            #html.Img(src=LOGO_DS4A, width="150px")
                        ]),
                    ],
                    align="center",
                    className="g-0",
                ),
                href="/about",
                style={"textDecoration": "none"},
            ),          
        ], className="d-flex justify-content-center"
    ),
    color="white",
    dark=False,
)