import pygame, sys
from settings import *
from level import Level

class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption('Farm land')
        self.clock = pygame.time.Clock()
        self.level = Level()
        self.font = pygame.font.Font('font/LycheeSoda.ttf', 24)
        self.start_image = pygame.image.load('graphics/world/start.gif')

    def instruction(self):
        text = " Q = swap tool\n E = swap seed\n SPACE = action key\n X = plant"
        lines = text.splitlines()
        y = 20
        for line in lines:
            text_surf = self.font.render(line, False, pygame.Color('black'))
            text_rect = text_surf.get_rect(topleft=(20, y))
            self.screen.blit(text_surf, text_rect)
            y += 30
        
    def start_screen(self):
        while True:
            start_image_scaled = pygame.transform.scale(self.start_image, (SCREEN_WIDTH, SCREEN_HEIGHT))
            self.screen.blit(start_image_scaled, (0, 0))

            title_surf = self.font.render('Farm land', False, pygame.Color('black'))
            title_rect = title_surf.get_rect(center=(SCREEN_WIDTH/2, SCREEN_HEIGHT/3))
            self.screen.blit(title_surf, title_rect)

            start_surf = pygame.font.Font('font/LycheeSoda.ttf', 50).render('Press ENTER to start', False, pygame.Color('black'))
            start_rect = start_surf.get_rect(center=(SCREEN_WIDTH/2, SCREEN_HEIGHT/2))
            self.screen.blit(start_surf, start_rect)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
                    return

            pygame.display.update()
            self.clock.tick(60)

    def run(self):
        self.start_screen()

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
