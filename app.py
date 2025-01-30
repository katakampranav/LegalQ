import streamlit as st
from streamlit_option_menu import option_menu
import home as home
import need_info as need_info
import know_law as know_law

# Streamlit Page Configuration
st.set_page_config(
    page_title="LegalQ",
    layout="wide",
    initial_sidebar_state="collapsed",
    page_icon="assets/emblem_of_india.png"
)

# Sidebar or horizontal menu for navigation
selected = option_menu(
    None,  # No title
    ["Home", "Need Info", "Know Law"],  # Menu options
    icons=["house", "info-circle", "bank"],  # Icons for each menu item
    menu_icon="cast",  # Main menu icon
    default_index=0,  # Default to Home
    orientation="horizontal",  # Horizontal menu
    styles={
        "container": {"padding": "0!important", "background-color": "#0E1117"},
        "icon": {"color": "white", "font-size": "25px"},
        "nav-link": {"font-size": "20px", "text-align": "center", "margin": "0px", "--hover-color": "#eee"},
        "nav-link-selected": {"background-color": "#FF4B4B", "color": "white"},
    }
)

# Route to the selected page
if selected == "Home":
    home.render_page()
elif selected == "Need Info":
    need_info.render_page()
elif selected == "Know Law":
    know_law.render_page()
