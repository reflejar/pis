import dash_bootstrap_components as dbc
from dash import html


GIS = dbc.Container(
        [
            html.H1("Proyección GIS", className="display-5 pt-5 text-white"),
            html.H5("Mapa municipal de áreas urbanizadas, zonas de exclusión y amortiguamiento", className="pb-5 text-white"),
            html.Br(className="py-5"),
            dbc.Button("Ver más", size="md", class_name=" text-dark", href="/gis")
        ],
        fluid=True,
        className="py-5 px-5 text-uppercase text-white",
        id="index-mapa"
    )


