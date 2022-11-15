
from dash import html

import dash_bootstrap_components as dbc

from .componentes.descripcion import Descripcion
from .componentes.filtros import Filtros
from .componentes.mapa import Mapa


layout = html.Div([
        dbc.Row([
            dbc.Col(html.Div(Filtros, className="anchor-top"), md=2),
            dbc.Col(html.Div(
                    html.Div(
                        children=[
                            html.Br(),
                            dbc.Row(dbc.Col(Descripcion)),
                            html.Hr(),
                            dbc.Row([
                                dbc.Col(Mapa, md=12),
                                ]),
                            html.Br(),
                    ]),
                    id='gis'
                ), md=9)
        ]),
        html.Hr(),
        ],
        className="my-5 min-vh-100",
    ) 