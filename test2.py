"""
TextLayer
========

Names of various public transit stops within San Francisco, plotted at the location of that stop
"""

import pydeck as pdk
from pydeck.types import String
import pandas as pd

df = pd.read_json("test2.json")
# Define a layer to display on a map
layer = pdk.Layer(
    "TextLayer",
    df,
    pickable=True,
    get_position="coordinates",
    get_text="name",
    get_size=16,
    get_color=[0, 0, 0],
    get_angle=0,
    # Note that string constants in pydeck are explicitly passed as strings
    # This distinguishes them from columns in a data set
    get_text_anchor=String("middle"),
    get_alignment_baseline=String("center"),
)

# Set the viewport location
view_state = pdk.ViewState(latitude=20.5937, longitude=78.9629, zoom=4, bearing=0, pitch=0)

# Render
r = pdk.Deck(
    layers=[layer],
    initial_view_state=view_state,
    tooltip={"text": "{name}\n{language}"},
    map_style=pdk.map_styles.ROAD,
)
r.to_html("test2.html")