# streamlit run app1/hello.py

import streamlit as st
from PIL import Image

st.title("Sample App")

image = st.camera_input("Take a picture")
if image:
    im = Image.fromarray(image)
    # purple gradient image
    im2 = Image.new("RGB",im.size,(128,0,128))
    #overlay the two images
    im= Image.blend(im,im2,0.5)
    #resize by 30%
    im = im.resize((int(im.size[0]*0.3),int(im.size[1]*0.3)))
    st.image(im)

filename = st.text_input("save as","image.png")
if st.button("save"):
    im.save(filename)
    st.snow()
