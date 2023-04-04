import dash_bootstrap_components as dbc
from dash import html


Testeando = html.Section(
            dbc.Row([
                dbc.Col([
                    html.Img(src="/assets/img/recursos/tubo.svg", height="120px"),
                ],
                md=2, 
                class_name="mt-5 text-end"),
                dbc.Col([
                    html.H1("Testeando", className="text-black display-4 strong"),
                    html.H4("Estamos midiendo los niveles de agroquímicos en orina humana - Provincia de Buenos Aires", className="text-black"),
                    html.H4("En breve publicaremos los resultados.", className="text-black"),
                ],
                md=10,
                class_name="my-5 px-5"),
            ]),
            className="min-vh-50 d-flex justify-content-center align-items-center",
            id="index-testeando",
)
