import RPi.GPIO as GPIO
import time
import threading
GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)

P_SERVO = 21  # GPIO端口号，根据实际修改
Y_SERVO = 22
fPWM = 50  # Hz (软件PWM方式，频率不能设置过高)
a = 10
b = 2

GPIO.setup(P_SERVO, GPIO.OUT)
GPIO.setup(Y_SERVO, GPIO.OUT)

pan = GPIO.PWM(P_SERVO,fPWM)
ban = GPIO.PWM(Y_SERVO,fPWM)




def print_111():
    while 1:
        for i in range(2, 13, 1):
            pan.start(0)
            pan.ChangeDutyCycle(i)
            time.sleep(0.1)

def print_222():
    while 1:
        for j in range(2, 13, 1):
            ban.start(0)
            ban.ChangeDutyCycle(j)
            time.sleep(0.1)

threads = []

t1 = threading.Thread(target=print_111)
threads.append(t1)
t2 = threading.Thread(target=print_222)
threads.append(t2)


if __name__=='__main__':
    for t in threads:
        t.start()
    for t in threads:
        t.join()
print ("退出线程")





# for i in range(2,13,1):
#     time.sleep(0.3)
#     ban.start(0)
#     ban.ChangeDutyCycle(i)

# def setDirection(duty,direction):
#     global pwm
#     pwm = GPIO.PWM(duty,50)
#     pwm.start(0)
#     duty = a / 180 * direction + b
#     print("direction =", direction, "-> duty =", duty)
#     time.sleep(0.3)
#
#
#
# print("starting")
# for direction in range(0, 181, 10):
#     setDirection(P_SERVO,direction)
#     setDirection(Y_SERVO,direction)
#
# direction = 0
#
# GPIO.cleanup()
# print("done")


