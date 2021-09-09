import streamlit as st
from PIL import Image, ImageDraw, ImageFont
import numpy as np
import cv2 
import sys


from streamlit_drawable_canvas import st_canvas

def main():
    """Detection"""
    
    st.title("新潟人工知能研究所")
    st.subheader("OMUNI APP")
    
    activities = ["Detection", "Paint", "About"]
    choice = st.sidebar.selectbox("Select Activity", activities)
    
    if choice == 'Detection':
        st.text("Detection")
        uploaded_file1 = st.file_uploader("Choose a file")
   
    if choice == 'Paint':
        st.text("Paint")
        stroke_width = st.sidebar.slider("Stroke width", 1, 16, 3)
        stroke_color = st.sidebar.color_picker("Stroke color hex: ")
        bg_image = st.sidebar.file_uploader("Background image:", type=["png", "jpg"])
        drawing_mode = st.sidebar.selectbox("Drawing tool:", ("freedraw", "line", "rect", "circle", "transform"))
        canvas_result = st_canvas(
            fill_color="rgba(255, 165, 0, 0.3)",
            stroke_width=stroke_width,
            stroke_color=stroke_color,
            background_image=Image.open(bg_image) if bg_image else None,
            height=400,width=500,drawing_mode=drawing_mode,key="canvas",)
        

    elif choice == 'About':
        st.text("About")

if __name__ == "__main__":
    main()
