import pygame, sys
from settings import *
from level import *


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
            start_color = pygame.Color('black')
           

            start_surf = pygame.font.Font('font/LycheeSoda.ttf', 50).render('Press ENTER to start', False, start_color)
            start_rect = start_surf.get_rect(center=(SCREEN_WIDTH/2, SCREEN_HEIGHT/2))

            # Calculate the scale factor for the pulsating effect
            scale_factor = abs((pygame.time.get_ticks() % 1000) - 500) / 500 + 1

            # Scale the start_surf
            pulsating_surf = pygame.transform.scale(start_surf, (int(start_surf.get_width() * scale_factor), int(start_surf.get_height() * scale_factor)))

            # Calculate the new rect for the pulsating_surf
            pulsating_rect = pulsating_surf.get_rect(center=start_rect.center)

            self.screen.blit(pulsating_surf, pulsating_rect)

            # Check for events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
                    return

            # Update display
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

            # Display the inventory on the bottom right corner
            money_surf = self.font.render(f"Money: {self.level.player.money}", False, pygame.Color('black'))
            money_rect = money_surf.get_rect(bottomright=(SCREEN_WIDTH-20, SCREEN_HEIGHT-20))
            self.screen.blit(money_surf, money_rect)

            inventory_surf = self.font.render("", False, pygame.Color('black'))
            inventory_rect = inventory_surf.get_rect(bottomright=(money_rect.left-20, SCREEN_HEIGHT-20))
            self.screen.blit(inventory_surf, inventory_rect)

            # Display the item inventory
            for i, (item, count) in enumerate(self.level.player.item_inventory.items()):
                item_surf = self.font.render(f"{item.capitalize()}: {count}", False, pygame.Color('black'))
                item_rect = item_surf.get_rect(bottomright=(inventory_rect.right+120, inventory_rect.bottom-40-(i*30)))
                self.screen.blit(item_surf, item_rect)

            # Display the seed inventory
            seed_inventory_surf = self.font.render("", False, pygame.Color('black'))
            seed_inventory_rect = seed_inventory_surf.get_rect(bottomright=(inventory_rect.left-20, SCREEN_HEIGHT-20))
            self.screen.blit(seed_inventory_surf, seed_inventory_rect)

            for i, (seed, count) in enumerate(self.level.player.seed_inventory.items()):
                seed_surf = self.font.render(f"{seed.capitalize()}: {count}", False, pygame.Color('black'))
                seed_rect = seed_surf.get_rect(bottomright=(seed_inventory_rect.right+30, seed_inventory_rect.bottom-40-(i*30)))
                self.screen.blit(seed_surf, seed_rect)

            pygame.display.update()


if __name__ == '__main__':
    game = Game()
    game.run()
