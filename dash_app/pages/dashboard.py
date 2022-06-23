### Import Packages ###
from dash import dcc
from dataframes.data import fig

### Import Dash Instance ###
#from app import app

### Page 1 Layout and Callback ###
layout = dcc.Graph(
        id='example-graph',
        figure=fig
    )