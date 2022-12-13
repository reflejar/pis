import dash_bootstrap_components as dbc
from dash import html


GisNormativo = html.Section(
            dbc.Row(
                dbc.Col([
                    html.H1("Proyección GIS", className="text-white mt-5 strong"),
                    html.H5("Mapa municipal de áreas urbanizadas, zonas de exclusión y amortiguamiento", className="pb-5 text-white"),
                    dbc.Button("Ver más", size="md", class_name="text-dark mt-5 px-4 rounded-pill strong", href="/gis/normativo")

                ], class_name="p-5"),
            ),
            className="d-flex text-uppercase h-50",
            id="index-gis-normativo",
)


GisResultados = html.Section(
            dbc.Row(
                dbc.Col([
                    html.H1("Mapa de resultados", className="text-white mt-5 strong"),
                    html.H5("Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.", className="pb-5 text-white"),
                    dbc.Button("Ver más", size="md", class_name="text-dark mt-5 px-4 rounded-pill strong", href="/gis/resultados")

                ], class_name="p-5"),
            ),
            className="d-flex text-uppercase h-50",
            id="index-gis-resultados",
)
