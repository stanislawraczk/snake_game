import random

import pygame

from pygame.locals import (
    K_UP,
    K_DOWN,
    K_LEFT,
    K_RIGHT,
    K_ESCAPE,
    KEYDOWN,
    QUIT,
    K_w,
    K_s,
    K_a,
    K_d,
)

pygame.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

# colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)


class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.surf = pygame.Surface((75, 25))
        self.surf.fill(WHITE)
        self.rect = self.surf.get_rect(left=200, top=200)

    def update(self, pressed_keys):
        if pressed_keys[K_w]:
            self.rect.move_ip(0, -1)
        if pressed_keys[K_s]:
            self.rect.move_ip(0, 1)
        if pressed_keys[K_a]:
            self.rect.move_ip(-1, 0)
        if pressed_keys[K_d]:
            self.rect.move_ip(1, 0)

        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > SCREEN_WIDTH:
            self.rect.right = SCREEN_WIDTH
        if self.rect.top <= 0:
            self.rect.top = 0
        if self.rect.bottom >= SCREEN_HEIGHT:
            self.rect.bottom = SCREEN_HEIGHT


class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.surf = pygame.Surface((20, 10))
        self.surf.fill(WHITE)
        self.rect = self.surf.get_rect(
            center=(
                random.randint(SCREEN_WIDTH + 20, SCREEN_WIDTH + 100),
                random.randint(0, SCREEN_HEIGHT),
            )
        )
        self.speed = random.randint(5, 20)

    def update(self):
        self.rect.move_ip(-self.speed, 0)
        if self.rect.right < 0:
            self.kill()


screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

player = Player()

running = True

while running:
    for event in pygame.event.get():
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                running = False
        elif event.type == QUIT:
            running = False

    pressed_keys = pygame.key.get_pressed()

    player.update(pressed_keys)

    screen.fill(BLACK)

    screen.blit(player.surf, player.rect)

    pygame.display.flip()
