import pygame as py

class StartMove(py.sprite.Sprite):
    def __init__(self, xpos, ypos, width, height):
        super().__init__()
        self.image = py.Surface((width,height))
        self.image.fill((100,100,100))
        self.rect = self.image.get_rect()
        self.rect.center = (xpos-width/2,ypos-height/2)

    def update(self, event):
        mouse_pos = py.mouse.get_pos()
        if self.rect.collidepoint(mouse_pos):
            self.image.fill((200,200,200))
        else:
            self.image.fill((100,100,100))
