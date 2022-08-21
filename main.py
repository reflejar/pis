import dash
import dash_bootstrap_components as dbc
from dash import html

from components import (
    Navbar, 
    Hero
)

# Se crea Dash y elegimos el tema
app = dash.Dash(
    __name__,
    external_stylesheets=[dbc.themes.LUX] # COSMO, FLATLY, LUX, MINTY
)

# Se agregan los componentes de la web
app.layout = html.Div(
    children=[
        Navbar, 
        Hero
    ]
)


# Se corre la aplicación
if __name__ == "__main__":
    app.run_server(debug=True)