import pygame as pg



class Player:
    def __init__(self, speed: int):
        self.x = 0
        self.y = 0
        self.speed = speed
    
    def logic(self):
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
        pg.draw.circle(surface, (255, 0, 0), (self.x, self.y), 30)

def main():
    pg.init()
    window = pg.display.set_mode((1920, 1080), pg.FULLSCREEN)

    running = True
    while running:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False
        window.fill((32, 32, 32))

        pg.display.flip()

if __name__ == '__main__':
    main()
