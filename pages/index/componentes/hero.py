import dash_bootstrap_components as dbc
from dash import html

Hero = html.Section(
		dbc.Container(html.Div([
					html.H1("¿Qué es P.I.S.?", className="hero-title text-white text-center mb-5"),
					html.H2([
						"Pesticidas introducidos silenciosamente",
					], className="hero-subtitle text-center text-uppercase text-dark mb-5"),
					html.H4([
						"Campaña de incidencia pública para la reducción de uso de plaguicidas  basados en datos, información y activación territorial efectiva.",
						html.Br(),
					], className="hero-description text-center text-dark"),					
				])),
	className="bg-image d-flex justify-content-center align-items-center min-vh-100",
	id="hero"
)