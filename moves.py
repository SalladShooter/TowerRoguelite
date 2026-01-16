import pygame as py

class Moves(py.sprite.Sprite):
    def __init__(self, xpos, ypos, width, height):
        super().__init__()
        self.image = py.Surface((width,height))
        self.image.fill((100,100,100))
        self.rect = self.image.get_rect()
        self.rect.topleft = (xpos-width/2,ypos-height/2)

    def update(self):
        pass
