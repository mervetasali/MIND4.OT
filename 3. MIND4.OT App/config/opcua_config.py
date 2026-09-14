
#OPC UA Servers Data
OPCUA_SERVERS = {
    "station1": {
        "endpoint" : "opc.tcp://192.168.0.1:4840",
        "nodes" : {
            "start_request" : "ns=4;i=942",
            "stop_request" : "ns=4;i=943",
            "state_no_act" : "ns=4;i=953",
            "state_no" : "ns=4;i=908",
            "state_description" : "ns=4;i=909",
            "error_code" : "ns=4;i=910",
            "error_description" : "ns=4;i=911",
            "warning_code" : "ns=4;i=912",
            "warning_description" : "ns=4;i=913",
            "produced_count" : "ns=4;i=915",
            "orderID" : "ns=4;i=900",
            "productID" : "ns=4;i=901",
            "serial_no" : "ns=4;i=904",
            "receipeID" : "ns=4;i=902",
            "target_quantity" : "ns=4;i=903",
            "material_act_level" : "ns=4;i=879",
            "temperature_act_level" : "ns=4;i=880",
            "pressure_act_level" : "ns=4;i=881",
            "mes_orderID" : "ns=4;i=890",
            "mes_productID" : "ns=4;i=891",
            "mes_receipeID" : "ns=4;i=892",
            "mes_target_quantity" : "ns=4;i=893"
        },

        "types" : {
            "start_request" : "Boolean",
            "stop_request" : "Boolean",
            "state_no_act" : "UInt16",
            "state_no" : "UInt16",
            "state_description" : "String",
            "error_code" : "UInt16",
            "error_description" : "String",
            "warning_code" : "UInt16",
            "warning_description" : "String",
            "produced_count" : "UInt16",
            "orderID" : "String",
            "productID" : "UInt16",
            "serial_no" : "UInt16",
            "receipeID" : "UInt16",
            "target_quantity" : "UInt16",
            "material_act_level" : "Float",
            "temperature_act_level" : "Float",
            "pressure_act_level" : "Float",
            "mes_orderID" : "String",
            "mes_productID" : "String",
            "mes_receipeID" : "String",
            "mes_target_quantity" : "UInt16"
        }
    }, 
    "station2": {},
    "station3": {}
}

