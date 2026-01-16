import pygame as py
from text import Text
from player import Player
from enemy import Enemy
from moves import Moves

py.init()
screen = py.display.set_mode((1280,720))
clock = py.time.Clock()
running = True

all_sprites = py.sprite.Group()
moves = py.sprite.Group()

energy = 0
move_count = 5
player = Player(300,360,50,50)
enemy = Enemy(980,360,50,50)
energyText = Text(f"{energy}/{move_count}",32,640,620)
all_sprites.add(player,enemy,energyText)

for i in range(move_count):
    move = Moves(move_count*15*i+(move_count*25),620,50,50)
    moves.add(move)
    all_sprites.add(move)

while running:
    for event in py.event.get():
        if event.type == py.QUIT:
            running = False
        elif event.type == py.MOUSEBUTTONDOWN:
            if event.button == 1:
                for move in moves:
                    if move.rect.collidepoint(event.pos):
                        move.toggle_selection()
                        if move.selected:
                            energy += 1
                        else:
                            energy -= 1

    screen.fill("black")

    all_sprites.update(event)
    energyText.update_text(f"{energy}/{move_count}")
    all_sprites.draw(screen)

    py.display.flip()

    clock.tick(60)

py.quit()
