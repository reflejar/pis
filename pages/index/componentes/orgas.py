import dash_bootstrap_components as dbc
from dash import html

Orgas = html.Section([
            html.H4("Un proyecto de", className="text-uppercase my-5 text-black "),
            html.A(html.Img(src="/assets/img/orgas/der.png", height="100px"), href="https://democraciaenred.org/", target="_blank"),
            html.H4("En alizanza con", className="text-uppercase my-5 text-black "),
            dbc.Row([
                dbc.Col(html.A(html.Img(src="/assets/img/orgas/amartya.png", height="70px", className="px-2"), href="https://www.amartya.org/ar/", target="_blank"), className="text-center my-3"),
                dbc.Col(html.A(html.Img(src="/assets/img/orgas/naturaleza.png", height="70px", className="px-2"), href="https://naturaleza.ar/", target="_blank"), className="text-center my-3"),
                dbc.Col(html.A(html.Img(src="/assets/img/orgas/art-41.png", height="70px", className="px-2"), href="https://articulo41.org/", target="_blank"), className="text-center my-3"),
                dbc.Col(html.A(html.Img(src="/assets/img/orgas/casa-de-cultura.png", height="70px", className="px-2"), href="", target="_blank"), className="text-center my-3"),
                dbc.Col(html.A(html.Img(src="/assets/img/orgas/reflejar.png", height="70px", className="px-2"), href="https://reflej.ar/", target="_blank"), className="text-center my-3"),
                dbc.Col(html.A(html.Img(src="/assets/img/orgas/simbiosis.png", height="70px", className="px-2"), href="https://simbiosis.cc/", target="_blank"), className="text-center my-3"),
            ])
            ],
            className="p-5 bg-white",
            id="index-orgas",
)
