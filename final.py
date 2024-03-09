import streamlit as st
from streamlit_option_menu import option_menu
import streamlit.components.v1 as html
from  PIL import Image
import numpy as np
import pandas as pd
from st_aggrid import AgGrid
from raceplotly.plots import barplot
from collections import deque
import plotly.graph_objects as go
import plotly.express as px
import geopandas as gpd
import json
import math


st.markdown(""" <style> .font {
    font-size:45px ; font-family: 'Comic Sans'; color: #cca300} 
    </style> """, unsafe_allow_html=True)

with open('refined.geojson') as response:
    geodata = json.load(response)
# print(geodata)
st.markdown('<p class="font">LANGUAGE MAP</p>', unsafe_allow_html=True)  

# df = pd.read_csv('crop_Arhar.csv')
df = pd.read_csv('data_refined.csv')
color_map={
    '"NA"' : 'Grey',
    '"DRAVIDIAN"' : 'Grey',
}
fig = px.choropleth_mapbox(
                    df, 
                    geojson = geodata, 
                    locations = df.Districts, 
                    color = df["Languages"], 
                    color_discrete_map=color_map,
                    featureidkey = "properties.District",
                    mapbox_style = "carto-positron",
                    center = {"lat": 22.5937, "lon": 82.9629},
                    hover_data=['STATE'],
                    # animation_frame = df["Crop_Year"],
                    zoom = 3.0,
                    opacity = 1.0
                    )
fig.update_layout(autosize=False,
            height=700,
            width=600,
            margin={"r":0,"t":0,"l":0,"b":0})
st.plotly_chart(fig, use_container_width=True)
 