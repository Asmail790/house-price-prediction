import pandas as pd
from dash import html, dcc, callback, Output, Input
import plotly.express as px
import plotly.graph_objects as go

from groups import DATAFIELDS_DESC, DESC_KEY, groups, COLUMNS
from typing import Final

price_formatter = lambda price: f"Expected house price:{(price if price else '?')}$"

data = pd.DataFrame({g: [1, 2, 3, 4, 5] for g in COLUMNS})
cofficents = pd.Series(
    (i +
     1 for i in range(
         len(COLUMNS))),
    index=(
        g for g in COLUMNS))
data = data.fillna(method="backfill") * cofficents.fillna(0)
fig_effect_plot: Final = px.box(data, x=COLUMNS,)


def __get_type(field_name: str):
    return pd.Int64Dtype


def create_attributes(group):
    attributes: dict[str, dict[str, any]] = {}
    for field in groups[group]:
        field_type = __get_type(field)
        if pd.api.types.is_numeric_dtype(field_type):
            attributes[field] = dict(
                type="number",
                id=f'field-{field}',
                required=True,
                min=1,
                value=data[field].mean()
            )

        elif pd.api.types.is_categorical_dtype(field_type):
            pass
        else:
            pass
    return attributes


def create_group(group: str):
    attributes = create_attributes(group)
    children: list[html.Div] = []

    for field in groups[group]:
        children.append(html.Div([
            html.Label(DATAFIELDS_DESC[field][DESC_KEY]),
            dcc.Input(**attributes[field])
        ], style={
            "display": "flex",
            "flex-direction": "column"
        }))

    attributes = html.Div(children=children, style={
        "display": "flex",
        "flex-direction": "column",
        "flex-wrap": "nowrap",
        "justify-content": "space-around",
        "height": "100%",
    })

    return html.Div(children=[html.H1(group), attributes], style={
        "display": "flex",
        "flex-direction": "column",
        "flex-wrap": "nowrap",
        "justify-content": "start",
    })


def create_groups():
    group_componets: list[html.Div] = []
    for group_name in groups:
        group = create_group(group_name)
        group_componets.append(group)

    return html.Div(children=group_componets, style={
        "display": "flex",
        "flex-direction": "row",
        "justify-content": "space-around",
        "flex-wrap": "nowrap",
        "margin-bottom": "50px"
    })


def house_price():

    return html.Div(
        html.H2(price_formatter(None), id="house-price"),
        style={
            "display": "flex",
            "flex-direction": "col",
            "justify-content": "center",
            "flex-wrap": "nowrap",
            "margin-bottom": "50px"
        }
    )


def graph():
    return dcc.Graph(figure=fig_effect_plot, id='example-graph')


@callback(
    Output(component_id='example-graph', component_property='figure'),
    inputs={col: Input(component_id=f'field-{col}', component_property='value')
            for col in COLUMNS
            }
)
def update_striplot(**kwargs):

    # TODO make as decorator
    if any(map(lambda x: x is None, kwargs.values())):
        return go.Figure()

    df = pd.DataFrame(data=kwargs, index=kwargs.keys())

    strip_plot = px.strip(df, x=COLUMNS).update_traces(
        jitter=0,
        marker=dict(
            color="red",
            symbol="circle"
        ),
    )
    fig = go.Figure(data=strip_plot.data + fig_effect_plot.data)
    return fig.update_layout(
        title_text='Effect plot',
        title_x=0.5,
        font_size=20,
        xaxis_title="Sale Price $",
        yaxis_title="Properties",
        hovermode=False
        )


@callback(
    Output(component_id='house-price', component_property='children'),
    inputs={col: Input(component_id=f'field-{col}', component_property='value')
            for col in COLUMNS
            }
)
def update_price(**kwargs):
    if any(map(lambda x: x is None, kwargs.values())):
        return "?"
    else:
        estimiated_price = sum(kwargs.values())
        return price_formatter(estimiated_price)
