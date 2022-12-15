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
        State("gis-normativo", "figure")
    ]
)
def update_mapa(municipio, recursos, anterior):
    fig = go.Figure(anterior)
    
    # Si los recursos a mostrarse son menores a los ya existentes hay que borrar el que ya no se necesita
    if len(recursos) < len(fig.data):
        fig.data = [data for data in fig.data if data.name in recursos]
    # Y sino hay que agregar las capas que no existen aun
    else:
        capas_existentes = [data.name for data in fig.data]
        capas_a_realizar = [i for i in recursos if i not in capas_existentes]
        fig.add_traces([MapHandler(r).create() for r in capas_a_realizar])

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
