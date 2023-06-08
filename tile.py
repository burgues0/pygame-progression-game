import pygame
from settings import *

class Tile(pygame.sprite.Sprite):
    def __init__(self, pos, spr_group):
        super().__init__(spr_group)
        self.image = pygame.image.load(PATH + '/sprites/world/wall.png').convert_alpha()
        self.rect = self.image.get_rect(topleft = pos)
        self.hitbox = self.rect.inflate(0, -10) #<- takes a rectangle and changes the size (y value is distributed between both extremities: -10 = -5 top -5 bottom)
        
