import pygame

from .settings import *


class Player(pygame.sprite.Sprite):
    def __init__(self, group):
        super().__init__(group)
        self.image = pygame.Surface((50, 50))
        self.image.fill("#35A635")
        self.rect = self.image.get_frect()

        # movement
        self.direction = pygame.Vector2()
        self.speed = 600

    def input(self):
        keys = pygame.key.get_pressed()
        self.direction.x = int(keys[pygame.K_RIGHT]) - int(keys[pygame.K_LEFT])
        self.direction.y = int(keys[pygame.K_DOWN]) - int(keys[pygame.K_UP])
        self.direction = (
            self.direction.normalize() if self.direction else self.direction
        )

    def move(self, dt):
        if not 0 <= self.rect.centerx <= WINDOW_WIDTH:
            self.rect.centerx = 0
        if not 0 <= self.rect.centery <= WINDOW_HEIGHT:
            self.rect.centery = 0

        self.rect.center += self.direction * self.speed * dt

    def update(self, *args, **kwargs):
        self.input()
        self.move(args[0])
