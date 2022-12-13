
from dash import html

import dash_bootstrap_components as dbc

from .componentes.filtros import Filtros
from .componentes.mapa import Mapa


layout = html.Div([
        dbc.Row([
            dbc.Col(html.Div(Filtros, className="anchor-top"), md=4),
            dbc.Col(Mapa, md=8)
        ]),
        html.Hr(),
        ],
        className="my-5 min-vh-100",
    ) 