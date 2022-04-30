import random

import pygame
import numpy as np

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

from game_objects import Fruit, Tail
from auto import dumb_algorithm as algorithm
from global_variables import SCREEN_WIDTH, SCREEN_HEIGHT, SNAKE_SIZE, WHITE, BLACK, QUIT_GAME, MAN, MENU, \
    AUTO, KEYS, ACTIONS
from additional_functions import get_state

pygame.init()
pygame.font.init()


class Game:
    def __init__(self, screen_in, snake_in, tails_in, fruit_in, mode=MENU, wait=1000):
        self.message = 'Press Enter to start or "a" to run automated'
        self.running = mode
        self.wait = wait
        self.fruit_on_screen = False
        self.screen_in = screen_in
        self.snake_in = snake_in
        self.tails_in = tails_in
        self.fruit_in = fruit_in
        self.score = 0

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

    def game_loop(self):
        self.score = 0
        while self.running in (MAN, AUTO):
            if not self.fruit_on_screen:
                fruit_x = SNAKE_SIZE * random.randint(1, (SCREEN_WIDTH // SNAKE_SIZE) - 1)
                fruit_y = SNAKE_SIZE * random.randint(1, (SCREEN_HEIGHT // SNAKE_SIZE) - 1)
                self.fruit_in = Fruit(screen_x=fruit_x, screen_y=fruit_y)
                self.fruit_on_screen = True
            
            if self.running == MAN:
                first_key_pressed = True
                for event in pygame.event.get():
                    if event.type == KEYDOWN:
                        if event.key == K_ESCAPE:
                            self.running = MENU
                        if event.key in (K_w, K_s, K_a, K_d) and first_key_pressed:
                            first_key_pressed = False
                            self.snake_in.set_direction(event.key)
                    if event.type == QUIT:
                        self.running = QUIT_GAME

            if self.running == AUTO:
                key = algorithm(snake=self.snake_in, fruit=self.fruit_in, tails=self.tails_in)
                if key in KEYS.keys():
                    self.snake_in.set_direction(KEYS[key])
                for event in pygame.event.get():
                    if event.type == KEYDOWN:
                        if event.key == K_ESCAPE:
                            self.running = MENU
                    if event.type == QUIT:
                        self.running = QUIT_GAME

            Tail.follow(self.tails_in, self.snake_in)
            self.snake_in.update()
            self.snake_in.check_collision(self.tails_in)
            if self.snake_in.collision:
                self.score -= 10
                self.game_over(self.snake_in)
                self.tails_in = list()
                break

            if self.snake_in.check_fruit(self.fruit_in):
                self.score += 10
                self.fruit_on_screen = False
                self.tails_in.append(Tail(screen_x=2 * self.snake_in.rect.centerx, screen_y=2 * self.snake_in.rect.centery))

            self.screen_in.fill(BLACK)
            self.screen_in.blit(self.snake_in.surf, self.snake_in.rect)
            self.screen_in.blit(self.fruit_in.surf, self.fruit_in.rect)
            for tail in self.tails_in:
                self.screen_in.blit(tail.surf, tail.rect)

            pygame.display.flip()

            pygame.time.wait(self.wait)
        return self.score

    def reset(self):
        self.snake_in.reset()

        fruit_x = SNAKE_SIZE * random.randint(1, (SCREEN_WIDTH // SNAKE_SIZE) - 1)
        fruit_y = SNAKE_SIZE * random.randint(1, (SCREEN_HEIGHT // SNAKE_SIZE) - 1)
        self.fruit_in = Fruit(screen_x=fruit_x, screen_y=fruit_y)
        self.fruit_on_screen = True

        return get_state(self.snake_in, self.tails_in, self.fruit_in)

    def step(self, action):
        done = 0
        reward = 0
        self.snake_in.set_direction(ACTIONS[action])

        Tail.follow(self.tails_in, self.snake_in)
        self.snake_in.update()
        self.snake_in.check_collision(self.tails_in)
        if self.snake_in.collision:
            self.score -= 10
            reward = -1
            self.game_over(self.snake_in)
            self.tails_in = list()
            done = 1

        if self.snake_in.check_fruit(self.fruit_in):
            self.score += 10
            reward = 1
            self.fruit_on_screen = False
            self.tails_in.append(Tail(screen_x=2 * self.snake_in.rect.centerx, screen_y=2 * self.snake_in.rect.centery))
        
        if not self.fruit_on_screen:
            fruit_x = SNAKE_SIZE * random.randint(1, (SCREEN_WIDTH // SNAKE_SIZE) - 1)
            fruit_y = SNAKE_SIZE * random.randint(1, (SCREEN_HEIGHT // SNAKE_SIZE) - 1)
            self.fruit_in = Fruit(screen_x=fruit_x, screen_y=fruit_y)
            self.fruit_on_screen = True

        self.screen_in.fill(BLACK)
        self.screen_in.blit(self.snake_in.surf, self.snake_in.rect)
        self.screen_in.blit(self.fruit_in.surf, self.fruit_in.rect)
        for tail in self.tails_in:
            self.screen_in.blit(tail.surf, tail.rect)

        pygame.display.flip()
        pygame.time.wait(self.wait)

        next_state = get_state(self.snake_in, self.tails_in, self.fruit_in)

        return next_state, reward, done

    def get_state_size(self):
        return np.array(get_state(self.snake_in, self.tails_in, self.fruit_in)).size

    def get_action_size(self):
        return np.array(list(ACTIONS.keys())).size
