import pygame as pg

pg.init()

screen = pg.display.set_mode((1920, 1080), pg.FULLSCREEN)

run_program = True

while run_program:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            run_program = False
    pass

