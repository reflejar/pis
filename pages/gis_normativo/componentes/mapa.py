import json
from dash import dcc, html, Input, Output, callback
import dash_bootstrap_components as dbc

import plotly.graph_objects as go

from data import Data


Mapa = dcc.Graph(id="gis-resultados", className="mt-4")

@callback(
    Output("gis-resultados", "figure"), 
    [
        Input("select-municipio", "value"),
        Input("switches-recursos", "value"),
    ]
)
def update_bar_chart(municipio, recursos):
    maps = []
    
    for r in recursos:
        data = Data(r)
        fig = maps.append(data.make_map())
    
    fig = go.Figure(maps)

    fig.update_layout(
        mapbox_style="open-street-map",
        mapbox_zoom=2, 
        uirevision=True,
        height=800,
        coloraxis_showscale=False,
        margin={"r":0,"t":0,"l":0,"b":0}
    )


    return fig
