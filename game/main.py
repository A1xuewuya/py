#!/usr/bin/env python
# -*- coding:utf-8 -*-
# 搭建界面，主要完成串窗口和背景图的显示
#
import pygame
import time


def main():
    # 创建一个窗口，用来显示内容 （宽，高）
    screen = pygame.display.set_mode((480, 852), 0, 32)

    # 创建一个和窗口大小的图片，用来充当背景
    background = pygame.image.load("./resources/bg.png")

    # 把背景放到窗口中显示
    while True:
        # 设定需要显示的背景图
        screen.blit(background, (0, 0))
        # 更新需要显示的内容
        pygame.display.update()
        # 时间延时操作
        time.sleep(1)


if __name__ == '__main__':
    main()


