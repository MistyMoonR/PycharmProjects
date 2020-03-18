# -*- coding: utf-8 -*-
#导入控制驱动
from __future__ import division
import time
import Adafruit_PCA9685

import math
#导入pygame
import pygame
from pygame.locals import *


#可以开启debug日志
# import logging
# logging.basicConfig(level=logging.DEBUG)

# 初始化PCA9685，默认使用地址(0x40).
pwm = Adafruit_PCA9685.PCA9685()
# 可以自己指定一个不同的地址
#pwm = Adafruit_PCA9685.PCA9685(address=0x41, busnum=2)

# 设置舵机活动范围
servo_min = 10  # Min pulse length out of 4096
servo_max = 800  # Max pulse length out of 4096
servo_angle = 0.03 # sleep时间，值越大，一次的转动幅度越大
servo_Dvalue = 0.01 # 控制左右旋转产生的误差

# 辅助功能，一个更简单的驱动方法
def set_servo_pulse(channel, pulse):
    pulse_length = 1000000    # 1,000,000 us per second
    pulse_length //= 60       # 60 Hz
    print('{0}us per period'.format(pulse_length))
    pulse_length //= 4096     # 12 bits of resolution
    print('{0}us per bit'.format(pulse_length))
    pulse *= 1000
    pulse //= pulse_length
    pwm.set_pwm(channel, 0, pulse)

# 设置频率为60Hz，这是一个比较好的值
pwm.set_pwm_freq(60)

#初始化
pygame.init()
#制造一个窗口
screen = pygame.display.set_mode((600,500))
pygame.display.set_caption("The Servo Control - Press 1,2,3,4")
myfont = pygame.font.Font(None, 60)
#参数
color = 200, 80, 60
width = 4
x = 300
y = 250
radius = 200
position = x-radius, y-radius, radius*2, radius*2


while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            exit()
        elif event.type == KEYUP:
            if event.key == pygame.K_ESCAPE:
                exit()
            elif event.key == pygame.K_1:
                pwm.set_pwm(1, 0, servo_min)
                time.sleep(servo_angle-servo_Dvalue)
                pwm.set_pwm(1, 0, 0)
            elif event.key == pygame.K_2:
                pwm.set_pwm(1, 0, servo_max)
                time.sleep(servo_angle)
                pwm.set_pwm(1, 0, 0)
            elif event.key == pygame.K_3:
                pwm.set_pwm(0, 0, servo_min)
                time.sleep(servo_angle-servo_Dvalue)
                pwm.set_pwm(0, 0, 0)
            elif event.key == pygame.K_4:
                pwm.set_pwm(0, 0, servo_max)
                time.sleep(servo_angle)
                pwm.set_pwm(0, 0, 0)



    #清屏
    screen.fill((0,0,200))
    #每片pie绘制
    textImg1 = myfont.render("1", True, color)
    screen.blit(textImg1, (x, y-radius/2))
    textImg2 = myfont.render("2", True, color)
    screen.blit(textImg2, (x, y+radius/2))
    textImg3 = myfont.render("3", True, color)
    screen.blit(textImg3, (x-radius/2, y))
    textImg4 = myfont.render("4", True, color)
    screen.blit(textImg4, (x+radius/2, y))
    #piece1
    start_angle = math.radians(45)
    end_angle = math.radians(135)
    pygame.draw.arc(screen, color, position, start_angle, end_angle, width)
    pygame.draw.line(screen, color, (x,y),(x-radius+60,y-radius+60), width)
    pygame.draw.line(screen, color, (x,y),(x+radius-60,y-radius+60), width)
    #piece2
    start_angle = math.radians(225)
    end_angle = math.radians(315)
    pygame.draw.arc(screen, color, position, start_angle, end_angle, width)
    pygame.draw.line(screen, color, (x,y),(x+radius-60,y+radius-60), width)
    pygame.draw.line(screen, color, (x,y),(x-radius+60,y+radius-60), width)
    #piece3
    start_angle = math.radians(135)
    end_angle = math.radians(225)
    pygame.draw.arc(screen, color, position, start_angle, end_angle, width)
    pygame.draw.line(screen, color, (x,y),(x-radius+60,y-radius+60), width)
    pygame.draw.line(screen, color, (x,y),(x-radius+60,y+radius-60), width)
    #piece4
    start_angle = math.radians(315)
    end_angle = math.radians(405)
    pygame.draw.arc(screen, color, position, start_angle, end_angle, width)
    pygame.draw.line(screen, color, (x,y),(x+radius-60,y-radius+60), width)
    pygame.draw.line(screen, color, (x,y),(x+radius-60,y+radius-60), width)



    pygame.display.update()