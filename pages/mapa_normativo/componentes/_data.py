import geopandas as gpd
import json


MUNICIPIOS = ['Mar Chiquita']

###### Se importan las bases de los objetos representados en el mapa ##############
cuerpos=gpd.read_parquet("./data/cuerpos.parquet")
localidades_parajes=gpd.read_parquet("./data/localidades_parajes.parquet")
escuelas_parcelas=gpd.read_parquet("./data/escuelas_parcelas.parquet")
reservas=gpd.read_parquet("./data/reservas.parquet")
cursos=gpd.read_parquet("./data/cursos_agua.parquet")

###### Se importan las bases de las zonas de exclusion y amortiguamiento de cada objeto ############
cuerpos_excl=gpd.read_parquet("./data/cuerpos_excl.parquet")
cursos_excl=gpd.read_parquet("./data/cursos_excl.parquet")
localidades_excl=gpd.read_parquet("./data/localidades_excl.parquet")
parajes_excl=gpd.read_parquet("./data/parajes_excl.parquet")
escuelas_parcelas_excl=gpd.read_parquet("./data/escuelas_parcelas_excl.parquet")
localidades_amort=gpd.read_parquet("./data/localidades_amort.parquet")
parajes_amort=gpd.read_parquet("./data/parajes_amort.parquet")
escuelas_parcelas_amort=gpd.read_parquet("./data/escuelas_parcelas_amort.parquet")

################ Se crea una columna llamada "tooltip" que luego sirve como etiqueta en el mapa #############
cursos["tooltip"]="<b>Nombre</b>: "+cursos["NOMBRE"]+'<extra></extra>'
cursos["popup"]=cursos["tooltip"]

escuelas_parcelas["tooltip"]='<b>Nombre</b>: '+escuelas_parcelas["nombre.establecimiento"]+'<br>'+'<b>Nivel</b>: '+escuelas_parcelas["nivel"]+ '<br>'+'<b>Teléfono</b>: '+escuelas_parcelas["Tel"]+'<br>'+'<b>Email</b>: '+escuelas_parcelas["email"]+'<extra></extra>'
escuelas_parcelas["popup"]=escuelas_parcelas["tooltip"]

cuerpos["tooltip"]='<b>Nombre</b>: '+cuerpos["NOMBRE"]+'<br>'+'<b>Tipo</b>: '+cuerpos['TIPO']+'<extra></extra>'
cuerpos["popup"]=cuerpos["tooltip"]

reservas["tooltip"]="<b>Nombre</b>: "+reservas["Name"]
reservas["popup"]="<b>Nombre</b>: "+reservas["Name"]

localidades_parajes["tooltip"]='<b>Nombre</b>: '+localidades_parajes["Name"]+'<br>'+'<b>Habitantes</b>: '+localidades_parajes["Habitantes"]+'<extra></extra>'
localidades_parajes["popup"]=localidades_parajes["tooltip"]

cuerpos_excl["tooltip"]='<b>Zona de Exclusión</b> <br>'+'<extra></extra>'
cursos_excl["tooltip"]='<b>Zona de Exclusión</b> <br>'+'<extra></extra>'
localidades_excl["tooltip"]='<b>Zona de Exclusión</b> <br>'+'<extra></extra>'
parajes_excl["tooltip"]='<b>Zona de Exclusión</b> <br>'+'<extra></extra>'
escuelas_parcelas_excl["tooltip"]='<b>Zona de Exclusión</b> <br>'+'<extra></extra>'

localidades_amort["tooltip"]='<b>Zona de Amortiguamiento</b> <br>'+'<extra></extra>'
parajes_amort["tooltip"]='<b>Zona de Amortiguamiento</b> <br>'+'<extra></extra>'
escuelas_parcelas_amort["tooltip"]='<b>Zona de Amortiguamiento</b> <br>'+'<extra></extra>'

################ se pasan las tablas a json #################################################################
localidades_amort_geojson = json.loads(localidades_amort.to_json(na="keep"))
parajes_amort_geojson = json.loads(parajes_amort.to_json(na="keep"))
escuelas_parcelas_amort_geojson = json.loads(escuelas_parcelas_amort.to_json(na="keep"))

cursos_excl_geojson = json.loads(cursos_excl.to_json(na="keep"))
cuerpos_excl_geojson = json.loads(cuerpos_excl.to_json(na="keep"))
localidades_excl_geojson = json.loads(localidades_excl.to_json(na="keep"))
parajes_excl_geojson = json.loads(parajes_excl.to_json(na="keep"))
escuelas_parcelas_excl_geojson = json.loads(escuelas_parcelas_excl.to_json(na="keep"))

cursos_geojson = json.loads(cursos.to_json(na="keep"))
cuerpos_geojson = json.loads(cuerpos.to_json(na="keep"))
localidades_parajes_geojson=json.loads(localidades_parajes.to_json(na="keep"))
escuelas_parcelas_geojson = json.loads(escuelas_parcelas.to_json(na="keep"))
reservas_geojson = json.loads(reservas.to_json(na="keep"))