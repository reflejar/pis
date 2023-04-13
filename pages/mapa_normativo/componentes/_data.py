import geopandas as gpd
import json
import pandas as pd
from itertools import combinations

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


################ se pasan las tablas a json #################################################################

cursos_geojson = json.loads(cursos.to_json(na="keep"))
cuerpos_geojson = json.loads(cuerpos.to_json(na="keep"))
localidades_parajes_geojson=json.loads(localidades_parajes.to_json(na="keep"))
escuelas_parcelas_geojson = json.loads(escuelas_parcelas.to_json(na="keep"))
reservas_geojson = json.loads(reservas.to_json(na="keep"))

###################### tabla general exclusion y amortiguamiento ####################################################
excl=[localidades_excl, parajes_excl,cursos_excl, cuerpos_excl,escuelas_parcelas_excl]
combinaciones=[]
for i in range(1,len(excl)+1):
    x = combinations(excl, i)
    for j in list(x):
        combinaciones.append(j)
combinaciones
exclusion=pd.DataFrame()
for i in list(combinaciones):
    exclusion_x=pd.DataFrame()
    lista=[]
    puntos_interes=pd.DataFrame()
    for j in i:
        exclusion_x=pd.concat([exclusion_x, j[["geometry"]]])
        nombre_variable=[name for name in globals() if globals()[name] is j]
        lista.append(nombre_variable[0][0:nombre_variable[0].find("_")])
    x=""
    for z in lista:
        x=x+z

    
    if "cuerpos" in x:
        puntos_interes=pd.concat([puntos_interes, cuerpos])
    if "localidades"  in x:
        puntos_interes=pd.concat([puntos_interes, localidades_parajes])
    if "parajes"  in x:
        if "localidades"  not in x:
            puntos_interes=pd.concat([puntos_interes, localidades_parajes])
    if "escuelas" in x:
        puntos_interes=pd.concat([puntos_interes, escuelas_parcelas])

    exclusion_x["id"]=x
    if x!="cursos":
        exclusion_x = exclusion_x.overlay(puntos_interes, how='difference')
    exclusion_x = exclusion_x.dissolve().explode(ignore_index=True,index_parts=False)
    exclusion=pd.concat([exclusion,exclusion_x])
exclusion.reset_index(inplace=True)

###################### tabla general amortiguamiento ####################################################
   
amort=[localidades_amort, parajes_amort, escuelas_parcelas_amort ]

combinaciones=[]
for i in range(1,len(amort)+1):
    x = combinations(amort, i)
    for j in list(x):
        combinaciones.append(j)
combinaciones

amortiguacion=pd.DataFrame()
for i in list(combinaciones):
    amortiguacion_x=pd.DataFrame()
    lista=[]
    puntos_interes=pd.DataFrame()
    for j in i:
        amortiguacion_x=pd.concat([amortiguacion_x, j[["geometry"]]])
        nombre_variable=[name for name in globals() if globals()[name] is j]
        lista.append(nombre_variable[0][0:nombre_variable[0].find("_")])
    x=""
    for z in lista:
        x=x+z
    
    puntos_interes=pd.concat([puntos_interes, cuerpos])
    if "localidades"  in x:
        puntos_interes=pd.concat([puntos_interes, localidades_parajes])
    if "parajes"  in x:
        if "localidades"  not in x:
            puntos_interes=pd.concat([puntos_interes, localidades_parajes])
    if "escuelas" in x:
        puntos_interes=pd.concat([puntos_interes, escuelas_parcelas])

    amortiguacion_x["id"]=x
    amortiguacion_x = amortiguacion_x.overlay(pd.concat([exclusion[exclusion["id"]==x],puntos_interes]), how='difference')
    amortiguacion_x = amortiguacion_x.dissolve().explode(ignore_index=True,index_parts=False)
    amortiguacion=pd.concat([amortiguacion,amortiguacion_x])
amortiguacion.reset_index(inplace=True)
