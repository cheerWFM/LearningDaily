#!/usr/bin/env python 
# coding:utf-8
import pygame

class Ship():
    def __init__(self,ai_settings,screen):
        """初始化飞船并设置其初始位置"""
        self.screen = screen
        self.ai_seetings = ai_settings
        # 加载飞船图像并获取外接矩形
        self.image = pygame.image.load('images/ship.bmp') # 返回一个表示飞船的surface，存储到self.image
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        # 将每艘新飞船放在屏幕底部中央
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom
        # 在飞船的属性center中存储小数值
        self.center = float(self.rect.centerx)
        # 移动标志
        self.moving_right = False
        self.moving_left = False
        # self.moving_up = False
        # self.moving_down = False


    def update(self):
        """根据移动标志调整飞船度位置"""
        # 更改飞船的center值，而不是rect
        # self.rect.right返回飞船外接矩形的右边缘的坐标，如果这个值小于elf.screen_rect.right的值则说明飞船未触及屏幕右边缘
        if self.moving_right and self.rect.right < self.screen_rect.right:
           self.center += self.ai_seetings.ship_speed_factor
        # 如果rect的左边缘的x坐标大于0 ，说明飞船未触及屏幕左边缘
        if self.moving_left and self.rect.left > 0:
            self.center -= self.ai_seetings.ship_speed_factor
        # 根据self.centerx 更新rect对象
        self.rect.centerx = self.center





    def blitme(self):
        """指定飞船位置绘制飞船"""
        self.screen.blit(self.image,self.rect)