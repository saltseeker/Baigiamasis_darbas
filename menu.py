import pygame
from settings import *

class Menu:
    def __init__(self, player, toggle_menu):

        self.player = player
        self.toggle_menu = toggle_menu
        self.display_surface = pygame.display.get_surface()
        self.font = pygame.font.Font(f'font/QuinqueFive.ttf', 30)

        #menu size
        self.width = 400
        self.space = 10
        self.padding = 8 

        self.options = list(self.player.item_inventory.keys()) + list(self.player.seed_inventory.keys())
        self.sell_border = len(self.player.item_inventory) - 1
        self.setup()

    def setup(self):
        #text surface
        self.text_surfs = []
        for item in self.options:
            text_surf = self.font.render(item, False, 'Black')
            self.text_surfs.append(text_surf)

    def input(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_ESCAPE]:
            self.toggle_menu()


    def update(self):
        self.input()
        for text_index, text_surf in enumerate(self.text_surfs):
            self.display_surface.blit(text_surf,(100,text_index * 50))
        