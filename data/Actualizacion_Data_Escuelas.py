import geopandas as gpd
import pandas as pd


# VARIABLES FIJAS
VAR_TELEFONO = 'Tel'
VAR_MAIL = ''
VAR_CODIGO_UNICO = 'codigo_unico_pis'
VAR_CUE = 'cue'
VAR_SEDE_ANEXO_EXT = 'sede/axo/ext'
VAR_COD_POSTAL = 'código postal'


#ARCHIVO CON INFORMACIÓN PROVINCIAL > DE ACA SE TOMA EL LISTADO DE VALIDACIÓN
establec_educativos_completo=gpd.read_file("./data/establecimientos_educativos_provincial.geojson")

#Limpieza y ordenamiento de los datos
establec_educativos_completo['direccion_gj'] = establec_educativos_completo['dirección calle'] + establec_educativos_completo['dirección nro.']
establec_educativos_completo['característica telefónica'] = '(' + establec_educativos_completo['característica telefónica'].fillna(0).astype(int).astype(str) + ')'
establec_educativos_completo['telefono_gj'] = establec_educativos_completo['característica telefónica'] +' ' + establec_educativos_completo['teléfono'].astype(str)
establec_educativos_completo = establec_educativos_completo.rename(columns = {'email': 'mail_gj'})

establec_educativos_completo[VAR_CODIGO_UNICO] = establec_educativos_completo[VAR_COD_POSTAL].fillna(0).astype(int).astype(str)+ ' - ' +  establec_educativos_completo[VAR_CUE].astype(str) + ' - ' + establec_educativos_completo[VAR_SEDE_ANEXO_EXT]

#listado_validacion_escuelas = establec_educativos_completo[['cue', 'nombre establecimiento', 'partido']].sort_values(by='cue')
#listado_validacion_escuelas.to_csv('listado_validacion_est_educ_provincia.csv', sep=';')


# Base de datos actualizada manualmente
escuelas_informacion_manual = pd.read_csv('data\est_educativos_actualizacion_provincial.csv', encoding = 'latin1', on_bad_lines='skip', sep = ";")
escuelas_informacion_manual = escuelas_informacion_manual.dropna(how= 'all', axis=0)
escuelas_informacion_manual = escuelas_informacion_manual.dropna(how= 'all', axis=1)
escuelas_informacion_manual[VAR_CODIGO_UNICO] = escuelas_informacion_manual[VAR_COD_POSTAL].astype(int).astype(str) + ' - ' + escuelas_informacion_manual[VAR_CUE].astype(str) + ' - ' + escuelas_informacion_manual[VAR_SEDE_ANEXO_EXT]
escuelas_informacion_manual['nombre_apellido_manual'] = escuelas_informacion_manual['nombre'] + ' ' + escuelas_informacion_manual['apellido']


VARIABLES_A_ACTUALIZAR = ['codigo_unico_pis', 'nombre establecimiento a considerar', 'direccion_manual', 'cargo', 'nombre_apellido_manual', 'telefono_manual', 'mail_manual', 'matricula_2021']
escuelas_informacion_manual = escuelas_informacion_manual[VARIABLES_A_ACTUALIZAR]


## UNIMOS LAS BASES DE DATOS

base_escuelas_actualizada = pd.merge(establec_educativos_completo , escuelas_informacion_manual, on = VAR_CODIGO_UNICO, how = 'left')

base_escuelas_actualizada['nombre.establecimiento'] = base_escuelas_actualizada['nombre establecimiento a considerar'].str.title()
base_escuelas_actualizada['email'] = base_escuelas_actualizada['mail_manual'].fillna(base_escuelas_actualizada['mail_gj']).str.lower()
base_escuelas_actualizada['Tel'] = base_escuelas_actualizada['telefono_manual'].fillna(base_escuelas_actualizada['telefono_gj'])
base_escuelas_actualizada['direccion'] = base_escuelas_actualizada['direccion_manual'].fillna(base_escuelas_actualizada['direccion_gj']).str.title()



#actualizado_check =gpd.read_file("./data/escuelas_informacion_actualizadas.geojson")

#print(actualizado_check)

#base_escuelas_actualizada_gsjon = gpd.GeoDataFrame(base_escuelas_actualizada, geometry = 'geometry', crs='EPSG:4326')  #epsg4326 is WGS84

#base_escuelas_actualizada_gsjon.to_file('escuelas_informacion_actualizadas.geojson', driver='GeoJSON')


#establec_educativos_PARQUET=gpd.read_parquet("./data/escuelas_parcelas.parquet")

##FALTA AGREGAR CASOS NUEVOS


