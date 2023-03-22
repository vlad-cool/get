import RPi.GPIO as GPIO
import time

leds = [24, 25, 8, 7, 12, 16, 20, 21]

GPIO.cleanup()
GPIO.setmode(GPIO.BCM)
GPIO.setup(leds, GPIO.OUT)

for i in range(3):
    for i in range(8):
        GPIO.output(leds, 0)
        GPIO.output(leds[i], 1)
        time.sleep(0.2)

GPIO.output(leds, 0)
GPIO.cleanup()
