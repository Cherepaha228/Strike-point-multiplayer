import pygame as pg

from player import Player


def main():
    pg.init()
    window = pg.display.set_mode((1920, 1080), pg.FULLSCREEN)
    player = Player(5)
    running = True
    while running:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False
        window.fill((32, 32, 32))
        player.draw(window)
        player.logic()
        pg.display.flip()

if __name__ == '__main__':
    main()
