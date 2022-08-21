import dash_bootstrap_components as dbc

Navbar = dbc.NavbarSimple(
    children=[
        dbc.NavItem(dbc.NavLink("Mapa resultados", href="#")),
        dbc.NavItem(dbc.NavLink("Ranking Municipal", href="#")),
        dbc.NavItem(dbc.NavLink("Proyección SIG", href="#")),
        dbc.NavItem(dbc.NavLink("Digesto", href="#")),
        dbc.NavItem(dbc.NavLink("Doctrinario", href="#")),
        dbc.NavItem(dbc.NavLink("Caja herramientas", href="#")),
        dbc.NavItem(dbc.NavLink("Donar", href="#")),
    ],
    brand="Home",
    brand_href="/",
    class_name="text-dark",
    id="navbar"
)