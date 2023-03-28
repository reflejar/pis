from dash import html, Input, Output, callback, State
import dash_bootstrap_components as dbc


PIS_ISOLOGOTIPO = "/assets/img/pis_isologotipo.png"
REFLEJAR_LOGOTIPO = "/assets/img/reflejar_logotipo.png"


Navbar = dbc.Navbar(
    dbc.Container(
        [
            html.A(
                html.Img(src=PIS_ISOLOGOTIPO, height="80px"),
                href="/",
            ),
            dbc.NavbarToggler(id="navbar-toggler", n_clicks=0),
            dbc.Collapse(
                dbc.Nav([
                        dbc.NavItem(html.A("Proyecto", className="text-white text-uppercase text-none-decoration mx-3", href="/#index-proyecto")),
                        dbc.NavItem(html.A("Testeos", className="text-white text-uppercase text-none-decoration mx-3", href="/#index-testeando")),
                        dbc.NavItem(html.A("Herramientas", className="text-white text-uppercase text-none-decoration mx-3", href="/#index-herramientas")),
                        dbc.NavItem(html.A("FAQS", className="text-white text-uppercase text-none-decoration mx-3", href="/#index-faqs")),          
                        dbc.NavItem(html.A("Donar", className="text-white text-uppercase text-none-decoration mx-3", href="/#index-donar")),
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
    dbc.Container([
        dbc.Row([
            dbc.Col([
                html.Div(
                    [
                        html.A(html.I(className="bi bi-twitter"), href="https://twitter.com/",target="_blank", className="btn mx-3 btn-lg btn-floating"),
                        html.A(html.I(className="bi bi-instagram"), href="https://www.instagram.com/",target="_blank", className="btn mx-3 btn-lg btn-floating"),
                        html.A(html.I(className="bi bi-facebook"), href="https://www.facebook.com/",target="_blank", className="btn mx-3 btn-lg btn-floating"),
                    ],
                    className="text-center"
                )
            ],
            md=12),
        ]),
    ])
    ],
    className="text-white position-relative",
    id="footer"
)


