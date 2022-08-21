import dash_bootstrap_components as dbc
from dash import html

Hero = html.Section(
    dbc.Container(
        [
            html.H1("Pesticidas introducidos \n silenciosamente", className="display-1"),
            html.H1("P.I.S", className="display-1"),
            html.Hr(className="my-2"),
            html.P(
                """Campaña de ciencia ciudadana e incidencia 
                pública P.I.S. sobre el uso de agroquímicos y la
                salud humana""",
                className="lead",
            ),
        ],
        fluid=True,
        className="py-3 text-dark",
    ),
    className="bg-image",
    id="hero"
)
