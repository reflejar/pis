from dash import html, dcc
import dash_bootstrap_components as dbc

MUNICIPIOS = ['Mar Chiquita']
TIPO_RECURSOS = {
    'cursos-agua': 'Cursos de agua',
    'cuerpos-agua': 'Cuerpos de agua',
    'escuelas': 'Escuelas',
    'radio-escuelas': 'Radio escuelas',
    'ciudades': 'Ciudades',
    'apiario': 'Apiario',
    'zonas-de-exclusion': 'Zonas de exclusión',
}

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
                        options=MUNICIPIOS,
                        multi=True,
                        searchable = True,
                        placeholder = 'Selecciona un municipio..',
                        value=["Mar Chiquita"],
                        clearable=True,
                        style={
                            'background-color': 'black',
                            'color': 'var(--primary)'
                        }
                    )        
            ], md=12), 
                         
        ]),    
        dbc.Row(
            dbc.Col([
                html.Div(
                    [
                        dbc.Checklist(
                            options=[{'label': v, 'value': k} for k,v in TIPO_RECURSOS.items()],
                            value=list(TIPO_RECURSOS.keys()),
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
