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

###### SE IMPORTAN LAS BASES DE LOS OBJETOS REPRESENTADOS EN EL MAPA ##############
cuerpos=gpd.read_parquet("./data/cuerpos.parquet")
localidades_parajes=gpd.read_parquet("./data/localidades_parajes.parquet")
escuelas_parcelas=gpd.read_parquet("./data/escuelas_parcelas.parquet")
reservas=gpd.read_parquet("./data/reservas.parquet")
cursos=gpd.read_file("./data/cursos_agua.geojson")
cursos=cursos.reset_index()

###### SE IMPORTAN LAS BASES DE LAS ZONAS DE EXCLUSION Y AMORTIGUAMIENTO DE CADA OBJETO ############

cuerpos_excl=gpd.read_parquet("./data/cuerpos_excl.parquet")
cursos_excl=gpd.read_parquet("./data/cursos_excl.parquet")
localidades_excl=gpd.read_parquet("./data/localidades_excl.parquet")
parajes_excl=gpd.read_parquet("./data/parajes_excl.parquet")
escuelas_parcelas_excl=gpd.read_parquet("./data/escuelas_parcelas_excl.parquet")


localidades_amort=gpd.read_parquet("./data/localidades_amort.parquet")
parajes_amort=gpd.read_parquet("./data/parajes_excl.parquet")
escuelas_parcelas_amort=gpd.read_parquet("./data/escuelas_parcelas_amort.parquet")

################ Se crea una columna llamada "tooltip" que luego sirve como etiqueta en el mapa #############
################ se pasan las tablas a json #################################################################

cursos["tooltip"]="<b>Nombre</b>: "+cursos["NOMBRE"]+'<extra></extra>'
cursos["popup"]=cursos["tooltip"]

cursos_geojson=json.loads(cursos.to_json(na="keep"))


escuelas_parcelas["tooltip"]='<b>Nombre</b>: '+escuelas_parcelas["nombre.establecimiento"]+'<br>'+'<b>Nivel</b>: '+escuelas_parcelas["nivel"]+ '<br>'+'<b>Teléfono</b>: '+escuelas_parcelas["Tel"]+'<br>'+'<b>Email</b>: '+escuelas_parcelas["email"]+'<extra></extra>'
escuelas_parcelas["popup"]=escuelas_parcelas["tooltip"]
escuelas_parcelas_geojson=json.loads(escuelas_parcelas.to_json(na="keep"))

cuerpos["tooltip"]='<b>Nombre</b>: '+cuerpos["NOMBRE"]+'<br>'+'<b>Tipo</b>: '+cuerpos['TIPO']+'<extra></extra>'
cuerpos["popup"]=cuerpos["tooltip"]
cuerpos_geojson=json.loads(cuerpos.to_json(na="keep"))

reservas["tooltip"]="<b>Nombre</b>: "+reservas["Name"]
reservas["popup"]="<b>Nombre</b>: "+reservas["Name"]
reservas_geojson=json.loads(reservas.to_json(na="keep"))

localidades_parajes["tooltip"]='<b>Nombre</b>: '+localidades_parajes["Name"]+'<br>'+'<b>Habitantes</b>: '+localidades_parajes["Habitantes"]+'<extra></extra>'
localidades_parajes["popup"]=localidades_parajes["tooltip"]
localidades_parajes_geojson=json.loads(localidades_parajes.to_json(na="keep"))

cuerpos_excl["tooltip"]='<b>Zona de Exclusión</b> <br>'+'<extra></extra>'
cuerpos_excl_geojson = json.loads(cuerpos_excl.to_json(na="keep"))

cursos_excl["tooltip"]='<b>Zona de Exclusión</b> <br>'+'<extra></extra>'
cursos_excl_geojson = json.loads(cursos_excl.to_json(na="keep"))

localidades_excl["tooltip"]='<b>Zona de Exclusión</b> <br>'+'<extra></extra>'
localidades_excl_geojson = json.loads(localidades_excl.to_json(na="keep"))

parajes_excl["tooltip"]='<b>Zona de Exclusión</b> <br>'+'<extra></extra>'
parajes_excl_geojson = json.loads(parajes_excl.to_json(na="keep"))

escuelas_parcelas_excl["tooltip"]='<b>Zona de Exclusión</b> <br>'+'<extra></extra>'
escuelas_parcelas_excl_geojson = json.loads(escuelas_parcelas_excl.to_json(na="keep"))

localidades_amort["tooltip"]='<b>Zona de Amortiguamiento</b> <br>'+'<extra></extra>'
localidades_amort_geojson = json.loads(localidades_amort.to_json(na="keep"))

parajes_amort["tooltip"]='<b>Zona de Amortiguamiento</b> <br>'+'<extra></extra>'
parajes_amort_geojson = json.loads(parajes_amort.to_json(na="keep"))

