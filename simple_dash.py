from dash import Dash, html, dash_table, dcc, callback, Output, Input
import plotly.express as px
import pandas as pd
import dash_bootstrap_components as dbc
from sklearn.linear_model import LinearRegression
import numpy as np
import pickle
import os
import sys

def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)


reg:None | LinearRegression = None

file_path = resource_path("predictor.p")
with open(file_path,"rb") as f:
    reg = pickle.load(f)



app = Dash(__name__,external_stylesheets=[dbc.themes.DARKLY])
flask_app =  app.server

app.layout = html.Div([
    html.Div(children='Hello World'),
    dcc.Input( type="number", value=0,min=0,id='controls-and-radio-item'),
    html.Plaintext(id="plain-text")
])

@callback(
    Output(component_id='plain-text', component_property='children'),
    Input(component_id='controls-and-radio-item', component_property='value')
)
def update_graph(x):
    x = np.array([x]).reshape((-1,1))
    y = reg.predict(x)
    y = np.squeeze(y)
    return f'estimated house cost: {y}'
    

def create_app():
   return flask_app

if __name__ == '__main__':
    app.run(debug=False)





   