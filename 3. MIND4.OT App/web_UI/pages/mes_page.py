import streamlit as st
from core import OPCUAClient
from config import OPCUA_SERVERS
import time


def show_mes_page():
    # -------------------------
    # Page Title
    # -------------------------
    st.title("MES4.OT - Production Line")

    st.markdown(
        """        
        Select a station to monitor and manage production.
        """
    )

    # -------------------------
    # Station Selection
    # -------------------------
    col1, col2, col3 = st.columns(3, gap="large")

    # Station 1
    with col1:
        st.image(
            "assets/images/station1.png",
            use_container_width=True
        )

        st.subheader("Station 01")
        st.write("Plastic Container Production")
        st.caption("Siemens")

        try:
            if st.button(
                        "Connect to Station 01 →",
                        use_container_width=True
                    ):
            
                        if "station1_client" not in st.session_state:
            
                            #Create a OPC-UA Client for Station-1
                            station1_client = OPCUAClient("station1")
                            station1_client.connect()      
                           
                            station1_client.create_subscription()
                            station1_client.subscribe_all_nodes()
                            #station1_client.subscribe_node("state_no_act")
                            #station1_client.subscribe_node("error_code")

                             # Keep the client during the Streamlit session                
                            st.session_state.station1_client = station1_client


                            # station1_client.subscribe_node("start_request")
                            # station1_client.subscribe_node("stop_request")
                            # station1_client.subscribe_node("state_no_act")
                            # station1_client.subscribe_node("state_description")                            
                            # station1_client.subscribe_node("error_description")
                            # station1_client.subscribe_node("pressure_act_level")
                            # station1_client.subscribe_node("serial_no")
                           
                            
                        st.session_state.page = "station1"
                        st.rerun()

        except (ConnectionError, TimeoutError):
             st.error("Connection is not successful. Check the connection of Station-1")


        

    # Station 2
    with col2:
        st.image(
            "assets/images/station2.png",
            use_container_width=True
        )

        st.subheader("Station 02")
        st.write("Recipe-Based Filling")
        st.caption("CODESYS / WAGO")

        st.button(
            "Open Station 02 →",
            use_container_width=True,
            disabled=True
        )

    # Station 3
    with col3:
        st.image(
            "assets/images/station3.png",
            use_container_width=True
        )

        st.subheader("Station 03")
        st.write("Quality Control & Packaging")
        st.caption("Beckhoff")

        st.button(
            "Open Station 03 →",
            use_container_width=True,
            disabled=True
        )