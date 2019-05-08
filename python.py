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
    print(pressure)
    sense.show_message(str(pressure))
    #pressure = round(pressure,1)
    trykEfterVaegt = pressure - 1002
    VaegtIGram = round(400/trykEfterVaegt)
      
    data = "Current time " + str(datetime.now()) + "Weight " + str(VaegtIGram)
    s.sendto(bytes(data, "UTF-8"), ('<broadcast>', BROADCAST_TO_PORT))
    print(data)
    time.sleep(5)
