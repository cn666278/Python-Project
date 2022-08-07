import pygame.image


class Settings():
    """The class used to stored all the settings in this game -- Alien Invasion"""

    def __init__(self):
        """初始化游戏的静态设置"""

        # 屏幕设置
        self.screen_width = 1300
        self.screen_height = 800
        self.bg_color = (230, 230, 230)


        # 飞船基本速度初始值设置
        self.ship_speed_factor = 1.5

        # 飞船设置
        self.ship_limit = 3

        # 子弹设置
        self.bullet_speed_factor = 1
        self.bullet_width = 50
        self.bullet_height = 30  # 控制子弹大小
        self.bullet_color = 255, 192, 203
        self.bullets_allowed = 30     # 限制未消失的子弹数量为10

        # 外星人设置
        self.alien_speed_factor = 0.5
        self.fleet_drop_speed = 5
        # fleet_direction 为 1 表示右移， 为 -1 表示往左移
        self.fleet_direction = 1

        # 以什么样的速度加快游戏节奏
        self.speedup_scale = 1.5
        # 外星人点数的提高速度
        self.score_scale = 2

        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        """初始化随游戏进行而变化的设置"""
        self.ship_speed_factor = 1.5
        self.bullet_speed_factor = 1
        self.alien_speed_factor = 0.5

        # fleet_direction 为 1 表示向右， -1 表示向左
        self.fleet_direction = 1

        # 记分
        self.alien_points = 50

    def increase_speed(self):
        """提高速度设置和外星人点数"""
        self.ship_speed_factor *= self.speedup_scale
        self.alien_speed_factor *= self.speedup_scale
        self.bullet_speed_factor *= self.speedup_scale

        self.alien_points = int(self.alien_points * self.score_scale)

        # print(self.alien_points)    # for test only
