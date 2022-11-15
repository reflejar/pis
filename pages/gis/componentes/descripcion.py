from dash import html, Input, Output, callback

##### VARIABLES ######
var_pais = 'municipio'

Descripcion = html.Div(
    '',
    className="text-center section-title",
    id="descripcion"
)

@callback(
    Output("descripcion", "children"), 
    Input("select-municipio", "value")
)

def update_descripcion(municipios):

    sel_municipio = [c for c in municipios if c != '']


    if len(sel_municipio)>1:
        municipio = ", ".join(sel_municipio[:-1]) + ' y ' + f'{sel_municipio[-1]}'
    else:
        municipio = sel_municipio[0]


    mensaje_general =  html.H5([
            'El siguiente mapa es una proyección de la normativa vigente del municipio de ', 
            html.Span(f'{municipio}. ', className="text-bold bg-primary text-white"),  #html.I(f'{municipio}', className="text-bold text-primary")
            html.Br(),
            'En etapas sucesivas sumaremos otros municipios', 
            
    ])

    return mensaje_general
