import dash_bootstrap_components as dbc
from dash import html

QueEs = html.Section(
    dbc.Container(
        [
            html.H2("¿Que es P.I.S?", className=""),
            html.Hr(className="my-2"),
            html.Br(),
            html.Video(src="https://www.youtube.com/watch?v=6hflhqRlSl8"),
            html.P(
                """
                    Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.
                    Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute
                    irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat
                    non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.
                """,
                className="",
            ),
        ],
        fluid=True,
        className="py-3 text-dark",
    ),
    className="text-center",
    id="que_es"
)
