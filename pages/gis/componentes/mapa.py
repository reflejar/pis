import json
from dash import dcc, html, Input, Output, callback
import dash_bootstrap_components as dbc

import plotly.graph_objects as go

from data.gis import DF_CUERPOS, DF_CURSOS_AGUA, DF_ESCUELAS


Mapa = dbc.Card(dbc.CardBody(dcc.Graph(id="gis-mapa")))

@callback(
    Output("gis-mapa", "figure"), 
    [
        Input("select-municipio", "value"),
        Input("select-recurso", "value"),
    ]
)
def update_bar_chart(municipio, recursos):
    
    sel_municipio = [c for c in municipio if c != '']
    sel_recurso = [c for c in recursos if c != '']
    print(municipio)

    df = DF_CUERPOS.copy()
    df['color'] = 1
    df_json = json.loads(DF_CUERPOS.to_json(na="keep"))

    fig = go.Figure(
        go.Choroplethmapbox(
            geojson=df_json, 
            featureidkey="properties.index",
            locations=df['index'], 
            z=df['color'],
            colorscale="YlGnBu", 
            marker_opacity=1,
            marker_line_width=0.1,
        )
    )

    fig.update_layout(
        mapbox_style="open-street-map", #open-street-map, carto-positron
        mapbox_zoom=2, 
        uirevision= True,
        height=800
    )
    fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0})

    fig.data[0].colorbar.x=0



    return fig
