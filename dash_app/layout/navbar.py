import dash_bootstrap_components as dbc
from dash import html

LOGO_INGES = "../assets/logo_inges.png"

"""
navbar = dbc.NavbarSimple(
    children=[
        html.Img(src=LOGO_INGES, height="30px"),
        dbc.NavItem(dbc.NavLink("Page 1", href="#")),
        dbc.DropdownMenu(
            children=[
                dbc.DropdownMenuItem("More pages", header=True),
                dbc.DropdownMenuItem("Page 2", href="#"),
                dbc.DropdownMenuItem("Page 3", href="#"),
            ],
            nav=True,
            in_navbar=True,
            label="More",
        ),
    ],
    color="light",
    dark=False,
)
"""

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
                    dbc.NavItem(dbc.NavLink("Dashboard", href="#")),
                    dbc.NavItem(dbc.NavLink("Models", href="#"))
                ],
                style={"display": "flex"}
            ),
            
        ]
    ),
    color="white",
    dark=False,
)