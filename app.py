
from dash import Dash, html, dcc
import dash_bootstrap_components as dbc
from components.navbar import navbar
from components.sidebar import sidebar
from pages import page1, page2

app = Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

app.layout = html.Div([
    navbar(),
    sidebar(),
    dcc.Location(id='url', refresh=False),
    html.Div(id='page-content')
])

@app.callback(
    dash.dependencies.Output('page-content', 'children'),
    [dash.dependencies.Input('url', 'pathname')]
)
def display_page(pathname):
    if pathname == '/page1':
        return page1.layout
    elif pathname == '/page2':
        return page2.layout
    return html.H1("Welcome to the Dashboard!", style={"textAlign": "center"})

if __name__ == '__main__':
    app.run_server(debug=True)
        