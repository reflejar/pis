from dash import dcc, html, Input, Output, State, callback, ctx
import plotly.graph_objects as go
import geopandas as gpd
import dash_leaflet.express as dlx
import json
from dash_extensions.javascript import arrow_function
from dash_extensions.javascript import Namespace
import dash_leaflet as dl

import pickle

from data import MapHandler

ns = Namespace("dash_props", "module")
# options=dict(onEachFeature=ns("on_each_feature"))

cuerpos=gpd.read_parquet("./data/cuerpos.parquet")
localidades_parajes=gpd.read_parquet("./data/localidades_parajes.parquet")
escuelas_parcelas=gpd.read_parquet("./data/escuelas_parcelas.parquet")
reservas=gpd.read_parquet("./data/reservas.parquet")

total_excl=gpd.read_parquet("./data/total_excl.parquet")
total_amort=gpd.read_parquet("./data/total_amort.parquet")


cursos=gpd.read_file("./data/cursos_agua.geojson")
cursos=cursos.reset_index()

cursos["tooltip"]="<b>Nombre</b>: "+cursos["NOMBRE"]+'<extra></extra>'
cursos["popup"]=cursos["tooltip"]

cursos_geojson=json.loads(cursos.to_json(na="keep"))


escuelas_parcelas["tooltip"]='<b>Nombre</b>: '+escuelas_parcelas["nombre.establecimiento"]+'<br>'+'<b>Nivel</b>: '+escuelas_parcelas["nivel"]+ '<br>'+'<b>Teléfono</b>: '+escuelas_parcelas["Tel"]+'<br>'+'<b>Email</b>: '+escuelas_parcelas["email"]+'<extra></extra>'
escuelas_parcelas["popup"]=escuelas_parcelas["tooltip"]
escuelas_parcelas_geojson=json.loads(escuelas_parcelas.to_json(na="keep"))

cuerpos["tooltip"]='<b>Nombre</b>: '+cuerpos["NOMBRE"]+'<br>'+'<b>Tipo</b>: '+cuerpos['TIPO']+'<extra></extra>'
cuerpos["popup"]=cuerpos["tooltip"]
cuerpos_geojson=json.loads(cuerpos.to_json(na="keep"))

total_excl["tooltip"]='<b>Zona de Exclusión</b> <br>'+'<extra></extra>'
total_excl_geojson=json.loads(total_excl.to_json(na="keep"))

total_amort["tooltip"]='<b>Zona de Amortiguamiento</b> <br>'+'<extra></extra>'
total_amort_geojson=json.loads(total_amort.to_json(na="keep"))

reservas["tooltip"]="<b>Nombre</b>: "+reservas["Name"]
reservas["popup"]="<b>Nombre</b>: "+reservas["Name"]
reservas_geojson=json.loads(reservas.to_json(na="keep"))

localidades_parajes["tooltip"]='<b>Nombre</b>: '+localidades_parajes["Name"]+'<br>'+'<b>Habitantes</b>: '+localidades_parajes["Habitantes"]+'<extra></extra>'
localidades_parajes["popup"]=localidades_parajes["tooltip"]
localidades_parajes_geojson=json.loads(localidades_parajes.to_json(na="keep"))

geobuf_cursos = dlx.geojson_to_geobuf(cursos_geojson)
geobuf_localidades = dlx.geojson_to_geobuf(localidades_parajes_geojson)
geobuf_amort = dlx.geojson_to_geobuf(total_amort_geojson)
geobuf_reservas = dlx.geojson_to_geobuf(reservas_geojson)
geobuf_excl = dlx.geojson_to_geobuf(total_excl_geojson)
geobuf_cuerpos = dlx.geojson_to_geobuf(cuerpos_geojson)
geobuf_escuelas = dlx.geojson_to_geobuf(escuelas_parcelas_geojson)

hover_style=dict(weight=3,fillOpacity=0.75)




