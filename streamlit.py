import streamlit as st
import pandas as pd

st.title("新潟人工知能研究所")
st.write("""オムニ株式会社""")

#number = st.slider("pick a number", 0 , 100)

#file = st.file_uploader("pick a file")

from PIL import Image
import numpy as np
import streamlit as st


def load_image(img):
    im = Image.open(img)
    image = np.array(im)
    return image



from streamlit_drawable_canvas import st_canvas

# Specify canvas parameters in application
stroke_width = st.sidebar.slider("Stroke width: ", 1, 25, 3)
stroke_color = st.sidebar.color_picker("Stroke color hex: ")
bg_image = st.sidebar.file_uploader("Background image:", type=["png", "jpg"])
drawing_mode = st.sidebar.selectbox(
    "Drawing tool:", ("freedraw", "line", "rect", "circle", "transform")
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
