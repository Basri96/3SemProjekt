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

#While loop for at kalibrer start trykket, da censoren ikke er tændt til at starte med
#if delen er for at gøre den mere korrekt da den ikke måler det korrekte tryk når den starter
while True:
    pressurecalibration = sense.get_pressure()
    if pressurecalibration >= 950:
        break
    time.sleep(5)
    
#Får pressure hver ~(10) sekund og printer det ud.
while True:
    pressure = sense.get_pressure()
    print(round(pressure,1))
    sense.show_message(str(round(pressure,1)))
    #pressure = round(pressure,1)
    trykEfterVaegt = (pressure - pressurecalibration)
    print("tryk efter vaegt " + str(round(trykEfterVaegt,1)))
    vaegtIGram = round((trykEfterVaegt)*300)
    #Fordi baggrundstrykket varierer så når der ikke er noget ekstra vægt vil den give minus tryk, som så bliver sat til 0
    if vaegtIGram < 0:
        vaegtIGram = 0
    print("vaegt i gram " + str(round(vaegtIGram,1)))
    
    #Finder Current time and date, og kombinerer det med vægten fra før og broadcaster dataen, hvor recieveren opfanger det  
    data = "Current time " + str(datetime.now()) + " Weight " + str(vaegtIGram)
    s.sendto(bytes(data, "UTF-8"), ('<broadcast>', BROADCAST_TO_PORT))
    print(data)
    time.sleep(10)
