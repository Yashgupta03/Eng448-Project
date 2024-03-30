import plotly.express as px
import pandas as pd
from dash import Dash, dcc, Input, Output, html
import json
import dash_echarts
import tree_data
import home_page
import numpy as np
import flask
from pathlib import Path
import plotly 


HERE = Path(__file__).parent

df_refined=pd.read_csv("data_refined.csv")
df_dialects=pd.read_csv("lang_dialects.csv")
with open('assets/update.geojson') as response:
    geodata = json.loads(response.read())

app = Dash(__name__)
app.config.suppress_callback_exceptions=True
app.layout = html.Div(children=[
    html.Div(className="row", children=[

        html.Div(className="six columns", children=[html.Label(['Mode:']),
            dcc.Dropdown(
                options=["Home Page","Language Tree","Language Specific","Language Distribution"],
                value="Home Page",
                id="dataframe_dropdown",
                style={"width": "40%"}
            )
        ])
    ]),
    html.Br(),
    html.A(html.Button("Physical Map"), href="/get_report", target="_blank"),

    html.Br(),
    html.Div(id="img")
])

@app.server.route("/get_report")
def get_report():
    return flask.send_from_directory(HERE, "physical_streamlit.html")

color_map={
    "NO": 'Grey',
    "DRAVIDIAN":'Grey',
    "KHETRANI": 'Grey',
    "SINO TIBETAN":"Grey",
    "ANGIKA": 'rgb(102,73,169)',
    "ASSAMESE": 'rgb(23,194,200)',
    "AWADHI": 'rgb(212,108,173)',
    "BAGHATI": 'rgb(189,214,229)',
    "BAGHELI": 'rgb(237,205,173)',
    "BAGRI": 'rgb(126,172,19)',
    "BAJJIKA": 'rgb(30,144,255)',
    "BASHKARIK": 'rgb(255,187,219)',
    "BENGALI": 'rgb(106,207,81)',
    "BHADRAWA HI-KHASHALI-BHALESI": 'rgb(112,80,128)',
    "BHATRI": 'rgb(255,235,159)',
    "BHATTI": 'rgb(170,204,207)',
    "BHILI": 'rgb(103,65,118)',
    "BHOJPURI": 'rgb(47,79,79)',
    "BISHNUPRIYA": 'rgb(69,164,230)',
    "BRAJ": 'rgb(255,127,80)',
    "BUNDELI": 'rgb(142,36,107)',
    "BURUSHASKI": 'rgb(204,204,0)',
    "CHAMEALI AND CHURAHI": 'rgb(63,224,208)',
    "CHHATTISGARHI": 'rgb(208,92,107)',
    "DHANNI": 'rgb(160,158,237)',
    "DHUNDARI": 'rgb(40,160,166)',
    "DHUNDHARI": 'rgb(230,216,171)',
    "DODA SIRAJI": 'rgb(181,216,166)',
    "DOGRI": 'rgb(255,99,71)',
    "EASTERN PUNJABI": 'rgb(76,175,80)',
    "GARHWALI": 'rgb(29,105,108)',
    "GAWARBATI": 'rgb(60,141,230)',
    "GODWARI": 'rgb(9,6,180)',
    "GONDI": 'rgb(241,43,179)',
    "GUJARATI": 'rgb(58,225,196)',
    "HALBI": 'rgb(138,224,74)',
    "HANDURI": 'rgb(245,15,118)',
    "HARAUTI": 'rgb(50,178,233)',
    "HARYANVI": 'rgb(207,112,51)',
    "HINDI": 'rgb(64,212,195)',
    "HINDKO": 'rgb(206,146,236)',
    "JAUNSARI": 'rgb(61,184,146)',
    "KACHCHHI": 'rgb(84,176,186)',
    "KAGANI": 'rgb(250,60,164)',
    "KALASHA": 'rgb(4,177,74)',
    "KANGRI": 'rgb(45,139,178)',
    "KANNAUJI": 'rgb(184,77,162)',
    "KASHMIRI": 'rgb(120,253,135)',
    "KASHTAWARI": 'rgb(25,42,109)',
    "KAURAVI": 'rgb(183,11,140)',
    "KHANDESHI": 'rgb(223,39,177)',
    "KHOWAR": 'rgb(249,131,85)',
    "KIUNTHALI (MAHASUI)": 'rgb(96,246,109)',
    "KOCHI AND SATLEJ GROUP": 'rgb(117,117,66)',
    "KONKANI": 'rgb(121,159,16)',
    "KULUI": 'rgb(190,14,94)',
    "KUMAUNI": 'rgb(22,247,248)',
    "MAGAHI": 'rgb(41,97,8)',
    "MAITHILI": 'rgb(132,2,170)',
    "MAIYA": 'rgb(45,17,252)',
    "MALVI": 'rgb(144,102,159)',
    "MANDEALI": 'rgb(58,218,122)',
    "MARATHI": 'rgb(7,103,84)',
    "MARWARI": 'rgb(176,161,22)',
    "MEWARI": 'rgb(164,175,227)',
    "MEWATI": 'rgb(166,214,37)',
    "NEPALI": 'rgb(125,210,227)',
    "NIMADI": 'rgb(119,121,228)',
    "ORIYA": 'rgb(107,81,4)',
    "PADARI": 'rgb(41,11,190)',
    "PAHARI POTHWARI": 'rgb(165,112,5)',
    "PANGWALI": 'rgb(19,132,214)',
    "POTHOHARI": 'rgb(71,96,253)',
    "PUNCHCHIL": 'rgb(140,184,148)',
    "PUNJABI": 'rgb(235,178,148)',
    "RAMBANI": 'rgb(139,56,204)',
    "SADANI": 'rgb(140,83,19)',
    "SARAIKI": 'rgb(51,186,63)',
    "SHAHPURI": 'rgb(119,197,141)',
    "SHINA": 'rgb(147,171,140)',
    "SINDHI": 'rgb(61,233,163)',
    "SINHALESE": 'rgb(186,35,186)',
    "SIRAIKI": 'rgb(167,249,95)',
    "SIRMAURI": 'rgb(227,4,28)',
    "TORWALI": 'rgb(240,21,92)',
    "VAGDI": 'rgb(179,101,106)',
    "VARLI": 'rgb(251,71,239)',
    "WESTERN PUNJABI": 'rgb(74,232,181)',



}
fig_gl = px.choropleth_mapbox(
                df_refined, 
                geojson = geodata, 
                locations = df_refined.Districts, 
                color = df_refined["Languages"],
                color_discrete_sequence = plotly.express.colors.get_colorscale('Viridis'), 
                color_discrete_map=color_map,
                featureidkey = "properties.District",
                mapbox_style = "carto-positron",
                center = {"lat": 22.5937, "lon": 82.9629},
                hover_name="STATE",
                hover_data=['STATE'],
                zoom = 3.0
                )
