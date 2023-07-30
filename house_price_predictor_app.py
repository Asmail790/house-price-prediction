from dash import Dash, html
import dash_bootstrap_components as dbc
from componets import house_price,create_inputs 


app = Dash(__name__,external_stylesheets=[dbc.themes.CYBORG])
flask_app = app.server

app.layout = html.Div([
    create_inputs(),
    house_price(),
])

def create_app():
    return flask_app


if __name__ == '__main__':
    app.run(debug=False)
