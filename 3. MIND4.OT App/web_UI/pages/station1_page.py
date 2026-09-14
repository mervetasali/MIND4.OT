import streamlit as st
import core.station1 as station1


import importlib

importlib.reload(station1)

def show_station1_page():

    if "station1_client" in st.session_state:
        st.success("Connection to Station-1 established.")
    else:
        st.error("Station-1 is not available.")

    # -------------------------
    # Order Storage
    # -------------------------
    if "station1_orders" not in st.session_state:
        st.session_state.station1_orders = []

    # -------------------------
    # Page Title
    # -------------------------
    st.title("Station 1 – Container Production")
    st.write("Create a new production order and send it to Station 1.")

    # -------------------------
    # Order Definition
    # -------------------------
    st.subheader("Order Definition")

    order_id = st.text_input(
        "Order ID",
        value="ORD-2026-0001"
    )

    # Product selection
    st.write("Product No")

    product_no = st.radio(
        "Select Product",
        ["0.5 L", "1 L", "2 L"],
        horizontal=True,
        label_visibility="collapsed"
    )

    # Recipe selection
    st.write("Recipe No")

    recipe_no = st.radio(
        "Select Recipe",
        ["001", "002", "003"],
        horizontal=True,
        label_visibility="collapsed"
    )

    # Target Quantity
    target_quantity = st.number_input(
        "Target Quantity",
        min_value=1,
        max_value=5000,
        value=1000,
        step=1
    )

    # Create Order
    if st.button(
        "Create Order →",
        use_container_width=True
    ):
        new_order = {
            "Order ID": order_id,
            "Product": product_no,
            "Recipe": recipe_no,
            "Target": target_quantity,
            #"Produced": 0,
            #"Status": "Pending"
        }

        control_order_data = station1.validate_order(new_order["Order ID"],st.session_state.station1_orders)

        if control_order_data[0]:
            st.session_state.station1_orders.append(new_order)
            st.session_state.current_order = new_order
            
            st.success(f"Order {order_id} created successfully.")

        else:
            st.error(f"{control_order_data[1]}")

    if st.session_state.get("current_order"):
        if st.button(
            "Send to Station 1 →",
            use_container_width=True
        ):
            st.info("Order will be sent to Station 1.")


        

    # -------------------------
    # Station Status
    # -------------------------
    st.subheader("Station Status")

    @st.fragment(run_every="1s")
    def show_station_status():

        status1, status2, status3, status4 = st.columns(4)

        if "station1_client" in st.session_state:

            state_no = st.session_state.station1_client.latest_values.get(
                "state_no_act", 0
            )

            error_code = st.session_state.station1_client.latest_values.get(
                "error_code", 0
            )

            if error_code == 0 and state_no == 0:
                status1.metric("Machine State", "IDLE")

            elif error_code == 1 and state_no == 0:
                status1.metric("Machine State", "ERROR")

            elif error_code == 0 and state_no != 0:
                status1.metric("Machine State", "RUNNING")

        else:
            status1.metric("Machine State", "---")

        status2.metric("Produced", 0)

        if st.session_state.station1_orders:
            current_target = st.session_state.station1_orders[-1]["Target"]
        else:
            current_target = "-"

        status3.metric("Target", current_target)
        status4.metric("Reject", 0)


    show_station_status()