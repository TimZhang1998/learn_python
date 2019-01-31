#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = '_张超'


import pygame

from pygame.sprite import Group

from game_modules.settings import Settings

from game_modules.ship import Ship

from game_modules import game_functions as gf

from game_modules.alien import Alien

from game_modules.game_states import GameStates


def run_game():
    # 初始化游戏并创建一个屏幕对象
    pygame.init()
    game_setting = Settings()
    screen = pygame.display.set_mode((game_setting.screen_width, game_setting.screen_height))
    pygame.display.set_caption('Alien Invasion')

    # 创建显示飞船数目的对象
    ship_number = Group()
    gf.create_ship_number(screen, game_setting, ship_number)

    # 创建一个飞船对象
    player_ship = Ship(screen, game_setting)

    # 创建一个子弹编组
    bullets = Group()

    # 创建一个外星人编组
    aliens = Group()
    gf.create_fleet(screen, game_setting, player_ship, aliens)

    # 创建一个游戏状态对象
    game_states = GameStates(game_setting)

    # 运行游戏是一个函数，把控游戏运行系统的是一个主循环
    while True:

        # 监视与响应鼠标和键盘事件
        gf.check_events(screen, game_setting, player_ship, bullets)

        # 更新配置
        if game_states.game_active:
            gf.update_ship(player_ship)
            gf.update_bullets(screen, game_setting, player_ship, bullets, aliens)
            gf.update_aliens(game_setting, aliens, player_ship, game_states, screen, player_ship, bullets, ship_number)

        # 刷新屏幕
        gf.update_screen(screen, game_setting, player_ship, bullets, aliens, ship_number)


run_game()