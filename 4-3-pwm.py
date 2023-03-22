#!/usr/bin/python3
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setup(2, GPIO.OUT)
pwm = GPIO.PWM(2, 1000)

try:
    while True:
        print("Enter fill: ", end="")
        fill = float(input())
        pwm.start(fill)
        print(f"V = {int(fill) * 3.3 / 100}")

finally:
    pwm.stop()
    GPIO.output(2, 0)
    GPIO.cleanup()
