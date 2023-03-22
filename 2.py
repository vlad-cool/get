import RPi.GPIO as GPIO
import time

GPIO.cleanup()
GPIO.setmode(GPIO.BCM)
GPIO.setup(18, GPIO.OUT)
GPIO.setup(27, GPIO.IN)

GPIO.output(18, GPIO.input(27))