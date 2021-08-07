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
    K_RETURN,
)

pygame.init()
pygame.font.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

SNAKE_SIZE = 30

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 128, 0)
RED = (255, 0, 0)


class GameLogic:
    def __init__(self):
        self.message = 'Press Enter to start or Escape to quit'
        self.running = False
        self.menu_running = True
        self.fruit_on_screen = False

    def game_over(self):
        self.message = 'GAME OVER'
        self.running = False
        self.menu_running = True


class Snake(pygame.sprite.Sprite):
    def __init__(self, width=SNAKE_SIZE, height=SNAKE_SIZE, x=SCREEN_WIDTH, y=SCREEN_HEIGHT):
        super().__init__()
        self.surf = pygame.Surface((width, height))
        self.surf.fill(GREEN)
        self.rect = self.surf.get_rect(center=(x / 2, y / 2))
        self.collision = False

    @staticmethod
    def direction(key_pressed, direction_in) -> str:
        if key_pressed == K_w and direction_in != 'DOWN':
            return 'UP'
        elif key_pressed == K_s and direction_in != 'UP':
            return 'DOWN'
        elif key_pressed == K_a and direction_in != 'RIGHT':
            return 'LEFT'
        elif key_pressed == K_d and direction_in != 'LEFT':
            return 'RIGHT'
        else:
            return direction_in

    def update(self, direction_in):
        if direction_in == 'UP':
            self.rect.move_ip(0, -SNAKE_SIZE)
        elif direction_in == 'DOWN':
            self.rect.move_ip(0, SNAKE_SIZE)
        elif direction_in == 'LEFT':
            self.rect.move_ip(-SNAKE_SIZE, 0)
        elif direction_in == 'RIGHT':
            self.rect.move_ip(SNAKE_SIZE, 0)

    def check_collision(self, tails_in):
        if self.rect.left < 0:
            self.rect.left = 0
            self.collision = True
        if self.rect.right > SCREEN_WIDTH:
            self.rect.right = SCREEN_WIDTH
            self.collision = True
        if self.rect.top < 0:
            self.rect.top = 0
            self.collision = True
        if self.rect.bottom > SCREEN_HEIGHT:
            self.rect.bottom = SCREEN_HEIGHT
            self.collision = True

        for tail_in in tails_in:
            if tail_in.rect.center == self.rect.center:
                self.collision = True


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
tails.append(Tail())
tails.append(Tail())

menu_text = pygame.font.SysFont('Calibri', 30)
direction = 'UP'
snake = Snake()
game = GameLogic()
# game.fruit_on_screen = False
# game.running = False
# game.menu_running = True
# game.message = 'Press Enter to start or Escape to quit'

while game.menu_running:
    for event in pygame.event.get():
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                game.menu_running = False
                game.running = False
            if event.key == K_RETURN:
                game.menu_running = False
                game.running = True
        if event.type == QUIT:
            game.menu_running = False
            game.running = False
    menu_text_surf = menu_text.render(game.message, False, WHITE)
    screen.blit(menu_text_surf, (0, 0))
    pygame.display.flip()

    while game.running:
        for event in pygame.event.get():
            print(event)
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    game.running = False
                    game.menu_running = True
                if event.key in (K_w, K_s, K_a, K_d):
                    direction = Snake.direction(event.key, direction)
            if event.type == QUIT:
                game.running = False

        Tail.follow(tails)
        snake.update(direction)
        snake.check_collision(tails)

        if snake.collision:
            game.game_over()

        screen.fill(BLACK)
        screen.blit(snake.surf, snake.rect)

        for tail in tails:
            screen.blit(tail.surf, tail.rect)

        pygame.display.flip()

        pygame.time.wait(200)
