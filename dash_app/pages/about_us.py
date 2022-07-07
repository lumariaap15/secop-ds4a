from dash import dcc, html, callback, Input, Output, State
import dash_bootstrap_components as dbc

from components.card_intro import card_intro


card1 = card_intro('JUAN PABLO PEÑA','assets/img_jpp.jpg', 'Bsc. Civil Engineering','Digital Transformation ', '','Amateur Baseball Player')
card2 = card_intro('CARLOS SÁNCHEZ','assets/img_csa.jpg', 'Msc. Data Analitycs & Bsc. Industrial','Engineering ','Data Scientist', 'Crypto Enthusiast')
card3 = card_intro('WVEIMAR LÓPEZ','assets/img_wlo.jpg', 'Sp. Project Management & Bsc.','Informatics Engineering ','CEO Data Experts', 'Mountain Bike Practitioner')
card4 = card_intro('CESAR CARPETA','assets/img_cdc.jpg', 'MSc. Business Intelligence and BigData','& Bsc. Informatics Engineer ', 'BI Professional','Intermediate Tennis Player')
card5 = card_intro('VICTOR MARIO NOBLE','assets/img_vmn.jpg', 'Msc. Industrial Production Engineering &','Bsc. Industrial Engineering ','Assistant Professor', 'Prayer')
card6 = card_intro('CAMILO URIBE','assets/img_cur.jpg', 'Sp. Business Analitycs & Bsc. Petroleum','Engineering ','Field Engineer', 'Prayer')
card7 = card_intro('LUISA MARÍA ALZATE','assets/img_lma.jpg', 'BSc. Informatics Engineering','Full Stack Developer ','', 'Design Enthusiast')

layout=  dbc.Container(
    [
        dbc.Row(
            [
                dbc.Col([
                    html.H2([
                        "ABOUT TEAM 219"
                    ],className="text-white"),
                ], align="center")
            ]),
        dbc.Row(
            [
                dbc.Col([
                    html.Div([
                        "We think, design and build..."
                    ],className="text-white mb-3"),
                ], align="center")
            ]),
        dbc.Row(
            [
                dbc.Col([
                    html.Div([
                        card1.display()
                    ]),
                ]),
                dbc.Col([
                    html.Div([
                        card2.display()
                    ]),
                ])
            ]),
        dbc.Row(
            [
                dbc.Col([
                    html.Div([
                        card3.display()
                    ]),
                ]),
                dbc.Col([
                    html.Div([
                        card7.display()
                    ]),
                ])
            ]),
        dbc.Row(
            [
                dbc.Col([
                    html.Div([
                        card5.display()
                    ]),
                ]),
                dbc.Col([
                    html.Div([
                        card4.display()
                    ]),
                ])
            ]),
        dbc.Row(
            [
                dbc.Col([
                    html.Div([
                        card6.display()
                    ]),
                ])
            ])
    ]
)