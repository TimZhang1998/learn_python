#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = '_张超'

import pygame

from pygame.sprite import Sprite


class Bullet(Sprite):
    """初始化飞船的子弹并对其进行管理"""

    def __init__(self, screen, setting, ship):
        """初始化子弹及其基本信息"""

        # 继承Sprite类中的属性
        super().__init__()

        # 捕捉屏幕信息
        self.screen = screen

        # 捕捉设置信息
        self.setting = setting

        # 捕捉飞船信息
        self.ship = ship

        # 设置初始位置
        self.rect = pygame.Rect(0, 0, self.setting.bullet_width, self.setting.bullet_height)
        self.rect.centerx = self.ship.rect.centerx
        self.rect.top = self.ship.rect.top

        # 捕捉子弹动态位置
        self.centery = float(self.rect.centery)

        # 从设置中获取子弹基本信息
        self.color = self.setting.bullet_color
        self.speed = self.setting.bullet_speed
        self.number = self.setting.bullet_number

    def update(self):
        """更新子弹位置信息"""

        # 子弹向上移动
        self.centery -= self.speed
        self.rect.centery = self.centery

    def draw_bullet(self):
        """绘制子弹"""

        pygame.draw.rect(self.screen, self.color, self.rect)
