#!/usr/bin/env python
# -*- coding:utf-8 -*-
# 显示玩家飞机 检测键盘 控制飞机移动
#
import pygame
import time
from pygame.locals import *


def main():
    # 创建一个窗口，用来显示内容 （宽，高）
    screen = pygame.display.set_mode((480, 852), 0, 32)
    # 创建一个和窗口大小的图片，用来充当背景
    background = pygame.image.load("./resources/bg.png")
    # 创建飞机图片
    airplane = pygame.image.load("./resources/airplane.png")

    x = 202
    y = 520
    # 把背景放到窗口中显示
    while True:
        # 设定需要显示的背景图
        screen.blit(background, (0, 0))

        # 检测键盘 获取事件，比如按键
        for event in pygame.event.get():
            # 判断是否点击了退出按钮
            if event.type == QUIT:
                print("---exit")
                exit()
            # 判断是否按了键
            elif event.type == KEYDOWN:
                # print(event.key) 打印出所有键盘事件
                # 检测键盘是否是a或者left
                if event.key == K_a or event.key == K_LEFT:
                    print("---left")
                    x -= 10
                # 检测键盘是否是d或者right
                elif event.key == K_d or event.key == K_RIGHT:
                    print("---right")
                    x += 10
                # 检测按键是否是空格键
                elif event.key == K_SPACE:
                    print("---space")

        # 设定飞机背景图
        screen.blit(airplane, (x, y))
        # 更新需要显示的内容
        pygame.display.update()
        # 时间延时操作
        # time.sleep(0.1)


if __name__ == '__main__':
    main()


