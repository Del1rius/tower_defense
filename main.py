import pygame as pg
import constants as c
import json
from world import World
from enemy import Enemy
from turrets import Turret

pg.init()

clock = pg.time.Clock()
#create game window
screen = pg.display.set_mode((c.SCREEN_WIDTH, c.SCREEN_HEIGHT))
pg.display.set_caption("Tower Defence")

#map images
map_image = pg.image.load('levels/level.png').convert_alpha()
#cursor as a turret
cursor_turret = pg.image.load('assets/images/turrets/cursor_turret.png').convert_alpha()
#enemy images
enemy_image = pg.image.load('assets/images/enemies/enemy_1.png').convert_alpha()

#load json data for level
with open('levels/level.tmj') as file:
    world_data = json.load(file)

#create world
world = World(world_data, map_image)
world.process_data()

#create groups
enemy_group = pg.sprite.Group()
turret_group = pg.sprite.Group()

waypoints = [
    (100, 100),
    (400, 200),
    (400, 100),
    (200, 300)
]


enemy = Enemy(world.waypoints, enemy_image)
enemy_group.add(enemy)

run = True
while run:

    clock.tick(c.FPS)

    screen.fill("purple")

    world.draw(screen)

    #draw enemey path
    pg.draw.lines(screen, "black", False, world.waypoints)

    enemy_group.update()

    #draw groups
    enemy_group.draw(screen)
    turret_group.draw(screen)

    #Event handler
    for event in pg.event.get():
        if event.type == pg.QUIT:
            run = False

        if event.type == pg.MOUSEBUTTONDOWN and event.button == 1:
            mouse_pos = pg.mouse.get_pos()
            turret = Turret(cursor_turret, mouse_pos)
            turret_group.add(turret)

    pg.display.flip()

pg.quit()
