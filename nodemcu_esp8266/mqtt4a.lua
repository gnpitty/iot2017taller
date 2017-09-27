loadfile("wifi1.lua")
print("Inicio MQTT")

MQTT_BrokerIP = "192.168.1.128"
MQTT_BrokerPort = 1883
MQTT_ClientID = "esp-001"

pin= 7
gpio.mode(pin,gpio.OUTPUT)
lighton=1

function    blink()
    print("H:" .. tostring(lighton))
    if lighton==0 then
        lighton=1
        gpio.write(pin,gpio.HIGH) -- Assign GPIO On
    else
        lighton=0
         gpio.write(pin,gpio.LOW) -- Assign GPIO off
    end
end

function    ledOFF()
         gpio.write(pin,gpio.LOW) -- Assign GPIO off
end




m = mqtt.Client(MQTT_ClientID, 120)

m:on("message", function(client, topic, data) 
    print(" ************* MQTT topic: "..topic .. ":" ) 
    conta = 1
    print("BLINKING LOOP..")
    while conta < 10 do
    conta=conta+1
    blink()
    --tmr.delay(500000)
    end
    conta = 1
    ledOFF()
    if data ~= nil then
        print(data)
    end
end)

m:on("offline", function(client)
    publishMqtt:stop()
    print("MQTT: offline")
end)

--MQTT reconnect logic timer
reconnMqtt = tmr.create()
function despuesConectar(client) 
    print("MQTT: connected")
    --publishMqtt:start()
    print("PUB: started")
    client:subscribe({["mqtt/queue/100"]=0,["mqtt/queue/400"]=1,topic2=2},0 , function(client) print("subscribe success") end)
    publishMqtt:start()
    --publishMqtt:stop()
     --  print("MQTT: connection failed with reason "..reason)
    --publishMqtt:start()
end 

reconnMqtt:register(10, tmr.ALARM_SEMI, function (t)
  reconnMqtt:interval(2500);
  print("MQTT: trying to connect to "..MQTT_BrokerIP..":"..MQTT_BrokerPort);
  m:close()
  m:connect(MQTT_BrokerIP, MQTT_BrokerPort, 0, despuesConectar , function(client, reason) 
    publishMqtt:stop()
    print("MQTT: connection failed with reason "..reason)
    reconnMqtt:start()
 end)
end)

--MQTT local timestamp publishing timer
function publicar() 
  --blink()
 -- if not 
 -- m:publish("mqtt/queue/300", "ABC1234567890XYZ:"..tmr.time().."."..((tmr.now()/1000)%1000), 0, 0)
  --if not 
 -- m:publish("mqtt/queue/300", "ABC1234567890XYZ:" , 0, 0)
-- then
    print("Publicando Temperatura:");

    pin = 5
print(conta)
status, temp, humi, temp_dec, humi_dec = dht.read(pin)
if status == dht.OK then
   tempvar = string.format("DHT Temperature:%d.%03d;Humidity:%d.%03d\r\n",
          math.floor(temp),
          temp_dec,
          math.floor(humi),
          humi_dec
    )
    -- Integer firmware using this example
    print(tempvar)
m:publish("mqtt/queue/300", tempvar , 0, 0)
    -- Float firmware using this example
   -- print("DHT Temperature:"..temp..";".."Humidity:"..humi)

elseif status == dht.ERROR_CHECKSUM then
    print( "DHT Checksum error." )
elseif status == dht.ERROR_TIMEOUT then
    print( "DHT timed out." )
end
  --end
end

print("** PUBLICAR... ")
publishMqtt = tmr.create()
publishMqtt:register(30000, tmr.ALARM_AUTO, publicar)

reconnMqtt:start()
