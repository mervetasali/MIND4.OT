import streamlit as st
import core.station1 as station1
import importlib

importlib.reload(station1)

def show_station1_page():

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

    status1, status2, status3, status4 = st.columns(4)

    status1.metric("Machine State", "IDLE")
    status2.metric("Produced", 0)
    if st.session_state.station1_orders:
        current_target = st.session_state.station1_orders[-1]["Target"]
    else:
        current_target = "-"

    status3.metric("Target", current_target)
    status4.metric("Reject", 0)

    # -------------------------
    # Recent Orders
    # -------------------------
    st.subheader("Recent Orders")

    if st.session_state.station1_orders:
        st.dataframe(
            st.session_state.station1_orders,
            use_container_width=True,
            hide_index=True
        )
    else:
        st.info("No production orders yet.")