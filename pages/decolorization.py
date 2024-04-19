import streamlit as st
import pandas as pd
from io import StringIO
from pages.main import decolorizeImage
from streamlit_extras.switch_page_button import switch_page

# ====================================================

st.set_page_config(
    page_title = "EditMaster::Decolorize",
    page_icon = "images\EditMaster-logo2.png",
    layout = "centered",
)

# ====================================================

st.page_link("Home.py", label="🏠 Home", icon="🔙")
st.title("Decolorize the Image 🌘")
st.markdown(
    """
        ### 1. Upload your image.
        Add an image from your device.

        ### 2. Specify output folder.
        Provide the path of the folder that you want your greyscale image to be saved to. And then press the "Enter" key.

        ### 3. Decolorize
        Click on the "Decolorize" button to start the conversion.

    """,
    unsafe_allow_html=True
)

# ====================================================

uploadedImage = st.file_uploader('Upload an image to remove the color:', type = ["jpg", "jpeg", "png"])
outputDirectory = st.text_input('Enter the path of output directory:')

# ====================================================

if uploadedImage is not None:

    # Display the image
    st.image(uploadedImage, caption = "Uploaded Image", use_column_width = True)

    if outputDirectory != "":
        
        if st.button('Decolorize Image', help = "Submit to decolorize the image."):
            success=decolorizeImage(uploadedImage,outputDirectory)

            if success:
                st.success(f"Black and white image saved successfully to {outputDirectory}")
                