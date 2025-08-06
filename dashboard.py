import streamlit as st
import base64

def set_bg(png_file):
    with open(png_file, "rb") as image_file:
        encoded_string = base64.b64encode(image_file.read()).decode()
    st.markdown(
        f"""
        <style>
        .stApp {{
            background-image: url("data:image/png;base64,{encoded_string}");
            background-size: cover;
            background-position: center;
            background-repeat: no-repeat;
            background-attachment: fixed;
        }}
        </style>
        """,
        unsafe_allow_html=True
    )

set_bg("dummy_cover.png")  

st.markdown(
    """
    <div style="text-align: center; margin-top: 40px; margin-bottom: 20px;">
        <img src="Prasarana-01.png" alt="Prasarana Logo" style="width: 150px; height: auto;" />
    </div>
    <h1 style="
        font-family: 'Arial Black', Gadget, sans-serif;
        font-size: 64px;
        color: white;
        text-shadow: 2px 2px 4px #000000;
        margin-top: 0;
        margin-bottom: 20px;
        text-align: center;
    ">
    Prasarana AI Projects Showcase
    </h1>
    """,
    unsafe_allow_html=True
)

# Your existing buttons layout
col1, col2 = st.columns(2)

with col1:
    st.markdown(
        """
        <a href="https://swiftroute.streamlit.app/" target="_blank" style="text-decoration:none">
            <button style="
                width: 100%;
                padding: 15px;
                font-size: 20px;
                color: white;
                background-color: #0072C6;
                border: none;
                border-radius: 8px;
                cursor: pointer;
                box-shadow: 2px 2px 5px #000000;
            ">
            AI for Bus Punctuality
            </button>
        </a>
        """,
        unsafe_allow_html=True,
    )

with col2:
    st.markdown(
        """
        <a href="https://swiftroute.streamlit.app/" target="_blank" style="text-decoration:none">
            <button style="
                width: 100%;
                padding: 15px;
                font-size: 20px;
                color: white;
                background-color: #FF4B4B;
                border: none;
                border-radius: 8px;
                cursor: pointer;
                box-shadow: 2px 2px 5px #000000;
            ">
            AI for Bus Replacement
            </button>
        </a>
        """,
        unsafe_allow_html=True,
    )
