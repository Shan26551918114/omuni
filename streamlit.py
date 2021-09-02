import streamlit as st
import pandas as pd
import streamlit.components.v1 as components

components.html("""<html>
<head>
<meta name="viewport" content="width=device-width, initial-scale=1">
<style>
body {
  font-family: Arial, Helvetica, sans-serif;
}

.pill-nav a {
  display: inline-block;
  color: black;
  text-align: center;
  padding: 14px;
  text-decoration: none;
  font-size: 17px;
  border-radius: 5px;
}

.pill-nav a:hover {
  background-color: #ddd;
  color: black;
}

.pill-nav a.active {
  background-color: dodgerblue;
  color: white;
}
</style>
</head>
<body>
<h2>新潟人工知能研究所</h2>


<div class="pill-nav">
  <a href="#home">Single Image</a>
  <a href="#news">Multiple Images</a>
  <a class="active" href="#contact">Drawing</a>
  <a href="#about">Help</a>
</div>

</body>
</html>


""")

st.title("新潟人工知能研究所")
st.write("""オムニ株式会社""")

from PIL import Image
import numpy as np

from streamlit_drawable_canvas import st_canvas

stroke_width = st.sidebar.slider("Stroke width: ", 1, 16, 3)
stroke_color = st.sidebar.color_picker("Stroke color hex: ")
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
