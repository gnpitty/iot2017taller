#!/usr/bin/env python3

import paho.mqtt.client as mqtt
import datetime
import sys


host = "gncon2017a"
host = "mqtt.mcs.mediatek.com"
host = "localhost"


topic1 = "mcs/D9SXS1fo/rEh6HWgwVbonHsY6/#"


topic_leds       = "iot2017/led/#"
topic_ledon   = "iot2017/led/3"
topic_ledoff  = "iot2017/led/0"

topic_temphum = "iot2017/temphum"
topic_servo   = "lacola"
topic_distancia   = "iot2017/distancia"
topic_resp =    "iot2017/respuesta";

# This is the Subscriber
print("Host:"+host)
def on_connect(client, userdata, flags, rc):
  print("Connected with result code "+str(rc))
  client.subscribe(topic_leds)
  client.subscribe(topic_temphum)
  client.subscribe(topic_servo)
  client.subscribe(topic_distancia)
  client.subscribe(topic_resp)




def on_message(client, userdata, msg):
  #if msg.payload.decode() == "Hello world!":
  fecha=  datetime.datetime.now()
  print(str(fecha)+"   Topic:"+msg.topic+"   Mensaje:"+msg.payload.decode())



    #client.disconnect()

client = mqtt.Client(client_id="MArtAPEREZ")
try:
    client.connect(host,1883,60)
except IOError as e:
    print ("Error al conectar al Broker error({0}): {1}".format(e.errno, e.strerror))
    sys.exit(1)
except:
    print ("Unexpected error:", sys.exc_info()[0])
    raise

client.on_connect = on_connect
client.on_message = on_message

client.loop_forever()
