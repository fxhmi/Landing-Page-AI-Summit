import streamlit as st
import base64

st.markdown(
    """
    <style>
    section.stMain .block-container {
        padding-top: 0rem;
        margin-top: 0rem;
    }
    header.stAppHeader {
        height: 0;
        min-height: 0;
        padding: 0;
        margin: 0;
    }
    </style>
    """,
    unsafe_allow_html=True
)


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
            height: 100vh;  /* makes bg full viewport height */
            margin: 0;      /* remove margin */
        }}
        </style>
        """,
        unsafe_allow_html=True
    )

#font-family: 'Arial Black', Gadget, sans-serif;
set_bg("dummy_cover.png")  

st.markdown(
    """
    <h1 style="
        font-family: 'Roboto Black', Gadget, sans-serif;
        font-size: 64px;
        color: white;
        text-shadow: 2px 2px 4px #000000;
        margin-top: 210px;
        margin-bottom: 150px;
        text-align: center;
    ">
    Prasarana AI Projects Showcase
    </h1>
    """,
    unsafe_allow_html=True
)

# Your existing buttons layout
col1, col2 = st.columns(2)

# with col1:
#     st.markdown(
#         """
#         <a href="https://swiftroute.streamlit.app/" target="_blank" style="text-decoration:none">
#             <button style="
#                 width: 100%;
#                 padding: 15px;
#                 font-size: 20px;
#                 color: white;
#                 background-color: #0072C6;
#                 border: none;
#                 border-radius: 8px;
#                 cursor: pointer;
#                 box-shadow: 2px 2px 5px #000000;
#             ">
#             AI for Bus Punctuality
#             </button>
#         </a>
#         """,
#         unsafe_allow_html=True,
#     )

# with col2:
#     st.markdown(
#         """
#         <a href="https://swiftroute.streamlit.app/" target="_blank" style="text-decoration:none">
#             <button style="
#                 width: 100%;
#                 padding: 15px;
#                 font-size: 20px;
#                 color: white;
#                 background-color: #FF4B4B;
#                 border: none;
#                 border-radius: 8px;
#                 cursor: pointer;
#                 box-shadow: 2px 2px 5px #000000;
#             ">
#             AI for Bus Replacement
#             </button>
#         </a>
#         """,
#         unsafe_allow_html=True,
#     )

with col1:
    st.markdown(
        """
        <a href="https://swiftroute.streamlit.app/" target="_blank" style="text-decoration:none">
            <div style="
                position: relative;
                width: 100%;
                padding: 15px 0;
                font-size: 20px;
                font-weight: 700;
                color: white;
                background: linear-gradient(135deg, #0072C6, #005A9E);
                border-radius: 30px 30px 15px 15px;
                box-shadow: 0 8px 15px rgba(0, 114, 198, 0.4);
                text-align: center;
                cursor: pointer;
                transition: transform 0.3s ease, box-shadow 0.3s ease;
                font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
                user-select: none;
                backdrop-filter: brightness(1.1);
                overflow: visible;
            "
            onmouseover="this.style.transform='scale(1.05)'; this.style.boxShadow='0 12px 20px rgba(0,114,198,0.6)';"
            onmouseout="this.style.transform='scale(1)'; this.style.boxShadow='0 8px 15px rgba(0,114,198,0.4)';"
            >
                AI for Bus Punctuality
                <span style="
                    position: absolute;
                    left: -30px;
                    top: 50%;
                    transform: translateY(-50%);
                    width: 25px;
                    height: 25px;
                    background: linear-gradient(135deg, #0072C6, #005A9E);
                    border-radius: 8px 0 0 8px;
                    box-shadow: 0 4px 10px rgba(0,114,198,0.3);
                "></span>
                <span style="
                    position: absolute;
                    right: -30px;
                    top: 50%;
                    transform: translateY(-50%);
                    width: 25px;
                    height: 25px;
                    background: linear-gradient(135deg, #005A9E, #003C66);
                    border-radius: 0 8px 8px 0;
                    box-shadow: 0 4px 10px rgba(0,56,102,0.3);
                "></span>
            </div>
        </a>
        """,
        unsafe_allow_html=True,
    )


with col2:
    st.markdown(
        """
        <a href="https://swiftroute.streamlit.app/" target="_blank" style="text-decoration:none">
            <div style="
                position: relative;
                width: 100%;
                padding: 15px 0;
                font-size: 20px;
                font-weight: 700;
                color: white;
                background: linear-gradient(135deg, #FF4B4B, #D03535);
                border-radius: 30px 30px 15px 15px;
                box-shadow: 0 8px 15px rgba(255, 75, 75, 0.4);
                text-align: center;
                cursor: pointer;
                transition: transform 0.3s ease, box-shadow 0.3s ease;
                font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
                user-select: none;
                backdrop-filter: brightness(1.1);
                overflow: visible;
            "
            onmouseover="this.style.transform='scale(1.05)'; this.style.boxShadow='0 12px 20px rgba(255,75,75,0.6)';"
            onmouseout="this.style.transform='scale(1)'; this.style.boxShadow='0 8px 15px rgba(255,75,75,0.4)';"
            >
                AI for Bus Replacement
                <span style="
                    position: absolute;
                    left: -30px;
                    top: 50%;
                    transform: translateY(-50%);
                    width: 25px;
                    height: 25px;
                    background: linear-gradient(135deg, #FF4B4B, #D03535);
                    border-radius: 8px 0 0 8px;
                    box-shadow: 0 4px 10px rgba(255,75,75,0.3);
                "></span>
                <span style="
                    position: absolute;
                    right: -30px;
                    top: 50%;
                    transform: translateY(-50%);
                    width: 25px;
                    height: 25px;
                    background: linear-gradient(135deg, #D03535, #990000);
                    border-radius: 0 8px 8px 0;
                    box-shadow: 0 4px 10px rgba(153,0,0,0.3);
                "></span>
            </div>
        </a>
        """,
        unsafe_allow_html=True,
    )
