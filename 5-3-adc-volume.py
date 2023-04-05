#!/usr/bin/python3
import RPi.GPIO as GPIO
import time

dac = [10, 9, 11, 5, 6, 13, 19, 26][::-1]
leds = [24, 25, 8, 7, 12, 16, 20, 21]
comp = 4
troyka = 17

GPIO.setmode(GPIO.BCM)
GPIO.setup(dac, GPIO.OUT)
GPIO.setup(comp, GPIO.IN)
GPIO.setup(troyka, GPIO.OUT, initial=1)
GPIO.setup(leds, GPIO.OUT)

number = [0] * 8


def dec2bin(val):
    return [int(bit) for bit in format(val, "b").zfill(8)]

def adc_simple():
    for i in range(256):
        GPIO.output(dac, dec2bin(int(i)))
        time.sleep(0.001)
        if 1 - GPIO.input(comp):
            GPIO.output(dac, 0)
            return i

def adc_sar():
    le = 0
    ri = 255
    while (ri - le) > 1:
        mi = (ri + le) // 2
        GPIO.output(dac, dec2bin(int(mi)))
        time.sleep(0.001)
        if 1 - GPIO.input(comp):
            ri = mi
        else:
            le = mi
    return le

try:
    while True:
        v = adc_sar()
        print(f"Voltage is: {round(v * 3.3 / 256, 4)}")
        n = int(round(v / (60/8)))
        n = min(8, n)
        GPIO.output(leds, [1] * n + [0] * (8 - n))

finally:
    GPIO.output(dac, 0)
    GPIO.cleanup()
