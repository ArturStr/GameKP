import pygame as pg

pg.init()

win = pg.display.set_mode((512, 512))

pg.display.set_caption('Plane')

bg = pg.image.load('bg.bmp')

clock = pg.time.Clock()

width = 67
height = 60
speed = 5
x = 250 - width / 2
y = 430
y_shot = y

left = False
right = False
isShot = False
animCount = 0


class attack():
    def __init__(self, x, y, radius, color):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color
        self.vel = 8

    def draw(self, win):
        pg.draw.circle(win, self.color, (self.x, self.y), self.radius)
        pg.draw.circle(win, (0, 255, 0), (self.x, self.y), self.radius - 3)


def drawWindow():
    global animCount
    win.blit(bg, (0, 0))

    if animCount + 1 >= 30:
        animCount = 0

    if left:
        win.blit(pg.image.load('-.png'), (x, y))
        animCount += 1
    elif right:
        win.blit(pg.image.load('+.png'), (x, y))
        animCount += 1
    else:
        win.blit(pg.image.load('0.png'), (x, y))

    for bullet in bullets:
        bullet.draw(win)

    pg.display.update()


bullets = []
rate = 0
run = True
while run:
    clock.tick(30)

    for event in pg.event.get():
        if event.type == pg.QUIT:
            run = False

    keys = pg.key.get_pressed()
    if keys[pg.K_LEFT] and x > 25:
        x -= speed
        left = True
        right = False
    elif keys[pg.K_RIGHT] and x < 500 - width - 20:
        x += speed
        left = False
        right = True
    elif keys[pg.K_LEFT] and keys[pg.K_RIGHT]:
        left = False
        right = False
        animCount = 0
    else:
        left = False
        right = False
        animCount = 0

    for bullet in bullets:
        if bullet.y > 20:
            bullet.y -= bullet.vel
        else:
            bullets.pop(bullets.index(bullet))

    if keys[pg.K_SPACE]:
        if len(bullets) < 5 and rate % 15 == 0:
            bullets.append(attack(round(x + 35), round(y + 20), 5, (255, 0, 0)))
        rate += 1
        if rate > 90:
            rate = 1

    drawWindow()

pg.quit()
