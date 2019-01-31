#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'player_ship'

__author__ = '_张超'


import pygame


class Ship(object):

    def __init__(self, screen, setting):
        """初始化飞船并设置其初始位置"""

        # 捕捉屏幕信息
        self.screen = screen

        # 捕捉设置信息
        self.setting = setting

        # 加载飞船图像并获取其外接矩形
        self.image = pygame.image.load('game_images/ship.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = self.screen.get_rect()

        # 将每艘新飞船放在屏幕底部中央
        self.rect.centerx = self.screen_rect.centerx
        self.rect.centery = self.setting.screen_height - self.rect.height

        # 飞船位置浮点化
        self.centerx = float(self.rect.centerx)
        self.centery = float(self.rect.centery)

        # 移动标志
        self.move_right = False
        self.move_left = False
        self.move_up = False
        self.move_down = False

    def blitme(self):
        """在指定位置绘制飞船"""

        self.screen.blit(self.image, self.rect)

    def center_ship(self):
        """将飞船重新放置于屏幕底部中央位置"""

        self.centerx = self.screen_rect.centerx
        self.centery = self.setting.screen_height - self.rect.height

    def update(self):
        """根据移动标志调整飞船位置"""

        if self.move_right and self.centerx < self.screen_rect.right:
            self.centerx += self.setting.ship_speed

        if self.move_left and self.centerx > self.screen_rect.left:
            self.centerx -= self.setting.ship_speed

        if self.move_up and self.centery > self.screen_rect.top:
            self.centery -= self.setting.ship_speed

        if self.move_down and self.centery < self.screen_rect.bottom:
            self.centery += self.setting.ship_speed

        self.rect.centerx = self.centerx
        self.rect.centery = self.centery