MapaNormativo = html.Div(
    [
        html.Br(),
        html.Br(),
        dl.Map([
        dl.LayersControl(
            [
                dl.BaseLayer(
                    dl.TileLayer(),
                    name="OpenStreetMaps",
                    checked=True,
                ),
                dl.BaseLayer(
                    dl.TileLayer(
                        url="https://server.arcgisonline.com/ArcGIS/rest/services/World_Imagery/MapServer/tile/{z}/{y}/{x}",
                        attribution="Tiles &copy; Esri &mdash; Source: Esri, i-cubed, USDA, USGS, AEX, GeoEye, Getmapping, Aerogrid, IGN, IGP, UPR-EGP, and the GIS User Community",
                        maxZoom=17
                    ),
                    name="Satelite",
                    checked=False,
                ),
            ],
        ),
        dl.Pane(dl.LayerGroup([dl.GeoJSON(data=geobuf_cursos, format='geobuf', zoomToBounds=True, zoomToBoundsOnClick=True,
                                              hoverStyle=arrow_function(hover_style),
                                              options=dict(onEachFeature=ns("on_each_feature"),style={"color":"#134dab","weight":1,"fillOpacity":0.5}))]), id="pane1"),                                               
        dl.Pane(dl.LayerGroup([    dl.GeoJSON(data=geobuf_localidades, format='geobuf', zoomToBounds=True, zoomToBoundsOnClick=True,
                                              hoverStyle=arrow_function(hover_style),
                                              options=dict(onEachFeature=ns("on_each_feature"),style={"color":"purple","weight":1,"fillOpacity":0.5}))]), id="pane2"),                                               
        dl.Pane(dl.LayerGroup([    dl.GeoJSON(data=geobuf_amort, format='geobuf', zoomToBounds=True, zoomToBoundsOnClick=True,                       
                                              hoverStyle=arrow_function(hover_style),
                                              options=dict(onEachFeature=ns("on_each_feature"),style={"color":"#8c0d22","weight":1,"fillOpacity":0.5}))]), id="pane3"),                                               
        dl.Pane(dl.LayerGroup([    dl.GeoJSON(data=geobuf_excl, format='geobuf', zoomToBounds=True, zoomToBoundsOnClick=True,
                                              hoverStyle=arrow_function(hover_style),
                                              options=dict(onEachFeature=ns("on_each_feature"),style={"color":"#8c0d22","weight":1,"fillOpacity":0.5}))]), id="pane4"),                                               
        dl.Pane(dl.LayerGroup([    dl.GeoJSON(data=geobuf_cuerpos, format='geobuf', zoomToBounds=True, zoomToBoundsOnClick=True,
                                              hoverStyle=arrow_function(hover_style),
                                              options=dict(onEachFeature=ns("on_each_feature"),style={"color":"#134dab","weight":1,"fillOpacity":0.5}))]), id="pane5"),                                               
        dl.Pane(dl.LayerGroup([    dl.GeoJSON(data=geobuf_reservas, format='geobuf', zoomToBounds=True, zoomToBoundsOnClick=True,
                                              hoverStyle=arrow_function(hover_style),
                                              options=dict(onEachFeature=ns("on_each_feature"),style={"color":"#06660b","weight":1,"fillOpacity":0.5}))]), id="pane6"),                                               
        dl.Pane(dl.LayerGroup([    dl.GeoJSON(data=geobuf_escuelas, format='geobuf', zoomToBounds=True, zoomToBoundsOnClick=True,
                                              hoverStyle=arrow_function(hover_style),
                                               options=dict(onEachFeature=ns("on_each_feature"),style={"color":"#cfc817","weight":1,"fillOpacity":0.5}))]), id="pane7"),
    ], style={'width': '1080px', 'height': '720px'}),

    ]
)



@callback(Output("pane1", "style"), Input("toggle1", "on"))
def toggle1(on):
    return {"display": "block" if on else "none"}


@callback(Output("pane2", "style"), Input("toggle2", "on"))
def toggle2(on):
    return {"display": "block" if on else "none"}

@callback(Output("pane3", "style"), Input("toggle3", "on"))
def toggle3(on):
    return {"display": "block" if on else "none"}

@callback(Output("pane4", "style"), Input("toggle4", "on"))
def toggle4(on):
    return {"display": "block" if on else "none"}

@callback(Output("pane5", "style"), Input("toggle5", "on"))
def toggle5(on):
    return {"display": "block" if on else "none"}

@callback(Output("pane6", "style"), Input("toggle6", "on"))
def toggle6(on):
    return {"display": "block" if on else "none"}

@callback(Output("pane7", "style"), Input("toggle7", "on"))
def toggle7(on):
    return {"display": "block" if on else "none"}


