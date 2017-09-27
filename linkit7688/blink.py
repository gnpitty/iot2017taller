import mraa
import time

# pin 44 interno y 43 externo 

pin43 = 44 
pin21 = 21 
pin20 = 20

x = mraa.Gpio(pin43)
y = mraa.Gpio(pin20)
z = mraa.Gpio(pin21)

x.dir(mraa.DIR_OUT)
y.dir(mraa.DIR_OUT)
z.dir(mraa.DIR_OUT)

def blink(delay1,conta1 ):
  conta = 1
  while conta < conta1 :
    x.write(1)
    y.write(0)
    z.write(1)
    time.sleep(delay1)
    x.write(0)
    y.write(1)
    z.write(0)
    time.sleep(delay1)
    conta = conta +1

while True:
  blink(.1,20 )
  print (".")
  time.sleep(1)
