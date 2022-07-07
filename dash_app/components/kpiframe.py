from dash import html 


import dash_bootstrap_components as dbc
from dash.dash_table import DataTable, FormatTemplate

class kpibadge:
    def __init__(self,kpi,label, badgetype):
        a = kpi.apply('{:,}'.format)
        if(badgetype!=''):
            a='$'+a
        self.kpi = a
        self.label = label
        self.badgetype = badgetype

    def display(self):
        
        layout = html.Div(
            [
             html.H5(self.label,className='card-title'),
             html.H2(self.kpi,className='d-flex justify-content-end'),
             html.Div(self.badgetype,className='d-flex justify-content-end'),
            ], className='m-2'
        )
        return layout