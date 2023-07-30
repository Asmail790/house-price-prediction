
import os
import sys

import pandas as pd
from dash import html, dcc, callback, Output, Input
from dash_daq import BooleanSwitch
import pickle

from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PowerTransformer

from groups import DATAFIELDS_DESC, DESC_KEY,FIELD_TYPE,MAX,MIN,VALUES_DESC_KEY

def price_str(price):
        if price is None:
            return "Price:"
        else:
            return f"Price:{price:.2f} $"
     

def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)


def load_model():
    with open(resource_path("model.p"),"rb") as f:
       model:LinearRegression = pickle.load(f)
    return model 

def load_transformers():
    with open(resource_path("transformers.p"),"rb") as f:
       transfomers:tuple[PowerTransformer,PowerTransformer] = pickle.load(f)
    return transfomers 


def load_defaults():
    return pd.read_csv(resource_path("defaults.csv"), index_col=0)



defaults_df = load_defaults()
transformers = load_transformers()
model = load_model()



from itertools import groupby

def create_inputs():
    def get_type(field):
        return DATAFIELDS_DESC[field][FIELD_TYPE]
    
    def get_drop_down_values(field):
        return DATAFIELDS_DESC[field][VALUES_DESC_KEY].values()
    
    def get_description(field):
        return DATAFIELDS_DESC[field][DESC_KEY]

    children: list[html.Div] = []

    fields = defaults_df.columns


    fields_sorted_by_type = sorted(fields,key=get_type)
    field_grouped_by_type = groupby(fields_sorted_by_type ,key=get_type)
    field_grouped_by_type = {k:list(g) for k, g in field_grouped_by_type}

    if "checkbox" in field_grouped_by_type:
        for field  in field_grouped_by_type["checkbox"]:
            componet = BooleanSwitch(
                on=defaults_df[field].iloc[0],
                label=get_description(field),
                labelPosition="top",
                id=field
            )
            children.append(componet)
    

    if "number" in field_grouped_by_type:
        for field in field_grouped_by_type["number"]:
            attributes = {"type":"number", "value":defaults_df[field].iloc[0]}


            if MAX in DATAFIELDS_DESC[field]:
                attributes["max"] = DATAFIELDS_DESC[field][MAX]  

            if MIN in DATAFIELDS_DESC[field]:
                attributes["min"] = DATAFIELDS_DESC[field][MIN] 
                         

            componet = dcc.Input(**attributes, id=field)

            wrapper = html.Div([
                html.Label(get_description(field)),
                componet
            ],
            style={
            "display": "flex",
            "flex-direction": "column"
            })
            
            children.append(wrapper)
    
    if "dropdown" in field_grouped_by_type:
         
        for field in field_grouped_by_type["dropdown"]:
            
            default_index = int(defaults_df[field].iloc[0])

            options = list(get_drop_down_values(field))
            componet = dcc.Dropdown(options,options[default_index] ,id=field ) 
            
            wrapper = html.Div([
                html.Label(get_description(field)),
                componet
            ],
            style={
            "display": "flex",
            "flex-direction": "column"
            })

            children.append(wrapper)

    attributes = html.Div(children=children, style={
        "display": "flex",
        "flex-direction": "row",
        "flex-wrap": "nowrap",
        "justify-content": "space-around",
        "margin":"30px"
    })

    return attributes


"""def create_inputs():
    group_componets: list[html.Div] = []
    for group_name in groups:
        group = create_group(groups[group_name],group_name,defaults)
        group_componets.append(group)

    return html.Div(children=group_componets, style={
        "display": "flex",
        "flex-direction": "row",
        "justify-content": "space-around",
        "flex-wrap": "nowrap",
        "margin-bottom": "50px"
    })
"""

def house_price():
    return html.Div(
        html.H2("", id="house-price"),
        style={
            "display": "flex",
            "flex-direction": "col",
            "justify-content": "center",
            "flex-wrap": "nowrap",
        }
    )


inputs1={col: Input(component_id=f'{col}', component_property='value') for col in defaults_df.columns if defaults_df[col].dtype != bool}
inputs2 = {col: Input(component_id=f'{col}', component_property='on') for col in defaults_df.columns if defaults_df[col].dtype == bool}


@callback(
    Output(component_id='house-price', component_property='children'),
    inputs={**inputs1,**inputs2}

    )
def update_price(**kwargs):
    kwargs = {k:[v] for k,v in kwargs.items()}
  

    if any(map(lambda x: x[0] is None, kwargs.values())):
        return "Fill in all inputs"
    else:
        price = predict_price(kwargs)
        return price_str(price)

#TODO check why so high price for bath_room
def predict_price(data:dict):
    df = pd.DataFrame(data)
    df = df[defaults_df.columns]
    matrix = df.to_numpy()
    x_transformer = transformers[0]
    y_transformer = transformers[1]
    matrix = x_transformer.transform(matrix)
    y = model.predict(matrix)
    predict_price = y_transformer.inverse_transform(y)
    
    return predict_price.squeeze().item()