escuelas_parcelas_amort["tooltip"]='<b>Zona de Amortiguamiento</b> <br>'+'<extra></extra>'
escuelas_parcelas_amort_geojson = json.loads(escuelas_parcelas_amort.to_json(na="keep"))


##################### se importan los json guardados en el paso anterior #################################################
geobuf_cursos = dlx.geojson_to_geobuf(cursos_geojson)
geobuf_localidades = dlx.geojson_to_geobuf(localidades_parajes_geojson)
geobuf_reservas = dlx.geojson_to_geobuf(reservas_geojson)
geobuf_cuerpos = dlx.geojson_to_geobuf(cuerpos_geojson)
geobuf_escuelas = dlx.geojson_to_geobuf(escuelas_parcelas_geojson)

geobuf_cursos_excl=dlx.geojson_to_geobuf(cursos_excl_geojson)
geobuf_cuerpos_excl=dlx.geojson_to_geobuf(cuerpos_excl_geojson)
geobuf_localidades_excl=dlx.geojson_to_geobuf(localidades_excl_geojson)
geobuf_parajes_excl=dlx.geojson_to_geobuf(parajes_excl_geojson)
geobuf_escuelas_parcelas_excl=dlx.geojson_to_geobuf(escuelas_parcelas_excl_geojson)

geobuf_localidades_amort=dlx.geojson_to_geobuf(localidades_amort_geojson)
geobuf_parajes_amort=dlx.geojson_to_geobuf(parajes_amort_geojson)
geobuf_escuelas_parcelas_amort=dlx.geojson_to_geobuf(escuelas_parcelas_amort_geojson)

###############################################################################################################################
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
                                              options=dict(onEachFeature=ns("on_each_feature"),style={"color":"#134dab","weight":1,"fillOpacity":0.5}))]), id="pane_cursos"),                                               
        dl.Pane(dl.LayerGroup([    dl.GeoJSON(data=geobuf_localidades, format='geobuf', zoomToBounds=True, zoomToBoundsOnClick=True,
                                              hoverStyle=arrow_function(hover_style),
                                              options=dict(onEachFeature=ns("on_each_feature"),style={"color":"purple","weight":1,"fillOpacity":0.5}))]), id="pane_localidades"),                                                                                             
        dl.Pane(dl.LayerGroup([    dl.GeoJSON(data=geobuf_cuerpos, format='geobuf', zoomToBounds=True, zoomToBoundsOnClick=True,
                                              hoverStyle=arrow_function(hover_style),
                                              options=dict(onEachFeature=ns("on_each_feature"),style={"color":"#134dab","weight":1,"fillOpacity":0.5}))]), id="pane_cuerpos"),                                               
        dl.Pane(dl.LayerGroup([    dl.GeoJSON(data=geobuf_reservas, format='geobuf', zoomToBounds=True, zoomToBoundsOnClick=True,
                                              hoverStyle=arrow_function(hover_style),
                                              options=dict(onEachFeature=ns("on_each_feature"),style={"color":"#06660b","weight":1,"fillOpacity":0.5}))]), id="pane_reservas"),                                               
        dl.Pane(dl.LayerGroup([    dl.GeoJSON(data=geobuf_escuelas, format='geobuf', zoomToBounds=True, zoomToBoundsOnClick=True,
                                              hoverStyle=arrow_function(hover_style),
                                               options=dict(onEachFeature=ns("on_each_feature"),style={"color":"#cfc817","weight":1,"fillOpacity":0.5}))]), id="pane_escuelas"),
        dl.Pane(dl.LayerGroup([    dl.GeoJSON(data=geobuf_localidades_amort, format='geobuf', zoomToBounds=True, zoomToBoundsOnClick=True,                       
                                              hoverStyle=arrow_function(hover_style),
                                              options=dict(onEachFeature=ns("on_each_feature"),style={"color":"#8c0d22","weight":1,"fillOpacity":0.5}))]), id="pane_localidades_amort"), 
        dl.Pane(dl.LayerGroup([    dl.GeoJSON(data=geobuf_parajes_amort, format='geobuf', zoomToBounds=True, zoomToBoundsOnClick=True,                       
                                              hoverStyle=arrow_function(hover_style),
                                              options=dict(onEachFeature=ns("on_each_feature"),style={"color":"#8c0d22","weight":1,"fillOpacity":0.5}))]), id="pane_parajes_amort"),
        dl.Pane(dl.LayerGroup([    dl.GeoJSON(data=geobuf_escuelas_parcelas_amort, format='geobuf', zoomToBounds=True, zoomToBoundsOnClick=True,                       
                                              hoverStyle=arrow_function(hover_style),
                                              options=dict(onEachFeature=ns("on_each_feature"),style={"color":"#8c0d22","weight":1,"fillOpacity":0.5}))]), id="pane_escuelas_parcelas_amort"),                                              
        dl.Pane(dl.LayerGroup([    dl.GeoJSON(data=geobuf_cursos_excl, format='geobuf', zoomToBounds=True, zoomToBoundsOnClick=True,
                                              hoverStyle=arrow_function(hover_style),
                                              options=dict(onEachFeature=ns("on_each_feature"),style={"color":"#8c0d22","weight":1,"fillOpacity":0.5}))]), id="pane_cursos_excl"), 
        dl.Pane(dl.LayerGroup([    dl.GeoJSON(data=geobuf_cuerpos_excl, format='geobuf', zoomToBounds=True, zoomToBoundsOnClick=True,
                                              hoverStyle=arrow_function(hover_style),
                                              options=dict(onEachFeature=ns("on_each_feature"),style={"color":"#8c0d22","weight":1,"fillOpacity":0.5}))]), id="pane_cuerpos_excl"),
        dl.Pane(dl.LayerGroup([    dl.GeoJSON(data=geobuf_localidades_excl, format='geobuf', zoomToBounds=True, zoomToBoundsOnClick=True,
                                              hoverStyle=arrow_function(hover_style),
                                              options=dict(onEachFeature=ns("on_each_feature"),style={"color":"#8c0d22","weight":1,"fillOpacity":0.5}))]), id="pane_localidades_excl"),
        dl.Pane(dl.LayerGroup([    dl.GeoJSON(data=geobuf_parajes_excl, format='geobuf', zoomToBounds=True, zoomToBoundsOnClick=True,
                                              hoverStyle=arrow_function(hover_style),
                                              options=dict(onEachFeature=ns("on_each_feature"),style={"color":"#8c0d22","weight":1,"fillOpacity":0.5}))]), id="pane_parajes_excl"),
        dl.Pane(dl.LayerGroup([    dl.GeoJSON(data=geobuf_escuelas_parcelas_excl, format='geobuf', zoomToBounds=True, zoomToBoundsOnClick=True,
                                              hoverStyle=arrow_function(hover_style),
                                              options=dict(onEachFeature=ns("on_each_feature"),style={"color":"#8c0d22","weight":1,"fillOpacity":0.5}))]), id="pane_escuelas_parcelas_excl"),                                                                                                                  
    ], style={'width': '1080px', 'height': '720px'}),

    ]
)



