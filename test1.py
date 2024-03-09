import streamlit as st
from streamlit_echarts import st_echarts
import pandas as pd
import numpy as np
import pydeck as pdk
from pydeck.types import String

x=0

df = pd.read_json("test2.json")
df1 = pd.read_json("test4.json")

r=pdk.Deck(
    map_style=None,
    initial_view_state=pdk.ViewState(
        latitude=20.5937,
        longitude=78.9629,
        zoom=4,
        pitch=0,
    ),
    layers=[
        pdk.Layer(
            "TextLayer",
            df,
            pickable=True,
            get_position="coordinates",
            get_text="name",
            get_size=16,
            get_color=[0, 0, 0],
            get_angle="degree",
            sdf=True,
            get_radius=30,
            # Note that string constants in pydeck are explicitly passed as strings
            # This distinguishes them from columns in a data set
            get_text_anchor=String("middle"),
            get_alignment_baseline=String("center"),
        ),
        pdk.Layer(
            "PathLayer",
            df1,
            pickable=True,
            get_path="path",
            get_color="color",
            width_scale=20,
            width_min_pixels=2,
            get_width=5,
        )
    ],
    tooltip={"html": "<b>Language:</b> {name}"},
)


data = {
    "name": "Indo-Aryan",
    "children": [
        {
            "name": "Old Indo-Aryan",
            "children": [
                {
                    "name": "Mittani-Aryan", "value": 3938,
                    "flag":1,
                },
                {
                    "name": "Early Old Indo-Aryan",
                    "children": [{"name": "Vedic-Sanskrit", "value": 7074}],
                },
                {
                    "name": "Late Old Indo-Aryan",
                    "children": [{"name": "Sanskrit", "value": 7074}],
                },
            ],
            # "collapsed": True,
        },
        {
            "name": "Middle Indo-Aryan",
            "children": [
                {
                    "name": "Dardic",
                    "children": [
                        {"name": "ArrayInterpolator", "value": 1983},
                    ],
                },
                {
                    "name": "North-Western Indo-Aryan",
                    "children": [
                        {"name": "ArrayInterpolator", "value": 1983},
                    ],
                },
                {
                    "name": "Northern Indo-Aryan",
                    "children": [
                        {"name": "ArrayInterpolator", "value": 1983},
                    ],
                },
                {
                    "name": "Western Indo-Aryan",
                    "children": [
                        {
                            "name": "North-Western Indo-Aryan",
                            "children": [
                                {"name": "ArrayInterpolator", "value": 1983},
                            ],
                        },
                    ],
                },
                {
                    "name": "Central Indo-Aryan",
                    "children": [
                        {"name": "ArrayInterpolator", "value": 1983},
                    ],
                },
                {
                    "name": "Transitional Central Indo-Aryan",
                    "children": [
                        {"name": "ArrayInterpolator", "value": 1983},
                    ],
                },
                {
                    "name": "Eastern Indo-Aryan",
                    "children": [
                        {"name": "ArrayInterpolator", "value": 1983},
                    ],
                },
                {
                    "name": "Transitional Eastern Indo-Aryan",
                    "children": [
                        {"name": "ArrayInterpolator", "value": 1983},
                    ],
                },
                {
                    "name": "Southern Indo-Aryan",
                    "children": [
                        {"name": "ArrayInterpolator", "value": 1983},
                    ],
                },
                {
                    "name": "Unclassified Indo-Aryan",
                    "children": [
                        {"name": "ArrayInterpolator", "value": 1983},
                    ],
                },
            ],
        },
    ],
}

opts = {
    "tooltip": {
        "trigger": "item",
        "triggerOn": "mousemove",
        # "formatter": "function (params) { return 'Parent: ' + params.name; }",
        # "formatter": "function(){ return 'yash';}"
    },
    "series": [
        {
            "type": "tree",
            "data": [data],
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
    # "events" : {
    #     "click": "function(para) { window.open('https://glottolog.org/'); console.log(para.data.name );  return para.name}"
    #     # "dblclick":"function(params) { return [params.type, params.name, params.value] }"
    # }
}

# opts["tooltip"] = {
#     "formatter": lambda api: "yash",
# }

events = {
    # "click": "function(para) { window.open('https://glottolog.org/'); console.log(para.data.name );  return para.name}"
    "click": "function(para) {  console.log(para.data.flag );  return para.data.flag}"
    # "dblclick":"function(params) { return [params.type, params.name, params.value] }"
}

# chart = st_echarts(opts,events=events, height=800)
# st.write(chart)
# print(chart)

def fun(x):
    if(x==0):
        chart = st_echarts(opts,events=events, height=800)
        print("in fun ",chart)
        return chart
    else:
        print("inside fun else ",x)
        st.pydeck_chart(r)


x=fun(x)

print("outside ",x)
if(x==1):
    print("yes")
    fun(x)