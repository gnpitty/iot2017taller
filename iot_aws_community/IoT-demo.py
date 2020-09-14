'''
/*
 * Copyright 2010-2017 Amazon.com, Inc. or its affiliates. All Rights Reserved.
 *
 * Licensed under the Apache License, Version 2.0 (the "License").
 * You may not use this file except in compliance with the License.
 * A copy of the License is located at
 *
 *  http://aws.amazon.com/apache2.0
 *
 * or in the "license" file accompanying this file. This file is distributed
 * on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either
 * express or implied. See the License for the specific language governing
 * permissions and limitations under the License.
 */
 '''

from AWSIoTPythonSDK.MQTTLib import AWSIoTMQTTClient
import logging
import time
import datetime
import json
import random
import uuid
#import paho.mqtt.client as mqtt



######------------------------------
AllowedActions = ['both', 'publish', 'subscribe']



# Custom MQTT message callback
def printMessage(message):
    logger.info("Received a new message: ")
    logger.info(message.payload)
    logger.info(type(message.payload))
    logger.info("from topic: ")
    logger.info(message.topic)
    logger.info("--------------\n\n")

def customCallback(client, userdata, message):
    printMessage(message)
    payload = message.payload.decode("utf-8")
    payload_dict = json.loads(payload)
    logger.info("data:"+str(payload_dict))

def mensaje_simulado(mensaje,tipo,estacion,serial):
        fecha=  str(datetime.datetime.now())
        temperatura = random.randint(26,36)
        humedad = random.randint(50,87)
        message = {}
        message['estacion'] = estacion
        message['time_stamp'] = datetime.datetime.now().timestamp()
        message['message'] = mensaje +" "+ fecha
        message['serialNumber'] = serial
        message['sequence'] = loopCount
        message['temperatura'] = temperatura
        message['humedad'] = humedad
        message['tipo'] = tipo

        message['uuid'] = str(uuid.uuid4())
        return message

#
host = "a2ujrzvqdjq89h-ats.iot.us-east-1.amazonaws.com"
rootCAPath = "certificados/root-CA.crt"
port = 8883
clientId = "basicPubSub"

## Certificados de IoT Core
certificatePath = "certificados/f7cc2449ac-certificate.pem.crt"
privateKeyPath =  "certificados/f7cc2449ac-private.pem.key"
#certificatePath = "certs-demo-iot/8b84afdafb-certificate.pem.crt"
#privateKeyPath =  "certs-demo-iot/8b84afdafb-private.pem.key"


topic = "demo/temperatura"
#Datos simulados (se cambian por dispositivo)
tipo = "MAC-OSX"
estacion =  "MAC-OSX-GNC-001"
mensaje = "Prueba desde la MAC "
serial = "SN-D7F3C8947867"




# Configure logging
logger = logging.getLogger("AWSIoTPythonSDK.core")
logger.setLevel(logging.INFO)
streamHandler = logging.StreamHandler()
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
streamHandler.setFormatter(formatter)
logger.addHandler(streamHandler)

# Parametros de MQTT AWS  AWSIoTMQTTClient
myAWSIoTMQTTClient = None


myAWSIoTMQTTClient = AWSIoTMQTTClient(clientId)
myAWSIoTMQTTClient.configureEndpoint(host, port)
myAWSIoTMQTTClient.configureCredentials(rootCAPath, privateKeyPath, certificatePath)

# AWSIoTMQTTClient connection configuration
myAWSIoTMQTTClient.configureAutoReconnectBackoffTime(1, 32, 20)
myAWSIoTMQTTClient.configureOfflinePublishQueueing(-1)  # Infinite offline Publish queueing
myAWSIoTMQTTClient.configureDrainingFrequency(2)  # Draining: 2 Hz
myAWSIoTMQTTClient.configureConnectDisconnectTimeout(10)  # 10 sec
myAWSIoTMQTTClient.configureMQTTOperationTimeout(5)  # 5 sec
logger.debug("*** Antes de conectar...")
# Conecxion al Broker
myAWSIoTMQTTClient.connect()
# Subscripcion al topico
myAWSIoTMQTTClient.subscribe(topic, 1, customCallback)
logger.debug("*** Conectado...")
time.sleep(2)

# Publicacion a Topico
loopCount = 0
while loopCount < 10 :
        message = mensaje_simulado(mensaje,tipo,estacion,serial)
        messageJson = json.dumps(message)
        myAWSIoTMQTTClient.publish(topic, messageJson, 1)
        logger.info('Published topic:{}  messageJson:{} \n'.format (topic, messageJson))
        loopCount += 1
        time.sleep(5)
# Loop para esperar nuevos mensajes
print("Fin de Publicacion*** ")
while True :
    time.sleep(.1)
