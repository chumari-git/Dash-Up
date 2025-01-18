
from dash import html
import dash_bootstrap_components as dbc

def navbar():
    return dbc.NavbarSimple(
        brand="My Dashboard",
        brand_href="/",
        color="primary",
        dark=True
    )
            