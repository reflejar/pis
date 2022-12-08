
from dash import html

import dash_bootstrap_components as dbc

from .componentes.hero import Hero
from .componentes.involucrate import Involucrate
from .componentes.gis import GIS

layout = html.Div(
        children=[
            Hero,
            GIS,
        ]
    )