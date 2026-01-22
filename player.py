import pygame as py

class Player(py.sprite.Sprite):
    def __init__(self, xpos, ypos, width, height, max_health, damage, energy):
        super().__init__()
        self.image = py.Surface((width,height))
        self.image.fill((0,255,0))
        self.rect = self.image.get_rect()
        self.rect.center = (xpos-width/2,ypos-height/2)
        self.max_health = max_health
        self.health = max_health
        self.damage = damage
        self.energy = energy
        self.healthbar_width = 100
        self.healthbar_height = 20

    def update(self, event):
        pass

    def draw_healthbar(self, screen):
        bar_rect = py.Rect(0, 0, self.healthbar_width, self.healthbar_height)
        bar_rect.midtop = (self.rect.centerx, self.rect.bottom + self.healthbar_height)
        py.draw.rect(screen, (55,55,55), bar_rect)

        current_width = int((self.health / max(self.max_health, 1)) * self.healthbar_width)
        current_rect = bar_rect.copy()
        current_rect.width = current_width
        py.draw.rect(screen, (0,255,0), current_rect)
