from dash import html, dcc

import dash_bootstrap_components as dbc

from data import MapHandler


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
        dbc.Row(
            dbc.Col([
                html.Div(
                    [
                        dbc.Label("Seleccione tipo de vista", class_name="mt-3"),
                        dbc.RadioItems(
                            options=[
                                {"label": "Poligono", "value": 'open-street-map'},
                                {"label": "Satelital", "value": 'white-bg'},
                            ],
                            value='open-street-map',
                            id="radioitems-vista",
                        ),
                    ]
                )
            ], md=12
            )
        ),        
        dbc.Row(
            dbc.Col([
                html.Div(
                    [
                        dbc.Label("Seleccione tipos de recursos", class_name="mt-3"),
                        dbc.Checklist(
                            options=[{'label': v['title'], 'value': k} for k,v in MapHandler.TIPO_RECURSOS.items()],
                            value=list(MapHandler.TIPO_RECURSOS.keys()),
                            id="switches-recursos",
                            switch=True,
                        ),
                    ], className="mt-3"
                )
            ], md=12
            )
        ),
        dbc.Row(dbc.Col(dbc.Spinner(html.Div(id="loading-output", className="mt-5"),color="primary"), md=12)),        

                   
    ],
    id="filtros",
    className=" text-white mt-5"
)