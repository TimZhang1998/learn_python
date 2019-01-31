#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = '_张超'

import pygame
from pygame.sprite import Sprite


class ShipNumber(Sprite):
    """显示飞船数目"""

    def __init__(self, screen, setting):
        """初始化信息"""

        super().__init__()

        # 捕捉屏幕信息
        self.screen = screen

        # 捕捉设置信息
        self.setting = setting

        # 加载飞船图像并获取其外接矩形
        self.image = pygame.image.load('game_images/ship.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = self.screen.get_rect()

        # 初始化位置信息
        self.rect.x = self.rect.width // 2
        self.rect.y = self.setting.screen_height - self.rect.height * 1.5

    def blitme(self):
        """绘制飞船数目"""

        self.screen.blit(self.image, self.rect)