fig_gl.update_layout(autosize=False,
            height=700,
            width=1000,
            margin={"r":0,"t":0,"l":0,"b":0},
            )
fig_gl.update_traces(marker_line_width=0.3)
h_choro=dcc.Graph(id="lang_map",figure=fig_gl)
h_g1=dcc.Graph(id="dist_lang")
h_g2=dcc.Graph(id="state_lang")
h_b1=html.Div([html.Label(['Language:']),dcc.Dropdown(options=np.append(df_refined['Languages'].dropna().unique(),["NO CHOOSEN",]),
            value="NO CHOOSEN",
            placeholder="Select a Language",
            id="lang_dropdown",
            style={"width": "40%"}
        )])

h_b2=html.Div([html.Label(['Districts:']),dcc.Dropdown(options=np.append(df_refined['Districts'].dropna().unique(),["NO CHOOSEN",]),
            value="NO CHOOSEN",
            placeholder="Select a District",
            id="district_dropdown",
            style={"width": "40%"}
        )])
h_d1=html.Div([h_choro,html.Br(),h_b1,html.Br(),h_b2],style={"display":"flex","flexDirection":"column"})
h_d2=html.Div([h_g1,h_g2],style={"display":"flex","flexDirection":"column"})
h_d3=html.Div([h_d1,h_d2],style={"display":"flex"})

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
    return [html.Label(['Language:']),dcc.Dropdown(
                options=np.append(df_refined['Languages'].dropna().unique(),["NO CHOOSEN",]),
                value="NO CHOOSEN",
                id="major_lang_dropdown",
                style={"width": "40%"}
            ),html.Div([dcc.Graph(id="choro_lang"),dcc.Graph(id="dialect_dist")],style={"display":"flex"})]

