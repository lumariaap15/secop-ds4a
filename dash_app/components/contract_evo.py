from dataframes.df_general import df_test
from dash import html , dcc
import plotly.express as px


class contract_evo:
    
   
    def __init__(self,evo_title:str, ID:str,df):
    
        self.evo_title = evo_title 
        self.id = ID
        self.df = df 
        
    @staticmethod
    def figura(self):
        
        fig = px.line(self.df, x='FECHA', y='CANTIDAD')
        
        fig.update_xaxes(
            rangeslider_visible=True,
            rangeselector=dict(
                buttons=list([
                    dict(count=1, label="1m", step="month", stepmode="backward"),
                    dict(count=6, label="6m", step="month", stepmode="backward"),
                    dict(count=1, label="YTD", step="year", stepmode="todate"),
                    dict(count=1, label="1y", step="year", stepmode="backward"),
                    dict(step="all")
                ])
            )
        )
        
        return fig

    def display(self):   
        layout = html.Div(
            [
                html.H4([self.evo_title]),
                html.Div([
                    dcc.Graph(id=self.id, figure=contract_evo.figura(self))
                ])

            ]
        )
        return layout