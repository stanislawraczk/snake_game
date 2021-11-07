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

SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600

SNAKE_SIZE = 30

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 128, 0)
RED = (255, 0, 0)


class Game:
    def __init__(self):
        self.message = 'Press Enter to start or Escape to quit'
        self.running = False
        self.menu_running = True
        self.fruit_on_screen = False

    def game_over(self):
        self.message = 'GAME OVER'
        self.running = False
        self.menu_running = True

    def menu_loop(self, menu_text_in, screen_in):
        for event in pygame.event.get():
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    self.menu_running = False
                    self.running = False
                if event.key == K_RETURN:
                    self.menu_running = False
                    self.running = True
            if event.type == QUIT:
                self.menu_running = False
                self.running = False
        menu_text_surf = menu_text_in.render(self.message, False, WHITE)
        screen_in.blit(menu_text_surf, (0, 0))
        pygame.display.flip()

    def game_loop(self, score_in, screen_in, snake_in, tails_in, fruit_in):
        while self.running:
            for event in pygame.event.get():
                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        self.running = False
                        self.menu_running = True
                    if event.key in (K_w, K_s, K_a, K_d):
                        snake_in.set_direction(event.key)
                        Tail.follow(tails_in, snake_in)
                        snake_in.update()
                        snake_in.moved = True
                if event.type == QUIT:
                    self.running = False

            if not snake_in.moved:
                Tail.follow(tails_in, snake_in)
                snake_in.update()
            snake_in.moved = False
            snake_in.check_collision(tails_in)
            if snake_in.collision:
                self.game_over()
                score_in -= 10

            if not self.fruit_on_screen:
                fruit_x = SNAKE_SIZE * random.randint(1, (SCREEN_WIDTH // SNAKE_SIZE) - 1)
                fruit_y = SNAKE_SIZE * random.randint(1, (SCREEN_HEIGHT // SNAKE_SIZE) - 1)
                fruit_in = Fruit(screen_x=fruit_x, screen_y=fruit_y)
                self.fruit_on_screen = True

            if snake_in.check_fruit(fruit_in):
                score_in += 10
                self.fruit_on_screen = False
                tails_in.append(Tail(screen_x=2 * snake_in.rect.centerx, screen_y=2 * snake_in.rect.centery))

            print(score_in)

            screen_in.fill(BLACK)
            screen_in.blit(snake_in.surf, snake_in.rect)
            screen_in.blit(fruit_in.surf, fruit_in.rect)
            for tail in tails_in:
                screen_in.blit(tail.surf, tail.rect)

            pygame.display.flip()

            pygame.time.wait(200)


class Snake(pygame.sprite.Sprite):
    def __init__(self, width=SNAKE_SIZE, height=SNAKE_SIZE, screen_x=SCREEN_WIDTH, screen_y=SCREEN_HEIGHT):
        super().__init__()
        self.surf = pygame.Surface((width, height))
        self.surf.fill(GREEN)
        self.rect = self.surf.get_rect(center=(screen_x / 2, screen_y / 2))
        self.direction = ''
        self.collision = False
        self.moved = False

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

    def check_fruit(self, fruit_in):
        if fruit_in.rect.center == self.rect.center:
            return True
        return False


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


def main():
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    menu_text = pygame.font.SysFont('Calibri', 30)
    game = Game()
    snake = Snake()
    tails = list()
    score = 0
    x = SNAKE_SIZE * random.randint(1, (SCREEN_WIDTH // SNAKE_SIZE) - 1)
    y = SNAKE_SIZE * random.randint(1, (SCREEN_HEIGHT // SNAKE_SIZE) - 1)
    fruit = Fruit(screen_x=x, screen_y=y)

    while game.menu_running:
        game.menu_loop(menu_text, screen)
        game.game_loop(score_in=score, screen_in=screen, snake_in=snake, tails_in=tails, fruit_in=fruit)


if __name__ == '__main__':
    main()
