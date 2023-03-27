import dash_bootstrap_components as dbc
from dash import html

Hero = html.Section(
		dbc.Container(html.Div([
					html.H1("P.I.S.", className="hero-title text-primary mb-3"),
					html.H2([
						"Pesticidas Introducidos Silenciosamente",
					], className="hero-subtitle text-primary mb-5"),
					html.H4([
						"Herramientas e informacion para reducir el impacto de los agroquimicos desde los territorios.",
						html.Br(),
					], className="hero-description text-white"),					
				])),
	className="bg-hero d-flex justify-content-center align-items-center min-vh-100",
	id="hero"
)