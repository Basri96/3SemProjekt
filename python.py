BROADCAST_TO_PORT = 7500
from sense_hat import SenseHat
import time
from socket import *
from datetime import datetime

sense = SenseHat()
sense.clear()

s = socket(AF_INET, SOCK_DGRAM)
#s.bind(('', 14593))     #(ip, port)
# no explicit bind: will bind to default IP + random port
s.setsockopt(SOL_SOCKET, SO_BROADCAST, 1)


while True:
    pressure = sense.get_pressure()
    print(round(pressure,1))
    sense.show_message(str(round(pressure,1)))
    #pressure = round(pressure,1)
    trykEfterVaegt = (pressure - 996)
    print("tryk efter vaegt " + str(round(trykEfterVaegt,1)))
    vaegtIGram = round((trykEfterVaegt)*105)
    print("vaegt i gram " + str(round(vaegtIGram,1)))
    
      
    data = "Current time " + str(datetime.now()) + "Weight " + str(vaegtIGram)
    s.sendto(bytes(data, "UTF-8"), ('<broadcast>', BROADCAST_TO_PORT))
    print(data)
    time.sleep(1)
