from dash import html
LOGO_DS4A = "/assets/COLOMBIA MAIN SANS TAG.svg"

footer = html.Div([
        html.Div([
            html.Div(html.A("About Us",href="#")),
            html.Div(html.A("Datafolio",href="#"))
        ], className="footer-links"),
        html.Div(html.Img(src=LOGO_DS4A, width="300px"))
    ],className="footer")