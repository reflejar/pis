import dash_bootstrap_components as dbc
from dash import html


top_card = dbc.Card(
    [
        dbc.CardImg(src="/images/lab.png", top=True),
        dbc.CardBody(
            [
                html.I(className="bi bi-info-circle-fill me-2 card-title"),
                html.H4("Testeate", className="card-title"),
                html.H6("¿donde puedo hacerme el test?", className="card-subtitle"),
            ]
        ),
    ],

)

bottom_card = dbc.Card(
    [
        dbc.CardImg(src="/images/lab.png", bottom=True),
        dbc.CardBody(
            [
                html.I(className="bi bi-info-circle-fill me-2 card-title"),
                html.H4("Testeate", className="card-title"),
                html.H6("¿donde puedo hacerme el test?", className="card-subtitle"),
            ]
        ),        
    ],
)

cards = dbc.Row(
    [
        dbc.Col(top_card, width=4),
        dbc.Col(bottom_card, width=4),
        dbc.Col(bottom_card, width=4),
    ]
)


Involucrate = html.Section(
    dbc.Container(
        [
            html.H2("Involucrate"),
            cards
        ],
        fluid=True,
        className="py-3 text-dark",
    ),
    className="text-center",
    id="involucrate"
)


