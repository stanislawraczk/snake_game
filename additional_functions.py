import numpy as np
from global_variables import SCREEN_HEIGHT, SCREEN_WIDTH, DEGREES

def polar(x, y) -> tuple:
  """returns rho, theta (degrees)"""
  return np.hypot(x, y), np.degrees(np.arctan2(y, x))

def calculate_second_cartesian(cartesian_coordinate, rho, axis):
    rho = rho * np.pi / 180
    second_coordinate = SCREEN_WIDTH + SCREEN_HEIGHT
    if axis == 'X' and np.cos(rho) != 0:
        second_coordinate = np.sqrt((cartesian_coordinate**2) / (np.cos(rho)**2) - cartesian_coordinate**2)
    if axis == 'Y' and np.sin(rho) != 0:
        second_coordinate = np.sqrt((cartesian_coordinate**2) / (np.sin(rho)**2) - cartesian_coordinate**2)
    return second_coordinate

def get_state(snake_in, tails_in, fruit_in):
    '''
    This function returns the current state of the enviroment.
    State is a 24 columns table where there are 8 sets of columns for each corresponding direction from snake's head.
    These sets consists of:
    * distance from a closest object (float)
    * is the object a wall (bool)
    * is the object a tail (bool)
    '''
    walls = {('X', '+') : SCREEN_WIDTH - snake_in.rect.center[0],
             ('X', '-') : -snake_in.rect.center[0],
             ('Y', '+') : SCREEN_HEIGHT - snake_in.rect.center[1],
             ('Y', '-') : -snake_in.rect.center[1]}
    state = list()
    for degree in DEGREES:
        distance = SCREEN_WIDTH + SCREEN_HEIGHT
        is_wall = 0
        is_tail = 0
        for key in walls.keys():
            second_coordinate = calculate_second_cartesian(walls[key], degree, key[0])
            if second_coordinate < walls[(key[0], '+')] and second_coordinate > walls[(key[0], '-')]:
                tmp_dist = np.hypot(walls[key], second_coordinate)
                if tmp_dist < distance:
                    distance = tmp_dist
                    is_wall = 1
        for tail in tails_in:
            polar_cords = polar(tail.rect.center[0], tail.rect.center[1])
            if polar_cords[1] == degree and polar_cords[0] < distance:
                distance = polar_cords[0]
                is_wall = 0
                is_tail = 1
        polar_cords = polar(fruit_in.rect.center[0], fruit_in.rect.center[1])
        if polar_cords[1] == degree and polar_cords[0] < distance:
            distance = polar_cords[0]
            is_wall = 0
            is_tail = 0

        state.append(distance)
        state.append(is_wall)
        state.append(is_tail)

    return state
