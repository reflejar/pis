import geopandas as gpd
import shapely
import numpy as np
import plotly.graph_objects as go
import json

class Mapa:

    """
    Obtencion del df de la data solicitada

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
        if not resource in self.TIPO_RECURSOS.keys():
            raise Exception(f"pedime un tipo de recursos valido bichi, osea: {self.TIPO_RECURSOS.keys()}")
        self.df = gpd.read_file(f"{folder or self.DEFAULT_FOLDER}/{resource}.geojson").reset_index()
        

    def create(self):
        return {
            'cuerpos_agua': self.choroplet,
            'cursos_agua': self.scatter,
            'escuelas_en_parcelas': self.choroplet,
        }[self.resource]()


    def choroplet(self):
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

    def scatter(self):
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

    @staticmethod
    def zoom_and_center(longitudes=None, latitudes=None):
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
        return zoom, b_box['center']        


    # def make_custom_data(self):
    #     hover_escuelas_parc='<b>Nombre</b>: %{customdata[0]}<br>'+'<b>Nivel</b>: %{customdata[1]}<br>'+'<b>Teléfono</b>: %{customdata[2]}'+'<extra></extra>'
    
    #     customdata_escuelas_parc = np.stack((self.df["nombre.establecimiento"], self.df['nivel'],
    #                         self.df["Tel"]), axis=-1)
    #     hover_cuerpos='<b>Nombre</b>: %{customdata[0]}<br>'+'<b>Tipo</b>: %{customdata[1]}<br>'+'<extra></extra>'
    #     customdata_cuerpos = np.stack((self.df["NOMBRE"], self.df['TIPO']), axis=-1)
    #     hover_cursos='<b>Nombre</b>: %{customdata[0]}<br>'+'<extra></extra>'
    #     customdata_cursos = np.stack((names,names), axis=-1)