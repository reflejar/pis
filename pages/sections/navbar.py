import dash_bootstrap_components as dbc

Navbar = dbc.NavbarSimple(
    children=[
        dbc.NavItem(dbc.NavLink("Mapa resultados", className="text-dark", href="/mapa")),
        dbc.NavItem(dbc.NavLink("Ranking Municipal", className="text-dark", href="/ranking")),
        dbc.NavItem(dbc.NavLink("Proyección SIG", className="text-dark", href="/gis")),
        dbc.NavItem(dbc.NavLink("Digesto", className="text-dark", href="/digesto")),
        dbc.NavItem(dbc.NavLink("Doctrinario", className="text-dark", href="/doctrinario")),
        dbc.NavItem(dbc.NavLink("Caja herramientas", className="text-dark", href="/herramientas")),
        dbc.NavItem(dbc.NavLink("Donar", className="text-dark", href="/donar")),
    ],
    brand="PIS",
    brand_href="/",
    class_name="text-dark",
    id="navbar"
)