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
        print(self.options)

    def input(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_ESCAPE]:
            self.toggle_menu()


    def update(self):
        self.input()
        self.display_surface.blit(pygame.Surface((1000,1000)),(0,0))
        