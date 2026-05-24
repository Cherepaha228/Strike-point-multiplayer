import pygame as pg

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
