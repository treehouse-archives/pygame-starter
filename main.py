import sys

import pygame

from scripts.player import Player
from scripts.settings import *


class Game:
    def __init__(self):
        # pygame setup
        pygame.init()
        self.display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
        pygame.display.set_caption(WINDOW_TITLE)
        self.clock = pygame.time.Clock()
        self.running = True

        # group
        self.all_sprites = pygame.sprite.Group()

        # sprites
        self.player = Player(self.all_sprites)

    def run(self):
        while self.running:
            # delta time
            dt = self.clock.tick() / 1000

            # event loop
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

            # update
            self.all_sprites.update(dt)

            # draw
            self.display_surface.fill("#073D5B")
            self.all_sprites.draw(self.display_surface)
            pygame.display.update()

        pygame.quit()
        sys.exit()


if __name__ == "__main__":
    game = Game()
    game.run()