@app.callback(
        Output("choro_lang", "figure"),
        [Input("major_lang_dropdown","value")]
)
def create_choro_specific(major_lang_dropdown):
    df_sp1=df_refined.copy()
    df_sp1.loc[df_sp1["Languages"] != major_lang_dropdown, "Languages"] = "Not Selected"
    color_map={
        "Not Selected": 'White',
        major_lang_dropdown : 'Red',
    }
    fig = px.choropleth_mapbox(
                    df_sp1, 
                    geojson = geodata, 
                    locations = df_sp1.Districts, 
                    color = df_sp1["Languages"], 
                    color_discrete_map=color_map,
                    featureidkey = "properties.District",
                    mapbox_style = "carto-positron",
                    center = {"lat": 22.5937, "lon": 81.0629},
                    hover_name="STATE",
                    zoom = 3.0,
                    opacity = 1.0,
                    )
    fig.update_layout(autosize=False,
                height=700,
                width=1000,
                margin={"r":0,"t":0,"l":0,"b":0},
                )
    return fig

@app.callback(
        Output("dialect_dist", "figure"),
        [Input("major_lang_dropdown","value")]
)
def create_graph2(major_lang_dropdown):
    dff = df_dialects[df_dialects["Dialect Name"] == major_lang_dropdown]
    t="Dialects vs Districts for language: "+major_lang_dropdown
    fig = px.scatter(dff, x="Districts", y="Dialects",hover_name="Dialect Name",title=t)
    return fig


@app.callback(
    Output("dist_lang", "figure"),
    [Input("lang_map", "clickData"),
    Input("dataframe_dropdown", "value")]
)
def create_graph(clickData,dataframe_dropdown):
    if dataframe_dropdown=="Language Tree":
        return 
    if clickData is None:
        district_name = "DELHI_TOTAL"
    else:
        district_name = clickData["points"][0]["location"]

    dff = df_dialects[df_dialects["Districts"] == district_name]
    fig = px.scatter(dff, x="Dialects", y="Dialect Name",hover_name="Dialect Name")
    return fig

@app.callback(
        Output("lang_dropdown","value"),
        Input("lang_map","clickData"),
        Input("district_dropdown","value")
)
def update_lang_dropdown(clickData,district_dropdown):
    return  "NO CHOOSEN"

@app.callback(
        Output("district_dropdown","value"),
        Input("lang_map","clickData")
)
def update_district_dropdown(clickData):
    return  "NO CHOOSEN"

@app.callback(
    Output("state_lang", "figure"),
    [Input("lang_map", "clickData"),
    Input("dataframe_dropdown", "value"),
    Input("lang_dropdown","value"),
    Input("district_dropdown","value")
    ]
)
def create_graph1(clickData,dataframe_dropdown,lang_dropdown,district_dropdown):
    if dataframe_dropdown=="Language Tree":
        return 
    elif lang_dropdown!="NO CHOOSEN" :
        dff = df_dialects[df_dialects["Dialect Name"] == lang_dropdown]
        fig = px.scatter(dff, x="Districts", y="Dialects",hover_name="Dialect Name")
        return fig
    elif district_dropdown!="NO CHOOSEN" :
        state_name=df_refined.loc[df_refined['Districts'] == district_dropdown, 'STATE'].iloc[0]
        dff = df_refined[df_refined["STATE"] == state_name]
        fig = px.scatter(dff, x="Districts", y="Languages",hover_name="Languages")
        return fig
    if clickData is None:
        state_name = "DELHI"
    else:
        state_name = clickData["points"][0]["customdata"][0]

    dff = df_refined[df_refined["STATE"] == state_name]
    fig = px.scatter(dff, x="Districts", y="Languages",hover_name="Languages")

    return fig

@app.callback(
    Output("img", "children"),
    Input("dataframe_dropdown", "value")
)
def update(dataframe_dropdown):
    if dataframe_dropdown=="Home Page":
        return home_page.h_home_page
    elif dataframe_dropdown=="Language Tree":
        return generate_tree()
    elif dataframe_dropdown=="Language Distribution":
        return h_d3
    else:
        return generate_choro_specific()

if __name__ == "__main__":
    app.run_server(debug=True)
