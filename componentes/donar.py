import dash_bootstrap_components as dbc
from dash import html


Donar = html.Section([
                    html.H1("Donaciones", className="text-black display-4 strong my-5 space-grotesk text-uppercase"),
                    dbc.Row(dbc.Col(
                        html.H4("Con tu donación nos ayudás a llevar esta información a más territorios y provincias.", className="text-black"),
                        lg={'offset': 4, 'size': 4}
                    )),
                    
                    dbc.Button("Doná", color="light", className="my-5 text-black fw-bold py-3 px-5 text-uppercase ", href="https://donaronline.org/democracia-en-red/campana-recaudacion-proyecto-pis", target="_blank"),
            ],
            className="min-vh-50 p-5 text-center",
            id="index-donar",
)
