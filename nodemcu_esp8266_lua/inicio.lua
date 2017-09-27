print("Inicio....")
lighton=0
localpin= 4
gpio.mode(localpin,gpio.OUTPUT)

function    prueba()
    print("Init:" .. tostring(lighton))
    if lighton==0 then
        lighton=1
        gpio.write(localpin,gpio.HIGH)
    else
        lighton=0
         gpio.write(localpin,gpio.LOW)
    end
end

function parpadea()
 for conta=0,8,1
  do
  prueba()
  tmr.delay(200000)
end
end

function startup()
    print('in startup')
    
    dofile('script3.lua')
    end
print("ESPERA 5 secs")
parpadea()
tmr.alarm(0,5000,0,startup)
 

