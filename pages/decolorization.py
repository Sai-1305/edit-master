import streamlit as st
from main import decolorize_image
from streamlit_extras.switch_page_button import switch_page

# ====================================================

st.set_page_config(
    page_title = "EditMaster::Decolorize",
    page_icon = "images/EditMaster-logo2.png",
    layout = "centered",
)

# ====================================================

st.title("Decolorize the Image 🌘")

# Home navigation button
if st.button("🏠 Home"):
    switch_page("Home")

st.markdown(
    """
        ### 1. Upload your image.
        Add an image from your device.

        ### 2. Decolorize
        Click on the "Decolorize" button to convert the image into black-and-white image.

    """,
    unsafe_allow_html=True
)

# ====================================================

uploaded_image = st.file_uploader('Upload an image to remove the color:', type = ["jpg", "jpeg", "png"])

# ====================================================

if uploaded_image is not None:

    # Display the image
    st.image(uploaded_image, caption = "Uploaded Image", use_column_width = True)

    if st.button('Decolorize Image', help = "Submit to decolorize the image."):
        gray_bytes=decolorize_image(uploaded_image)

        if gray_bytes:
            st.success(f"Decolorization complete!")
            st.download_button(label="Download Decolorized Image", data=gray_bytes,file_name="decolorized_image.jpg", mime="image/jpeg")
                