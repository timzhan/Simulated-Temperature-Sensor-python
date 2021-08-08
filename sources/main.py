######################################################################################
# This sample is to create a simulated temperature sensor module using Azure IoT Device Python SDK
# v0.1
# by tz
######################################################################################

import asyncio
from azure.iot.device.aio import IoTHubModuleClient
from azure.iot.device import Message
import json
import random as rnd
import time


number_of_messages = 20

# Write a method to simulate telemetry
def simulate_telemetry():
    t = round(rnd.uniform(10.0, 35.0), 2)
    h = round(rnd.uniform(0.1, 0.8), 2)

    telemetry = {
        "temperature": t,
        "humidity": h
        }

    return telemetry

async def main():
    # Set EdgeHub Connection String
    # Azure Global
    # EdgeHubConnectionString = "HostName=iothub-0707.azure-devices.net;DeviceId=RPi4-01;SharedAccessKey=INh*************************nxo="
    
    # Azure China
    EdgeHubConnectionString="HostName=iothub-0713.azure-devices.cn;DeviceId=RPi4-01;SharedAccessKey=Lr1*************************HI4="

    # Create client object to interact with Azure IoT Hub
    # module_client = IoTHubModuleClient.create_from_edge_environment()
    module_client = IoTHubModuleClient.create_from_connection_string(EdgeHubConnectionString)

    # Connect the client
    await module_client.connect()


    # define a send_test_message method
    async def send_test_message(n):
        for i in range(1, n + 1):
            print("Sending message # " + str(i))
            msg = Message(json.dumps(simulate_telemetry()))
            await module_client.send_message(msg)
            print("Successfully sent message #" + str(i))
            time.sleep(1)

    # send `specified times` messages in parallel
    await send_test_message(number_of_messages)

    # Finally, disconnect
    await module_client.disconnect()


if __name__ == "__main__":
    asyncio.run(main())

