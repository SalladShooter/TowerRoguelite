import pygame as py

class Text(py.sprite.Sprite):
    def __init__(self, text, size, xpos, ypos):
        super().__init__()
        py.font.init()
        self.font = py.font.SysFont('Arial', size)
        self.image = self.font.render(str(text), False, (255,255,255))
        self.xpos, self.ypos = xpos, ypos
        self.rect = self.image.get_rect()
        width, height = self.rect.width, self.rect.height
        self.rect.topleft = (self.xpos - width/2, self.ypos - height/2)

    def update_text(self, text):
        self.image = self.font.render(str(text), False, (255,255,255))
        self.rect = self.image.get_rect()
        width, height = self.rect.width, self.rect.height
        self.rect.topleft = (self.xpos - width/2, self.ypos - height/2)
