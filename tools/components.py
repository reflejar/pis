from dash import html
import dash_bootstrap_components as dbc

import plotly.express as px

NoHayDatos = {
    'alert': dbc.Alert([
            html.I(className="bi bi-exclamation-triangle"), #bi-exclamation-octagon
            html.Br(),        
            html.P(f'No existen datos para los filtros solicitados.'),         
        ], 
        color="light",
        class_name="border-danger text-danger"
    ),
    'bar': px.bar(),
    'funnel': px.funnel(),
    'line': px.line(),
    'pie': px.pie(),
}
