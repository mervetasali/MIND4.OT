import streamlit as st

from web_UI.styles import load_css
import web_UI.pages.main_page as mainPage
import web_UI.pages.mes_page as mesPage
import web_UI.pages.mind_page as mindPage
import web_UI.pages.station1_page as st1Page
import web_UI.pages.about_page as aboutPage
import web_UI.pages.doc_page as docPage
import web_UI.pages.settings_page as settingsPage

st.set_page_config(
    page_title="MIND4.OT",
    page_icon="🧠",
    layout="wide",
    initial_sidebar_state="expanded"
)

load_css()

# Current page
if "page" not in st.session_state:
    st.session_state.page = "main"

# Hide scrollbar at main page
st.markdown(
    """
    <style>
    [data-testid="stAppViewContainer"] {
        overflow-y: hidden;
    }

    .block-container {
        padding-bottom: 0rem;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# -------------------------
# Sidebar
# -------------------------
with st.sidebar:

    st.markdown("## MIND4.OT")

    if st.button(
        "⌂  Home",
        use_container_width=True
    ):
        st.session_state.page = "main"
        st.rerun()

    if st.button(
        "ⓘ  About",
        use_container_width=True
    ):
        st.session_state.page = "about"
        st.rerun()

    if st.button(
        "▣  Documentation",
        use_container_width=True
    ):
        st.session_state.page = "documentation"
        st.rerun()

    if st.button(
        "⚙  Settings",
        use_container_width=True
    ): 
        st.session_state.page = "settings"
        st.rerun()

    # -------------------------
    # Header
    # -------------------------
    st.markdown(
        """
        <div class="user-area">
            👤 User
        </div>
        """,
        unsafe_allow_html=True
    )



if st.session_state.page == "main":
    mainPage.show_main_page()

elif st.session_state.page == "mes":
    mesPage.show_mes_page()

elif st.session_state.page == "mind":
    mindPage.show_mind_page()
elif st.session_state.page == "station1":
    st1Page.show_station1_page()

if st.session_state.page == "about":
    aboutPage.show_about_page()

if st.session_state.page == "documentation":
    docPage.show_documentation_page()

if st.session_state.page == "settings":
    settingsPage.show_settings_page()