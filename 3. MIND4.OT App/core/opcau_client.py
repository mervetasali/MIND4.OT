from asyncua.sync import Client
from config import OPCUA_SERVERS

class OPCUAClient:

    def __init__(self, station_no):

        #Get endpoint of the Station from config 
        self.endpoint = OPCUA_SERVERS[station_no]["endpoint"]

        #Create a OPC-UA Client for the Station
        self.client = Client(self.endpoint)

        #NodeID read from the Station
        self.node = OPCUA_SERVERS[station_no]["nodes"]

    #Connect to the Server
    def connect(self):
        self.client.connect()

    #Disconnect from the Server
    def disconnect(self):
        self.client.disconnect()

    #Read from the Server
    def read_node(self, node_name):

        #find out node details of the parameters read from the Server
        node_id = self.node[node_name]
        
        node = self.client.get_node(node_id)
        value = node.read_value()

        return value
        

