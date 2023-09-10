import random
import time
from azure.iot.device import IoTHubDeviceClient, Message

CONNECTION_STRING = "HostName=chaachub.azure-devices.net;DeviceId=orangeBox;SharedAccessKey=ESBu8Ry8JAWX6aIE32NgstA4g6SpkWKFo9ztLsftuVM="

MSG_SND = '{{"temperature": {temperature},"humidity": {humidity}}}'


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
            # Simulate temperature and humidity values for testing
            humidity = random.uniform(30, 60)
            temperature = random.uniform(20, 30)

            msg_txt_formatted = MSG_SND.format(temperature=temperature, humidity=humidity)
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
