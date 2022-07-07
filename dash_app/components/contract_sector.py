from dataframes.df_general import df_test
from dash import html , dcc
import plotly.express as px
import plotly.graph_objects as go

class contract_sector:
    
    def __init__(self,sec_title:str, ID:str,df):
    
        self.sec_title = sec_title 
        self.id = ID
        self.df = df 
        
    @staticmethod
    def figura(self):
        
        fig = go.Figure(go.Bar( y=self.df.CANTIDAD,x=self.df.SECTOR))
        
        return fig

    def display(self):   
        layout = html.Div(
            [
                html.H4([self.sec_title]),
                html.Div([
                    dcc.Graph(id=self.id, figure=contract_sector.figura(self))
                ])

            ]
        )
        return layout