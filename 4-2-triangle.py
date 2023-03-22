#!/usr/bin/python3
import RPi.GPIO as GPIO
import time

dac = [10, 9, 11, 5, 6, 13, 19, 26][::-1]
number = [0] * 8

GPIO.setmode(GPIO.BCM)
GPIO.setup(dac, GPIO.OUT)

def dec2bin(val):
    return [int(bit) for bit in format(val, "b").zfill(8)]

try:
    print("Enter period: ", end="")
    per = float(input())
    while True:
        for i in range(256):
            GPIO.output(dac, dec2bin(int(i)))
            time.sleep(per / 512)
        for i in range(254, 0, -1):
            GPIO.output(dac, dec2bin(int(i)))
            time.sleep(per / 512)
finally:
    GPIO.output(dac, 0)
    GPIO.cleanup()
