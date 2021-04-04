import pygame as pg


class EnemyPlane(pg.sprite.Sprite):
    def __init__(self, x, y, speed):
        super(EnemyPlane, self).__init__()

        self.x = x
        self.y = y
        self.speed = speed
        self.image = pg.image.load('img/enemy.png')
        self.rect = self.image.get_rect()

    def draw(self, win):
        win.blit(self.image, (self.x, self.y))


class Attack(pg.sprite.Sprite):
    def __init__(self, x, y, vel):
        super(Attack, self).__init__()

        self.x = x
        self.y = y
        self.vel = vel
        self.image = pg.image.load('img/bullet2.png')
        self.rect = self.image.get_rect()

    def draw(self, win):
        win.blit(self.image, (self.x - 11, self.y - 11))
