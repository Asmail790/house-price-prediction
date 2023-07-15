from dash import Dash, html, dash_table, dcc, callback, Output, Input
import plotly.express as px
import pandas as pd
import dash_bootstrap_components as dbc
from sklearn.linear_model import LinearRegression
import numpy as np
import pickle
df = pd.read_csv('train.csv')

reg:None | LinearRegression = None
with open("predictor.p","rb") as f:
    reg = pickle.load(f)



app = Dash(__name__,external_stylesheets=[dbc.themes.DARKLY])

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
    

if __name__ == '__main__':
    app.run(debug=True)