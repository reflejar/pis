from dash import html, Input, Output, callback, State
import dash_bootstrap_components as dbc


PIS_ISOTIPO = "/assets/img/pis_isotipo.png"
PIS_ISOLOGOTIPO = "/assets/img/pis_isologotipo.png"
REFLEJAR_LOGOTIPO = "/assets/img/reflejar_logotipo.png"


Navbar = dbc.Navbar(
    dbc.Container(
        [
            html.Img(src=PIS_ISOTIPO, height="50px"),
            dbc.NavbarToggler(id="navbar-toggler", n_clicks=0),
            dbc.Collapse(
                dbc.Nav([
                        dbc.NavItem(dbc.NavLink("Inicio", active="exact", class_name="text-white fw-bolder mx-3", href="/")),
                        dbc.NavItem(dbc.NavLink("Mapa Normativo", active="exact", class_name="text-white fw-bolder mx-3", href="/gis/normativo")),
                        dbc.NavItem(dbc.NavLink("Ranking", active="exact", class_name="text-white fw-bolder mx-3", href="/ranking")),
                        dbc.NavItem(dbc.NavLink("Mapa Resultados", active="exact", class_name="text-white fw-bolder mx-3", href="/gis/resultados")),          
                        dbc.NavItem(dbc.NavLink("Digesto", active="exact", class_name="text-white fw-bolder mx-3", href="/digesto")),          
                        # dbc.NavItem(dbc.NavLink(dbc.Button("Donar", size="sm", class_name="bg-grey border-grey"), active="exact", class_name="text-white mx-3", href="/donar")),
                    ],
                    className="ms-auto",
                    navbar=True,
                    pills=True
                ),
                id="navbar-collapse",
                navbar=True,
            ),
        ],
    ),
    
    fixed="top",
    className="text-white",
    id="navbar"
)

def toggle_navbar_collapse(n, is_open):
    if n:
        return not is_open
    return is_open

callback(
    Output(f"navbar-collapse", "is_open"),
    [Input(f"navbar-toggler", "n_clicks")],
    [State(f"navbar-collapse", "is_open")],
)(toggle_navbar_collapse)



Footer = html.Footer([
    html.Div(style={'height': '9px'}, className="bg-primary mb-5"),
    dbc.Container([
        dbc.Row([
            dbc.Col(
                html.Div(
                    [
                        html.A(html.Img(src=PIS_ISOLOGOTIPO, height="100px"), href="/"),

                    ],
                    className="text-center"
                )
                
                , md=3),
            dbc.Col([
                html.Div(
                    [
                        html.A(html.I(className="bi bi-twitter"), href="https://twitter.com/",target="_blank", className="btn mx-3 btn-outline-primary btn-sm btn-floating"),
                        html.A(html.I(className="bi bi-instagram"), href="https://www.instagram.com/",target="_blank", className="btn mx-3 btn-outline-primary btn-sm btn-floating"),
                        html.A(html.I(className="bi bi-facebook"), href="https://www.facebook.com/",target="_blank", className="btn mx-3 btn-outline-primary btn-sm btn-floating"),
                        # html.A(html.I(className="bi bi-youtube"), href="https://www.youtube.com/channel/UC3OKs4eBtLXLeIDLpEDCZYw",target="_blank", className="btn mx-2 btn-outline-primary btn-sm btn-floating"),
                        # html.A(html.I(className="bi bi-linkedin"), href="https://www.linkedin.com/company/mundosur/",target="_blank", className="btn mx-2 btn-outline-primary btn-sm btn-floating"),
                    ],
                    className="text-center"
                )
            ],
                md=3),
            dbc.Col([
                dbc.NavItem(dbc.NavLink("¿Cómo funciona?", class_name="text-dark my-2", href="/como")),
                dbc.NavItem(dbc.NavLink("Acerca de este sitio", class_name="text-dark my-2", href="/acerca-de")),
                dbc.NavItem(dbc.NavLink("Contacto", class_name="text-dark my-2", href="/contacto")),
            ],
            md=3),
            dbc.Col([
                dbc.NavItem(dbc.NavLink("Terminos y condiciones", class_name="text-dark my-2", href="/tyc")),
                dbc.NavItem(dbc.NavLink("Politica de privacidad", class_name="text-dark my-2", href="/pp")),
            ],
            md=3),
        ]),
    ])
    ],
    className="text-white position-relative",
    id="footer"
)


