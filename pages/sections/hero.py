import dash_bootstrap_components as dbc
from dash import html

Hero = html.Section(
    dbc.Container(
        [
            html.H1("Pesticidas", className="display-1 hero-title"),
            html.H1("introducidos", className="display-1 hero-title"),
            html.H1("silenciosamente", className="display-1 hero-title"),
            html.H1("(P.I.S.)", className="display-1 hero-subtitle"),
            html.Hr(className="my-2"),
            html.P(
                """Campaña de ciencia ciudadana e incidencia 
                pública P.I.S. sobre el uso de agroquímicos y la
                salud humana""",
                className="lead text-dark",
            ),
        ],
        fluid=True,
        className="py-3 hero-inside",
    ),
    className="bg-image",
    id="hero"
)
