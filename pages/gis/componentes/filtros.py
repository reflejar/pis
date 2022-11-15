from dash import html, dcc
import dash_bootstrap_components as dbc

MUNICIPIOS = ['Mar Chiquita']
TIPO_RECURSOS = ['Escuelas', 'Rios']

Filtros = html.Div(
    [
        html.H4("Filtros"), 
        dbc.Row([dbc.Col([
                    html.Label(htmlFor="select-municipio", title='Municipio'),
                    dcc.Dropdown(
                        id="select-municipio",
                        options=MUNICIPIOS,
                        multi=True,
                        searchable = True,
                        placeholder = 'Selecciona un municipio..',
                        value=["Mar Chiquita"],
                        clearable=True
                    )        
            ], md=12), 
                         
        ]),
        dbc.Row(dbc.Col([
                    html.Label(htmlFor="select-recurso", title='Recurso'),
                    dcc.Dropdown(
                        id="select-recurso",
                        options=TIPO_RECURSOS,
                        multi=True,
                        searchable=True,
                        placeholder = 'Selecciona un tipo de recurso..',
                        value=['Escuelas'],
                        clearable=True
                    )        
            ], md=12
            ))
                   
    ],
    id="filtros",
    className="bg-body"
)
