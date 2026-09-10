from core import OPCUAClient
from config import OPCUA_SERVERS

#Create a OPC-UA Client for Station-1
station1_client = OPCUAClient("station1")
station1_client.connect()
print("OPC UA connection successful.")


for i in range(0,100000):

    if i % 20 == 0:

        val1 = station1_client.read_node("start_request")
        val2 = station1_client.read_node("stop_request")
        val3 = station1_client.read_node("state_no")
        val4 = station1_client.read_node("state_description")
        val5 = station1_client.read_node("error_code")
        val6 = station1_client.read_node("error_description")
        val7 = station1_client.read_node("pressure_act_level")
        val8 = station1_client.read_node("serial_no")

        print(f"start_request           {val1}")
        print(f"stop_request            {val2}")
        print(f"state_no                {val3}")
        print(f"state_description       {val4}")
        print(f"error_code              {val5}")
        print(f"error_description       {val6}")
        print(f"pressure_act_level      {val7}")
        print(f"serial_no               {val8}")

        

        

   

#station1_client.disconnect()
#print("disconnected")