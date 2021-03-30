import pygame as pg

pg.init()

win = pg.display.set_mode((512, 512))

pg.display.set_caption('Plane')

bg = pg.image.load('bg.bmp')

clock = pg.time.Clock()

width = 67
height = 60
speed = 5
x = 250-width/2
y = 430
y_shot = y

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
        win.blit(pg.image.load('-.png'), (x, y))
        animCount += 1
    elif right:
        win.blit(pg.image.load('+.png'), (x, y))
        animCount += 1
    else:
        win.blit(pg.image.load('0.png'), (x, y))

    if isShot:
        pg.draw.line(win, (0, 255, 255), (x + 37, y+20), (x + 37, 0), 2)
        pg.draw.line(win, (0, 255, 255), (x + 32, y+20), (x + 32, 0), 2)
        pg.draw.line(win, (0, 0, 255), (x + 35, y+20), (x + 35, 0), 3)
        animCount += 1

    pg.display.update()


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
    elif keys[pg.K_RIGHT] and x < 500-width-20:
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

    if not(isShot):
        if keys[pg.K_SPACE]:
            isShot = True
    else:
        isShot = False

    drawWindow()


pg.quit()