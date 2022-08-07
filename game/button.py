import pygame.font

class Button():

    def __init__(self, ai_settings, screen, msg):
        """初始化按钮的属性"""
        self.screen = screen
        self.screen_rect = screen.get_rect()

        # 设置按钮的尺寸和其他属性
        self.width, self.height = 200, 50
        self.button_color = (0, 255, 0)     # 亮绿色
        self.text_color = (255, 255, 255)   # 白色
        self.font = pygame.font.SysFont(None, 48)   # None 表示默认字体， 48 为字号

        # 创建摁扭的 rect 对象，并且使其居中
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.center = self.screen_rect.center

        # 摁扭的标签只需要创建一次
        self.prep_msg(msg)

    def prep_msg(self, msg):
        """将 msg 渲染为图像， 并且在按钮上居中"""
        self.msg_image = self.font.render(msg, True, self.text_color, self.button_color)
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center

    def draw_button(self):
        """"绘制一个用颜色填充的摁扭，再绘制文本"""
        self.screen.fill(self.button_color, self.rect)
        self.screen.blit(self.msg_image, self.msg_image_rect)