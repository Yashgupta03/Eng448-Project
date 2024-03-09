import streamlit as st
from streamlit_echarts import st_echarts

data = {
    "name": "Indo-Aryan",
    "children": [
        {
            "name": "Old Indo-Aryan",
            "children": [
                {
                    "name": "Mittani-Aryan", "value": 3938,
                    # "events": [{"click": "function() {window.open('https://www.google.com)}"}]
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
        # "formatter": "function(){ return 'yash';}"
    },
    "series": [
        {
            "type": "tree",
            "data": [data],
            "top": "1%",
            "left": "7%",
            "bottom": "1%",
            "right": "20%",
            "symbolSize": 7,
            "label": {
                "position": "left",
                "verticalAlign": "middle",
                "align": "right",
                "fontSize": 9,
            },
            "leaves": {
                "label": {
                    "position": "right",
                    "verticalAlign": "middle",
                    "align": "left",
                }
            },
            "expandAndCollapse": True,
            # "nodeClick": 'https://www.google.com/',
            "animationDuration": 550,
            "animationDurationUpdate": 750,
        }
    ],
}

# opts["tooltip"] = {
#     "formatter": lambda api: "yash",
# }

events = {
    "click": "function(para) { console.log(para.data.name );  return para.name}"
    # "dblclick":"function(params) { return [params.type, params.name, params.value] }"
}

chart = st_echarts(opts,events=events, height=800)
