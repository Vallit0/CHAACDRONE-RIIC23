# Rally Interdepartamental de Innovación 4.0 (SENACYT) 🧑‍🔬 🗺️
# Equipo Chaac 🥬 
# Configuracion Orange Pi 🍊

## PASO 1
1. Buscar una MICRO SD que funcionara como Hard Disk
2. Descargar [Ambian](https://www.armbian.com/orange-pi-zero/) (Sistema Operativo para Orange Pi)
3. Descargar [Etcher](https://etcher.balena.io/)

Esto ya lo he hecho antes, básicamente tomas una memoria y la conviertes en un dispositivo "Booteable". Esto significa que descargas el SO a la memoria y la computadora accede a ella una única vez para instalarlo. Etcher sirve para hacer "bootable" memoria, Ambien es el sistema operativo. 

:green_heart: Green Light and Red Light -> Ready To Use

## PASO 2
Eventualmente se necesita una conexión para hacer uso de ella. Se puede usar USB o RX/TX Serial UART

1. Conectar Via USB Orange Pi y usar Arduino IDE
2. Abrir Terminal (Monitor)

Notarás aquí que básicamente se entra a una terminal de UBUNTU o UNIX.

- El password default es **1234**
- El usuario default es **root**

Luego de esto debe aparecer una sección para setear nuevos password y usuario.

Luego debe aparecer un prompt: `root@rangepizero:-#`

(Cada vez que ponga '>>' de aquí en adelante, significa lo que debes ingresar en consola, un comando básicamente. Si ves algo entre `<>`, significa que todo es sustituible, por ejemplo `<nombre>@gmail`, algo correcto sería `estuardo@gmail`.)

3. Ver información del Sistema (Opcional)
3. Ver informacion Sistema (Opcional) 
>> ls 
Si no aparece nada, no importa. 
>> df -h (Disk Free -Human) Ver que tanta memoria hay etc etc
 
>> find 

>> cat /proc/cpuinfo

Configurar Network (DESDE TU COMPUTADOR)
Conecta el OrangePi Zero a tu Router 
>> nmap -sn [INSERTAR TU RED]/24 (network Map, Search Networks buscamos hosts. Un host es un computador que puede recibir y/o enviar datos. Un host se identifica con un IP ADDRESS) 

Te puedes evitar este paso y usar una aplicacion de Android llamada 
FING que te mapea todos los dispositivos. 

Apunta el IP ADDRESS NUEVO 
>> <USERNAME>@<IP ADDRESS>

# Python, Librerías y Dependencias :snake:
Uno de los problemas que se dieron durante la ejecución del proyecto fue el uso de Python 3.6 pues Orange Pi solamente permite el uso hasta la versión Python 5, este problema es algo interesante pues la integración directa con Azure se lleva a cabo por medio de un SDK (Librería en Python) y el análisis de imágenes y correlación de datos con múltiples librerías como Tensorflow y OpenCV, así que fue necesario un cambio. 

## Actualización Sistema Operativo 🖥️
# Pinout y Necesario 🔌

# Azure IoT Reference Architecture :electron:
'''cmd
>> az iot hub monitor-events --hub-name <<NOMBRE_TU_HUB>> --device-id <<NOMBRE_TU_DISPOSITIVO>>
'''
# ¿Cómo sabmos cuantos datos son necesarios para una medición ótpima? 📚 
Para esto, se debe hacer uso de Estadística Inferencial. Para ello, acdimos a lo llamada 
## Intervalos de Confianza 
https://newprairiepress.org/cgi/viewcontent.cgi?article=1397&context=agstatconference

Bajo este estudio, es posible notar que solamente se deben realizar 12 muestreos maximos si se asume **Normalidad** en los datos. 
## Estado del Arte de Vuelos Autonomos
https://la.mathworks.com/help/uav/ug/approximate-high-fidelity-uav-model-with-guidance-model.html

