import dash_leaflet.express as dlx
import dash_leaflet as dl

from dash import  html, Input, Output, callback
from dash_extensions.javascript import arrow_function
from dash_extensions.javascript import Namespace

from ._data import (
    cursos_geojson,
    escuelas_parcelas_geojson,
    cuerpos_geojson,
    reservas_geojson,
    localidades_parajes_geojson,
    cuerpos_excl_geojson,
    cursos_excl_geojson,
    localidades_excl_geojson,
    parajes_excl_geojson,
    escuelas_parcelas_excl_geojson,
    localidades_amort_geojson,
    parajes_amort_geojson,
    escuelas_parcelas_amort_geojson,
)

###### Constantes ###########
HOVER_STYLE=dict(weight=3,fillOpacity=0.75)
ns = Namespace("dash_props", "module")



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

            dl.Pane(
                dl.LayerGroup([
                    dl.GeoJSON(
                        data=dlx.geojson_to_geobuf(localidades_amort_geojson), 
                        format='geobuf', 
                        zoomToBounds=True, 
                        zoomToBoundsOnClick=True,                       
                        hoverStyle=arrow_function(HOVER_STYLE),
                        options=dict(onEachFeature=ns("on_each_feature"),
                        style={"color":"#8c0d22","weight":2,"fillOpacity":0.3}))
                ]), 
                id="pane_localidades_amort"
            ), 
            dl.Pane(
                dl.LayerGroup([
                    dl.GeoJSON(
                        data=dlx.geojson_to_geobuf(parajes_amort_geojson), 
                        format='geobuf', 
                        zoomToBounds=True, 
                        zoomToBoundsOnClick=True,                       
                        hoverStyle=arrow_function(HOVER_STYLE),
                        options=dict(onEachFeature=ns("on_each_feature"),
                        style={"color":"#8c0d22","weight":2,"fillOpacity":0.3}))
                ]), 
                id="pane_parajes_amort"
            ),
            dl.Pane(
                dl.LayerGroup([
                    dl.GeoJSON(
                        data=dlx.geojson_to_geobuf(escuelas_parcelas_amort_geojson), 
                        format='geobuf', 
                        zoomToBounds=True, 
                        zoomToBoundsOnClick=True,                       
                        hoverStyle=arrow_function(HOVER_STYLE),
                        options=dict(onEachFeature=ns("on_each_feature"),
                        style={"color":"#8c0d22","weight":2,"fillOpacity":0.3}))
                ]), 
                id="pane_escuelas_parcelas_amort"
            ),                                              
            dl.Pane(
                dl.LayerGroup([
                    dl.GeoJSON(
                        data=dlx.geojson_to_geobuf(cursos_excl_geojson), 
                        format='geobuf', 
                        zoomToBounds=True, 
                        zoomToBoundsOnClick=True,
                        hoverStyle=arrow_function(HOVER_STYLE),
                        options=dict(onEachFeature=ns("on_each_feature"),
                        style={"color":"#8c0d22","weight":2,"fillOpacity":0.3}))
                ]), 
                id="pane_cursos_excl"
            ), 
            dl.Pane(
                dl.LayerGroup([
                    dl.GeoJSON(
                        data=dlx.geojson_to_geobuf(cuerpos_excl_geojson), 
                        format='geobuf', 
                        zoomToBounds=True, 
                        zoomToBoundsOnClick=True,
                        hoverStyle=arrow_function(HOVER_STYLE),
                        options=dict(onEachFeature=ns("on_each_feature"),
                        style={"color":"#8c0d22","weight":2,"fillOpacity":0.3}))
                ]), 
                id="pane_cuerpos_excl"
            ),
            dl.Pane(
                dl.LayerGroup([
                    dl.GeoJSON(
                        data=dlx.geojson_to_geobuf(localidades_excl_geojson), 
                        format='geobuf', 
                        zoomToBounds=True, 
                        zoomToBoundsOnClick=True,
                        hoverStyle=arrow_function(HOVER_STYLE),
                        options=dict(onEachFeature=ns("on_each_feature"),
                        style={"color":"#8c0d22","weight":2,"fillOpacity":0.3}))
                ]), 
                id="pane_localidades_excl"
            ),
            dl.Pane(
                dl.LayerGroup([
                    dl.GeoJSON(
                        data=dlx.geojson_to_geobuf(parajes_excl_geojson), 
                        format='geobuf', 
                        zoomToBounds=True, 
                        zoomToBoundsOnClick=True,
                        hoverStyle=arrow_function(HOVER_STYLE),
                        options=dict(onEachFeature=ns("on_each_feature"),
                        style={"color":"#8c0d22","weight":2,"fillOpacity":0.3}))
                ]), 
                id="pane_parajes_excl"
            ),
            dl.Pane(
                dl.LayerGroup([
                    dl.GeoJSON(
                        data=dlx.geojson_to_geobuf(escuelas_parcelas_excl_geojson), 
                        format='geobuf', 
                        zoomToBounds=True, 
                        zoomToBoundsOnClick=True,
                        hoverStyle=arrow_function(HOVER_STYLE),
                        options=dict(onEachFeature=ns("on_each_feature"),
                        style={"color":"#8c0d22","weight":2,"fillOpacity":0.3}))
                ]), 
                id="pane_escuelas_parcelas_excl"
            ),
            dl.Pane(
                dl.LayerGroup([
                    dl.GeoJSON(
                        data=dlx.geojson_to_geobuf(cursos_geojson), 
                        format='geobuf', 
                        zoomToBounds=True, 
                        zoomToBoundsOnClick=True,
                        hoverStyle=arrow_function(HOVER_STYLE),
                        options=dict(onEachFeature=ns("on_each_feature"),
                        style={"color":"#134dab","weight":2,"fillOpacity":0.3}))
                ]), 
                id="pane_cursos"
            ),
            dl.Pane(
                dl.LayerGroup([
                    dl.GeoJSON(
                        data=dlx.geojson_to_geobuf(cuerpos_geojson), 
                        format='geobuf', 
                        zoomToBounds=True, 
                        zoomToBoundsOnClick=True,
                        hoverStyle=arrow_function(HOVER_STYLE),
                        options=dict(onEachFeature=ns("on_each_feature"),
                        style={"color":"#134dab","weight":2,"fillOpacity":0.3}))
                ]),
                id="pane_cuerpos"
            ),            
            dl.Pane(
                dl.LayerGroup([
                    dl.GeoJSON(
                        data=dlx.geojson_to_geobuf(localidades_parajes_geojson), 
                        format='geobuf', 
                        zoomToBounds=True, 
                        zoomToBoundsOnClick=True,
                        hoverStyle=arrow_function(HOVER_STYLE),
                        options=dict(onEachFeature=ns("on_each_feature"),
                        style={"color":"purple","weight":2,"fillOpacity":0.4}))
                ]), 
                id="pane_localidades"
            ),
            dl.Pane(
                dl.LayerGroup([
                    dl.GeoJSON(
                        data=dlx.geojson_to_geobuf(reservas_geojson), 
                        format='geobuf', 
                        zoomToBoundsOnClick=True,
                        hoverStyle=arrow_function(HOVER_STYLE),
                        options=dict(onEachFeature=ns("on_each_feature"),
                        style={"color":"#06660b","weight":2,"fillOpacity":0.3}))
                ]), 
                id="pane_reservas"),
            dl.Pane(
                dl.LayerGroup([
                    dl.GeoJSON(
                        data=dlx.geojson_to_geobuf(escuelas_parcelas_geojson), 
                        format='geobuf', 
                        zoomToBounds=True, 
                        zoomToBoundsOnClick=True,
                        hoverStyle=arrow_function(HOVER_STYLE),
                        options=dict(onEachFeature=ns("on_each_feature"),
                        style={"color":"#cfc817","weight":3,"fillOpacity":0.4}))
                ]), 
                id="pane_escuelas"
            ),            
        ], 
        style={'width': '1080px', 'height': '720px'},
        className="mt-3"
        ),
    ]
)



