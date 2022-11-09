import dash_bootstrap_components as dbc
from dash import html


CARD_STYLE = {
    'padding': '3rem',
    'background': '#FFFFFF',
    'box-shadow': '0px 7.52px 18.8px rgba(0, 0, 0, 0.25)',
    'border-radius': '10px',
}

Involucrate = html.Section(
    dbc.Container(
        [
            html.H2("Involucrate"),
            html.Div([
                dbc.Row(
                        [
                            dbc.Col(dbc.Card(
                                    dbc.CardBody(
                                        [
                                            html.Img(src="assets/img/involucrate/lab.png", width="80px", className="card-title mb-5"),
                                            html.H5("TESTEATE", className="card-subtitle"),
                                            html.P("¿donde puedo hacerme el test?", className="card-text"),
                                        ]
                                    ), style=CARD_STYLE
                                ), lg=4
                            ),
                            dbc.Col(dbc.Card(
                                    dbc.CardBody(
                                        [
                                            html.Img(src="assets/img/involucrate/salud.png", width="80px", className="card-title mb-5"),
                                            html.H5("ENVIANOS TUS RESULTADOS", className="card-subtitle"),
                                        ]
                                    ), style=CARD_STYLE
                                ), lg=4
                            ),             
                            dbc.Col(dbc.Card(
                                    dbc.CardBody(
                                        [
                                            html.Img(src="assets/img/involucrate/figuras.png", width="80px", className="card-title mb-5"),
                                            html.H5("COMPARTÍ RECURSOS", className="card-subtitle"),
                                        ]
                                    ), style=CARD_STYLE
                                ), lg=4
                            ),                                              
                        ]
                )                
            ], className="py-5")
        ],
        fluid=True,
        className="py-3 text-dark",
    ),
    className="text-center",
    id="involucrate"
)


