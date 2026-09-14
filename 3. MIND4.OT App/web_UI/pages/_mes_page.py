import streamlit as st

def show_mes_page():
    # -------------------------
    # Page Title
    # -------------------------
    st.title("MES4.OT")

    st.markdown(
        """
        ### Production Lines
        Select a production line to view stations and manage orders.
        """
    )

    # -------------------------
    # Production Lines
    # -------------------------
    col1, col2, col3 = st.columns(3, gap="medium")

    with col1:
        st.subheader("Product Line 1")
        st.write("Plastic Container Production")

        #st.write("ST1 — Container Production")
        #st.write("ST2 — Filling")
        #st.write("ST3 — Packaging")

        selected_station = st.radio(
            "Select Station",
            [
                "ST1 — Container Production",
                "ST2 — Filling",
                "ST3 — Packaging"
            ],
            key="product_line1_station"
        )

        if st.button(
            "Open Product Line 1 →",
            use_container_width=True
        ):
            if selected_station.startswith("ST1"):
                st.session_state.page = "station1"
                st.rerun()

            elif selected_station.startswith("ST2"):
                st.info("Station 2 is not available yet.")

            elif selected_station.startswith("ST3"):
                st.info("Station 3 is not available yet.")

    with col2:
        st.subheader("Product Line 2")
        st.write("Future Production Line")

        #st.write("ST1 —")
        #st.write("ST2 —")
        #st.write("ST3 —")

        selected_station = st.radio(
            "Select Station",
            [
                "ST1 — ...",
                "ST2 — ...",
                "ST3 — ..."
            ],
            key="product_line2_station"
        )

        st.button(
            "Open Product Line 2 →",
            use_container_width=True,
            disabled=True
        )

    with col3:
        st.subheader("Product Line 3")
        st.write("Future Production Line")

        #st.write("ST1 —")
        #st.write("ST2 —")
        #st.write("ST3 —")

        selected_station = st.radio(
            "Select Station",
            [
                "ST1 — ...",
                "ST2 — ...",
                "ST3 — ..."
            ],
            key="product_line3_station"
        )

        st.button(
            "Open Product Line 3 →",
            use_container_width=True,
            disabled=True
        )

    # -------------------------
    # Quick Stats
    # -------------------------
    st.subheader("Quick Stats")

    stat1, stat2, stat3, stat4 = st.columns(4)

    stat1.metric("Total Orders", 0)
    stat2.metric("Running", 0)
    stat3.metric("Idle", 3)
    stat4.metric("Fault", 0)

    # -------------------------
    # Recent Orders
    # -------------------------
    st.subheader("Recent Orders")

    st.info("No production orders yet.")