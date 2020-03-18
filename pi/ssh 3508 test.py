# Software PWM Servo.py


import RPi.GPIO as GPIO
import time
import random

P_SERVO = 22  # GPIO端口号，根据实际修改
fPWM = 50  # Hz (软件PWM方式，频率不能设置过高)


def setup():
    global pwm
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(P_SERVO, GPIO.OUT)
    pwm = GPIO.PWM(P_SERVO, fPWM)
    pwm.start(0)


def setSpeed(speed):
    duty = speed / 12.5 + 2.
    pwm.ChangeDutyCycle(duty)
    print("speed =", speed, "-> duty =", duty)
    time.sleep(0.25)

a = 20
b = 1
c = 61
c = int(c)
print("starting")
setup()
for i in range(7):
    if i < 3:

        for speed in range(c, c+b*a, a):
            setSpeed(speed)
        for speed in range(c+b*a, c+1, -a):
            setSpeed(speed)
        # time.sleep(1)
        for speed in range(c, c-b*a, -a):
            setSpeed(speed)
        for speed in range(c-b*a, c+1, a):
            setSpeed(speed)
    else:
        time.sleep(0.1)
        setSpeed(61)
        GPIO.cleanup()
        print("done")
        break


