#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = '_张超'


import pygame
from pygame.sprite import Sprite


class Alien(Sprite):
    """对外星人进行架构"""

    def __init__(self, screen, setting):
        """初始化外星人并设置其初始位置"""

        # 继承并捕捉信息
        super().__init__()
        self.setting = setting
        self.screen = screen

        # 外星人初始信息
        self.image = pygame.image.load('game_images/alien.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = self.screen.get_rect()
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # 动态追踪外星人位置
        self.x = float(self.rect.x)

    def blitme(self):
        """绘制外星人"""

        self.screen.blit(self.image, self.rect)

    def update(self):
        """更新外星人位置"""

        self.x += (self.setting.alien_speed * self.setting.fleet_speed_direction)
        self.rect.x = self.x

    def check_edge(self):
        """检查外星人是否触及边缘"""

        if self.rect.right >= self.screen_rect.right:
            return True
        elif self.rect.left <= 0:
            return True

