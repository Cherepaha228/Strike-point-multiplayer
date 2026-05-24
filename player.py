import pygame as pg


class Player:
    """ Класс игрока.
    """

    def __init__(self, speed: int):
        """
        Создание класса.
        :param speed: Скорость игрока.
        """
        self.pos: pg.Vector2 = pg.Vector2(0, 0)
        self.speed = speed

    def logic(self, dt):
        """ Обработка нажатий на кнопки.
        """
        keys = pg.key.get_pressed()
        if keys[pg.K_d]:
            self.pos.x += self.speed * dt
        if keys[pg.K_a]:
            self.pos.x -= self.speed * dt
        if keys[pg.K_s]:
            self.pos.y += self.speed * dt
        if keys[pg.K_w]:
            self.pos.y -= self.speed * dt

    def draw(self, surface):
        """Отрисовывать игрока на карте.
        """
        pg.draw.circle(surface, (255, 0, 0), self.pos, 30)
