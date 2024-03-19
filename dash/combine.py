import plotly.express as px
import pandas as pd
from dash import Dash, dcc, Input, Output, html, callback, ctx
import json
import dash_echarts
from dash.exceptions import PreventUpdate
import tree_data
import numpy as np

df_data=pd.read_csv("data_refined.csv")
df_lang=pd.read_csv("lang_data.csv")
with open('refined.geojson') as response:
    geodata = json.load(response)

app = Dash(__name__)
app.config.suppress_callback_exceptions=True
app.layout = html.Div(children=[
    html.Div(className="row", children=[

        html.Div(className="six columns", children=[
            dcc.Dropdown(
                options=["tree","choro","choro_specific"],
                value="tree",
                id="dataframe_dropdown",
                style={"width": "40%"}
            )
        ])
    ]),

    html.Br(),

    html.Div(id="img"),
    

])

def generate_choro():
    fig = px.choropleth_mapbox(
                    df_data, 
                    geojson = geodata, 
                    locations = df_data.Districts, 
                    color = df_data["Languages"], 
                    featureidkey = "properties.District",
                    mapbox_style = "carto-positron",
                    center = {"lat": 22.5937, "lon": 82.9629},
                    hover_name="STATE",
                    hover_data=['STATE'],
                    zoom = 3.0,
                    opacity = 1.0
                    )
    fig.update_layout(autosize=False,
                height=700,
                width=600,
                margin={"r":0,"t":0,"l":0,"b":0})


    return [dcc.Graph(id="lang_map",figure=fig),html.Br(),dcc.Graph(id="dist_lang",style={'display':'inline-block'}),dcc.Graph(id="state_lang",style={'display':'inline-block'}),dcc.Dropdown(
                options=np.append(df_lang['Languages'].dropna().unique(),["NO CHOOSEN",]),
                value="NO CHOOSEN",
                id="lang_dropdown",
                style={"width": "40%"}
            )]

def generate_tree():
    opts = {
        "tooltip": {
            "trigger": "item",
            "triggerOn": "mousemove",
            'formatter': '{b}'
        },
        "series": [
            {
                "type": "tree",
                "data": [tree_data.data],
                "top": "1%",
                "left": "10%",
                "bottom": "1%",
                "right": "20%",
                "symbolSize": 7,
                "label": {
                    "position": "bottom",
                    "verticalAlign": "middle",
                    "align": "right",
                    "fontSize": 10,
                    "color": "black",
                },
                "leaves": {
                    "label": {
                        "position": "right",
                        "verticalAlign": "middle",
                        "align": "left",
                    }
                },
                # "emphasis": {
                #     "focus": 'descendant'
                # },
                "expandAndCollapse": True,
                "animationDuration": 550,
                "animationDurationUpdate": 750,
            },
            
        ],
    }
    fig=dash_echarts.DashECharts(
        option = opts,
        id='echarts',
        style={
            "width": '100vw',
            "height": '100vh',
        }
    )
    return fig

def generate_choro_specific():
    return [dcc.Dropdown(
                options=np.append(df_lang['Languages'].dropna().unique(),["NO CHOOSEN",]),
                value="NO CHOOSEN",
                id="major_lang_dropdown",
                style={"width": "40%"}
            ),dcc.Graph(id="choro_lang")]

@app.callback(
        Output("choro_lang", "figure"),
        [Input("major_lang_dropdown","value")]
)
def create_graph2(major_lang_dropdown):
    df_specific=df_data[df_data["Languages"] == major_lang_dropdown]
    fig = px.choropleth_mapbox(
                    df_specific, 
                    geojson = geodata, 
                    locations = df_specific.Districts, 
                    color = df_specific["Languages"], 
                    featureidkey = "properties.District",
                    mapbox_style = "carto-positron",
                    center = {"lat": 22.5937, "lon": 82.9629},
                    hover_name="STATE",
                    hover_data=['STATE'],
                    zoom = 3.0,
                    opacity = 1.0
                    )
    fig.update_layout(autosize=False,
                height=700,
                width=600,
                margin={"r":0,"t":0,"l":0,"b":0})
    return fig

@app.callback(
    Output("dist_lang", "figure"),
    [Input("lang_map", "clickData"),
    Input("dataframe_dropdown", "value"),
    Input("lang_dropdown","value")]
    # Input("lang_map", "hoverData"),
    # prevent_initial_call=True,
    # suppress_callback_exceptions=True
)
def create_graph(clickData,dataframe_dropdown,lang_dropdown):
    if dataframe_dropdown=="tree":
        return 
    elif lang_dropdown!="NO CHOOSEN" :
        df1=df_lang[df_lang["Languages"] == lang_dropdown]
        fig = px.line(df1, x="Districts", y="Languages", markers=True)
        return fig
    if clickData is None:
        district_name = "GHAZIABAD"
    else:
        district_name = clickData["points"][0]["location"]

    dff = df_lang[df_lang["Districts"] == district_name]
    fig = px.line(dff, x="Districts", y="Languages", markers=True)
    fig.update_layout(width=600)
    return fig

@app.callback(
        Output("lang_dropdown","value"),
        Input("lang_map","clickData")
)
def update_prev_click(clickData):
    return  "NO CHOOSEN"

@app.callback(
    Output("state_lang", "figure"),
    [Input("lang_map", "clickData"),
    Input("dataframe_dropdown", "value")]
)
def create_graph1(clickData,dataframe_dropdown):
    if dataframe_dropdown=="tree":
        return 
    if clickData is None:
        state_name = "RAJASTHAN"
    else:
        state_name = clickData["points"][0]["customdata"][0]

    dff = df_data[df_data["STATE"] == state_name]
    fig = px.line(dff, x="Districts", y="Languages", markers=True)
    fig.update_layout(width=800)

    return fig

@app.callback(
    Output("img", "children"),
    Input("dataframe_dropdown", "value"),
    # suppress_callback_exceptions=True
)
def update(dataframe_dropdown):
    if dataframe_dropdown=="tree":
        return generate_tree()
    elif dataframe_dropdown=="choro":
        return generate_choro()
    else:
        return generate_choro_specific()

if __name__ == "__main__":
    print(df_lang['Languages'].unique())
    app.run_server(debug=True)
