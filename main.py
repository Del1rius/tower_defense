import pygame as pg
import constants as c
import json
from world import World
from enemy import Enemy

pg.init()

clock = pg.time.Clock()
#create game window
screen = pg.display.set_mode((c.SCREEN_WIDTH, c.SCREEN_HEIGHT))
pg.display.set_caption("Tower Defence")

#map images
map_image = pg.image.load('levels/level.png').convert_alpha()
#enemy images
enemy_image = pg.image.load('assets/images/enemies/enemy_1.png').convert_alpha()

#load json data for level
with open('levels/level.tmj') as file:
    world_data = json.load(file)
print(world_data)

#create world
world = World(world_data, map_image)
world.process_data()

#create groups
enemy_group = pg.sprite.Group()

waypoints = [
    (100, 100),
    (400, 200),
    (400, 100),
    (200, 300)
]

print(world.waypoints)

enemy = Enemy(waypoints, enemy_image)
enemy_group.add(enemy)

run = True
while run:

    clock.tick(c.FPS)

    screen.fill("purple")

    world.draw(screen)

    #draw enemey path
    pg.draw.lines(screen, "black", False, waypoints)

    enemy_group.update()

    enemy_group.draw(screen)

    for event in pg.event.get():
        if event.type == pg.QUIT:
            run = False

    pg.display.flip()

pg.quit()
