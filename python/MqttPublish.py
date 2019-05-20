import paho.mqtt.client as mqtt
import datetime
import json
from random import randint
import time
import sys

# Ejemplo de programa que publica en Topic del Broker MQTT
# Utiliza la biblioteca PAHO de eclipse para conexiones MQTT
#Parametros Genelares y del Broker MQTT

# IP o nombre del broker
host = "localhost"

topic_leds       = "iot2017/led/#"
topic_ledon   = "iot2017/led/1"
topic_ledoff  = "iot2017/led/2"
topic_temphum = "iot2017/temphum"

# conexion al Broker
def on_connect(client, userdata, flags, rc):
  print("Connected with result code "+str(rc))
  client.subscribe(topic_leds)

# Recepcion de Mensajes (Este ejemplo no hace nada, solo imrime el mensaje)
def on_message(client, userdata, msg):
  #if msg.payload.decode() == "Hello world!":
  fecha=  datetime.datetime.now()
  print(str(fecha)+"   Topic:"+msg.topic+"   Mensaje:"+msg.payload.decode())



temp=22+randint(0,20)

client = mqtt.Client(client_id="PEDRO_PERS")
try:
    client.connect(host,1883,60)
except IOError as e:
    print ("Error al conectar al Broker error({0}): {1}".format(e.errno, e.strerror))
    sys.exit(1)
except:
    print ("Unexpected error:", sys.exc_info()[0])
    raise

### inicio del Programa
fecha=  datetime.datetime.now()
print("FECHAx:",fecha)
num_envios = 5
pausa = .3

mensaje = topic_temphum +" >> Python MAC  Hello world! Esta es una prueba "+str(fecha)
conta = 0
while (conta <  num_envios ):
  var2 =  {'temperatura': temp, 'id': "ABC123",'estacion':'macosx','motor': str(randint(1,4))}
  j2 = str(json.dumps( var2))
  j2 = "0,DUMMSTATION,20, "+str(conta)
  topic = "iot2017/led/"+str(conta % 4)
  print ("Topic:["+topic+"]  Envia:["+j2+"]")
  client.publish(topic, j2);
  conta= conta +1
  client.publish(topic_temphum, mensaje)
  time.sleep(pausa)

client.publish(topic_ledoff, j2);
print ("Topic:["+topic_temphum+"]  Envia:["+mensaje+"]")
client.disconnect();
