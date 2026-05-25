"""Файл описывающий класс оружия.
"""
import os.path

import pygame as pg


class Weapon:
    def __init__(self, texture_name: str, pos: pg.Vector2 | None, damage: float, weight: float):
        """ Создание оружия.
        :param texture_name: Имя текстуры.
        :param pos: Позиция, если орущие лежит на земле.
        :param damage: Урон от оружия.
        :param weight: Вес оружия.
        """
        self.pos: pg.Vector2 | None = pos
        self.texture: pg.Surface = pg.image.load(os.path.join('resources', 'textures', 'guns', f'{texture_name}.png'))
        self.damage: float = damage
        self.weight: float = weight

    def draw(self, surface: pg.Surface):
        """ Отрисовать оружие.
        :param surface: Поверхность для отрисовки.
        :return:
        """
        if self.pos:
            surface.blit(self.texture, self.pos)
