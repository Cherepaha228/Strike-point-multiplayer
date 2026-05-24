"""Главный файл программы.
"""
import pygame as pg

from player import Player


def main():
    """ Осноная функция для общей логики.
    """
    pg.init()
    window = pg.display.set_mode((1920, 1080), pg.FULLSCREEN)
    player = Player(5)

    clock = pg.time.Clock()
    running = True
    while running:
        dt: float = clock.tick(60)
        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False
        window.fill((32, 32, 32))
        player.draw(window)
        player.logic(dt)
        pg.display.flip()

if __name__ == '__main__':
    main()
