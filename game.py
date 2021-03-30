import pygame as pg

pg.init()

win = pg.display.set_mode((512, 512))

pg.display.set_caption('Plane')

walkRight = [pg.image.load('1.png'), pg.image.load('2.png')]
walkLeft = [pg.image.load('-1.png'), pg.image.load('-2.png')]
planeStand = pg.image.load('0.png')
bg = pg.image.load('bg.bmp')

clock = pg.time.Clock()

width = 40
height = 60
speed = 3
x = 250-width/2
y = 430

left = False
right = False
animCount = 0


def drawWindow():
    global animCount
    win.blit(bg, (0, 0))

    if animCount + 1 >= 30:
        animCount = 0

    if left:
        win.blit(walkLeft[animCount // 15], (x, y))
        animCount += 1
    elif right:
        win.blit(walkRight[animCount // 15], (x, y))
        animCount += 1
    else:
        win.blit(planeStand, (x, y))

    pg.display.update()


run = True
while run:
    clock.tick(30)

    for event in pg.event.get():
        if event.type == pg.QUIT:
            run = False

    keys = pg.key.get_pressed()
    if keys[pg.K_LEFT] and x > 20:
        x -= speed
        left = True
        right = False
    elif keys[pg.K_RIGHT] and x < 500-width-20:
        x += speed
        left = False
        right = True
    else:
        left = False
        right = False
        animCount = 0

    drawWindow()


pg.quit()