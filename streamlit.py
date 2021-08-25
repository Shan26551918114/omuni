import streamlit as st

import matplotlib.pyplot as plt

import numpy as np


st.date_input('Date input')
st.time_input('Time entry')

from PIL import Image
import numpy as np

from streamlit_drawable_canvas import st_canvas

# Specify canvas parameters in application
stroke_width = st.sidebar.slider("Stroke width: ", 1, 16, 3)
stroke_color = st.sidebar.color_picker("Stroke color hex: ")
#bg_color = st.sidebar.color_picker("Background color hex: ", "#eee")
bg_image = st.sidebar.file_uploader("Background image:", type=["png", "jpg"])
drawing_mode = st.sidebar.selectbox(
    "Drawing tool:", ("freedraw", "line", "rect", "transform")
)

canvas_result = st_canvas(
    fill_color="rgba(255, 165, 0, 0.3)",  # Fixed fill color with some opacity
    stroke_width=stroke_width,
    stroke_color=stroke_color, 
    background_image=Image.open(bg_image) if bg_image else None,
    height=400,
    width=600,
    drawing_mode=drawing_mode,
    key="canvas",
)
