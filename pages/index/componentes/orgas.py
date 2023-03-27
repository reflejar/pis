import dash_bootstrap_components as dbc
from dash import html

Orgas = html.Section([
            html.H4("Un proyecto de", className="text-uppercase my-5 text-black"),
            html.Img(src="/assets/img/orgas/der.png", height="100px"),
            html.H4("En alizanza con", className="text-uppercase my-5 text-black"),
            html.Div([
                html.Img(src="/assets/img/orgas/amartya.png", height="70px", className="px-5"),
                html.Img(src="/assets/img/orgas/naturaleza.png", height="70px", className="px-5"),
                html.Img(src="/assets/img/orgas/art-41.png", height="70px", className="px-5"),
                html.Img(src="/assets/img/orgas/casa-de-cultura.png", height="70px", className="px-5"),
                html.Img(src="/assets/img/orgas/reflejar.png", height="70px", className="px-5"),
                html.Img(src="/assets/img/orgas/simbiosis.png", height="70px", className="px-5"),
                ],
                className="d-flex"
            )
            ],
            className="p-5 bg-white",
            id="index-orgas",
)

# @callback(
#     Output("collapse", "is_open"),
#     [Input("collapse-button", "n_clicks")],
#     [State("collapse", "is_open")],
# )
# def toggle_collapse(n, is_open):
#     if n:
#         return not is_open
#     return is_open