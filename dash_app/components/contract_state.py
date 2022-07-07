from dataframes.df_general import df_test
from dash import html , dcc
import plotly.express as px


class contract_state:
    
   
    def __init__(self,pie_title:str, ID:str,df):
    
        self.pie_title = pie_title 
        self.id = ID
        self.df = df 
        
    @staticmethod
    def figura(self):
        
        fig = px.pie(self.df, values='CANTIDAD', names='ESTADO')
        
        return fig

    def display(self):   
        layout = html.Div(
            [
                html.H4([self.pie_title]),
                html.Div([
                    dcc.Graph(id=self.id, figure=contract_state.figura(self))
                ])

            ]
        )
        return layout