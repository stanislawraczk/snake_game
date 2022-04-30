import random

import pygame
import torch


from dqn_agent import Agent
from game import Game
from game_objects import Fruit, Snake
from global_variables import SCREEN_WIDTH, SCREEN_HEIGHT, SNAKE_SIZE

agent = Agent(state_size=25, action_size=4, seed=0)
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
menu_text = pygame.font.SysFont('Calibri', 30)
x = SNAKE_SIZE * random.randint(1, (SCREEN_WIDTH // SNAKE_SIZE) - 1)
y = SNAKE_SIZE * random.randint(1, (SCREEN_HEIGHT // SNAKE_SIZE) - 1)
fruit = Fruit(screen_x=x, screen_y=y)
snake = Snake()
tails = list()
env = Game(screen_in=screen, snake_in=snake, tails_in=tails, fruit_in=fruit, wait=100)

agent.qnetwork_local.load_state_dict(torch.load('model.pth'))

state = env.reset()
score = 0
for t in range(2000):
    action = agent.act(state)
    next_state, reward, done = env.step(action)
    score += reward
    state = next_state
    if done:
        break