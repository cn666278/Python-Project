import sys
import pygame
from settings import Settings
from ship import Ship
from alien import Alien
import game_functions as gf
from pygame.sprite import Group
from game_stats import GameStats
from button import Button
from scoreboard import Scoreboard

def run_game():
    # 初始化pygame, 设置和屏幕对象
    pygame.init()
    ai_settings = Settings()    # 创建一个Settings实例

    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("钟沛霖 x 喵喵 VS 陆先森(爱情保卫战）")
    # 用于添加背景照片（fail)
    # bg_image = pygame.image.load('images/abc.bmp')
    # screen.blit(bg_image, (0,0))
    # pygame.display.update()

    # 创建 play 摁扭
    play_button = Button(ai_settings, screen, "Play")

    # 创建一个用于储存游戏统计数据信息的实例, 并创建得分牌
    stats = GameStats(ai_settings)
    sb = Scoreboard(ai_settings, screen, stats)

    # 创建一艘飞船,一个子弹编组以及一个外星人编组
    ship = Ship(ai_settings, screen)
    bullets = Group()
    aliens = Group()

    # 创建外星人群
    gf.create_fleet(ai_settings, screen, ship, aliens)

    # 开始游戏的主循环
    while True:
        gf.check_events(ai_settings, screen, stats, sb,  play_button, ship, aliens, bullets)

        if stats.game_active:
            ship.update()
            gf.update_bullets(ai_settings, screen, stats, sb, ship, aliens, bullets)
            gf.update_aliens(ai_settings, screen, stats, sb, ship, aliens, bullets)

        gf.update_screen(ai_settings, screen, stats, sb, ship, aliens, bullets, play_button)

run_game()