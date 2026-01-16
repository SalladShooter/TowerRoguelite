import pygame as py

class Moves(py.sprite.Sprite):
    def __init__(self, xpos, ypos, width, height):
        super().__init__()
        self.image = py.Surface((width,height))
        self.image.fill((100,100,100))
        self.rect = self.image.get_rect()
        self.rect.topleft = (xpos-width/2,ypos-height/2)
        self.selected = False

    def update(self, event):
        mouse_pos = py.mouse.get_pos()
        if self.selected:
            self.image.fill((100,100,200))
        elif self.rect.collidepoint(mouse_pos):
            self.image.fill((200,200,200))
        else:
            self.image.fill((100,100,100))

    def toggle_selection(self):
        self.selected = not self.selected
