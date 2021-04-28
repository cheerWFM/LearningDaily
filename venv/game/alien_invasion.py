#!/usr/bin/env python 
# coding:utf-8
import pygame
from settings import Settings
from ship import Ship
import game_functions as gf

def run_game():
    # 初始化游戏并创建一个屏幕对象
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width,ai_settings.screen_height))# 创建（500，800）的显示窗口，指定窗口大小
    pygame.display.set_caption("Alien Invasion")
    # 创建一艘飞船
    ship = Ship(ai_settings,screen)
    # 开始游戏的主熏循环
    while True:
        """每次执行while循环时都会绘制一个空屏幕，并擦去旧屏幕，使得只有新屏幕可见"""
        # 监视键盘和鼠标事件
        gf.check_events(ship)
        ship.update()
            # 每次循环都重绘屏幕，使用颜色填充背景
        gf.update_screen(ai_settings,screen,ship)

run_game()