import RPi.GPIO as GPIO
from time import sleep

#define pin numbers
enable = 6
in1 = 16
in2 = 17

#set the mode
GPIO.setmode(GPIO.BCM)

#set up the pins as outputs
GPIO.setup(enable, GPIO.OUT)
GPIO.setup(in1, GPIO.OUT)
GPIO.setup(in2, GPIO.OUT)

modulate = GPIO.PWM(enable, 100)
modulate.start(0)

def move(dutyCycle, direction, time):
    modulate.ChangeDutyCycle(dutyCycle)
    GPIO.output(enable, True)
    GPIO.output(in1, direction)
    GPIO.output(in2, not direction)
    sleep(time)
    GPIO.output(enable, False)



move(50, True, 3)
move(100, False, 3)



modulate.stop()
GPIO.cleanup()