@callback(Output("pane_cursos", "style"), Input("toggle_cursos", "on"))
def toggle_cursos(on): return {"display": "block" if on else "none"}

@callback(Output("pane_localidades", "style"), Input("toggle_localidades", "on"),)
def toggle_localidades(on): return {"display": "block" if on else "none"}
    
@callback(Output("pane_cuerpos", "style"), Input("toggle_cuerpos", "on"))
def toggle_cuerpos(on): return {"display": "block" if on else "none"}

@callback(Output("pane_reservas", "style"), Input("toggle_reservas", "on"))
def toggle_reservas(on): return {"display": "block" if on else "none"}

@callback(Output("pane_escuelas", "style"),Input("toggle_escuelas", "on"))
def toggle_escuelas(on): return {"display": "block" if on else "none"}


@callback(
        [Output("pane_localidades_amort", "style"),
         Output("pane_parajes_amort", "style"),
         Output("pane_escuelas_parcelas_amort", "style")], 
        [Input("toggle_amort", "on"),
         Input("toggle_localidades", "on"),
         Input("toggle_escuelas", "on")]
        )
def toggle_amort(on, loc_on, esc_on):
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
         [Input("toggle_excl", "on"),
         Input("toggle_localidades", "on"),
         Input("toggle_cursos", "on"),
         Input("toggle_cuerpos", "on"),
         Input("toggle_escuelas", "on")]
         )
def toggle_excl(on, loc_on, cur_on, cue_on, esc_on ):
    if  on:
        return {"display": "block" if loc_on else "none"}, {"display": "block" if loc_on else "none"}, {"display": "block" if cur_on else "none"},{"display": "block" if cue_on else "none"}, {"display": "block" if esc_on else "none"}
    else: 
        return {"display": "none"}, {"display": "none"}, {"display": "none"},{"display": "none"}, {"display": "none"}    


    
