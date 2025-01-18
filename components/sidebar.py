
from dash import html
import dash_bootstrap_components as dbc

def sidebar():
    links = [
        dbc.NavLink("Page 1", href="/page1", active="exact"),
        dbc.NavLink("Page 2", href="/page2", active="exact"),
    ]
    return dbc.Nav(
        links,
        vertical=True,
        pills=True,
        style={"position": "fixed", "top": "70px", "left": "0", "width": "200px", "padding": "10px"}
    )
            