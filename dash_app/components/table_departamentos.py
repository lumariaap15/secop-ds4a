

from dash import html 
from dash import dash_table
from dash.dash_table import  FormatTemplate
from dash.dash_table.Format import Format, Align

import dash_bootstrap_components as dbc


class table:
    def __init__(self,data, params):
        self.data = data
        self.params = params
        
    
    @staticmethod
    def columns(self):
        money = FormatTemplate.money(2)
        if self.params['columns']:
            columns = [{"name": i, "id": i, "type":'numeric', "format":'money'} for i in self.params['columns']]
          
        else:
            columns = [{"name": i, "id": i} for i in self.data.columns]
        
        columns = [{"name": "DEPARTAMENTO", "id": "DEPARTAMENTO"},
                   {"name": "CANTIDAD", "id": "CANTIDAD", "type":'numeric',"format":Format().group(True)},
                   {"name": "TOTAL", "id": "TOTAL", "type":'numeric', "format":money}]
                   
        return columns



    def display(self):
        layout=html.Div(id='table',
            children=[
                dbc.Row(
                [
                    dbc.Col(
                            [
                                html.Div(self.params['title'],className='card-title'),
                                html.P(self.params['description'],className='card-intro'),
                                dash_table.DataTable(
                                    id='table_users_data',
                                    page_size=7,
                                    columns=table.columns(self),
                                    data = self.data.to_dict('records'),
                                    filter_action="native",
                                    sort_action="native",
                                    style_cell_conditional=[
                                         {
                                             'if': {'column_id': c},
                                             'textAlign': 'center',
                                             'paddingLeft':'1em',
                                             'font-size': "0.7em",
                                             'font-family': "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Open Sans', 'Helvetica Neue', sans-serif",
                                    
                                         #} for c in self.params['columns']
                                        } for c in self.params['columns'] 
                                     ],
                                    style_data_conditional=[
                                        {
                                            'if': {'row_index': 'odd'},
                                            'backgroundColor': 'rgb(240, 240, 240)',
                                            
                                        }
                                    ],
                                    style_header={
                                        'backgroundColor': 'silver',
                                        'fontWeight': 'bold',
                                        'textTransform':'uppercase',
                                        'paddingLeft':'1em',
                                        'font-family': "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Open Sans', 'Helvetica Neue', sans-serif",
                                        'font-size': "0.8em",
                                        'text-align':'left'
                                    }
                                )
    
                            ]
                        ),

                ] 
                )
            ]

        )
        return layout



