import pygame as pg
class Gun:
    def __init__(self, is_down, pos, texture, gun_damage, gun_weight):
        self.is_down = is_down
        self.pos = pos
        self.texture = texture
        self.gun_damage = gun_damage
        self.gun_weight = gun_weight
    def draw(self, surface):
        if self.is_down:
            pg.draw.circle(surface, (0, 255, 0), self.pos, 30)



