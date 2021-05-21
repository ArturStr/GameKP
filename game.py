import random
from animations import *

pg.init()

win = pg.display.set_mode((500, 500))

pg.display.set_caption('Plane')

pg.display.set_icon(pg.image.load('img/icon.png'))

bg = pg.image.load('img/bg2.jpg')

clock = pg.time.Clock()

boom = [pg.image.load('img/boom_1.png'), pg.image.load('img/boom_2.png'),
        pg.image.load('img/boom_3.png'), pg.image.load('img/boom_4.png'),
        pg.image.load('img/boom_5.png'), pg.image.load('img/boom_6.png')]

width = 67
height = 60
speed = 6
x = 250 - width / 2
y = 430
bg_y = -800

bullets = []
enemies = []
hits = []
planeRate = 0
enemySpeed = 3
bulletSpeed = 8
rate = 0
scores = 1
HP = 5

left = False
right = False
boomCount = 0
g_over = True

font = pg.font.SysFont('comicsansms', 15, True, True)
drawScore = font.render(f'Score: {scores - 1}', True, (47, 248, 82))
drawHP = font.render(f'HP: {HP}', True, (255, 18, 13))


def drawWindow():
    global boomCount
    win.blit(bg, (0, bg_y))
    win.blit(drawScore, (0, 0))
    win.blit(drawHP, (450, 0))
    if left:
        win.blit(pg.image.load('img/-.png'), (x, y))
    elif right:
        win.blit(pg.image.load('img/+.png'), (x, y))
    else:
        win.blit(pg.image.load('img/0.png'), (x, y))

    if boomCount + 1 >= 30:
        boomCount = 0
        hits.pop(0)

    for ob in hits:
        win.blit(boom[boomCount // 6], (ob[0], ob[1]))
        boomCount += 1

    for bullet in bullets:
        bullet.draw(win)

    for enemy in enemies:
        enemy.draw(win)

    pg.display.update()


run = True
while run:
    clock.tick(30)
    keys = pg.key.get_pressed()
    if bg_y < 0:
        bg_y += 1
    else:
        bg_y = -800

    for event in pg.event.get():
        if event.type == pg.QUIT:
            run = False

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
            bullets.append(Attack(round(x + 35), round(y + 20), bulletSpeed))
        rate += 1
        if rate > 8:
            rate = 1

    for enemy in enemies:
        if enemy.y < 420:
            enemy.y += enemy.speed
        else:
            enemies.pop(enemies.index(enemy))
            HP -= 1
            drawHP = font.render(f'HP: {HP}', True, (255, 18, 13))
            if HP == 0:
                pg.time.delay(200)
                run = False

    if len(enemies) < random.randint(2, 5) and planeRate % 8 == 0:
        enemies.append(EnemyPlane(random.randint(20, 420), -55,
                                  random.randint(enemySpeed, enemySpeed + 2)))
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
                    hits.append([enemy.x, enemy.y])
                    scores += 1
                    drawScore = font.render(f'Score: {scores - 1}', True, (47, 248, 82))

    if scores == 10:
        speed = 7
        enemySpeed = 4
    elif scores == 100:
        enemySpeed = 5
    elif scores == 120:
        enemySpeed = 6

    drawWindow()

pg.quit()
