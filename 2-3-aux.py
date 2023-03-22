import RPi.GPIO as GPIO
import time

leds = [24, 25, 8, 7, 12, 16, 20, 21]
aux = [2, 3, 14, 15, 18, 27, 23, 22]

GPIO.cleanup()
GPIO.setmode(GPIO.BCM)
GPIO.setup(aux, GPIO.IN)
GPIO.setup(leds, GPIO.OUT)

while True:
    for i in range(8):
        GPIO.output(leds[i], GPIO.input(aux[i]))

GPIO.output(leds, 0)
GPIO.cleanup()
