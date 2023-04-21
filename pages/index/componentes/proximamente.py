import dash_bootstrap_components as dbc
from dash import html


Proximamente = html.Section([
                dbc.Row(dbc.Col(html.H3("Proximamente", className="text-uppercase my-5 space-grotesk text-white"))),
                dbc.Row([
                    dbc.Col([
                        html.Img(src="/assets/img/recursos/buenos_aires.svg", height="120px", className="mt-5"),
                        html.H4("Un mapa lleno de PIS", className="text-white mt-3 fw-bold"),
                        html.P("Conocé los resultados de la campaña de testeos en orina y análisis en el ambiente para saber dónde y en qué medida se detectaron trazas de agroquímicos.", className="text-white px-1 mt-3")
                        
                    ], 
                    lg={'offset': 3, 'size': 3}),
                    dbc.Col([
                        html.Img(src="/assets/img/recursos/ranking.svg", height="120px", className="mt-5"),
                        html.H4("Ranking Normativo", className="text-white mt-3 fw-bold"),
                        html.P("Conocé en qué puesto del ranking normativo está la regulación de agroquímicos de tu territorio para saber cómo puede mejorar.", className="text-white px-1 mt-3")
                    ], 
                    lg=3),
                ], class_name="px-5"),
                dbc.Row([
                    dbc.Col([
                        html.Img(src="/assets/img/recursos/justicia.svg", height="120px", className="mt-5"),
                        html.H4("PIS también en la justicia", className="text-white mt-3 fw-bold"),
                        html.P("Descubrí el compendio de todos los fallos judiciales sobre el tema para saber en cuáles te podés apoyar y así exigir cambios.", className="text-white px-1 mt-3")
                        
                    ], 
                    lg={'offset': 3, 'size': 3}),
                    dbc.Col([
                        html.Img(src="/assets/img/recursos/normativo.svg", height="120px", className="mt-5"),
                        html.H4("PIS desde arriba", className="text-white mt-3 fw-bold"),
                        html.P("Desde una georreferenciación, conocé las restricciones municipales a las aplicaciones de agroquímicos para saber cuál está vigente en el lugar en que vivís.", className="text-white px-1 mt-3")
                    ], 
                    lg=3),
                ], class_name="px-5"),                
                dbc.Row(dbc.Col(html.H5("Suscribite a nuestro newsletter y seguí todos los lanzamientos.", className="mt-5 text-white "))),
                dbc.Row(dbc.Col(dbc.Button("Noticias sin spamear", color="primary", className="my-5 text-black p-3 text-uppercase ", href="https://preguntarparaacordar.typeform.com/to/B8k4SNx5", target="_blank"))),
            ],
            className="p-5 mb-5 text-center",
            id="index-herramientas",
)
