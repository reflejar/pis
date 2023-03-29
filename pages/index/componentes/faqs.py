import dash_bootstrap_components as dbc
from dash import html, callback, Input, Output, State

FAQs = html.Section([
            dbc.Row(dbc.Col(html.H1("FAQs", className="text-uppercase my-5 text-black"))),
            dbc.Row("", id="index-faqs-react"),
            ],
            className="p-5 h-50 bg-white",
            id="index-faqs",
)
