import streamlit as st

def show_main_page():
        
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

            if st.button(
                "Open MES4.OT →",
                use_container_width=True
            ):
                st.session_state.page = "mes"
                st.rerun()

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

            if st.button(
                "Open MIND4.OT →",
                use_container_width=True
            ):
                st.session_state.page = "mind"
                st.rerun()

   