from dash import Dash, html, dash_table, dcc, callback, Output, Input
import plotly.express as px
import pandas as pd
import dash_bootstrap_components as dbc
from sklearn.linear_model import LinearRegression
import numpy as np
import pickle
import os
import sys
import plotly.graph_objects as go
from componets import create_groups,house_price, graph

def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)


reg: None | LinearRegression = None

file_path = resource_path("predictor.p")
with open(file_path, "rb") as f:
    reg = pickle.load(f)



app = Dash(__name__,external_stylesheets=[dbc.themes.CYBORG])
flask_app = app.server

app.layout = html.Div([
    create_groups(),
    house_price(),
   graph()
])

"""@callback(
    Output(component_id='example-graph', component_property='figure'),
    inputs={
        "x": Input(component_id='controls-and-radio-item', component_property='value'),
        "y": Input(component_id='second-input', component_property='value')
    }
)
def create_graph(x: int, y: int):
    df = pd.DataFrame(data={"tip": [x], "total_bill": [y]})

    fig1 = px.strip(df, x=["tip", "total_bill"]). \
        update_traces(
        jitter=0,
        marker=dict(color="red", symbol="circle"),
    )

    fig2 = px.box(info, x=["tip", "total_bill"])
    fig = go.Figure(data=fig2.data + fig1.data)
    return fig
"""

def create_app():
    return flask_app


if __name__ == '__main__':
    app.run(debug=True, dev_tools_hot_reload=True)
