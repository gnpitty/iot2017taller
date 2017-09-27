#include <SPI.h>
#include <Ethernet.h>
#include <PubSubClient.h>

// Direccion MAC
byte mac[] = { 0xDE, 0xAD, 0xBE, 0xEF, 0xFE, 0xED };

// IP del servidor
IPAddress mqtt_server(172, 100, 1, 100);
IPAddress ip(172, 100, 1, 170);
int estado = 1;

// Topic con el que trabajamos
const char* topicName = "iot2017/led/#";
const char* topicName2 = "iot2017/led/3";

EthernetClient ethClient;
PubSubClient client(ethClient);

void setup()
{
  pinMode(LED_BUILTIN, OUTPUT);
  Serial.begin(9600);
  Ethernet.begin(mac,ip);
  Serial.println(Ethernet.localIP());
  /**
  if (Ethernet.begin(mac) == 0) {
    Serial.println("Failed to configure Ethernet using DHCP");
  }
  **/
  client.setServer(mqtt_server, 1883);
}

void callback(char* topic, byte* payload, unsigned int length) {
  Serial.print("Message arrived [");
  Serial.print(topic);
  Serial.print("] ");
  blink();
  int i=0;
  for (i=0;i<length;i++) {
    Serial.print((char)payload[i]);
  }
  Serial.println();
}

void blink() {
  if (estado == 1){
  digitalWrite(LED_BUILTIN, HIGH);
  estado = 0;
  } else {
    digitalWrite(LED_BUILTIN, LOW);  
     estado = 1;
  }                     
}

void loop()
{

  
  if (!client.connected()) {
      Serial.print("Connecting ...");
      if (client.connect("arduino_station")) {
        Serial.println("connected");
        boolean sub1 = client.subscribe(topicName);
        
        
         Serial.print("subscribe:");
          Serial.print(sub1);
         client.setCallback (callback);
            
      } else {
        delay(5000);
      }
      
  }/*else {
     client.publish(topicName2,"3,ARDUINOSTATION,Esta es una prueba desde arduino .........");
   }*/
     
  // Cliente a la escucha
  client.loop();
}
