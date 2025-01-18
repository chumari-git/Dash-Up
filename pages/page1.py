
from dash import html, dcc

layout = html.Div([
    html.H2("Page 1"),
    dcc.Graph(
        figure={
            "data": [
                {"x": [1, 2, 3], "y": [4, 1, 2], "type": "bar", "name": "Bar Chart"}
            ],
            "layout": {"title": "Sample Chart"}
        }
    )
])
            