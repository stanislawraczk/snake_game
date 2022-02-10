from typing import List
from random import randint

from pygame import key
import numpy as np

from game_objects import Fruit, Snake
from global_variables import SCREEN_HEIGHT, SCREEN_WIDTH, SNAKE_SIZE

OPPOSITE = {'UP': 'DOWN', 'DOWN': 'UP', 'LEFT': 'RIGHT', 'RIGHT': 'LEFT'}
MOVE_VECTOR = {'UP': (0, -SNAKE_SIZE), 'DOWN': (0, SNAKE_SIZE), 'LEFT': (-SNAKE_SIZE, 0), 'RIGHT': (SNAKE_SIZE, 0)}
NUM_OF_WALLS = 4

def collision(snake, tails_in, move_x=0, move_y=0):
    if snake.rect.centerx + move_x <= 0:
        return True
    if snake.rect.centerx + move_x >= SCREEN_WIDTH:
        return True
    if snake.rect.centery + move_y <= 0:
        return True
    if snake.rect.centery + move_y >= SCREEN_HEIGHT:
        return True

    for tail_in in tails_in:
        if tail_in.rect.centerx == snake.rect.centerx + move_x and tail_in.rect.centery == snake.rect.centery + move_y:
            return True
    return False

def dumb_algorithm(snake: Snake, fruit: Fruit, tails: List) -> str:
    key = ''

    distance = abs(snake.rect.centerx - fruit.rect.centerx) + abs(snake.rect.centery - fruit.rect.centery) + 2 * abs(SNAKE_SIZE)

    for move in MOVE_VECTOR.keys():
        fruit_distance = (snake.rect.centerx - fruit.rect.centerx + MOVE_VECTOR[move][0],\
                          snake.rect.centery - fruit.rect.centery + MOVE_VECTOR[move][1])
        
        distance_temp = abs(fruit_distance[0]) + abs(fruit_distance[1])

        if snake.direction == OPPOSITE[move] or collision(snake, tails, MOVE_VECTOR[move][0], MOVE_VECTOR[move][1]):
            continue
        elif distance_temp < distance:
            key = move
            distance = distance_temp
    return key



class SnakeAI:
    def __init__(self, tail_pieces=0, mu=0, sigma=1) -> None:
        self.w1 = np.random.normal(mu,sigma)
        self.w2 = np.random.normal(mu,sigma,NUM_OF_WALLS)
        if tail_pieces != 0:
            self.w3 = np.random.normal(mu,sigma,tail_pieces)
        else:
            self.w3 = np.array([], dtype=float)

    def value_function(self, fd, wd, tpd):
        return self.w1 * fd + np.dot(wd, self.w2) + np.dot(tpd, self.w3)

"""
inputs:
    fruit distance - fd
    every wall distance - wd[]
    every tail piece distance - tpd[[]]
output:
    direction
functions:
    for every direction:
        z = w1 * fd + w2[] * wd[] + w3[[]] * tpd[[]]
    choose a move with the biggest z
order of execution:
    update weights (to maximize z for every equation) if first iteration choose random weigths
    run algorithm
    save all moves (i. e. every z, weigths, fruit distances, wall distances and tail pieces distances)
    
"""