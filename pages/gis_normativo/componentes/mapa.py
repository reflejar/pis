from dash import dcc, html, Input, Output, State, callback

import plotly.graph_objects as go

from data import MapHandler


MapaNormativo = dcc.Graph(id="gis-normativo", className="mt-4")


@callback(
    Output("gis-normativo", "figure"), 
    Output("loading-output", "children"),
    [
        Input("select-municipio", "value"),
        Input("switches-recursos", "value"),
        Input("radioitems-vista", "value"),
    ]
)
def update_map_layers(municipios, recursos, vista):
    mapa = MapHandler(municipios, recursos, vista)
    return mapa.render(), ''

