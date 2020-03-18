# -*- coding: utf-8 -*-
#导入控制驱动
from __future__ import division
import time
import Adafruit_PCA9685


#导入pygame


#可以开启debug日志
# import logging
# logging.basicConfig(level=logging.DEBUG)

# 初始化PCA9685，默认使用地址(0x40).
pwm = Adafruit_PCA9685.PCA9685()
# 可以自己指定一个不同的地址
#pwm = Adafruit_PCA9685.PCA9685(address=0x41, busnum=2)
# pwm.set_pwm(1, 0, 400)
# pwm.set_pwm(0, 0, 400)
# 设置舵机活动范围
# servo_min = 10  # Min pulse length out of 4096
# servo_max = 800  # Max pulse length out of 4096
# servo_angle = 0.03 # sleep时间，值越大，一次的转动幅度越大
# servo_Dvalue = 0.01 # 控制左右旋转产生的误差
#
# 辅助功能，一个更简单的驱动方法
servo_min = 150  # Min pulse length out of 4096
servo_max = 600  # Max pulse length out of 4096


def set_servo_pulse(channel, pulse):
    pulse_length = 2000    # 1,000,000 us per second
    pulse_length //= 60       # 60 Hz
    print('{0}us per period'.format(pulse_length))
    pulse_length //= 4096     # 12 bits of resolution
    print('{0}us per bit'.format(pulse_length))
    pulse *= 1000
    pulse //= pulse_length
    pwm.set_pwm(channel, 0, pulse)

# 设置频率为60Hz，这是一个比较好的值
pwm.set_pwm_freq(60)

print('Moving servo on channel 0, press Ctrl-C to quit...')
while True:
    # Move servo on channel O between extremes.
    pwm.set_pwm(0, 0, 1080)
    time.sleep(1)
    pwm.set_pwm(0, 0, 1500)
    time.sleep(1)


pwm.set_pwm_freq(60)

def setAngle(angle):
    servo = (150-angle)/4.5
    print("angle =", angle, "-> servo =", servo)
    pwm.set_pwm(0, 0, servo)
    time.sleep(0.2)

a = 1
b = 2
c = 375
c = int(c)
print("starting")

while True:
    for i in range(7):
        if i < 3:

            for angle in range(c, c+b*a, a):
                setAngle(angle)
            for angle in range(c+b*a, c+1, -a):
                setAngle(angle)
            # time.sleep(1)
            for angle in range(c, c-b*a, -a):
                setAngle(angle)
            for angle in range(c-b*a, c+1, a):
                setAngle(angle)
        else:
            time.sleep(0.1)
            setAngle(375)


