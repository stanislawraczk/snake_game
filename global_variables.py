from pygame.locals import (
    K_w,
    K_s,
    K_a,
    K_d,
)

SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600

SNAKE_SIZE = 30

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 128, 0)
RED = (255, 0, 0)

QUIT_GAME = 'QUIT'
MAN = 'MANUAL'
MENU = 'MENU'
AUTO = 'AUTO'
TRAIN = 'TRAIN'
TEST = 'TEST'

KEYS = {'UP': K_w, 'DOWN': K_s, 'LEFT': K_a, 'RIGHT': K_d}
ACTIONS = {0 : K_w, 1 : K_s, 2 : K_a, 3 : K_d}
OPPOSITE = {'UP': 'DOWN', 'DOWN': 'UP', 'LEFT': 'RIGHT', 'RIGHT': 'LEFT'}
MOVE_VECTOR = {'UP': (0, -SNAKE_SIZE), 'DOWN': (0, SNAKE_SIZE), 'LEFT': (-SNAKE_SIZE, 0), 'RIGHT': (SNAKE_SIZE, 0)}
NUM_OF_WALLS = 4
DIRECTIONS = ('UP', 'UP_R', 'RIGHT', 'DOWN_R', 'DOWN', 'DOWN_L', 'LEFT', 'UP_L')
DEGREES = [0, 45, 90, 135, 180, 225, 270, 315]
