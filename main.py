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

from componentes.navbar import Navbar
from componentes.footer import Footer
from componentes.hero import Hero
from componentes.testeando import Testeando
from componentes.proximamente import Proximamente
from componentes.faqs import FAQs
from componentes.donar import Donar
from componentes.orgas import Orgas

# Se crea Dash y elegimos el tema
app = dash.Dash(
	__name__,
	server=server,
	external_stylesheets=[dbc.icons.BOOTSTRAP], # COSMO, FLATLY, LUX, MINTY
	update_title="Actualizando...",
	prevent_initial_callbacks=True,
	title="PIS | Pesticidas Introducidos Silenciosamente"
)


# Analytics
import os
GOOGLE_ANALYTICS_TRACKING_ID = os.getenv('GOOGLE_ANALYTICS_TRACKING_ID')
if GOOGLE_ANALYTICS_TRACKING_ID:
	app.index_string = f"""<!DOCTYPE html>
	<html>
		<head>
			<!-- Google tag (gtag.js) -->
			<script async src="https://www.googletagmanager.com/gtag/js?id={GOOGLE_ANALYTICS_TRACKING_ID}"</script>>
			<script>
			window.dataLayer = window.dataLayer || [];""" + """
			function gtag(){dataLayer.push(arguments);}
			gtag('js', new Date());""" +f"""
			gtag('config', '{GOOGLE_ANALYTICS_TRACKING_ID}'); """ + """
			</script>
			{%metas%}
			<title>{%title%}</title>
			{%favicon%}
			{%css%}
		</head>
		<body>
			{%app_entry%}
			<footer>
				{%config%}
				{%scripts%}
				{%renderer%}
			</footer>
		</body>
	</html>"""

	

# Se agregan los componentes de la web
app.layout = html.Div(
	children=[
		Navbar,     
		html.Div(
			children=[
				Hero,
				Testeando,
				Proximamente,
				FAQs,
				Donar,
				Orgas,
			]
		),
		Footer
	]
)

# Se corre la aplicación
if __name__ == "__main__":
	app.run(host="0.0.0.0", port=5000, debug=True, use_reloader=True)