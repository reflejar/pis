import dash
import dash_bootstrap_components as dbc
from dash import html

from pages.sections import (
    Navbar, 
)

# Se crea Dash y elegimos el tema
app = dash.Dash(
    __name__,
    external_stylesheets=[dbc.themes.MINTY], # COSMO, FLATLY, LUX, MINTY
    use_pages=True
)

# Se agregan los componentes de la web
app.layout = html.Div(
    children=[
        Navbar, 
        dash.page_container
    ]
)




# Se corre la aplicación
if __name__ == "__main__":
    app.run_server(host="0.0.0.0", port=8050, debug=True, use_reloader=True)