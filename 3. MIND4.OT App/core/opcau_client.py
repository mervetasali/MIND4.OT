from asyncua.sync import Client
from config import OPCUA_SERVERS

class SubscriptionHandler:

    def __init__(self, latest_values, node_map):
        self.latest_values = latest_values
        self.node_map = node_map
        

    def datachange_notification(self, node, val, data):

        #Get the node_id of the node received from the Station and convert it to string
        node_id = node.nodeid.to_string()

        #print("CALLBACK NODE ID:", repr(node_id))
        #print("NODE MAP:", self.node_map)

        #Search the node_id in the node_map 
        node_name = self.node_map[node_id]
        #Write the received value of the PLC tag to own key
        self.latest_values[node_name] = val

        print(node_name, "changed:", val)


class OPCUAClient:

    def __init__(self, station_no):

        #Get endpoint of the Station from config 
        self.endpoint = OPCUA_SERVERS[station_no]["endpoint"]

        #Create a OPC-UA Client for the Station
        self.client = Client(self.endpoint)

        #NodeID read from the Station
        self.node = OPCUA_SERVERS[station_no]["nodes"]

        #Create a new dict to check the received data from the Station
        self.node_map = {}
        for node_name, node_id in self.node.items():
            self.node_map[node_id] = node_name

        #Create a dict to hold the data received from the Server subscription
        self.latest_values = {}
        self.subscription = None

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

    #Read from the Server
    def subscribe_node(self, node_name):
        
        node_id = self.node[node_name]
        node = self.client.get_node(node_id)

        self.subscription.subscribe_data_change(node)

    def create_subscription(self):

        handler = SubscriptionHandler(self.latest_values, self.node_map)

        self.subscription = self.client.create_subscription(
            1000,
            handler
    )

    #Request for all tag that will be read from the station
    def subscribe_all_nodes(self):

        for node_name in self.node:
            self.subscribe_node(node_name)
                

