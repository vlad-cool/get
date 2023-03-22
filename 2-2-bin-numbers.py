import RPi.GPIO as GPIO
import time

dac = [10, 9, 11, 5, 6, 13, 19, 26]
number = [0] * 8
n = int(input())

GPIO.cleanup()
GPIO.setmode(GPIO.BCM)
GPIO.setup(dac, GPIO.OUT)

for i in range(8):
    number[i] = n % 2
    n //= 2

GPIO.output(dac, number)
time.sleep(15)
GPIO.output(dac, 0)
GPIO.cleanup()
