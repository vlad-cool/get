#!/usr/bin/python3
import RPi.GPIO as GPIO

dac = [10, 9, 11, 5, 6, 13, 19, 26][::-1]
number = [0] * 8

GPIO.setmode(GPIO.BCM)
GPIO.setup(dac, GPIO.OUT)

def dec2bin(val):
    return [int(bit) for bit in format(val, "b").zfill(8)]

try:
    while True:
        a = input()
        if a[0] == "q":
            break
        if int(a) > 255 or int(a) < 0:
            print("Wrong number! Should be int between 0 and 255")
            continue
        GPIO.output(dac, dec2bin(int(a)))
        print(f"V = {int(a) * 3.3 / 2**8}")
finally:
    GPIO.output(dac, 0)
    GPIO.cleanup()
