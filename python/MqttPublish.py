import paho.mqtt.client as mqtt
import datetime
import json
from random import randint
import time
import sys


fecha=  datetime.datetime.now()
print("FECHAx:",fecha)

# This is the Publisher

host = "192.168.1.128"
host = "gncon2017a"
host = "localhost"

topic ="mqtt/queue/100"

topic_ledon   = "iot2017/led/1"
topic_ledoff  = "iot2017/led/2"
topic_temphum = "iot2017/temphum"
topic_servo   = "iot2017/servo"
topic_resp =    "iot2017/respuesta";

def on_connect(client, userdata, flags, rc):
  print("Connected with result code "+str(rc))
  client.subscribe(topic_resp)

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
mensaje = topic +" >> Python 3 MAC  Hello world! Esta es una prueba 2222  "+str(fecha)





conta = 1
while (conta <  10 ):
  var2 =  {'temperatura': temp, 'id': "ABC123",'estacion':'macosx','motor': str(randint(1,4))}
  j2 = str(json.dumps( var2))
  j2 = "0,DUMMSTATION,20, "+str(conta)
  topic = "iot2017/led/"+str(conta % 4)
  print ("Topic:["+topic+"]  Envia:["+j2+"]")
  client.publish(topic, j2);
  conta= conta +1
# client.publish(topic_servo, j2);
  time.sleep(.5)
  if conta % 16 ==0 :
    time.sleep(1)

#client.publish(topic_servo, j2);
client.publish(topic_ledoff, j2);
client.disconnect();
