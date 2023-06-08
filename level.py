# contains all sprites, and deals with their interacions effectively (hundreds of them)
# visible_sprites -> only sprite group that will be drawn
# obstacle_sprites -> sprite groups that has collision with the player
import pygame
from settings import *
from tile import Tile
from player import Player
from debug import debug

class Level:
    def __init__(self):
        
        # getting the current
        self.display_surface = pygame.display.get_surface()

        # setting up the sprite groups 
        self.visible_sprites = YSortCameraGroup()
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
                    Tile((x,y),[self.visible_sprites, self.obstacle_sprites])
                if tile == 'p':
                    self.player = Player((x,y),[self.visible_sprites], self.obstacle_sprites)

    def run(self):
        # update and draw the sprites
        self.visible_sprites.custom_draw(self.player)
        self.visible_sprites.update()

#class created for sprite priorities in the camera
class YSortCameraGroup(pygame.sprite.Group):
    def __init__(self):
        #general setup
        super().__init__()
        self.display_surface = pygame.display.get_surface()
        self.half_width = self.display_surface.get_size()[0] // 2
        self.half_height = self.display_surface.get_size()[1] // 2
        self.offset = pygame.math.Vector2()

    def custom_draw(self, player):
        #getting the offset
        self.offset.x = player.rect.centerx - self.half_width
        self.offset.y = player.rect.centery - self.half_height

        for sprite in self.sprites():
            offset_pos = sprite.rect.topleft - self.offset
            self.display_surface.blit(sprite.image, offset_pos)
