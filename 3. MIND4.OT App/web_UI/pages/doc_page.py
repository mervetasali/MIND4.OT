import streamlit as st


def show_documentation_page():

    st.title("Documentation")

    st.write(
        "Technical documentation for the MIND4.OT smart manufacturing platform."
    )

    st.divider()

    # -------------------------
    # System Architecture
    # -------------------------
    st.subheader("System Architecture")

    st.info(
        "System architecture documentation will be added "
        "as the project architecture evolves."
    )

    st.divider()

    # -------------------------
    # Production Line
    # -------------------------
    st.subheader("Production Line")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.markdown("### Station 01")
        st.write("Plastic Container Production")
        st.caption("Siemens | TIA Portal | S7-1500")

        if st.button(
            "Station 01 Documentation →",
            use_container_width=True,
            key="station1_doc_btn"
        ):
            st.session_state.page = "station1_documentation"
            st.rerun()

    with col2:
        st.markdown("### Station 02")
        st.write("Recipe-Based Filling")
        st.caption("WAGO | CODESYS")

        st.button(
            "Coming Soon",
            disabled=True,
            use_container_width=True,
            key="station2_doc_btn"
        )

    with col3:
        st.markdown("### Station 03")
        st.write("Quality Control & Packaging")
        st.caption("Beckhoff | TwinCAT 3")

        st.button(
            "Coming Soon",
            disabled=True,
            use_container_width=True,
            key="station3_doc_btn"
        )

    st.divider()

    # -------------------------
    # Technical Documentation
    # -------------------------
    st.subheader("Technical Documentation")

    st.write(
        """
        - OPC UA Data Model
        - MES Data Model
        - Database Architecture
        """
    )