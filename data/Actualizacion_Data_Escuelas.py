import geopandas as gpd
import pandas as pd


# VARIABLES FIJAS UTILIZADAS PARA EL MERGE Y PARA EL TOOLTIP
VAR_CUE = 'cue'
VAR_SEDE_ANEXO_EXT = 'sede/axo/ext'
VAR_COD_POSTAL = 'código postal'

VAR_TELEFONO = 'Tel'
VAR_MAIL = 'email'
VAR_CODIGO_UNICO = 'codigo_unico_pis'
VAR_DIRECCION = 'direccion'
VAR_NOM_ESTABLEC = 'nombre.establecimiento'
VAR_LATITUD = 'latitud'
VAR_LONGITUD = 'longitud'
VAR_GEOMETRIA = 'geometry'


# ARCHIVO CON INFORMACIÓN PROVINCIAL > DE ACA SE TOMA EL LISTADO DE VALIDACIÓN
establec_educativos_completo=gpd.read_file("./data/establecimientos-educativos-PBA.geojson")

# LIMPIEZA Y ORDENAMIENTO DE DATOS
establec_educativos_completo['direccion_gj'] = establec_educativos_completo['dirección calle'] + establec_educativos_completo['dirección nro.']
establec_educativos_completo['característica telefónica'] = '(' + establec_educativos_completo['característica telefónica'].fillna(0).astype(int).astype(str) + ')'
establec_educativos_completo['telefono_gj'] = establec_educativos_completo['característica telefónica'] +' ' + establec_educativos_completo['teléfono'].astype(str)
establec_educativos_completo = establec_educativos_completo.rename(columns = {VAR_MAIL: 'mail_gj', VAR_LATITUD : 'latitud_gj', VAR_LONGITUD : 'longitud_gj'})

establec_educativos_completo[VAR_CODIGO_UNICO] = establec_educativos_completo[VAR_COD_POSTAL].fillna(0).astype(int).astype(str)+ ' - ' +  establec_educativos_completo[VAR_CUE].astype(str) + ' - ' + establec_educativos_completo[VAR_SEDE_ANEXO_EXT]

# Base de datos actualizada manualmente
escuelas_informacion_manual = pd.read_csv('data\est_educativos_actualizacion_provincial.csv', encoding = 'latin1', on_bad_lines='skip', sep = ";")
escuelas_informacion_manual = escuelas_informacion_manual.dropna(how= 'all', axis=0)
escuelas_informacion_manual = escuelas_informacion_manual.dropna(how= 'all', axis=1)

# Filtramos para solo quedarnos con las escuelas rurales. Las urbanas se incluyen dentro de las localidades.
escuelas_informacion_manual = escuelas_informacion_manual[escuelas_informacion_manual['ubicacion_manual']!= 'Urbano']
# Construimos codigo para el merge
escuelas_informacion_manual[VAR_CODIGO_UNICO] = escuelas_informacion_manual[VAR_COD_POSTAL].astype(int).astype(str) + ' - ' + escuelas_informacion_manual[VAR_CUE].astype(str) + ' - ' + escuelas_informacion_manual[VAR_SEDE_ANEXO_EXT]
# Construimos nombre a mostrar del establecimiento
escuelas_informacion_manual['nombre_apellido_manual'] = escuelas_informacion_manual['nombre'] + ' ' + escuelas_informacion_manual['apellido']

## ACHICAMOS LA BBDD A UNIR CON EL GEOJSON
VARIABLES_A_ACTUALIZAR = ['codigo_unico_pis', 'nombre establecimiento a considerar', 'direccion_manual', 'cargo', 'nombre_apellido_manual', 'telefono_manual', 'mail_manual', 'matricula_2021', 'latitud_manual', 'longitud_manual', 'nueva_existente']
escuelas_informacion_manual = escuelas_informacion_manual[VARIABLES_A_ACTUALIZAR]

## UNIMOS LAS BASES DE DATOS CON LOS DATOS DE ESCUELAS EXISTENTES EN BBDD DE INDEC

### Separamos las bbdd segun si es escuela que está en el catastro o no
escuelas_existentes_informacion_manual = escuelas_informacion_manual[escuelas_informacion_manual['nueva_existente']=='Existente'].copy()
escuelas_nuevas_informacion_manual = escuelas_informacion_manual[escuelas_informacion_manual['nueva_existente']=='Nueva'].copy()

#### Unimos GeoJson con la info de escuelas existentes
base_escuelas_actualizada = pd.merge(establec_educativos_completo , escuelas_existentes_informacion_manual, on = VAR_CODIGO_UNICO, how = 'left')


if len(escuelas_nuevas_informacion_manual):
    base_escuelas_actualizada = pd.concat([base_escuelas_actualizada, escuelas_nuevas_informacion_manual])

base_escuelas_actualizada[VAR_NOM_ESTABLEC] = base_escuelas_actualizada['nombre establecimiento a considerar'].str.title()
base_escuelas_actualizada[VAR_MAIL] = base_escuelas_actualizada['mail_manual'].fillna(base_escuelas_actualizada['mail_gj']).str.lower()
base_escuelas_actualizada[VAR_TELEFONO] = base_escuelas_actualizada['telefono_manual'].fillna(base_escuelas_actualizada['telefono_gj'])
base_escuelas_actualizada[VAR_DIRECCION] = base_escuelas_actualizada['direccion_manual'].fillna(base_escuelas_actualizada['direccion_gj']).str.title()
base_escuelas_actualizada[VAR_LATITUD] = base_escuelas_actualizada['latitud_manual'].fillna(base_escuelas_actualizada['latitud_gj'])
base_escuelas_actualizada[VAR_LONGITUD] = base_escuelas_actualizada['longitud_manual'].fillna(base_escuelas_actualizada['longitud_gj'])
#base_escuelas_actualizada[VAR_GEOMETRIA] = base_escuelas_actualizada['geometry_gj']
#base_escuelas_actualizada['PRUEBA'] = { "type": "Point", "coordinates": 'PROBANDO' }

base_escuelas_actualizada_gsjon = gpd.GeoDataFrame(base_escuelas_actualizada, geometry = 'geometry', crs='EPSG:4326')  #epsg4326 is WGS84

base_escuelas_actualizada_gsjon.to_file('./data/escuelas_informacion_actualizada.geojson', driver='GeoJSON')

#actualizado_check =gpd.read_file("./data/escuelas_informacion_actualizada.geojson")








