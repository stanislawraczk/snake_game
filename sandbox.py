import random
import pygame
import numpy as np
from game import Game
from game_objects import Fruit, Snake
from global_variables import SCREEN_WIDTH, SCREEN_HEIGHT, SNAKE_SIZE, AUTO, DIRECTIONS
from auto import dumb_algorithm

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
snake = Snake()
tails = list()
x = SNAKE_SIZE * random.randint(1, (SCREEN_WIDTH // SNAKE_SIZE) - 1)
y = SNAKE_SIZE * random.randint(1, (SCREEN_HEIGHT // SNAKE_SIZE) - 1)
fruit = Fruit(screen_x=x, screen_y=y)
scores = []
game = Game(mode=AUTO, wait=10000, screen_in=screen, snake_in=snake, tails_in=tails, fruit_in=fruit)

print(game.reset())
while True:
    action = dumb_algorithm(game.snake_in, game.fruit_in, game.tails_in)
    next_state, reward, done = game.step(DIRECTIONS[action])
    print(next_state)
    #print(f'reward: {reward}')
    if done:
        break