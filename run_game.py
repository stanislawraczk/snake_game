import random

import pygame

from global_variables import SCREEN_WIDTH, SCREEN_HEIGHT, SNAKE_SIZE, MENU
from game import Game
from game_objects import Snake, Fruit

def main():
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    menu_text = pygame.font.SysFont('Calibri', 30)
    x = SNAKE_SIZE * random.randint(1, (SCREEN_WIDTH // SNAKE_SIZE) - 1)
    y = SNAKE_SIZE * random.randint(1, (SCREEN_HEIGHT // SNAKE_SIZE) - 1)
    fruit = Fruit(screen_x=x, screen_y=y)
    snake = Snake()
    tails = list()
    game = Game(screen_in=screen, snake_in=snake, tails_in=tails, fruit_in=fruit, wait=0)

    while game.running == MENU:
        game.menu_loop(menu_text, screen)
        game.game_loop()


if __name__ == '__main__':
    main()