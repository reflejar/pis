import dash_bootstrap_components as dbc
from dash import html


Donar = html.Section([
                    html.H1("Donaciones", className="text-black display-4 strong pt-5 text-uppercase"),
                    html.H3("¿Querés que más personas conozcan el valor de su PIS y cómo reducirlo?", className="text-black strong"),
                    html.H4("Con tu donación nos ayudás a llevar esta información a más territorios y provincias.", className="text-black"),
                    dbc.Button("Doná información", color="primary", className="my-5 text-black p-3 text-uppercase"),
            ],
            className="h-50 text-center",
            id="index-donar",
)
