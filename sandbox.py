import random
import pygame
import numpy as np
from game import Game
from game_objects import Fruit, Snake
from global_variables import SCREEN_WIDTH, SCREEN_HEIGHT, SNAKE_SIZE, AUTO

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
snake = Snake()
tails = list()
x = SNAKE_SIZE * random.randint(1, (SCREEN_WIDTH // SNAKE_SIZE) - 1)
y = SNAKE_SIZE * random.randint(1, (SCREEN_HEIGHT // SNAKE_SIZE) - 1)
fruit = Fruit(screen_x=x, screen_y=y)
scores = []
game = Game(mode=AUTO, wait=10, screen_in=screen, snake_in=snake, tails_in=tails, fruit_in=fruit)

print(game.reset())
while True:
    next_state, reward, done = game.step(random.randint(0,3))
    print(next_state, end='\r')
    print(f'Done: {done}')
    if done:
        break