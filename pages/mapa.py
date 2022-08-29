import dash
from dash import html

dash.register_page(__name__)

layout = html.Div(children=[
    html.H1(children='El mapa que se va a mostrar'),
])