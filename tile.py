import pygame
from settings import *

class Tile(pygame.sprite.Sprite):
    def __init__(self, pos, spr_group):
        super().__init__(spr_group)
        self.image = pygame.image.load('../sprites/world/wall.png').convert_alpha()
        self.rect = self.image.get_rect(topleft = pos)
