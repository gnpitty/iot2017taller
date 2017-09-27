#!/usr/bin/env python3
import paho.mqtt.client as mqtt
import datetime
import time



estado=1
host = "172.100.1.100"
topic1 = "mqtt/queue/100"
topic2 = "mqtt/queue/200"
topic3 = "mqtt/queue/#"


# This is the Subscriber
print("Topic:"+topic1)
def on_connect(client, userdata, flags, rc):
  print("Connected with result code "+str(rc))
  client.subscribe(topic1)
  client.subscribe(topic2)
  client.subscribe(topic3)


def on_message(client, userdata, msg):
  fecha=  datetime.datetime.now()
  blink()
  topic = msg.topic
  print(str(fecha)+"   Topic:"+msg.topic+"   Mensaje:"+msg.payload.decode())
  if  topic == "mqtt/queue/100" :
     ledON()
  if  topic == "mqtt/queue/200" :
     ledOFF()
  if  topic == "mqtt/queue/400" :
     conta = 1
     while conta < 10:
       blink()
       time.sleep(.100)
       conta = conta +1
     ledOFF()


def blink():
  global estado
  #if msg.payload.decode() == "Hello world!":
  print("blinking.."+str(estado))
  if estado == 1:
     x.write(1)
     y.write(0)
     estado = 0
  else:
     x.write(0)
     y.write(1)
     estado = 1
    
def ledON():
     global estado
     x.write(1)
     y.write(1)
     estado = 1

def ledOFF():
     global estado
     x.write(0)
     y.write(0)
     estado = 0


#client.disconnect()

client = mqtt.Client()
client.connect(host,1883,60)

client.on_connect = on_connect
client.on_message = on_message

client.loop_forever()

