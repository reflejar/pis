
from dash import html

import dash_bootstrap_components as dbc

from .componentes.hero import Hero
from .componentes.que_es import QueEs
from .componentes.involucrate import Involucrate

layout = html.Div(
        children=[
            Hero,
            dbc.Container(
                [
                    # QueEs,
                    # html.Hr(),
                    Involucrate,
                ]
            )
        ]
    )