
from dash import html

import dash_bootstrap_components as dbc

from .componentes.hero import Hero
from .componentes.productos import (
    GisNormativo, GisResultados
)

layout = html.Div(
        children=[
            Hero,
            GisNormativo,
            GisResultados,
        ]
    )