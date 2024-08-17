import streamlit as st
import numpy as np
from PIL import Image
import cv2

page_title = "Adaptive Thresholding of an Image"
page_icon = "🔢"
st.set_page_config(page_title=page_title, page_icon=page_icon, layout="wide")

st.title(page_title)
st.write("This web application allows users to upload an image and apply adaptive thresholding for enhanced image "
         "processing. Users can adjust key parameters, such as block size and fine-tuning constants, to customize the "
         "thresholding effect. The updated image is displayed in real-time, providing an interactive way to experiment "
         "with adaptive thresholding and visualize the results.")
st.subheader("Upload an Image")
uploaded_image = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"], label_visibility="collapsed")

if uploaded_image:
    st.subheader("Configuration")
    block_size = st.number_input("Block Size", 3, 51, 11, 2)
    fine_tuning = st.number_input("Fine Tuning", -30, 50, 2, 1)

    # Open the uploaded image, convert it to format readable by opencv, resize and change to gray scale
    image = np.array(Image.open(uploaded_image))
    img = cv2.resize(image, (512, 512))
    img = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)

    st.subheader("Result")
    col1, col2, col3 = st.columns(3, vertical_alignment="bottom")
    with col1:
        st.write(':blue[***Original Image***]')
        st.image(img)

    with col2:
        st.write(':blue[***Mean Adaptive Threshold***]')
        th2 = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, block_size, fine_tuning)
        st.image(th2)

    with col3:
        st.write(':blue[***Gaussian Adaptive Threshold***]')
        th3 = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, block_size, fine_tuning)
        st.image(th3)
