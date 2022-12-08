import dash_bootstrap_components as dbc
from dash import html

Hero = html.Section(
	dbc.Container(
		dbc.Row(
			dbc.Col([
					html.H1("¿Qué es P.I.S.?", className="display-1 hero-title text-white"),
					html.H2([
						"Plaguicidas introducidos silenciosamente",
					], className="hero-title text-dark mb-5"),
					html.H4([
						"Campaña de incidencia pública para la reducción de uso de plaguicidas  basados en datos , información y activación territorial efectiva.",
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