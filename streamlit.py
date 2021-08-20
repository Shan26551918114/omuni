import streamlit as st
import pandas as pd

st.title("新潟人工知能研究所")
st.write("""オムニ株式会社""")

#number = st.slider("pick a number", 0 , 100)

#file = st.file_uploader("pick a file")

from PIL import Image
import numpy as np 
import streamlit as st 

# Function to Read and Manupilate Images
def load_image(img):
    im = Image.open(img)
    image = np.array(im)
    return image

# Uploading the File to the Page
#uploadFile = st.file_uploader(label="Upload image", type=['jpg', 'png'])

# Checking the Format of the page
#if uploadFile is not None:
    # Perform your Manupilations (In my Case applying Filters)
#    img = load_image(uploadFile)
#    st.image(img)
#    st.write("Image Uploaded Successfully")
#else:
#    st.write("Make sure you image is in JPG/PNG Format.")
 #   st.write("画像の形式はJPG/PNGに対応しています")

import pandas as pd
from PIL import Image
import streamlit as st
from streamlit_drawable_canvas import st_canvas

# Specify canvas parameters in application
stroke_width = st.sidebar.slider("Stroke width: ", 1, 25, 3)
stroke_color = st.sidebar.color_picker("Stroke color hex: ")
bg_color = st.sidebar.color_picker("Background color hex: ", "#eee")
bg_image = st.sidebar.file_uploader("Background image:", type=["png", "jpg"])
drawing_mode = st.sidebar.selectbox(
    "Drawing tool:", ("freedraw", "line", "rect", "circle", "transform")
)
realtime_update = st.sidebar.checkbox("Update in realtime", True)

# Create a canvas component
canvas_result = st_canvas(
    fill_color="rgba(255, 165, 0, 0.3)",  # Fixed fill color with some opacity
    stroke_width=stroke_width,
    stroke_color=stroke_color,
    background_color=bg_color,
    
    background_image=Image.open(bg_image) if bg_image else None,
    update_streamlit=realtime_update,
    height=600,
    width=600,
    drawing_mode=drawing_mode,
    key="canvas",
)

