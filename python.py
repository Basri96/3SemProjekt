from sense_hat import SenseHat
import time

sense = SenseHat()
sense.clear()



while True:
    pressure = sense.get_pressure()
    pressure = round(pressure,1)
    print(pressure)
    sense.show_message(str(pressure))
    time.sleep(5)
