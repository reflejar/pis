from dash import html, Input, Output, callback, State
import dash_bootstrap_components as dbc
import plotly.express as px

PIS_ISOTIPO = "assets/img/pis_isotipo.png"
PIS_ISOLOGOTIPO = "assets/img/pis_isologotipo.png"
REFLEJAR_LOGOTIPO = "assets/img/reflejar_logotipo.png"


Navbar = dbc.Navbar(
    dbc.Container(
        [
            html.A(
                html.Strong("P.I.S."),
                href="/",
                className="text-white",
            ),
            dbc.NavbarToggler(id="navbar-toggler", n_clicks=0),
            dbc.Collapse(
                dbc.Nav([
                        dbc.NavItem(dbc.NavLink("Mapa resultados", active="exact", class_name="text-white mx-3", href="/mapa")),
                        dbc.NavItem(dbc.NavLink("Ranking Municipal", active="exact", class_name="text-white mx-3", href="/ranking")),
                        dbc.NavItem(dbc.NavLink("Proyección GIS", active="exact", class_name="text-white mx-3", href="/resultados")),
                        dbc.NavItem(dbc.NavLink("Digesto", active="exact", class_name="text-white mx-3", href="/digesto")),          
                        dbc.NavItem(dbc.NavLink("Doctrinario", active="exact", class_name="text-white mx-3", href="/doctrinario")),          
                        dbc.NavItem(dbc.NavLink("Caja herramientas", active="exact", class_name="text-white mx-3", href="/herramientas")),   
                        dbc.NavItem(dbc.NavLink("Donar", active="exact", class_name="text-white mx-3", href="/Donar")),
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



Footer = html.Footer(dbc.Container([
        dbc.Row([
            dbc.Col(
                html.Div(
                    [
                        html.A(html.Img(src=PIS_ISOLOGOTIPO, height="100px"), target="_blank", href="https://mundosur.org"),
                        html.Hr(),
                        html.Div(
                            [
                                html.A(html.I(className="bi bi-instagram"), href="https://www.instagram.com/mundosur_org",target="_blank", className="btn btn-outline-white btn-sm btn-floating"),
                                html.A(html.I(className="bi bi-youtube"), href="https://www.youtube.com/channel/UC3OKs4eBtLXLeIDLpEDCZYw",target="_blank", className="btn btn-outline-white btn-sm btn-floating"),
                                html.A(html.I(className="bi bi-twitter"), href="https://twitter.com/MundoSur",target="_blank", className="btn btn-outline-white btn-sm btn-floating"),
                                html.A(html.I(className="bi bi-facebook"), href="https://www.facebook.com/mundosur.org",target="_blank", className="btn btn-outline-white btn-sm btn-floating"),
                                html.A(html.I(className="bi bi-linkedin"), href="https://www.linkedin.com/company/mundosur/",target="_blank", className="btn btn-outline-white btn-sm btn-floating"),
                            ]
                        )
                    ],
                    className="text-center"
                )
                
                , md=2),
            dbc.Col([
                html.P(html.Small("MundoSur es una Asociación Civil Franco-Argentina que visibiliza e impulsa los cambios sociales y políticos necesarios para la construcción colectiva de sociedades inclusivas, participativas, diversas y democráticas en América Latina y el Caribe.")),
                html.P(html.Small("El Mapa Latinoamericano de Feminicidios (MLF) es una herramienta de incidencia política, que proporciona la información necesaria para exigirle a los Estados de América Latina y el Caribe el cumplimiento de sus obligaciones internacionales, conforme lo dispuesto por la Convención Interamericana  para prevenir, sancionar y erradicar la violencia contra la mujer (Convención Belém do Pará)")),
            ],
                md=7
            ),
            dbc.Col([
                dbc.NavItem(dbc.NavLink("Feminicidios bajo la lupa", class_name="text-white", href="/lupa")),
                dbc.NavItem(dbc.NavLink("Lo que los Estados nos deben", class_name="text-white", href="/estados")),
                dbc.NavItem(dbc.NavLink("Metodología", class_name="text-white", href="/metodologia")),
                dbc.NavItem(dbc.NavLink("Contacto", class_name="text-white", href="/contacto")),
            ],
            md=3,
            ),
        ]),
        html.Hr(),
        dbc.Row(
            dbc.Col(html.P([
                "Desarrollado por ",
                html.Img(src=REFLEJAR_LOGOTIPO, height="18px"),
                
            ]))
        )
    ]),
    className="text-white bg-primary",
    id="footer"
)


NoHayDatos = {
    'alert': dbc.Alert([
            html.I(className="bi bi-exclamation-triangle"), #bi-exclamation-octagon
            html.Br(),        
            html.P(f'No existen datos para los filtros solicitados.'),         
        ], 
        color="light",
        class_name="border-danger text-danger"
    ),
    'bar': px.bar(),
    'funnel': px.funnel(),
    'line': px.line(),
    'pie': px.pie(),
}
