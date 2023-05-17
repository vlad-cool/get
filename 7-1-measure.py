#!/usr/bin/python3
import RPi.GPIO as GPIO
import time
import matplotlib.pyplot as plt

dac = [10, 9, 11, 5, 6, 13, 19, 26][::-1]
leds = [24, 25, 8, 7, 12, 16, 20, 21]
comp = 4
troyka = 17

GPIO.setmode(GPIO.BCM)
GPIO.setup(dac, GPIO.OUT)
GPIO.setup(comp, GPIO.IN)
GPIO.setup(troyka, GPIO.OUT, initial=0)
GPIO.setup(leds, GPIO.OUT)

number = [0] * 8

def dec2bin(val):
    return [int(bit) for bit in format(val, "b").zfill(8)]

def adc():
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

def leds_output(v):
    n = int(round(v * 8 / 256))
    n = min(8, n)
    GPIO.output(leds, [1] * n + [0] * (8 - n))

try:
    res = []
    t_beg = time.time()
    GPIO.output(troyka, 0)
    v = 0
    while v < 132:
        v = adc()
        print(f"Voltage is: {round(v * 3.3 / 256, 4)}, v: {v}")
        res.append(v)
        leds_output(v)
    GPIO.output(troyka, 1)
    while v > 67:
        v = adc()
        print(f"Voltage is: {round(v * 3.3 / 256, 4)}, v: {v}")
        res.append(v)
        leds_output(v)
    t_end = time.time()

    duration = t_end - t_beg

    res_v = []
    for re in res:
        res_v.append(round(re * 3.3/256, 4))
    plt.plot(res_v)
    plt.show()
    with open("data.txt", "w") as f:
        for dat in res:
            f.write(f"{dat}\n")
    with open("settings.txt", "w") as f:
        f.write(f"{len(res) / duration}\n")
        f.write(f"{3.3 / 255}\n")
    print(f"experiment duration: {round(duration)} seconds")
    print(f"period: {round(1000 * duration / len(res), 3)} milliseconds")
    print(f"frequency: {round(len(res) / duration)} Hz")
    print(f"adc step: {round(3.3 / 255 * 1000)} mV")
finally:
    GPIO.output(dac, 0)
    GPIO.output(leds, 0)
    GPIO.output(troyka, 0)
    GPIO.cleanup()
