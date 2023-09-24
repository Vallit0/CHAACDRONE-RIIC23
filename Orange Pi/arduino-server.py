import time
import logging

import sys

sys.path.append("lib")

from arduino_iot_cloud import ArduinoCloudClient

DEVICE_ID = b"5f6c551a-20a7-4913-8f5e-03589b7fa4c0"
SECRET_KEY = b"PRFJWUOKNUD0E2ENZNPO"


def logging_func():
    logging.basicConfig(
        datefmt="%H:%M:%S",
        format="%(asctime)s.%(msecs)03d %(message)s",
        level=logging.INFO,
    )


# This function is executed each time the "ledSwitch" variable changes
def on_switch_changed(client, value):
    print("Switch Pressed! Status is: ", value)


if __name__ == "__main__":
    logging_func()
    client = ArduinoCloudClient(device_id=DEVICE_ID, username=DEVICE_ID, password=SECRET_KEY)

    client.register("temperature")
    client["temperature"] = 20
    client.register("ledSwitch", value=None, on_write=on_switch_changed)

    client.start()