"""Файл с классом текста.
"""
import pygame as pg


class Text:
    """Класс отрисовывающий текст.
    """

    def __init__(self,
                 pos: pg.Vector2,
                 text: str,
                 color: tuple[int, int, int],
                 size: int):
        """Создание класса.
        :param pos:  Позиция картинки.
        :param text: Текст картинки.
        :param color: Цвет картинки.
        :param size: Размер картинки.
        """
        self.pos: pg.Vector2 = pos
        self.text: str = text
        self.color: tuple[int, int, int] = color
        self.size: int = size

        self.font: pg.font.Font = pg.font.SysFont('freesanbold.ttf', size)
        self.texture = self.font.render(text, True, color)

    def draw(self, surface: pg.Surface):
        """Отрисовка картинки.
        :param surface: Поверхность на которой будет отрисована картинка.
        :return:
        """
        surface.blit(self.texture, self.pos)
