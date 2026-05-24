"""Файл содеражащий класс игрока.
"""

class Player:
    """ Класс игрока.
    """
    def __init__(self, speed: int):
        self.x = 0
        self.y = 0
        self.speed = speed

    def logic(self):
        """ Обработка нажатий на кнопки.
        """
        keys = pg.key.get_pressed()
        if (keys[pg.K_d]):
            self.x += 1
        if (keys[pg.K_a]):
            self.x -= 1
        if (keys[pg.K_s]):
            self.y += 1
        if (keys[pg.K_w]):
            self.y -= 1

    def draw(self, surface):
        """Отрисовывать игрока на карте.
        """
        pg.draw.circle(surface, (255, 0, 0), (self.x, self.y), 30)