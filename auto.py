from typing import List
from random import randint

from pygame import key
from game_objects import Fruit, Snake
from global_variables import SCREEN_HEIGHT, SCREEN_WIDTH, SNAKE_SIZE

OPPOSITE = {'UP': 'DOWN', 'DOWN': 'UP', 'LEFT': 'RIGHT', 'RIGHT': 'LEFT'}
MOVE_VECTOR = {'UP': (0, -SNAKE_SIZE), 'DOWN': (0, SNAKE_SIZE), 'LEFT': (-SNAKE_SIZE, 0), 'RIGHT': (SNAKE_SIZE, 0)}

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
    pass

"""
inputs:
    fruit distance
    every wall distance
    every tail piece distance
output:
    direction
functions:
    
"""