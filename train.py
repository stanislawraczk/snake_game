from collections import deque
import random

from matplotlib import pyplot as plt
import pygame
import torch
import numpy as np


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
env = Game(screen_in=screen, snake_in=snake, tails_in=tails, fruit_in=fruit, wait=0)

def dqn(n_episodes=2000, max_t=1000, eps_start=1.0, eps_end=0.1, eps_decay=0.995):
    eps = eps_start
    scores = []
    scores_window = deque(maxlen=100)

    for i_episode in range(n_episodes):
        state = env.reset()
        score = 0
        for t in range(max_t):
            action = agent.act(state, eps)
            next_state, reward, done = env.step(action)
            agent.step(state, action, reward, next_state, done)
            score += reward
            state = next_state
            if done:
                break

        scores_window.append(score)
        scores.append(score)
        eps = max(eps_end, eps * eps_decay)
        print(f'Episode {i_episode}\tAverage score {np.mean(scores_window)}', end='\r')
        if (i_episode + 1) % 100 == 0:
            print(f'\rEpisode {i_episode}\tAverage score {np.mean(scores_window)}')
        if np.mean(scores_window) > 15:
            print(f'\rEnviroment solved in {i_episode-100} episodes\t Average score {np.mean(scores_window)}')
            torch.save(agent.qnetwork_local.state_dict(), 'model.pth')
            break
        if (i_episode + 1) % 1000 == 0:
            torch.save(agent.qnetwork_local.state_dict(), 'checkpoint.pth')

    return scores

scores = dqn(n_episodes=1000, max_t=2000, eps_decay=0.995, eps_end=0.1)

plt.plot(np.arange(len(scores)), scores)
plt.ylabel = 'Score'
plt.xlabel = 'Episode number'
plt.show()
