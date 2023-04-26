# ############################
# ### Se inicia el servidor de R-shiny
# ############################
# import os
# cmd = 'R -e "shiny::runApp(\'shiny/app.R\', port=1203)"'
# os.system(cmd)

############################
### Se inicia Flask
############################
from flask import Flask
server = Flask(__name__)
# Se incorporan endpoints necesarios para k8s
@server.route('/k8s/readiness/')
def readiness(): return "OK", 200 
@server.route('/k8s/liveness/') 
def liveness(): return "OK", 200  

############################
### Se inicia Dash
############################
import dash
import dash_bootstrap_components as dbc
from dash import html

from tools.layout import Navbar, Footer

from pages import (
	index, 
    # mapa_normativo, 
	# gis_resultados, 
    # ranking,
	# digesto
)
# Se crea Dash y elegimos el tema
app = dash.Dash(
	__name__,
	server=server,
	external_stylesheets=[dbc.icons.BOOTSTRAP], # COSMO, FLATLY, LUX, MINTY
	use_pages=True,
	update_title="Actualizando...",
	prevent_initial_callbacks=True,
	title="PIS | Pesticidas Introducidos Silenciosamente"
)
dash.register_page(index.__name__, title="Pesticidas Introducidos Silenciosamente", path='/', layout=index.layout)
# dash.register_page(mapa_normativo.__name__, title="Mapa Normativo", path='/mapa-normativo', layout=mapa_normativo.layout)
# dash.register_page(gis_resultados.__name__, title="Mapa Normativo", path='/mapa-resultados', layout=gis_resultados.layout)	
# dash.register_page(ranking.__name__, title="Mapa Normativo", path='/ranking', layout=ranking.layout)
# dash.register_page(digesto.__name__, title="Mapa Normativo", path='/digesto', layout=digesto.layout)


# Se agregan los componentes de la web
app.layout = html.Div(
	children=[
		Navbar,     
		dash.page_container,
		Footer
	]
)
