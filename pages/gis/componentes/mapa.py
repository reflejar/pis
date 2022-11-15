import json
from dash import dcc, html, Input, Output, callback
import dash_bootstrap_components as dbc
from dash_loading_spinners import Hash

import plotly.graph_objects as go

from data.estatal import estatal

var_municipio = 'PAIS'
var_fem = 'FEMINICIDIOS'
var_recurso = 'PERIODO'
var_fuente = 'TIPO DE RECURSO'


##### BASE DE DATOS ######

# Datos estatales: solo aquellos que tienen su contraparte territorial
df_general = estatal.copy()


Mapa = dbc.Card(
    [  
        dbc.CardBody(
            Hash(
                dcc.Graph(id="mapa"),
                color="#FFA929",
                size=20,
            )
            
        )
    ],
    color="light", 
    outline=True,
    class_name="shadow",
    id="gis-mapa"    
)

@callback(
    Output("mapa", "figure"), 
    [
        Input("select-municipio", "value"),
        Input("select-recurso", "value"),
    ]
)
def update_bar_chart(municipio, recursos, ):
    
    sel_municipio = [c for c in municipio if c != '']
    sel_recurso = [c for c in recursos if c != '']

    with open('data/custom.geo.json', encoding='utf-8') as response:
        municipio = json.load(response)


    df = df_general.copy()
    if len(sel_municipio) >0:
        mask = df[var_municipio].isin(sel_municipio)
        df = df[mask]
    if len(sel_recurso) >0:
        mask = df[var_recurso].isin(sel_recurso)
        df = df[mask]


    fig = go.Figure(
        go.Choroplethmapbox(
            geojson=municipio, 
            featureidkey="properties.name_es",
            locations=df[var_municipio], 
            z=df[var_fem],
            colorscale="Purp", 
            marker_opacity=1,
            marker_line_width=0.1,
        )
    )

    fig.update_layout(
        mapbox_style="open-street-map", #open-street-map, carto-positron
        mapbox_zoom=2, 
        mapbox_center = {"lat": -10.9342, "lon": -75.9430},
        height=600
    )
    fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0})

    fig.data[0].colorbar.x=0



    return fig
