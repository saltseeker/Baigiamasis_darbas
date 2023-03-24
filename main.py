import pygame, sys
from settings import *
from level import Level


class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
        pygame.display.set_caption('Farm land')
        self.clock = pygame.time.Clock()
        self.level = Level()

    def instruction(self):
        font = pygame.font.Font('font/LycheeSoda.ttf', 24)
        text = " Q = swap tool\n E = swap seed\n SPACE = action key\n X = plant"
        lines = text.splitlines()
        y = 20
        for line in lines:
            text_surf = font.render(line, False, pygame.Color('black'))
            text_rect = text_surf.get_rect(topleft=(20, y))
            self.screen.blit(text_surf, text_rect)
            y += 30
        
    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
  
            dt = self.clock.tick() / 1000
            self.level.run(dt)
            self.instruction()
            pygame.display.update()

if __name__ == '__main__':
    game = Game()
    game.run()
