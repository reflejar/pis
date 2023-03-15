from dash import html, dcc

import dash_bootstrap_components as dbc
import dash_daq as daq

from data import MapHandler

RECURSOS_INICIAL = ['reservas','cuerpos_agua','cursos_agua','localidades_parajes','escuelas_parcelas']
# RECURSOS_INICIAL = list(MapHandler.TIPO_RECURSOS.keys())

Filtros = html.Div(
    [
        html.H4("MAPA NORMATIVO", className="text-white"),
        html.P([
            "Seleccioná el municipio de tu interés.",
            html.Br(),
            "Activá y desactivá las capas de los diferentes elementos."
        ]),
        dbc.Row([dbc.Col([
                    html.Label(htmlFor="select-municipio", title='Municipio'),
                    dcc.Dropdown(
                        id="select-municipio",
                        options=MapHandler.MUNICIPIOS,
                        multi=True,
                        searchable = True,
                        placeholder = 'Selecciona un municipio..',
                        value=["Mar Chiquita"],
                        clearable=True,
                        style={'background-color': 'black'}
                    )        
            ], md=12), 
                         
        ]),
        html.Br(),
        daq.BooleanSwitch(on=True, id="toggle_cursos",color="#134dab",label="Cursos de agua"),
        daq.BooleanSwitch(on=True, id="toggle_localidades",color="purple",label="Localidades"),
        daq.BooleanSwitch(on=True, id="toggle_amort",color="#8c0d22",label="Zonas Amortización"),
        daq.BooleanSwitch(on=True, id="toggle_excl",color="#8c0d22",label="Zonas Exclusión"),
        daq.BooleanSwitch(on=True, id="toggle_cuerpos",color="#134dab",label="Cuerpos de agua"),
        daq.BooleanSwitch(on=True, id="toggle_reservas",color="#06660b",label="Reservas"),
        daq.BooleanSwitch(on=True, id="toggle_escuelas",color="#cfc817",label="Escuelas")
    ],
    id="filtros",
    className=" text-white mt-5"
)