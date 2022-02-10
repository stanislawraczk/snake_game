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

KEYS = {'UP': K_w, 'DOWN': K_s, 'LEFT': K_a, 'RIGHT': K_d}

print(KEYS['UP'])
print(K_w)
