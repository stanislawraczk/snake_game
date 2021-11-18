import pygame

from pygame.locals import (
    K_w,
    K_s,
    K_a,
    K_d,
)
from global_variables import SCREEN_WIDTH, SCREEN_HEIGHT, SNAKE_SIZE, GREEN, RED


class Snake(pygame.sprite.Sprite):
    def __init__(self, width=SNAKE_SIZE, height=SNAKE_SIZE, screen_x=SCREEN_WIDTH, screen_y=SCREEN_HEIGHT):
        super().__init__()
        self.surf = pygame.Surface((width, height))
        self.surf.fill(GREEN)
        self.rect = self.surf.get_rect(center=(screen_x / 2, screen_y / 2))
        self.direction = ''
        self.collision = False

    def set_direction(self, key_pressed):
        if key_pressed == K_w and self.direction != 'DOWN':
            self.direction = 'UP'
        elif key_pressed == K_s and self.direction != 'UP':
            self.direction = 'DOWN'
        elif key_pressed == K_a and self.direction != 'RIGHT':
            self.direction = 'LEFT'
        elif key_pressed == K_d and self.direction != 'LEFT':
            self.direction = 'RIGHT'

    def update(self):
        if self.direction == 'UP':
            self.rect.move_ip(0, -SNAKE_SIZE)
        elif self.direction == 'DOWN':
            self.rect.move_ip(0, SNAKE_SIZE)
        elif self.direction == 'LEFT':
            self.rect.move_ip(-SNAKE_SIZE, 0)
        elif self.direction == 'RIGHT':
            self.rect.move_ip(SNAKE_SIZE, 0)

    def check_collision(self, tails_in, move_x=0, move_y=0):
        if self.rect.left < 0:
            self.collision = True
        if self.rect.right > SCREEN_WIDTH:
            self.collision = True
        if self.rect.top < 0:
            #self.rect.top = 0
            self.collision = True
        if self.rect.bottom > SCREEN_HEIGHT:
            self.collision = True

        for tail_in in tails_in:
            if tail_in.rect.center == self.rect.center:
                self.collision = True

    def check_fruit(self, fruit_in):
        if fruit_in.rect.center == self.rect.center:
            return True
        return False

    def reset(self):
        self.rect = self.surf.get_rect(center=(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2))
        self.collision = False
        self.direction = ''


class Tail(Snake):
    def __init__(self, screen_x=0, screen_y=0):
        super(Tail, self).__init__(width=SNAKE_SIZE, height=SNAKE_SIZE, screen_x=screen_x, screen_y=screen_y)

    @staticmethod
    def follow(tails_in, snake):
        for i, tail_in in enumerate(tails_in, start=1):
            if i == len(tails_in):
                tails_in[0].rect.center = snake.rect.center
            else:
                tails_in[-i].rect.center = tails_in[-i - 1].rect.center


class Fruit(pygame.sprite.Sprite):
    def __init__(self, width=SNAKE_SIZE, height=SNAKE_SIZE, screen_x=SCREEN_WIDTH, screen_y=SCREEN_HEIGHT):
        super(Fruit, self).__init__()
        self.surf = pygame.Surface((width, height))
        self.surf.fill(RED)
        self.rect = self.surf.get_rect(center=(screen_x, screen_y))
