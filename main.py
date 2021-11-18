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

from game_objects import Fruit, Snake, Tail
from auto import dumb_algorithm as algorithm
from global_variables import SCREEN_WIDTH, SCREEN_HEIGHT, SNAKE_SIZE, WHITE, BLACK, QUIT_GAME, MAN, MENU, \
    AUTO, KEYS

pygame.init()
pygame.font.init()


class Game:
    def __init__(self):
        self.message = 'Press Enter to start or Escape to quit'
        self.running = MENU
        self.fruit_on_screen = False

    def game_over(self, snake_in):
        self.message = 'GAME OVER'
        if self.running == MAN:
            self.running = MENU
        snake_in.reset()

    def menu_loop(self, menu_text_in, screen_in):
        for event in pygame.event.get():
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    self.running = QUIT_GAME
                if event.key == K_RETURN:
                    self.running = MAN
                if event.key == K_a:
                    self.running = AUTO
            if event.type == QUIT:
                self.running = QUIT_GAME
        menu_text_surf = menu_text_in.render(self.message, False, WHITE)
        screen_in.blit(menu_text_surf, (0, 0))
        pygame.display.flip()

    def game_loop(self, score_in, screen_in, snake_in, tails_in, fruit_in):
        while self.running in (MAN, AUTO):
            if not self.fruit_on_screen:
                fruit_x = SNAKE_SIZE * random.randint(1, (SCREEN_WIDTH // SNAKE_SIZE) - 1)
                fruit_y = SNAKE_SIZE * random.randint(1, (SCREEN_HEIGHT // SNAKE_SIZE) - 1)
                fruit_in = Fruit(screen_x=fruit_x, screen_y=fruit_y)
                self.fruit_on_screen = True
            
            if self.running == MAN:
                first_key_pressed = True
                for event in pygame.event.get():
                    if event.type == KEYDOWN:
                        if event.key == K_ESCAPE:
                            self.running = MENU
                        if event.key in (K_w, K_s, K_a, K_d) and first_key_pressed:
                            first_key_pressed = False
                            snake_in.set_direction(event.key)
                    if event.type == QUIT:
                        self.running = QUIT_GAME

            if self.running == AUTO:
                key = algorithm(snake=snake_in, fruit=fruit_in, tails=tails_in)
                if key in KEYS.keys():
                    snake_in.set_direction(KEYS[key])
                for event in pygame.event.get():
                    if event.type == KEYDOWN:
                        if event.key == K_ESCAPE:
                            self.running = MENU
                    if event.type == QUIT:
                        self.running = QUIT_GAME

            Tail.follow(tails_in, snake_in)
            snake_in.update()
            snake_in.check_collision(tails_in)
            if snake_in.collision:
                self.game_over(snake_in)
                tails_in = list()
                score_in -= 10

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

            pygame.time.wait(50)


def main():
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    menu_text = pygame.font.SysFont('Calibri', 30)
    game = Game()
    snake = Snake()
    score = 0
    x = SNAKE_SIZE * random.randint(1, (SCREEN_WIDTH // SNAKE_SIZE) - 1)
    y = SNAKE_SIZE * random.randint(1, (SCREEN_HEIGHT // SNAKE_SIZE) - 1)
    fruit = Fruit(screen_x=x, screen_y=y)

    while game.running == MENU:
        tails = list()
        game.menu_loop(menu_text, screen)
        game.game_loop(score_in=score, screen_in=screen, snake_in=snake, tails_in=tails, fruit_in=fruit)


if __name__ == '__main__':
    main()
