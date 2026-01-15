import pygame as py
from player import Player
from moves import Moves

py.init()
screen = py.display.set_mode((1280,720))
clock = py.time.Clock()
running = True

all_sprites = py.sprite.Group()
moves = py.sprite.Group()

player = Player()
all_sprites.add(player)

for i in range(5):
    move = Moves()
    moves.add(move)
    all_sprites.add(move)

while running:
    for event in py.event.get():
        if event.type == py.QUIT:
            running = False

    screen.fill("black")

    all_sprites.update()

    py.display.flip()

    clock.tick(60)

py.quit()
