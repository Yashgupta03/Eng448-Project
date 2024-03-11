import streamlit as st
import pandas as pd
import numpy as np
import pydeck as pdk
from pydeck.types import String

df = pd.read_json("test2.json")
df1 = pd.read_json("test4.json")

r=pdk.Deck(
     map_style="mapbox://styles/mapbox/light-v9",  #"https://basemaps.cartocdn.com/gl/voyager-nolabels-gl-style/style.json"
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
        # pdk.Layer(
        #     "PathLayer",
        #     df1,
        #     pickable=True,
        #     get_path="path",
        #     get_color="color",
        #     width_scale=20,
        #     width_min_pixels=2,
        #     get_width=5,
        # )
    ],
    tooltip={"html": "<b>Language:</b> {val}"},
)

st.pydeck_chart(r)