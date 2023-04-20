import dash_bootstrap_components as dbc
from dash import html

Orgas = html.Section([
            dbc.Row(dbc.Col([
                html.H4("Un proyecto de", className="text-uppercase mt-5 mb-4 text-black "),
                html.A(html.Img(src="/assets/img/orgas/der.png", height="80px", className="mb-5"), href="https://democraciaenred.org/", target="_blank"),
                html.Br(),
                html.H4("En alizanza con", className="text-uppercase mt-5 text-black "),
                dbc.Row([
                    dbc.Col(html.A(html.Img(src="/assets/img/orgas/amartya.png", height="130px", className="px-2"), href="https://www.amartya.org/ar/", target="_blank"), className="text-center"),
                    dbc.Col(html.A(html.Img(src="/assets/img/orgas/art41.png", height="130px", className="px-2"), href="https://articulo41.org/", target="_blank"), className="text-center"),
                    dbc.Col(html.A(html.Img(src="/assets/img/orgas/casaLobos.png", height="130px", className="px-2"), href="", target="_blank"), className="text-center"),
                    dbc.Col(html.A(html.Img(src="/assets/img/orgas/naturaleza.png", height="130px", className="px-2"), href="https://naturaleza.ar/", target="_blank"), className="text-center"),
                    dbc.Col(html.A(html.Img(src="/assets/img/orgas/reflejar.png", height="130px", className="px-2"), href="https://reflej.ar/", target="_blank"), className="text-center"),
                    dbc.Col(html.A(html.Img(src="/assets/img/orgas/simbiosis.png", height="130px", className="px-2"), href="https://simbiosis.cc/", target="_blank"), className="text-center"),
                ])
            ],
            md={'offset': 1, 'size': 10}
            ))
            ],
            className="min-vh-50 p-5 bg-white",
            id="index-orgas",
)
