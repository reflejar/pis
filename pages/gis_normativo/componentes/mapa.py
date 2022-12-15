import json
from dash import dcc, html, Input, Output, State, callback
import dash_bootstrap_components as dbc

import plotly.graph_objects as go

from data import MapHandler


MapaNormativo = dcc.Graph(id="gis-normativo", className="mt-4")

@callback(
    Output("gis-normativo", "figure"), 
    [
        Input("select-municipio", "value"),
        Input("switches-recursos", "value"),
        Input("radioitems-vista", "value"),
        State("gis-normativo", "figure"),
    ]
)
def update_map_layers(municipios, recursos, vista, anterior):
    mapa = MapHandler(municipios, recursos, vista, anterior)
    return mapa.render()