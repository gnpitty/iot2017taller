lighton=0
pin=7
localpin= 4

gpio.mode(pin,gpio.OUTPUT) -- Assign GPIO to Output
gpio.mode(localpin,gpio.OUTPUT)

function    prueba()
    print("M:" .. tostring(lighton))
    if lighton==0 then
        lighton=1
        gpio.write(pin,gpio.HIGH) -- Assign GPIO On
        gpio.write(localpin,gpio.HIGH)
    else
        lighton=0
         gpio.write(pin,gpio.LOW) -- Assign GPIO off
         gpio.write(localpin,gpio.LOW)
    end
end



cfg = {
  ip = "192.168.1.26",
  netmask = "255.255.255.0",
  gateway = "192.168.1.1"
}

wifi.sta.setip(cfg)
wifi.setmode(wifi.STATION)
wifi.sta.config("GNConsult50","maria123")
print( wifi.sta.getip())

sv = net.createServer(net.TCP, 30)

function receiver(sck, data)
  print(data)
  sck:close()
end

if sv then
    sv:listen(80, function(conn)
    conn:on("receive", receiver)
 --   conn:send("hello world")
    buffer =  'HTTP/1.1 200 OK\n\n'
     buffer = buffer .. '<!DOCTYPE HTML>\n'
    buffer = buffer .. '<html>\n'
    buffer = buffer .. '<head><meta  content="text/html; charset=utf-8">\n'
    buffer = buffer .. '<title>ESP8266</title></head>\n'
    buffer = "<h1> Hello, NodeMcu PRUEBA.</h1>"
    buffer = buffer .. tmr.time()
    prueba()
    tmr.delay(80000)
    conn:send(buffer)
   
  end)
end
