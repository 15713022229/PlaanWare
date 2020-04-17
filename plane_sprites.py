import random
import pygame
# 屏幕大小的常量
SCREEN_RECT = pygame.Rect(0, 0, 480, 700)
# 刷新的频率
FRAME_PER_SEC = 60
# 创建敌机的定时器常量
CREAT_ENEMY_EVENT = pygame.USEREVENT

class GameSprite(pygame.sprite.Sprite):
    """飞机大战游戏精灵"""

    def __init__(self, image_name, speed=1):
        # 父类不是object基类 一定要主动调用父类的初始化方法
        # 调用父类的初始化方法
        super().__init__()
        # 定义对象的属性
        self.image = pygame.image.load(image_name)
        self.rect = self.image.get_rect()
        self.speed = speed

    def update(self):
        # 在屏幕的垂直方向上移动
        self.rect.y += self.speed


class Background(GameSprite):
    """"游戏背景精灵"""
    def __init__(self, is_alt=False):

        # 1. 调用父类方法,实现精灵的创建(images/rect/speed)
        super().__init__("./images/background.png")
        # 2. 判断是否是交替图像,如果是,需要设置初始位置
        if is_alt:
            self.rect.y = -self.rect.height

    def update(self):

        # 1. 调用父类的方法实现
        # 就丢了俩括号!!!
        super().update()
        # 2. 判断是否移出屏幕,如果移出屏幕,就将图像设置到屏幕的上方
        if self.rect.y >= SCREEN_RECT.height:
            self.rect.y = -self.rect.height

class Enemy(GameSprite):

    def __init__(self):

        # 1. 调用父类方法,创建敌机精灵,同时指定敌人飞机图片
        super().__init__("./images/enemy1.png")
        # 2. 指定敌人的初始随机速度
        self.speed = random.randint(1, 3)
        # 3. 指定敌机的初始随机位置
        # bottom = y + height
        self.rect.bottom = 0

        max_x = SCREEN_RECT.width - self.rect.width
        self.rect.x = random.randint(0, max_x)


    def update(self):

        # 1. 调用父类方法,保持垂直方向飞行
        super().update()
        # 2. 判断是否飞出屏幕,如果飞出屏幕,就从精灵组删除

        if self.rect.y >= SCREEN_RECT.height:
            # 销毁精灵,同时在精灵组内也删除
            self.kill()

    def __del__(self):
        # print("敌人挂了 %s" % self.rect)
        pass

class Hero(GameSprite):

    def __init__(self):
        # 设置英雄的图像 设置图像
        super().__init__("./images/me1.png", 0)
        # 设置英雄的初始位置
        self.rect.centerx = SCREEN_RECT.centerx
        self.rect.bottom = SCREEN_RECT.bottom - 120

    def update(self):
        # 英雄在水平方向移动
        self.rect.x += self.speed

        # 控制英雄不能离开屏幕
        if self.rect.x < 0:
            self.rect.x = 0

        elif self.rect.right > SCREEN_RECT.right:
            self.rect.right = SCREEN_RECT.right



