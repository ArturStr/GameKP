import random
from animations import *

pg.init()

win = pg.display.set_mode((512, 512))

pg.display.set_caption('Plane')

pg.display.set_icon(pg.image.load('img/icon.png'))

bg = pg.image.load('img/bg.bmp')

clock = pg.time.Clock()

width = 67
height = 60
speed = 6
x = 250 - width / 2
y = 430
y_shot = y

bullets = []
enemies = []
planeRate = 0
enemySpeed = 3
rate = 0

left = False
right = False
isShot = False
animCount = 0


def drawWindow():
    global animCount
    win.blit(bg, (0, 0))

    if animCount + 1 >= 30:
        animCount = 0

    if left:
        win.blit(pg.image.load('img/-.png'), (x, y))
        animCount += 1
    elif right:
        win.blit(pg.image.load('img/+.png'), (x, y))
        animCount += 1
    else:
        win.blit(pg.image.load('img/0.png'), (x, y))

    for bullet in bullets:
        bullet.draw(win)

    for enemy in enemies:
        enemy.draw(win)

    pg.display.update()


run = True

while run:
    clock.tick(30)

    for event in pg.event.get():
        if event.type == pg.QUIT:
            run = False

    keys = pg.key.get_pressed()
    if (keys[pg.K_LEFT] or keys[pg.K_a]) and x > 25:
        x -= speed
        left = True
        right = False
    elif (keys[pg.K_RIGHT] or keys[pg.K_d]) and x < 500 - width - 20:
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
        if rate % 7 == 0:
            bullets.append(Attack(round(x + 35), round(y + 20)))
        rate += 1
        if rate > 8:
            rate = 1

    for enemy in enemies:
        if enemy.y < 420:
            enemy.y += enemySpeed
        else:
            enemies.pop(enemies.index(enemy))

    if len(enemies) < random.randint(2, 5) and planeRate % 8 == 0:
        enemies.append(EnemyPlane(random.randint(20, 420), -55))
    planeRate += 1

    if planeRate > 8:
        planeRate = 1

    for enemy in enemies:
        for bullet in bullets:
            if enemy.x - 5 < bullet.x < enemy.x + 50 and \
                    enemy.y - 15 < bullet.y < enemy.y + 15:
                a = True
                if a:
                    enemies.pop(enemies.index(enemy))
                    bullets.pop(bullets.index(bullet))

    drawWindow()

pg.quit()
