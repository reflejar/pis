import dash_bootstrap_components as dbc
from dash import html

Hero = html.Section(
		dbc.Container(html.Div([
					html.H1("PIS", className="hero-title text-primary mb-3 space-grotesk"),
					html.H2([
						"Pesticidas Introducidos Silenciosamente",
					], className="hero-subtitle text-primary mb-2 fw-bold display-4 space-grotesk"),
					html.H4([
    					"Información y herramientas para reducir el impacto de los agroquímicos en nuestros cuerpos.",
						html.Br(),
					], className="hero-description text-white space-grotesk"),					
				])),
	className="bg-hero d-flex justify-content-center align-items-center min-vh-100",
	id="index-proyecto"
)