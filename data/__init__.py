import geopandas as gpd
import shapely
import numpy as np
import plotly.graph_objects as go
import json

class Data:

    """
    Obtencion del df de la eph solicitada

    Parametros
    ----------
        resource : str
            tipo de recurso
        folder : str
            carpeta en la que se encuentra. Default: data
        extension : list
            extensión del archivo. Default: geojson

    Atributos
    ----------
        df: pandas.Dataframe
            Dataframe final
            
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
        resource:str=None,
        folder:str=None,
    ) -> None:
        if not isinstance(resource, str):
            raise Exception("dame un string para el tipo de recurso porfis")
        self.resource = resource
        if resource in self.TIPO_RECURSOS.keys():
            self.df = gpd.read_file(f"{folder or self.DEFAULT_FOLDER}/{resource}.geojson").reset_index()
        else:
            self.df = gpd.read_file(f"{folder or self.DEFAULT_FOLDER}/{resource}.csv").reset_index()


    def make_map(self):
        return {
            'cuerpos_agua': self.create_choropletmapbox,
            'cursos_agua': self.create_scattermapbox,
            'escuelas_en_parcelas': self.create_choropletmapbox,
        }[self.resource]()


    def create_choropletmapbox(self):
        self.df['color'] = self.TIPO_RECURSOS[self.resource]['color']

        return go.Choroplethmapbox(
            geojson=json.loads(self.df.to_json(na="keep")), 
            featureidkey="properties.index",
            locations=self.df['index'], 
            z=self.df['color'],
            zmax=1,
            zmin=0,
            colorscale=self.COLOR_SCALE,
            marker_opacity=1,
            marker_line_width=0.5,
            # customdata=,
            showscale=False
        )

    def create_scattermapbox(self):
        #Crear latitudes y longitudes de rios
        lats = []
        lons = []
        names = []
        for feature, name in zip(self.df.geometry, self.df.NOMBRE):
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
            name="Rios"
            )            


    # def make_custom_data(self):
    #     hover_escuelas_parc='<b>Nombre</b>: %{customdata[0]}<br>'+'<b>Nivel</b>: %{customdata[1]}<br>'+'<b>Teléfono</b>: %{customdata[2]}'+'<extra></extra>'
    
    #     customdata_escuelas_parc = np.stack((self.df["nombre.establecimiento"], self.df['nivel'],
    #                         self.df["Tel"]), axis=-1)
    #     hover_cuerpos='<b>Nombre</b>: %{customdata[0]}<br>'+'<b>Tipo</b>: %{customdata[1]}<br>'+'<extra></extra>'
    #     customdata_cuerpos = np.stack((self.df["NOMBRE"], self.df['TIPO']), axis=-1)
    #     hover_cursos='<b>Nombre</b>: %{customdata[0]}<br>'+'<extra></extra>'
    #     customdata_cursos = np.stack((names,names), axis=-1)