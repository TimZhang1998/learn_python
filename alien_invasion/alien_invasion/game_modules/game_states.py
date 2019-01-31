#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = '_张超'


class GameStates():
    """跟踪游戏的统计信息"""

    def __init__(self, game_setting):
        """初始化游戏信息"""

        self.setting = game_setting
        self.game_active = True
        self.ship_number = self.setting.ship_limit
        self.rest_game()

    def rest_game(self):
        """重置游戏数据"""

        self.ship_number = self.setting.ship_limit
