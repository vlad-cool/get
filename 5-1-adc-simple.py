#!/usr/bin/python3
import RPi.GPIO as GPIO
import time

dac = [10, 9, 11, 5, 6, 13, 19, 26][::-1]
comp = 4
troyka = 17

GPIO.setmode(GPIO.BCM)
GPIO.setup(dac, GPIO.OUT)
GPIO.setup(comp, GPIO.IN)
GPIO.setup(troyka, GPIO.OUT, initial=1)

number = [0] * 8


def dec2bin(val):
    return [int(bit) for bit in format(val, "b").zfill(8)]

def adc():
    for i in range(256):
        GPIO.output(dac, dec2bin(int(i)))
        time.sleep(0.001)
        if 1 - GPIO.input(comp):
            GPIO.output(dac, 0)
            return i


try:
    while True:
        print(f"Voltage is: {round(adc() * 3.3 / 256, 4)}")
finally:
    GPIO.output(dac, 0)
    GPIO.cleanup()
