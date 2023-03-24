import pygame
from settings import *

class Menu:
    def __init__(self, player, toggle_menu):

        self.player = player
        self.toggle_menu = toggle_menu
        self.display_surface = pygame.display.get_surface()
        self.font = pygame.font.Font(f'font/QuinqueFive.ttf', 30)

    def update(self):
        self.display_surface.blit(pygame.Surface((1000,1000)),(0,0))
        