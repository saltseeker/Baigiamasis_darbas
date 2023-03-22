import pygame
from settings import *
from pytmx.util_pygame import load_pygame

class SoilLayer:
    def __init__(self, all_sprites):

        # sprite group
        self.all_sprites = all_sprites
        self.soil_sprites = pygame.sprite.Group()


        self.soil_surf = pygame.image.load('graphics/soil/o.png')

        self.create_soil_grid

    def create_soil_grid(self):
        ground = pygame.image.load('graphics/world/ground.png')
        h_tiles, v_tiles = ground.get_width() // TILE_SIZE, ground.get_height() // TILE_SIZE

        self.grid = [[[] for col in range(h_tiles)] for row in range(v_tiles)]
        for x, y, _ in load_pygame('data/map.tmx').get_layer_by_name('Farmable').tiles():
            self.grid[y][x].append('F')
        