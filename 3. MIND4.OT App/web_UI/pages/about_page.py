import streamlit as st


def show_about_page():

    col1, col2 = st.columns([1, 2])

    with col1:
        st.title("About MIND4.OT")

    with col2:
        st.markdown(
            """
            > **PLC** controls the machine.<br>
            > **MES4.OT** manages production.<br>
            > **MIND4.OT** analyzes, predicts and recommends.
            """,
            unsafe_allow_html=True
        )

    st.markdown(
        """
        ### Industrial Intelligence & Smart Manufacturing Platform

        **MIND4.OT** is a simulation-based Industry 4.0 project designed to
        demonstrate an end-to-end smart manufacturing architecture from
        machine control to production management, industrial data and
        intelligent analysis.
        """
    )

    st.divider()

    st.subheader("What is MIND4.OT?")

    st.write(
        """
        MIND4.OT combines industrial automation, MES, industrial communication,
        data management and analytics within a single modular architecture.

        The project is designed to simulate how different industrial systems
        can communicate, exchange production data and support smarter
        manufacturing decisions.
        """
    )

    st.divider()

    st.image(
        "assets/images/CurrentStatus_V2.png",
        use_container_width=True
    )

    st.divider()

    st.subheader("MES4.OT and MIND4.OT")

    col3, col4 = st.columns(2, gap="large")

    with col3:
        st.markdown("### MES4.OT")

        st.write(
            """
            MES4.OT is the production management layer of the project.

            It manages production orders, communicates with PLC-based stations,
            monitors production status and collects manufacturing data.
            """
        )

    with col4:
        st.markdown("### MIND4.OT")

        st.write(
            """
            MIND4.OT is the industrial intelligence layer.

            It uses production data for monitoring, analysis, prediction and
            decision support.
            """
        )

    st.divider()

    st.subheader("System Architecture")

    st.code(
        """
Production Order
        ↓
     MES4.OT
        ↓
 Python OT Gateway
        ↓
     OPC UA
        ↓
 ┌────────────┬──────────────┬─────────────┐
 │  Siemens   │ CODESYS/WAGO │  Beckhoff   │
 │ Station 01 │  Station 02  │ Station 03  │
 └────────────┴──────────────┴─────────────┘
        ↓
   Industrial Data
        ↓
    PostgreSQL
        ↓
 Analytics / Vision / ML
        ↓
     MIND4.OT
        """
    )

    st.divider()

    st.subheader("Technologies")

    st.write(
        """
        **Industrial Automation**
        - Siemens S7-1500 / TIA Portal
        - CODESYS / WAGO
        - Beckhoff / TwinCAT 3

        **Communication**
        - OPC UA

        **Software**
        - Python
        - Streamlit

        **Data & Intelligence**
        - PostgreSQL
        - Analytics
        - Machine Learning
        """
    )

    

    