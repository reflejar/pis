import dash
import dash_bootstrap_components as dbc
from dash import html

from tools.layout import Navbar, Footer

from server import server

from pages import (
	index, gis_normativo, 
	gis_resultados, ranking,
	digesto
)

# Se crea Dash y elegimos el tema
app = dash.Dash(
	__name__,
	server=server,
	external_stylesheets=[dbc.icons.BOOTSTRAP], # COSMO, FLATLY, LUX, MINTY
	use_pages=True,
	update_title="Actualizando...",
	title="PIS | Pesticidas Introducidos Silenciosamente"
)
dash.register_page(index.__name__, title="Pesticidas Introducidos Silenciosamente", path='/', layout=index.layout)
dash.register_page(gis_normativo.__name__, title="Proyección GIS", path='/gis/normativo', layout=gis_normativo.layout)
dash.register_page(gis_resultados.__name__, title="Proyección GIS", path='/gis/resultados', layout=gis_resultados.layout)
dash.register_page(ranking.__name__, title="Proyección GIS", path='/ranking', layout=ranking.layout)
dash.register_page(digesto.__name__, title="Proyección GIS", path='/digesto', layout=digesto.layout)

# Se agregan los componentes de la web
app.layout = html.Div(
	children=[
		Navbar, 
		dash.page_container,
		Footer
	]
)

# Se corre la aplicación
if __name__ == "__main__":
	app.run_server(host="0.0.0.0", port=8050, debug=True, use_reloader=True)