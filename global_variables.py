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
ACTIONS = {0 : K_d, 1 : K_w, 2 : K_a, 3 : K_s}
OPPOSITE = {'UP': 'DOWN', 'DOWN': 'UP', 'LEFT': 'RIGHT', 'RIGHT': 'LEFT'}
MOVE_VECTOR = {'UP': (0, -SNAKE_SIZE), 'DOWN': (0, SNAKE_SIZE), 'LEFT': (-SNAKE_SIZE, 0), 'RIGHT': (SNAKE_SIZE, 0)}
NUM_OF_WALLS = 4
DIRECTIONS = {'RIGHT' : 0, 'UP' : 1,  'LEFT' : 2, 'DOWN' : 3}
ANGLES = [0, 45, 90, 135, 180, 225, 270, 315]

BUFFER_SIZE = int(1e6)
BATCH_SIZE = 128
GAMMA = 1.1
TAU = 5e-4
LR = 1e-4
UPDATE_EVERY = 4
SOFT_UPDATE_EVERY = 1
