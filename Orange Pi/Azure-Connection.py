import random
import time
import datetime
from azure.iot.device import IoTHubDeviceClient, Message

CONNECTION_STRING = "HostName=chaachub.azure-devices.net;DeviceId=orangeBox;SharedAccessKey=ESBu8Ry8JAWX6aIE32NgstA4g6SpkWKFo9ztLsftuVM="

MSG_SND = '{{"temperature": {temperature}, "humidity": {humidity}, "pressure": {pressure}, "soil_temp": {soil_temp}, "soil_hum": {soil_hum}, "TimeStamp": "{TimeStamp}", "UTC": "{UTC}", "description": "{description}", "danger": "{danger}"}}'



def iothub_client_init():
    try:
        client = IoTHubDeviceClient.create_from_connection_string(CONNECTION_STRING)
        return client
    except Exception as e:
        print("Error initializing IoT Hub client:", str(e))
        return None


def iothub_client_telemetry_sample_run():
    client = iothub_client_init()
    if client is None:
        return

    try:
        print("Sending data to IoT Hub. To exit, press Ctrl-C")
        while True:

            # Generate random values for the fields
            humidity = random.uniform(30, 60)
            temperature = random.uniform(20, 30)
            pressure = random.uniform(900, 1100)  # Replace with appropriate pressure range
            soil_temp = random.uniform(10, 30)  # Replace with appropriate soil_temp range
            soil_hum = random.uniform(40, 80)  # Replace with appropriate soil_hum range
            TimeStamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            UTC = "UTC+0"
            description = "Sample description"
            danger = '0'  # Replace with an appropriate danger level

            # Define the MSG_SND string
            MSG_SND = '{{"temperature": {temperature}, "humidity": {humidity}, "pressure": {pressure}, "soil_temp": {soil_temp}, "soil_hum": {soil_hum}, "TimeStamp": "{TimeStamp}", "UTC": "{UTC}", "description": "{description}", "danger": "{danger}"}}'

            # Format the MSG_SND string with the generated values
            msg_txt_formatted = MSG_SND.format(temperature=temperature,
                                               humidity=humidity,
                                               pressure=pressure,
                                               soil_temp=soil_temp,
                                               soil_hum=soil_hum,
                                               TimeStamp=TimeStamp,
                                               UTC=UTC,
                                               description=description,
                                               danger=danger)

            # Create a message object with the formatted string
            message = Message(msg_txt_formatted)

            print("Sending message: {}".format(message))
            client.send_message(message)

            print("Message successfully sent")
            time.sleep(10)
    except KeyboardInterrupt:
        print("IoTHubClient stopped")


if __name__ == '__main__':
    print("Press Ctrl-C to exit")
    iothub_client_telemetry_sample_run()
