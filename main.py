import random

import pygame

from pygame.locals import (
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

SNAKE_SIZE = 30

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 128, 0)


class Snake(pygame.sprite.Sprite):
    def __init__(self, width=SNAKE_SIZE, height=SNAKE_SIZE, x=SCREEN_WIDTH, y=SCREEN_HEIGHT):
        super().__init__()
        self.surf = pygame.Surface((width, height))
        self.surf.fill(GREEN)
        self.rect = self.surf.get_rect(center=(x / 2, y / 2))

    @staticmethod
    def direction(key_pressed) -> str:
        if key_pressed == K_w:
            return 'UP'
        elif key_pressed == K_s:
            return 'DOWN'
        elif key_pressed == K_a:
            return 'LEFT'
        elif key_pressed == K_d:
            return 'RIGHT'

    def update(self, direction_in):
        if direction_in == 'UP':
            self.rect.move_ip(0, -SNAKE_SIZE)
        elif direction_in == 'DOWN':
            self.rect.move_ip(0, SNAKE_SIZE)
        elif direction_in == 'LEFT':
            self.rect.move_ip(-SNAKE_SIZE, 0)
        elif direction_in == 'RIGHT':
            self.rect.move_ip(SNAKE_SIZE, 0)

        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > SCREEN_WIDTH:
            self.rect.right = SCREEN_WIDTH
        if self.rect.top < 0:
            self.rect.top = 0
        if self.rect.bottom > SCREEN_HEIGHT:
            self.rect.bottom = SCREEN_HEIGHT


class Tail(Snake):
    def __init__(self, x=0, y=0):
        super(Tail, self).__init__(width=SNAKE_SIZE, height=SNAKE_SIZE, x=x, y=y)

    @staticmethod
    def follow(tails_in):
        for i, tail_in in enumerate(tails_in, start=1):
            if i == len(tails):
                tails[0].rect.center = snake.rect.center
            else:
                tails[-i].rect.center = tails[-i - 1].rect.center


screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

tails = list()

tails.append(Tail())
tails.append(Tail())
tails.append(Tail())
tails.append(Tail())
tails.append(Tail())

running = True
direction = None
snake = Snake()

while running:
    for event in pygame.event.get():
        print(event)
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                running = False
            if event.key in (K_w, K_s, K_a, K_d):
                direction = Snake.direction(event.key)
        if event.type == QUIT:
            running = False

    Tail.follow(tails)

    snake.update(direction)

    screen.fill(BLACK)

    screen.blit(snake.surf, snake.rect)
    for tail in tails:
        screen.blit(tail.surf, tail.rect)

    pygame.display.flip()

    pygame.time.wait(200)
