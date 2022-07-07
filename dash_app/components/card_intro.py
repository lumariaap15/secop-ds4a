import dash_bootstrap_components as dbc
from dash import html


class card_intro:
    def __init__(self,title,url_image,label1,label2,label3, desc_small):
        self.title = title
        self.url_image = url_image
        self.label1 = label1
        self.label2 = label2
        self.label3 = label3
        self.desc_small = desc_small
        
    def display(self):
        
        
        layout = dbc.Card(
            [
                dbc.Row(
                    [
                        dbc.Col(
                            dbc.CardImg(
                                src=self.url_image ,
                                className="img-fluid rounded-start",
                            ),
                            className="col-md-4",
                        ),
                        dbc.Col(
                            dbc.CardBody(
                                [
                                    html.H4(self.title, className="card-title"),
                                    html.P(
                                        [self.label1,
                                         html.Br(),
                                        self.label2,
                                         html.Br(),
                                        self.label3],
                                        className="card-text",
                                    ),
                                    html.Small(
                                        self.desc_small,
                                        className="card-text text-muted",
                                    ),
                                ]
                            ),
                            className="col-md-8",
                        ),
                    ],
                    className="g-0 d-flex align-items-center",
                )
            ],
            className="mb-3",
            style={"maxWidth": "540px"},
        )
        return layout