#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = '_张超'

import sys

import pygame

from game_modules.bullet import Bullet

from game_modules.alien import Alien

from time import sleep

from game_modules.ship_number import ShipNumber


def fire_bullet(screen, game_setting, player_ship, bullets):
    if len(bullets) < game_setting.bullet_number:
        # 每按一次空格生成一个子弹并限制数目
        new_bullet = Bullet(screen, game_setting, player_ship)
        bullets.add(new_bullet)


def check_event_keydown(screen, game_setting, event, player_ship, bullets):
    """响应按键按下的操作"""

    if event.key == pygame.K_RIGHT:
        # 修改移动标志
        player_ship.move_right = True
    elif event.key == pygame.K_LEFT:
        # 修改移动标志
        player_ship.move_left = True
    elif event.key == pygame.K_UP:
        # 修改移动标志
        player_ship.move_up = True
    elif event.key == pygame.K_DOWN:
        # 修改移动标志
        player_ship.move_down = True
    elif event.key == pygame.K_SPACE:
        # 根据子弹数目生成新的子弹
        fire_bullet(screen, game_setting, player_ship, bullets)
    elif event.key == pygame.K_q:
        # 游戏退出快捷键
        sys.exit()


def check_event_keyup(event, player_ship):
    """响应按键松开的操作"""

    if event.key == pygame.K_RIGHT:
        # 修改移动标志
        player_ship.move_right = False
    elif event.key == pygame.K_LEFT:
        # 修改移动标志
        player_ship.move_left = False
    elif event.key == pygame.K_UP:
        # 修改移动标志
        player_ship.move_up = False
    elif event.key == pygame.K_DOWN:
        # 修改移动标志
        player_ship.move_down = False


def check_events(screen, game_setting, player_ship, bullets):
    """监视与响应鼠标和键盘事件"""

    # 监视鼠标与按键事件并进行响应
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        elif event.type == pygame.KEYDOWN:
            check_event_keydown(screen, game_setting, event, player_ship, bullets)

        elif event.type == pygame.KEYUP:
            check_event_keyup(event, player_ship)


def update_screen(screen, game_setting, player_ship, bullets, aliens, ship_number):
    """主循环过程中更新游戏界面"""

    # 每次循环时都重绘屏幕，填充背景色，绘制飞船和子弹
    screen.fill(game_setting.bg_color)
    ship_number.draw(screen)
    player_ship.blitme()
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    aliens.draw(screen)

    # 刷新屏幕，显示用户最新操作
    pygame.display.flip()


def update_bullets(screen, game_setting, player_ship, bullets, aliens):
    """主循环过程中更新子弹"""

    # 更新子弹位置
    bullets.update()

    # 删除已消失的子弹
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)

    # 监测并响应子弹与外星人的碰撞与外星人的再生成
    check_bullets_aliens_collisions(screen, game_setting, player_ship, bullets, aliens)


def update_ship(ship):
    """更新飞船位置"""

    ship.update()


def update_aliens(game_setting, aliens, player_ship, game_states, screen, ship, bullets, ship_number):
    """监控外星人群方向与和飞船之间的碰撞并更新外星人位置"""

    # 监测外星人是否到达屏幕边缘并改变其运动方向，及时更新外星人位置
    check_fleet_edge(game_setting, aliens)
    aliens.update()
    check_alien_bottom(game_setting, game_states, screen, ship, aliens, bullets, ship_number)

    # 监测外星人与飞船之间的碰撞
    if pygame.sprite.spritecollideany(ship, aliens):
        ship_reduce(game_setting, game_states, screen, ship, aliens, bullets, ship_number)


def get_number_x(screen, setting):
    """创建第一个外星人(获取数值)并计算一行可容纳外星人数目"""

    alien = Alien(screen, setting)
    alien_width = alien.rect.width
    available_space_x = setting.screen_width - 2 * alien_width
    number_alien_x = int(available_space_x / (2 * alien_width))
    return number_alien_x


def get_number_y(screen, setting, ship):
    """创建第一个外星人(获取数值)并计算一列可容纳外星人数目"""

    alien = Alien(screen, setting)
    alien_height = alien.rect.height
    available_space_y = setting.screen_height - 3 * alien_height - ship.rect.height
    number_alien_y = int(available_space_y / (2 * alien_height))
    return number_alien_y


def create_ship_number(screen, setting, ship_number):
    """显示飞船数目"""
    for number in range(setting.ship_limit - 1):
        new_ship_number = ShipNumber(screen, setting)
        new_ship_number.x = (new_ship_number.rect.width // 2) + (1.5 * number * new_ship_number.rect.width)
        new_ship_number.rect.x = new_ship_number.x
        ship_number.add(new_ship_number)


def create_alien(screen, setting, aliens, alien_number_x, alien_number_y):
    """创建外星人"""

    new_alien = Alien(screen, setting)
    new_alien.x = new_alien.rect.width + 2 * alien_number_x * new_alien.rect.width
    new_alien.rect.x = new_alien.x
    new_alien.y = new_alien.rect.height + 2 * alien_number_y * new_alien.rect.height
    new_alien.rect.y = new_alien.y
    aliens.add(new_alien)


def create_fleet(screen, setting, ship, aliens):
    """创建一群外星人"""

    for alien_number_y in range(get_number_y(screen, setting, ship)):
        for alien_number_x in range(get_number_x(screen, setting)):
            create_alien(screen, setting, aliens, alien_number_x, alien_number_y)


def check_fleet_edge(setting, aliens):
    """检查是否有外星人触及边缘"""

    for alien in aliens.sprites():
        if alien.check_edge():
            change_fleet_direction(setting, aliens)
            break


def check_bullets_aliens_collisions(screen, game_setting, player_ship, bullets, aliens):
    """监测并响应子弹与外星人的碰撞与外星人的再生成"""

    # 监测并响应子弹与外星人的碰撞
    collisions = pygame.sprite.groupcollide(bullets, aliens, True, True)

    # 监测外星人群是否完全消灭并清空子弹
    if len(aliens) == 0:
        bullets.empty()
        create_fleet(screen, game_setting, player_ship, aliens)


def check_alien_bottom(game_setting, game_states, screen, ship, aliens, bullets, ship_number):
    """检查外星人有没有到达屏幕底部"""

    screen_rect = screen.get_rect()
    for alien in aliens.sprites():
        if alien.rect.bottom >= screen_rect.bottom:
            ship_reduce(game_setting, game_states, screen, ship, aliens, bullets, ship_number)
            break


def change_fleet_direction(setting, aliens):
    """改变外星人群方向"""

    for alien in aliens.sprites():
        alien.rect.y += setting.alien_speed_drop
    setting.fleet_speed_direction *= -1


def ship_reduce(game_setting, game_states, screen, ship, aliens, bullets, ship_number):
    """飞船与外星人碰撞后作出响应"""

    if game_states.ship_number > 1:

        # 飞船数减1
        game_states.ship_number -= 1

        # 表示飞船数的图像减1
        ship_number_list = ship_number.sprites()
        ship_number_list.pop()
        ship_number.empty()
        for ship_number_image in ship_number_list:
            ship_number.add(ship_number_image)

        # 清空外星人列表和子弹列表
        aliens.empty()
        bullets.empty()

        # 创建新的外星人并将飞船放置于屏幕底部中央
        create_fleet(screen, game_setting, ship, aliens)
        ship.center_ship()

        # 暂停
        sleep(0.5)

    else:
        game_states.game_active = False
