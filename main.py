import pygame as pg
import constants as c
from enemy import Enemy

pg.init()

clock = pg.time.Clock()

screen = pg.display.set_mode((c.SCREEN_WIDTH, c.SCREEN_HEIGHT))
pg.display.set_caption("Tower Defence")

enemy_image = pg.image.load('assets/images/enemies/enemy_1.png').convert_alpha()

enemy_group = pg.sprite.Group()

enemy = Enemy((200, 300), enemy_image)
enemy_group.add(enemy)

run = True
while run:

    clock.tick(c.FPS)

    enemy.move()

    enemy_group.draw(screen)

    for event in pg.event.get():
        if event.type == pg.QUIT:
            run = False

    pg.display.flip()

pg.quit()
