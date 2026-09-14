from core import OPCUAClient
import time

client = OPCUAClient("station1")

client.connect()
client.create_subscription()
client.subscribe_node("state_no")

print("Subscription active. Waiting for changes...")

try:
    while True:
        time.sleep(1)

except KeyboardInterrupt:
    client.disconnect()