import pygame as pg

pg.init()

win = pg.display.set_mode((500, 500))

pg.display.set_caption('Plane')

x = 450
y = 430
width = 40
height = 60
speed = 15

run = True
while run:
    pg.time.delay(100)

    for event in pg.event.get():
        if event.type == pg.QUIT:
            run = False

    keys = pg.key.get_pressed()
    if keys[pg.K_LEFT]:
        x -= speed
    if keys[pg.K_RIGHT]:
        x += speed

    win.fill((0, 0, 0))
    pg.draw.rect(win, (0, 0, 255), (x, y, width, height))
    pg.display.update()

pg.quit()