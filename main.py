"""Главный файл программы.
"""
import pygame as pg

from player import Player
from text import Text


def main():
    """ Основная функция для общей логики.
    """
    pg.init()
    window = pg.display.set_mode((1920, 1080), pg.FULLSCREEN)
    player = Player(5)
    text = Text(pg.Vector2(50, 50), 'Hi world!', (0, 255, 0), 44)

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
        text.draw(window)
        pg.display.flip()

if __name__ == '__main__':
    main()
