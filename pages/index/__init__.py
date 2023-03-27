
from dash import html

import dash_bootstrap_components as dbc

from .componentes.hero import Hero
from .componentes.testeando import Testeando
from .componentes.proximamente import Proximamente
from .componentes.faqs import FAQs
from .componentes.donar import Donar
from .componentes.orgas import Orgas


layout = html.Div(
        children=[
            Hero,
            Testeando,
            Proximamente,
            FAQs,
            Donar,
            Orgas,
        ]
    )