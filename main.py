import pygame, sys
from settings import *

class Main:
    def __init__(self) -> None:
        pygame.init()
        self.display_surface =  pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))

    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            
            self.clock.tick() / 1000
            self.display_surface.fill((249,131,103))

            pygame.display.update()

if __name__ == '__main__' :
    main = Main()
    main.run()