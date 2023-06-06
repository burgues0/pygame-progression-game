# contains all sprites, and deals with their interacions effectively (hundreds of them)
# visible_sprites -> only sprite group that will be drawn
# obstacle_sprites -> sprite groups that has collision with the player
import pygame
from settings import *
from tile import Tile
from player import Player
class Level:
    def __init__(self):
        
        # getting the current
        self.display_surface = pygame.display.get_surface()

        # setting up the sprite groups 
        self.visible_sprites = pygame.sprite.Group()
        self.obstacle_sprites = pygame.sprite.Group()

        # sprite setup
        self.init_map()
    
    def init_map(self):
        # map_array = each row
        # tile = each item(col)
        # index is needed to multiply the tilesize and space the tiles evenly
        for map_array_index, map_array in enumerate(PLAIN_FIELDS):
            for tile_index, tile in enumerate(map_array):
                x = tile_index * TILESIZE
                y = map_array_index * TILESIZE
                if tile == 'x':
                    # creates an instance of Tile(position(tuple), groups(array, because it can be in multiple groups at once))
                    Tile((x,y),[self.visible_sprites])
                if tile == 'p':
                    Player((x,y),[self.visible_sprites])

    def run(self):
        # update and draw the sprites
        pass