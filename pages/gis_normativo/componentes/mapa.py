import json
from dash import dcc, html, Input, Output, callback
import dash_bootstrap_components as dbc

import plotly.graph_objects as go

from data import Mapa


MapaNormativo = dcc.Graph(id="gis-normativo", className="mt-4")

@callback(
    Output("gis-normativo", "figure"), 
    [
        Input("select-municipio", "value"),
        Input("switches-recursos", "value"),
    ]
)
def update_bar_chart(municipio, recursos):
    
    fig = go.Figure([Mapa(r).create() for r in recursos])

    fig.update_layout(
        mapbox_style="open-street-map",
        mapbox_zoom=6, 
        uirevision=True,
        height=800,
        coloraxis_showscale=False,
        margin={"r":0,"t":0,"l":0,"b":0},
        mapbox_center={"lat": -36.26, "lon": -60.23},
    )

    return fig
