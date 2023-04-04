import dash_bootstrap_components as dbc
from dash import html


Proximamente = html.Section([
                dbc.Row(dbc.Col(html.H3("Proximamente", className="text-uppercase my-5 space-grotesk text-white"))),
                dbc.Row([
                    dbc.Col([
                        html.Img(src="/assets/img/recursos/buenos_aires.svg", height="120px"),
                        html.H4("Un mapa lleno de PIS", className="text-white mt-3 "),
                        html.P("Mapeo de resultados de la campaña de testeo y análisis de agua, suelo, sangre y orina existentes en los distintos.", className="text-white ")
                        
                    ], 
                    md={'offset': 2, 'size': 4}),
                    dbc.Col([
                        html.Img(src="/assets/img/recursos/ranking.svg", height="120px"),
                        html.H4("Ranking Normativo", className="text-white mt-3 "),
                        html.P("Las normativas rankeadas sobre el nivel de protección de las distintas regulaciones de agroquímicos en PBA.", className="text-white ")
                    ], 
                    md=4),
                ], class_name="px-5"),
                dbc.Row([
                    dbc.Col([
                        html.Img(src="/assets/img/recursos/justicia.svg", height="120px"),
                        html.H4("PIS también en la justicia", className="text-white mt-3 "),
                        html.P("Compendio de toda los fallos judiciales sobre el tema.", className="text-white ")
                        
                    ], 
                    md={'offset': 2, 'size': 4}),
                    dbc.Col([
                        html.Img(src="/assets/img/recursos/normativo.svg", height="120px"),
                        html.H4("PIS desde arriba", className="text-white mt-3 "),
                        html.P("Georreferenciación de las restricciones munipales a las aplicaciones de agroquímicos.", className="text-white ")
                    ], 
                    md=4),
                ], class_name="px-5"),                
                dbc.Row(dbc.Col(html.H5("Si querés estar al tanto de cada uno de los lanzamientos, suscribite a nuestro newsletter.", className="mt-5 text-white "))),
                dbc.Row(dbc.Col(dbc.Button("Noticias sin spamear", color="primary", className="my-5 text-black p-3 text-uppercase ", href="https://preguntarparaacordar.typeform.com/to/B8k4SNx5", target="_blank"))),
            ],
            className="p-5 mb-5 text-center",
            id="index-herramientas",
)
