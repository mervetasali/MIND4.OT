from core import OPCUAClient
from asyncua import ua


client = OPCUAClient("station1")

try:
    client.connect()

    client.write_node(
        "mes_orderID",
        "ORD-2026-0005"
    )

    client.write_node(
        "mes_productID",
        "CAP-2L"
    )

    client.write_node(
        "mes_receipeID",
        "RCP-999"
    )

    client.write_node(
        "mes_target_quantity",
        999,
    )

    print("OrderID write successful.")

finally:
    client.disconnect()