import dash_bootstrap_components as dbc
from dash import html

Hero = html.Section(
	dbc.Container(
		dbc.Row(
			dbc.Col([
					html.H1("P.I.S.", className="display-1 hero-title text-white"),
					html.H2([
						"Peligros Introducidos Silenciosamente",
					], className="hero-title text-dark mb-5"),
					html.H4([
						"Campaña de mapeo y sistematización colectivo de datos e información sobre el uso de agroquímicos y la salud humana",
						html.Br(),
					], className="text-dark"),					
				],
				md=9
			),
		),
		fluid=True,
		className="d-flex justify-content-center align-items-center min-vh-100",
	),
	className="bg-image",
	id="hero"
)