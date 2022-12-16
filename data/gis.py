import geopandas as gpd
import shapely
import numpy as np
import plotly.graph_objects as go
import json

class MapHandler:

    """

        Clase para la manipulación de mapas

        Parametros que recibe
        ----------
            municipios: list
                Municipios que quiera mostrar.
            recursos: list
                Lista de recursos que se quiera mostrar.
            vista: str
                Tipo de vista que se quiera mostrar 'open-street-map' o 'white-bg'.
                Default: 'open-street-map'.

        Atributos principales
        ----------
            TIPO_RECURSOS: dict
                Diccionario de los tipos de recursos disponibles con sus caracterizaciones.
                    [cursos_agua, cuerpos_agua, escuelas_en_parcelas, ...]
            MUNICIPIOS: 
                Municipios de Bs As. (Por ahora solo Mar Chiquita).
                Falta ...
            fig: go.Figure
                Figura a la que se le agregarán y quitarán capas.
        
        Métodos principales
        ----------
            .render() -> go.Figure
                Prende y apaga las capas y el tipo de vista.
                Retorna el mapa entero.
            
    """

    DEFAULT_FOLDER = 'data'

    TIPO_RECURSOS = {
        'cursos_agua': {
            'title': 'Cursos de agua',
            'color': None
        },
        'cuerpos_agua': {
            'title': 'Cuerpos de agua',
            'color': 0
        },
        'escuelas_en_parcelas': {
            'title': 'Escuelas',
            'color': 1
        },
    }

    MUNICIPIOS = ['Mar Chiquita']
    COLOR_SCALE = [[0, 'rgb(17, 56, 173)'], [1,'rgb(199, 30, 30)' ]]


    def __init__(
        self,
        municipios:list=[],
        recursos:list=[],
        vista:str='open-street-map',
    ) -> None:
        if not isinstance(recursos, list):
            raise Exception("dame una lista de strings para los tipos de recurso porfis")
        self.fig = go.Figure()
        self.municipios = municipios or self.MUNICIPIOS
        self.recursos = recursos
        self.vista = vista

    def render(self):
        self.switch_vista()        
        self.switch_municipio()
        self.switch_capas()
        return self.fig
        
    
    def switch_municipio(self):
        # Por ahora no hace nada mas que centrar y centra con un gdf dummy
        gdf = gpd.read_file(f"{self.DEFAULT_FOLDER}/cursos_agua.geojson").reset_index()
        self.zoom_and_center(gdf)


    def switch_vista(self):
        if len(self.fig.data) == 0:
            self.fig.update_layout(
                mapbox_style="open-street-map",
                mapbox_zoom=6, 
                uirevision=True,
                height=800,
                coloraxis_showscale=False,
                margin={"r":0,"t":0,"l":0,"b":0},
                mapbox_center={"lat": -36.26, "lon": -60.23},
            )
        if self.vista != self.fig.layout.mapbox.style:
            if self.vista == "open-street-map":
                self.fig.update_layout(
                    mapbox_style="open-street-map",
                    mapbox_layers=[]
                )
            else:
                self.fig.update_layout(
                    mapbox_style="white-bg",
                    mapbox_layers=[
                        {
                            "below": 'traces',
                            "sourcetype": "raster",
                            "sourceattribution": 'Tiles &copy; Esri &mdash; Source: Esri, i-cubed, USDA, USGS, AEX, GeoEye, Getmapping, Aerogrid, IGN, IGP, UPR-EGP, and the GIS User Community',
                            "source": [
                                "https://server.arcgisonline.com/ArcGIS/rest/services/World_Imagery/MapServer/tile/{z}/{y}/{x}"
                            ]
                            
                        }
                    ]
                )                

    def switch_capas(self):
        # Solo si hay cambio en lo solicitado
        if len(self.recursos) != len(self.fig.data):
            # Si los recursos a mostrarse son menores a los ya existentes hay que borrar el que ya no se necesita
            if len(self.recursos) < len(self.fig.data):
                self.fig.data = [data for data in self.fig.data if data.name in self.recursos]
            # Y sino hay que agregar las capas que no existen aun
            else:
                capas_existentes = [data.name for data in self.fig.data]
                capas_a_realizar = [i for i in self.recursos if i not in capas_existentes]
                for r in capas_a_realizar:
                    gdf = gpd.read_file(f"{self.DEFAULT_FOLDER}/{r}.geojson").reset_index()
                    if r in ['cuerpos_agua', 'escuelas_en_parcelas']:
                        self.fig.add_trace(self._choroplet(gdf, r))
                    elif r in ['cursos_agua']:
                        self.fig.add_trace(self._scatter(gdf, r))                    

    def _choroplet(self, gdf, recurso):
        gdf['color'] = self.TIPO_RECURSOS[recurso]['color']

        return go.Choroplethmapbox(
            geojson=json.loads(gdf.to_json(na="keep")), 
            featureidkey="properties.index",
            locations=gdf['index'], 
            z=gdf['color'],
            zmax=1,
            zmin=0,
            colorscale=self.COLOR_SCALE,
            marker_opacity=1,
            marker_line_width=0.5,
            # customdata=,
            showscale=False,
            name=recurso
        )

    def _scatter(self, gdf, recurso):
        #Crear latitudes y longitudes de rios
        lats = []
        lons = []
        names = []
        for feature, name in zip(gdf.geometry, gdf.NOMBRE):
            if isinstance(feature, shapely.geometry.linestring.LineString):
                linestrings = [feature]
            elif isinstance(feature, shapely.geometry.multilinestring.MultiLineString):
                linestrings = feature.geoms
            else:
                continue
            for linestring in linestrings:
                x, y = linestring.xy
                lats = np.append(lats, y)
                lons = np.append(lons, x)
                names = np.append(names, [name]*len(y))
                lats = np.append(lats, None)
                lons = np.append(lons, None)
                names = np.append(names, None)
                
        return go.Scattermapbox(
            lat = lats,
            lon = lons,
            mode = 'lines',
            marker_size=12,
            marker_color='rgb(30, 115, 199)',
            name=recurso
            )            

    def zoom_and_center(self, gdf):
        """Function documentation:\n
        Basic framework adopted from Krichardson under the following thread:
        https://community.plotly.com/t/dynamic-zoom-for-mapbox/32658/7

        # NOTE:
        # THIS IS A TEMPORARY SOLUTION UNTIL THE DASH TEAM IMPLEMENTS DYNAMIC ZOOM
        # in their plotly-functions associated with mapbox, such as go.Densitymapbox() etc.

        Returns the appropriate zoom-level for these plotly-mapbox-graphics along with
        the center coordinate tuple of all provided coordinate tuples.
        """

        # Check whether both latitudes and longitudes have been passed,
        x1,y1,x2,y2 = gdf['geometry'].total_bounds
        longitudes=np.array([x1,x2])
        latitudes=np.array([y1,y2])
        max_bound = max(abs(x1-x2), abs(y1-y2)) * 111
        zoom = 11.5 - np.log(max_bound)

        # or if the list lenghts don't match
        if ((latitudes is None or longitudes is None)
                or (len(latitudes) != len(longitudes))):
            # Otherwise, return the default values of 0 zoom and the coordinate origin as center point
            return 0, (0, 0)

        # Get the boundary-box 
        b_box = {} 
        b_box['height'] = latitudes.max()-latitudes.min()
        b_box['width'] = longitudes.max()-longitudes.min()
        b_box['center']= (np.mean(longitudes), np.mean(latitudes))

        # get the area of the bounding box in order to calculate a zoom-level
        area = b_box['height'] * b_box['width']

        # * 1D-linear interpolation with numpy:
        # - Pass the area as the only x-value and not as a list, in order to return a scalar as well
        # - The x-points "xp" should be in parts in comparable order of magnitude of the given area
        # - The zpom-levels are adapted to the areas, i.e. start with the smallest area possible of 0
        # which leads to the highest possible zoom value 20, and so forth decreasing with increasing areas
        # as these variables are antiproportional
        zoom = np.interp(x=area,
                        xp=[0, 5**-10, 4**-10, 3**-10, 2**-10, 1**-10, 1**-5],
                        fp=[20, 15,    14,     13,     12,     7,      5])

        # Finally, return the zoom level and the associated boundary-box center coordinates
        self.fig.update_layout(
            mapbox_zoom=zoom-1, 
            mapbox_center = {"lat": b_box['center'][1], "lon": b_box['center'][0]},
        )


    # def create_hover_info(self):
    #     hover_escuelas_parc='<b>Nombre</b>: %{customdata[0]}<br>'+'<b>Nivel</b>: %{customdata[1]}<br>'+'<b>Teléfono</b>: %{customdata[2]}'+'<extra></extra>'
    
    #     customdata_escuelas_parc = np.stack((gdf["nombre.establecimiento"], gdf['nivel'],
    #                         gdf["Tel"]), axis=-1)
    #     hover_cuerpos='<b>Nombre</b>: %{customdata[0]}<br>'+'<b>Tipo</b>: %{customdata[1]}<br>'+'<extra></extra>'
    #     customdata_cuerpos = np.stack((gdf["NOMBRE"], gdf['TIPO']), axis=-1)
    #     hover_cursos='<b>Nombre</b>: %{customdata[0]}<br>'+'<extra></extra>'
    #     customdata_cursos = np.stack((names,names), axis=-1)