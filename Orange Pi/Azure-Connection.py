import random
import Adafruit_DHT
import time
from azure.iot.device import IoTHubDeviceClient, Message


#Definicion de Sensores
sensor = Adafruit_DHT.DHT22
pin = 4 #Pin de humedad (Faltarian los demas pines)
print(pin)
#define the connection String, go to IoT Hub -Devices - Primary connection String -> Conectar datos
CONNECTION_STRING = "HostName=hub name.azure-devices.net;DeviceId=your device id;SharedAccessKey=copied key"

#Aqui vamos a enviar los datos a Azure
MSG_SND = '{{"temperature": {temperature},"humidity": {humidity}}}'

while True:
    humidity, temperature = Adafruit_DHT.read_retry(sensor, pin) #Lectura de las variables

    #Function to connect Pi to IoT Hub using the connection string that is predefined up there
    def iothub_client_init():
        client = IoTHubDeviceClient.create_from_connection_string(CONNECTION_STRING)
        return client
        #function to send the data to hub
    def iothub_client_telemetry_sample_run():
        try:  #this is to help catch any possible errors.
            client = iothub_client_init()
            print ( "AronAyub Pi is Sending data to IoT Hub, To exit, press Ctrl-C " )
            while True:
                msg_txt_formatted = MSG_SND.format(temperature=temperature, humidity=humidity)
                message = Message(msg_txt_formatted)
                print( "Sending message: {}".format(message) )
                client.send_message(message)
                print ( "Message successfully sent" )
                time.sleep(10)
        except KeyboardInterrupt:
            print ( "IoTHubClient stopped" )

    if __name__ == '__main__':
        print ( "Press Ctrl-C to exit" )
        iothub_client_telemetry_sample_run()
