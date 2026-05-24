import pygame as pg


class Text:
    def __init__(self,
                 pos: pg.Vector2,
                 text: str,
                 color: tuple[int, int, int],
                 size: int):
        self.pos: pg.Vector2 = pos
        self.text: str = text
        self.color: tuple[int, int, int] = color
        self.size: int = size

        self.font: pg.font.Font = pg.font.SysFont('freesanbold.ttf', size)
        self.texture = self.font.render(text, True, color)

    def draw(self, surface: pg.Surface):
        surface.blit(self.texture, self.pos)
