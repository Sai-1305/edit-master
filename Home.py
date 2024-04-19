import streamlit as st
from streamlit_extras.switch_page_button import switch_page

# ====================================================

st.set_page_config(
    page_title = "EditMaster::Home",
    page_icon = "images\EditMaster-logo2.png",
    layout = "centered",
)

# ====================================================

st.title("EditMaster: Image Editor ⚙️")
st.markdown(
    """
        ### Welcome to the free modern AI powered photo editor by ImageWizards.

        #### Start editing your photos in seconds.

        EditMaster features built-in photo editing functions to make it the ideal tool for perfecting pictures. The easy-to-use free photo editor offers decolorizing and background removal options for professional quality results right at your fingertips.

        Start editing by clicking on either one of the buttons.

    """,
    unsafe_allow_html=True
)

# ====================================================

col1, col2 = st.columns(2)

with col1:
    btnDecolorize = st.button('Decolorize Image',type = 'primary',help = "Decolorize the image.")

with col2:
    btnRemoveBg = st.button('Remove Background',type = 'primary', help = "Remove background from the image.")

if btnDecolorize:
    switch_page("decolorization")

if btnRemoveBg:
    switch_page("backgroundRemoval")