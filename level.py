# contains all sprites, and deals with their interacions effectively (hundreds of them)
# visible_sprites -> only sprite group that will be drawn
# obstacle_sprites -> sprite groups that has collision with the player
import pygame

class Level:
    def __init__(self):
        
        # getting the current
        self.display_surface = pygame.display.get_surface()

        # setting up the sprite groups 
        self.visible_sprites = pygame.sprite.Group()
        self.obstacle_sprites = pygame.sprite.Group()
    
    def run(self):
        # update and draw the sprites
        pass