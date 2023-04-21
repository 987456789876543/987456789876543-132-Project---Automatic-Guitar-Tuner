import RPi.GPIO as gpio
from time import sleep
from gui import *

enable = 6
in1 = 16
in2 = 17

gpio.setmode(gpio.BCM)

gpio.setup(enable, gpio.OUT)
gpio.setup(in1, gpio.OUT)
gpio.setup(in2, gpio.OUT)

modulate = gpio.PWM(enable, 100)
modulate.start(0)

def start(dutyCycle, direction):
    if clockwise:
        modulate.ChangeDutyCycle(dutyCycle)
        gpio.output(enable, True)
        gpio.output(in1, direction)
        gpio.output(in2, not direction)

    else:
        modulate.ChangeDutyCycle(dutyCycle)
        gpio.output(enable, True)
        gpio.output(in1, not direction)
        gpio.output(in2, direction)


def Stop():
    gpio.output(enable, False)