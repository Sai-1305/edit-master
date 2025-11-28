import streamlit as st
from main import remove_background
from streamlit_extras.switch_page_button import switch_page

# ====================================================
st.set_page_config(
    page_title = "EditMaster::Remove Background",
    page_icon = "images/EditMaster-logo2.png",
    layout = "centered",
)
# ====================================================

st.title("Remove the Background 🔥")

# Home navigation button
if st.button("🏠 Home"):
    switch_page("Home")


st.markdown(
    """
        ### 1. Upload your image.
        Add an image from your device.

        ### 2. Remove Background
        Click on the "Remove Background" button to convert the image into no-background image.

    """,
    unsafe_allow_html=True
)


uploaded_image = st.file_uploader('Upload an image to remove the color:', type = ["jpg","png"])

if uploaded_image is not None:

    # Display the image
    st.image(uploaded_image, caption = "Uploaded Image", use_column_width = True)

    if st.button('Remove Background',help = "Submit to remove the background from the image."):
        no_bg_bytes=remove_background(uploaded_image)

        if no_bg_bytes:
            st.success(f"Background removal complete!")
            st.download_button(label="Download Image with Transparent Background", data=no_bg_bytes.getvalue(), file_name="no_bg_image.png", mime="image/png")
