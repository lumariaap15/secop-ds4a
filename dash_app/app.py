from click import style
import dash
import dash_bootstrap_components as dbc
from dash import Input, Output, dcc, html
from pages import maps
from pages import predict
from pages import dashboard
from pages import about_us
from layout import navbar
from layout import sidebar
from layout import footer
from pages import datafolio

app = dash.Dash(external_stylesheets=[dbc.themes.BOOTSTRAP])
app.config.suppress_callback_exceptions=True

# the styles for the main content position it to the right of the sidebar and
# add some padding.
CONTENT_STYLE = {
    "marginLeft": "300px",
    "marginRight": "2rem",
    "marginTop": "50px",
    "padding": "2rem 1rem",
}

content = html.Div([
    html.Div(id="page-content", style=CONTENT_STYLE),
    html.Div(className="all-content-background"),
    footer.footer
])

app.layout = html.Div([dcc.Location(id="url"), sidebar.sidebar, navbar.navbar, content])


@app.callback(Output("page-content", "children"), [Input("url", "pathname")])
def render_page_content(pathname):
    if pathname == "/map1":
        return maps.layout
    elif pathname == "/predict":
        return predict.layout
    elif pathname == "/":
        return dashboard.layout
    elif pathname == "/about":
        return about_us.layout
    elif pathname == "/datafolio":
        return datafolio.layout
    # If the user tries to reach a different page, return a 404 message
    return dbc.Jumbotron(
        [
            html.H1("404: Not found", className="text-danger"),
            html.Hr(),
            html.P(f"The pathname {pathname} was not recognised..."),
        ]
    )


if __name__ == "__main__":
    app.run_server(host="0.0.0.0", port="8050", debug=False)