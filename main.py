import pygame as py
from text import Text
from player import Player
from startmove import StartMove
from enemy import Enemy
from actions import Actions

py.init()
screen = py.display.set_mode((1280,720))
clock = py.time.Clock()
running = True

all_sprites = py.sprite.Group()
moves = py.sprite.Group()

energy = 0
max_energy = 3
move_count = 5
player = Player(300,360,50,50)
enemy = Enemy(980,360,50,50)
energyText = Text(f"{energy}/{max_energy}",32,640,570)
startButton = StartMove(640+100/2,645,100,50)
startText = Text(f"Start",32,640,620)
all_sprites.add(player,enemy,energyText,startButton,startText)

for i in range(move_count):
    move = Actions(move_count*15*i+(move_count*25),620,50,50)
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
                        old_state = move.selected
                        move.toggle_selection(energy, max_energy)
                        if not old_state and move.selected:
                            energy += 1
                        elif old_state and not move.selected:
                            energy -= 1

    screen.fill("black")

    all_sprites.update(event)
    energyText.update_text(f"{energy}/{max_energy}")
    all_sprites.draw(screen)

    py.display.flip()

    clock.tick(60)

py.quit()
