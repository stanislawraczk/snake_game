import numpy as np
from global_variables import SCREEN_HEIGHT, SCREEN_WIDTH, DIRECTIONS, ANGLES

def polar(x, y) -> tuple:
    """returns rho, theta (degrees)"""
    if np.degrees(np.arctan2(y, x)) < 0:
        return np.hypot(x, y), 360 + np.degrees(np.arctan2(y, x)) #* -1 + 180
    else:
        return np.hypot(x, y), np.degrees(np.arctan2(y, x))

def calculate_second_cartesian(cartesian_coordinate, rho, axis):
    rho = np.radians(rho)
    second_coordinate = SCREEN_WIDTH + SCREEN_HEIGHT
    if axis == 'X' and np.cos(rho) != 0:
        second_coordinate = cartesian_coordinate / np.cos(rho) * np.sin(rho)
    if axis == 'Y' and np.sin(rho) != 0:
        second_coordinate = cartesian_coordinate / np.sin(rho) * np.cos(rho)
    return np.around(second_coordinate)

def get_state(snake_in, tails_in, fruit_in):
    '''
    This function returns the current state of the enviroment.
    State is a 25 columns table where there are 8 sets of columns for each corresponding direction from snake's head.
    And one for snake's direction
    These sets consists of:
    * distance from a closest object (float)
    * is the object a wall (bool)
    * is the object a tail (bool)
    '''
    walls = {('X', '+') : SCREEN_WIDTH - snake_in.rect.center[0],
             ('X', '-') : -snake_in.rect.center[0],
             # Coordinate system in pygame is calculated from the top right,
             # that is why the Y coordinate is calculated differently
             ('Y', '+') : snake_in.rect.center[1],
             ('Y', '-') : snake_in.rect.center[1] - SCREEN_HEIGHT}
    state = list()
    for angle in ANGLES:
        distance = SCREEN_WIDTH + SCREEN_HEIGHT
        is_wall = 0
        is_tail = 0
        for key in walls.keys():
            second_coordinate = calculate_second_cartesian(walls[key], angle, key[0])
            if key[0] == 'X':
                polar_cords = polar(walls[key], second_coordinate)
            else:
                polar_cords = polar(second_coordinate, walls[key])

            if np.around(polar_cords[1]) == angle and polar_cords[0] < distance:
                distance = polar_cords[0]
                is_wall = 1
        for tail in tails_in:
            polar_cords = polar(tail.rect.center[0] - snake_in.rect.center[0], snake_in.rect.center[1] - tail.rect.center[1])
            if np.around(polar_cords[1]) == angle and polar_cords[0] < distance:
                distance = polar_cords[0]
                is_wall = 0
                is_tail = 1
        polar_cords = polar(fruit_in.rect.center[0] - snake_in.rect.center[0], snake_in.rect.center[1] - fruit_in.rect.center[1])
        if np.around(polar_cords[1]) == angle and polar_cords[0] < distance:
            distance = polar_cords[0]
            is_wall = 0
            is_tail = 0

        state.append(distance / max(SCREEN_HEIGHT, SCREEN_WIDTH))
        state.append(is_wall)
        state.append(is_tail)
    direction = DIRECTIONS[snake_in.direction]
    state.append(direction)

    return np.array(state)
