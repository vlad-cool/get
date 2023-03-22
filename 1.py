import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BCM)
GPIO.setup(18, GPIO.OUT)

for i in range(179):
    GPIO.output(18, 1)
    sleep(1)
    GPIO.output(18, 0)
    sleep(1)
