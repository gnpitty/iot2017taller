import paho.mqtt.client as mqtt
import datetime
import json
from random import randint


fecha=  datetime.datetime.now()
print("FECHA:",fecha)

# This is the Publisher
host = "gncon2017a"

host = "172.100.1.100"
topic ="iot2017/led/3"
temp=22+randint(0,20)
print("Conectar....:")

client = mqtt.Client()
client.connect(host,1883,60)

mensaje = topic +" >> Python 3 MAC  Hello world! Esta es una prueba 2222  "+str(fecha)
print("Conectar....:"+mensaje)
var2 =  {'temperatura': temp, 'id': "ABC123",'estacion':'linkit7688Duo'}
j2 = str(json.dumps( var2, sort_keys=True, indent=4))

j2 = str(json.dumps( var2))
print(j2)


print ("Topic:"+topic+"Envia:["+j2+"]")

client.publish(topic, j2);
client.disconnect();

