import pygame
from settings import *

class Player(pygame.sprite.Sprite):
    def __init__(self, pos, sprite_group, collision_sprites):
        super().__init__(sprite_group)
        self.image = pygame.image.load(PATH + '/sprites/entities/player.png').convert_alpha()
        self.rect = self.image.get_rect(topleft = pos)

        self.direction = pygame.math.Vector2()
        self.speed = 5
        self.obstacles = collision_sprites
    
    def kb_input(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_w]: self.direction.y = -1
        elif keys[pygame.K_s]: self.direction.y = 1
        else: self.direction.y = 0
        
        if keys[pygame.K_a]: self.direction.x = -1
        elif keys[pygame.K_d]: self.direction.x = 1
        else: self.direction.x = 0
    
    def move(self, speed):
        if self.direction.magnitude() != 0:
            self.direction = self.direction.normalize()
        self.rect.x += self.direction.x * speed
        self.collision('horizontal')
        self.rect.y += self.direction.y * speed
        self.collision('vertical')

    def collision(self, direction):
        if direction == 'horizontal':
            for sprites in self.obstacles:
                if sprites.rect.colliderect(self.rect):
                    if self.direction.x > 0:
                        self.rect.right = sprites.rect.left
                    if self.direction.x < 0:
                        self.rect.left = sprites.rect.right
        if direction == 'vertical':
            for sprites in self.obstacles:
                if sprites.rect.colliderect(self.rect):
                    if self.direction.y > 0:
                        self.rect.bottom = sprites.rect.top
                    if self.direction.y  < 0:
                        self.rect.top = sprites.rect.bottom        

    def update(self):
        self.kb_input()
        self.move(self.speed)
    
