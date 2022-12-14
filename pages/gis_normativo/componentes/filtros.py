from dash import html, dcc

import dash_bootstrap_components as dbc

from data import Data


Filtros = html.Div(
    [
        html.H4("PROYECCIÓN GIS", className="text-white"),
        html.P([
            "Seleccioná el municipio de tu interés.",
            html.Br(),
            "Activá y desactivá las capas de los diferentes elementos."
        ]),
        dbc.Row([dbc.Col([
                    html.Label(htmlFor="select-municipio", title='Municipio'),
                    dcc.Dropdown(
                        id="select-municipio",
                        options=Data.MUNICIPIOS,
                        multi=True,
                        searchable = True,
                        placeholder = 'Selecciona un municipio..',
                        value=["Mar Chiquita"],
                        clearable=True,
                        style={'background-color': 'black'}
                    )        
            ], md=12), 
                         
        ]),    
        dbc.Row(
            dbc.Col([
                html.Div(
                    [
                        dbc.Checklist(
                            options=[{'label': v['title'], 'value': k} for k,v in Data.TIPO_RECURSOS.items()],
                            value=list(Data.TIPO_RECURSOS.keys()),
                            id="switches-recursos",
                            switch=True,
                        ),
                    ], className="mt-3"
                )
            ], md=12
            )
        )            
                   
    ],
    id="filtros",
    className=" text-white"
)
