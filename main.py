import pygame as py
from player import Player
from enemy import Enemy
from moves import Moves

py.init()
screen = py.display.set_mode((1280,720))
clock = py.time.Clock()
running = True

all_sprites = py.sprite.Group()
moves = py.sprite.Group()

player = Player(300,360,50,50)
enemy = Enemy(980,360,50,50)
all_sprites.add(player,enemy)

move_count = 5
for i in range(move_count):
    move = Moves(move_count*15*i+(move_count*25),620,50,50)
    moves.add(move)
    all_sprites.add(move)

while running:
    for event in py.event.get():
        if event.type == py.QUIT:
            running = False

    screen.fill("black")

    all_sprites.update()
    all_sprites.draw(screen)

    py.display.flip()

    clock.tick(60)

py.quit()
