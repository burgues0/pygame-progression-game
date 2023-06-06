import pygame
from settings import *

class Player(pygame.sprite.Sprite):
    def __init__(self, pos, spr_group):
        super().__init__(spr_group)
        self.image = pygame.image.load('../sprites/entities/player.png').convert_alpha()
        self.rect = self.image.get_rect(topleft = pos)