@callback(Output("pane_cursos", "style"), Input("toggle1", "on"))
def toggle1(on):
    return {"display": "block" if on else "none"}


@callback(Output("pane_localidades", "style"), Input("toggle2", "on"),)
def toggle2(on):
    return {"display": "block" if on else "none"}

@callback(
        [Output("pane_localidades_amort", "style"),
         Output("pane_parajes_amort", "style"),
         Output("pane_escuelas_parcelas_amort", "style")], 
         Input("toggle3", "on"),
         Input("toggle2", "on"),
         Input("toggle7", "on"),
        )
def toggle3(on, loc_on, esc_on):
    if on:
        return {"display": "block" if loc_on else "none"}, {"display": "block" if loc_on else "none"}, {"display": "block" if esc_on else "none"}
    else:
        return {"display": "none"}, {"display": "none"}, {"display": "none"}
    
@callback(
        [Output("pane_localidades_excl", "style"),
         Output("pane_parajes_excl", "style"),
         Output("pane_cursos_excl", "style"),
         Output("pane_cuerpos_excl", "style"),
         Output("pane_escuelas_parcelas_excl", "style")], 
         Input("toggle4", "on"),
         Input("toggle2", "on"),
         Input("toggle1", "on"),
         Input("toggle5", "on"),
         Input("toggle7", "on"),)
def toggle4(on, loc_on, cur_on, cue_on, esc_on ):
    if  on:
        return {"display": "block" if loc_on else "none"}, {"display": "block" if loc_on else "none"}, {"display": "block" if cur_on else "none"},{"display": "block" if cue_on else "none"}, {"display": "block" if esc_on else "none"}
    else: 
        return {"display": "none"}, {"display": "none"}, {"display": "none"},{"display": "none"}, {"display": "none"}
    
@callback(Output("pane_cuerpos", "style"), Input("toggle5", "on"))
def toggle5(on):
    return {"display": "block" if on else "none"}

@callback(Output("pane_reservas", "style"), Input("toggle6", "on"))
def toggle6(on):
    return {"display": "block" if on else "none"}

@callback(Output("pane_escuelas", "style"),Input("toggle7", "on"))
def toggle7(on):
    return {"display": "block" if on else "none"}


    


    
