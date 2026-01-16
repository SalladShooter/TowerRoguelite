import pygame as py

class Player(py.sprite.Sprite):
    def __init__(self, xpos, ypos, width, height):
        super().__init__()
        self.image = py.Surface((width,height))
        self.image.fill((0,255,0))
        self.rect = self.image.get_rect()
        self.rect.center = (xpos-width/2,ypos-height/2)

    def update(self, event):
        pass
