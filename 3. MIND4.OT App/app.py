import streamlit as st

from web_UI.styles import load_css


st.set_page_config(
    page_title="MIND4.OT",
    page_icon="🧠",
    layout="wide",
    initial_sidebar_state="expanded"
)

load_css()

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

    st.button(
        "⌂  Home",
        use_container_width=True
    )

    st.button(
        "ⓘ  About",
        use_container_width=True
    )

    st.button(
        "▣  Documentation",
        use_container_width=True
    )

    st.button(
        "⚙  Settings",
        use_container_width=True
    )

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




# -------------------------
# Main Content
# -------------------------
st.markdown(
    """
    <div class="welcome">
        <h1>Welcome to MIND4.OT</h1>
        <p>Industrial Intelligence & Smart Manufacturing Platform</p>
    </div>
    """,
    unsafe_allow_html=True
)


col1, col2 = st.columns(2, gap="large")


# -------------------------
# MES4.OT Card
# -------------------------
with col1:

    left_space, content, right_space = st.columns([1, 6, 1])

    with content:

        st.image(
            "assets/images/mes4ot_logo.png",
            use_container_width=True
        )

        st.markdown(
            """
            <div class="card-description">
                Manage Production
            </div>
            """,
            unsafe_allow_html=True
        )

        st.button(
            "Open MES4.OT →",
            use_container_width=True
        )

# -------------------------
# MIND4.OT Card
# -------------------------
with col2:

    left_space, content, right_space = st.columns([1, 6, 1])

    with content:

        st.image(
            "assets/images/mind4ot_logo.png",
            use_container_width=True
        )

        st.markdown(
            """
            <div class="card-description">
                Analyze & Optimize
            </div>
            """,
            unsafe_allow_html=True
        )

        st.button(
            "Open MIND4.OT →",
            use_container_width=True
        )