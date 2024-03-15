import dash_echarts
import dash, random
from dash.dependencies import Input, Output
from dash import html
from dash import dcc
from dash.exceptions import PreventUpdate


app = dash.Dash(__name__)

data = {
    "name": "Indo-Aryan",
    "children": [
        {
            "name": "Old Indo-Aryan",
            "children": [
                {
                    "name": "Mittani-Aryan", "value": 3938,
                    "flag":0,
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
}
events = {
    "click": "function(para) { window.open('https://www.google.com/maps/'); console.log(para.data.name );  return para.name}",
}
app.layout = html.Div([
    dash_echarts.DashECharts(
        option = opts,
        event=events,
        id='echarts',
        style={
            "width": '100vw',
            "height": '100vh',
        }
    ),
    # dcc.Graph(id="line_graph")

])

# @app.callback(
#     Output("line_graph", "figure"),
#     Input("echarts", "clickData")
# )
# def create_graph(clickData):
#     print(clickData)
    # if clickData is None:
    #     district_name = "GHAZIABAD"
    # else:
    #     district_name = clickData["points"][0]["location"]

    # dff = df_data[df_lang["Districts"] == district_name]
    # fig = px.line(dff, x="Districts", y="Languages", markers=True)

    # return fig

    # @app.callback(
    #     Output('echarts', 'option'),
    #     [Input('interval', 'n_intervals')])
    # def update(n_intervals):
    #     if n_intervals == 0:
    #         raise PreventUpdate
    #     else:
    #         option['series'][0]['data'] = gen_randlist(200)
    #         option['series'][1]['data'] = gen_randlist(200)
    #     return option
    # app.run_server(debug=True)

if __name__ == '__main__':
    app.run_server(debug=True)