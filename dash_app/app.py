from click import style
import dash
import dash_bootstrap_components as dbc
from dash import Input, Output, dcc, html, State
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

SIDEBAR_HIDEN = {
    "position": "fixed",
    "top": 0,
    "left": "-19rem",
    "bottom": 0,
    "width": "300px",
    "padding": "2rem 1rem",
    "backgroundColor": "#F8F9F9",
    "marginTop": "50px",
    "display":"flex",
    "flexDirection":"column",
    "justifyContent": "space-between",
    "overflow-x": "hidden",
    "transition": "all 0.5s",
    "alignItems": "center",
    "boxShadow": "5px 5px 10px rgba(0,0,0,.05)"
}

CONTENT_STYLE = {
    "marginLeft": "300px",
    "marginRight": "2rem",
    "marginTop": "50px",
    "padding": "2rem 1rem",
}

CONTENT_STYLE1 = {
    "transition": "margin-left .5s",
    "marginLeft": "2rem",
    "marginRight": "2rem",
    "marginTop": "50px",
    "padding": "2rem 1rem",
}


content = html.Div([
    html.Div(id="page-content", style=CONTENT_STYLE),
    html.Div(className="all-content-background"),
    footer.footer
])

app.layout = html.Div([dcc.Store(id="side_click"),dcc.Location(id="url"), sidebar.sidebar, navbar.navbar, content])


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

@app.callback(
    [
        Output("sidebar", "style"),
        Output("page-content", "style"),
        Output("side_click", "data"),
    ],

    [Input("btn_sidebar", "n_clicks")],
    [
        State("side_click", "data"),
    ]
)
def toggle_sidebar(n, nclick):
    if n:
        if nclick == "SHOW":
            sidebar_style = SIDEBAR_HIDEN
            content_style = CONTENT_STYLE1
            cur_nclick = "HIDDEN"
        else:
            sidebar_style = SIDEBAR_STYLE
            content_style = CONTENT_STYLE
            cur_nclick = "SHOW"
    else:
        sidebar_style = SIDEBAR_STYLE
        content_style = CONTENT_STYLE
        cur_nclick = 'SHOW'

    return sidebar_style, content_style, cur_nclick

if __name__ == "__main__":
    app.run_server(host="0.0.0.0", port="8050", debug=False)