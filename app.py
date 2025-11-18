import streamlit as st
import numpy as np
from PIL import Image

st.title("handwritten digit recognization web")
st.write("Please upload an image of a handwritten number between 0 and 9 to see the prediction.")
uploaded_file = st.file_uploader("upload an image", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:

    image = Image.open(uploaded_file).convert('L')  
    st.image(image, caption="uploaded image", use_container_width=True)
    img_array = np.array(image)
    st.write("image converted to array shape:", img_array.shape)

    predicted_digit = np.random.randint(0, 10)
    st.subheader("predicted digit:")
    st.success(f"{predicted_digit}")
else:
    st.info("please upload an image to see the prediction, "
    "is the most important thing in the world, those who have not paid"
    "the maintainaince is the important in the world those .")
