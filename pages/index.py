import dash
from dash import html
from .sections import (
    Hero,
    QueEs,
    Involucrate
)

dash.register_page(__name__, path='/')

layout = html.Div(children=[
    html.Div(
        children=[
            Hero,
            QueEs,
            Involucrate,
        ]
    )
])