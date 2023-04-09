import RPi.GPIO as GPIO
from time import sleep

#define pin numbers
enable = 6
in1 = 16
in2 = 17

#setup pins
GPIO.setmode(GPIO.BCM)
GPIO.setup(enable, GPIO.OUT)
GPIO.setup(in1, GPIO.OUT)
GPIO.setup(in2, GPIO.OUT)

def goForward():
    GPIO.output(enable, GPIO.HIGH)
    GPIO.output(in1, GPIO.HIGH)
    GPIO.output(in2, GPIO.LOW)

def goBackward():
    GPIO.output(enable, GPIO.HIGH)
    GPIO.output(in1, GPIO.LOW)
    GPIO.output(in2, GPIO.HIGH)

def stop():
    GPIO.output(enable, GPIO.LOW)

goForward()
sleep(3)
goBackward()
sleep(3)
stop()
GPIO.cleanup()
