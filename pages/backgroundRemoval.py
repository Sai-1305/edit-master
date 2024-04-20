from rembg import remove 
from PIL import Image
import streamlit as st
from streamlit_extras.switch_page_button import switch_page
from pages.main import removeBackground

# ====================================================
st.set_page_config(
    page_title = "EditMaster::Remove Background",
    page_icon = "images\EditMaster-logo2.png",
    layout = "centered",
)
# ====================================================

st.page_link("Home.py", label="🏠 Home", icon="🔙")
st.title("Remove the Background 🔥")
st.markdown(
    """
        ### 1. Upload your image.
        Add an image from your device.

        ### 2. Specify output folder.
        Provide the path of the folder that you want your background-free image to be saved to. And then press the "Enter" key.

        ### 3. Remove Background
        Click on the "Remove Background" button to start the conversion.

    """,
    unsafe_allow_html=True
)


uploadedImage = st.file_uploader('Upload an image to remove the color:', type = ["jpg","png"])

outputDirectory = st.text_input('Enter the path of output directory:')

if uploadedImage is not None:

    # Display the image
    st.image(uploadedImage, caption = "Uploaded Image", use_column_width = True)

    if outputDirectory != "":
        
        if st.button('Remove Background',help = "Submit to remove the background from the image."):
            success=removeBackground(uploadedImage,outputDirectory)

            if success:
                st.success(f"No-background image saved successfully to {outputDirectory}")