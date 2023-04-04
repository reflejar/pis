import dash_bootstrap_components as dbc
from dash import html, callback, Input, Output, State

FAQs = html.Section([
            dbc.Row(dbc.Col([
                html.H1("FAQs", className="text-uppercase my-5 text-black space-grotesk"),
                dbc.Row([
                    dbc.Col([
                        html.H5([
                            html.Span("+",className="text-primary display-5"), "¿Qué significa PIS?"
                        ], className="text-dark pointer", n_clicks=0, id="faq-1"),
                        dbc.Collapse(
                            html.P("PIS es el acrónimo de PESTICIDAS INTRODUCIDOS SILENCIOSAMENTE"),
                            id="faq-1-collapse",
                            is_open=True,
                        ),
                        html.H5([
                            html.Span("+",className="text-primary display-5"), "¿Qué es PIS?"
                        ], className="text-dark pointer", n_clicks=0, id="faq-2"),
                        dbc.Collapse(
                            html.P("Pesticidas Introducidos Silenciosamente (PIS) es una serie de  herramientas , datos e información que  facilitan la  reducción  del impacto de los agroquímicos desde los territorios."),
                            id="faq-2-collapse",
                            is_open=True,
                        ),
                        html.H5([
                            html.Span("+",className="text-primary display-5"), "¿A quién está dirigido PIS?"
                        ], className="text-dark pointer", n_clicks=0, id="faq-3"),
                        dbc.Collapse(
                            html.P("En términos generales a todo el mundo pero específicamente está pensado para: comunidades afectadas, escuelas rurales, gobiernos locales, legisladores, productores agropecuarios, investigadoras/es, activistas, abogados con causas ambientalistas, etc."),
                            id="faq-3-collapse",
                            is_open=True,
                        ),                           
                    ], lg=4),
                    dbc.Col([
                        html.H5([
                            html.Span("+",className="text-primary display-5"), "¿Qué están haciendo?"
                        ], className="text-dark pointer", n_clicks=0, id="faq-4"),
                        dbc.Collapse(
                            html.Ul([
                                html.Li("Una campaña de testeos en humanos (Buenos Aires, Argentina)."),
                                html.Li("Un estudio científico  con los resultados de la campaña."),
                                html.Li("Un mapa con los resultados de varias campañas de testeos en humanos y ambientales."),
                                html.Li("Un repositorio con toda la jurisprudencia sobre la temática (Argentina)."),
                                html.Li("Análisis comparativo de las normas de regulación de agroquímicos de todos los municipios de PBA."),
                                html.Li("Sistematización  de toda la información local relevante de los últimos censos agropecuarios."),
                                html.Li("Una georreferenciación de la zonificación de aplicaciones de agroquímicos de algunos municipios."),
                            ]),
                            id="faq-4-collapse",
                            is_open=True,
                        ),
                        html.H5([
                            html.Span("+",className="text-primary display-5"), "¿Cómo me entero de los próximos lanzamientos?"
                        ], className="text-dark pointer", n_clicks=0, id="faq-5"),
                        dbc.Collapse(
                            html.P("Nos podés seguir en redes sociales y/o nos podés dejar  tu mail para que te mantengamos al tanto."),
                            id="faq-5-collapse",
                            is_open=True,
                        ),
                        html.H5([
                            html.Span("+",className="text-primary display-5"), "¿Necesitan más plata? ¿Para qué?"
                        ], className="text-dark pointer", n_clicks=0, id="faq-6"),
                        dbc.Collapse(
                            html.P("Si, Para terminar esta etapa y sobre todo para  que el proyecto crezca. Queremos llevar PIS ala siguiente etapa."),
                            id="faq-6-collapse",
                            is_open=True,
                        ),                           
                    ], lg=4),                    

                    dbc.Col([
                        html.H5([
                            html.Span("+",className="text-primary display-5"), "¿Cómo puedo donar?"
                        ], className="text-dark pointer", n_clicks=0, id="faq-7"),
                        dbc.Collapse(
                            html.A("Te dejamos acá un link para donaciones", href="https://donaronline.org/democracia-en-red/pis-dona-un-testeo-de-agroquimicos", target="_blank"),
                            id="faq-7-collapse",
                            is_open=True,
                        ),                      
                    ], lg=4),
                ])
            ],
            lg={'offset': 1, 'size':10}
            )),
            ],
            className="min-vh-50 p-5 bg-white",
            id="index-faqs",
)

@callback(
    Output("faq-1-collapse", "is_open"),
    [Input("faq-1", "n_clicks")],
    [State("faq-1-collapse", "is_open")],
)
def show(n_left, is_open):return not is_open

@callback(
    Output("faq-2-collapse", "is_open"),
    [Input("faq-2", "n_clicks")],
    [State("faq-2-collapse", "is_open")],
)
def show(n_left, is_open):return not is_open

@callback(
    Output("faq-3-collapse", "is_open"),
    [Input("faq-3", "n_clicks")],
    [State("faq-3-collapse", "is_open")],
)
def show(n_left, is_open):return not is_open

@callback(
    Output("faq-4-collapse", "is_open"),
    [Input("faq-4", "n_clicks")],
    [State("faq-4-collapse", "is_open")],
)
def show(n_left, is_open):return not is_open

@callback(
    Output("faq-5-collapse", "is_open"),
    [Input("faq-5", "n_clicks")],
    [State("faq-5-collapse", "is_open")],
)
def show(n_left, is_open):return not is_open

@callback(
    Output("faq-6-collapse", "is_open"),
    [Input("faq-6", "n_clicks")],
    [State("faq-6-collapse", "is_open")],
)
def show(n_left, is_open):return not is_open

@callback(
    Output("faq-7-collapse", "is_open"),
    [Input("faq-7", "n_clicks")],
    [State("faq-7-collapse", "is_open")],
)
def show(n_left, is_open):return not is_open