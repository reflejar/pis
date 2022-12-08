import geopandas as gpd

DF_CUERPOS = gpd.read_file("data/cuerpos.geojson").reset_index()
DF_CURSOS_AGUA = gpd.read_file("data/cursos_agua.geojson")
DF_ESCUELAS = gpd.read_file("data/escuelas.geojson")