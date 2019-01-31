#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'game setting'

__author__ = '_张超'


class Settings(object):
    """储《外星人入侵》的所有设置的类"""

    def __init__(self):
        """初始化游戏的设置"""

        # 屏幕设置
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)

        # 飞船设置
        self.ship_speed = 1.5
        self.ship_limit = 3

        # 子弹设置
        self.bullet_speed = 3
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)
        self.bullet_number = 3

        # 外星人设置
        self.alien_speed = 1
        self.alien_speed_drop = 10
        self.fleet_speed_direction = 1


