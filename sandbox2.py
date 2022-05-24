import numpy as np
from global_variables import SCREEN_HEIGHT, SCREEN_WIDTH, ACTIONS, DIRECTIONS_TO_ANGLES, NUM_OF_ANGLES
from additional_functions import get_state

def polar(x, y) -> tuple:
    """returns rho, theta (degrees)"""
    if np.degrees(np.arctan2(y, x)) < 0:
        return np.hypot(x, y), 360 + np.degrees(np.arctan2(y, x))
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

# print(polar(-0,300))
# print(polar(300,-0))
angle = 135
# print(calculate_second_cartesian(1, angle, 'X'), polar(1,calculate_second_cartesian(1, angle, 'X')))
# print(calculate_second_cartesian(-1, angle, 'X'), polar(-1,calculate_second_cartesian(-1, angle, 'X')))
# print(calculate_second_cartesian(1, angle, 'Y'), polar(calculate_second_cartesian(1, angle, 'Y'), 1))
# print(calculate_second_cartesian(-1, angle, 'Y'), polar(calculate_second_cartesian(-1, angle, 'Y'), -1))
# print(polar(-1,-1))


direction_angle = DIRECTIONS_TO_ANGLES['DOWN']
angle_diff = 360 / (NUM_OF_ANGLES + 1)
angles = []
for i in range(NUM_OF_ANGLES):
    num_of_angles_on_sides = (NUM_OF_ANGLES - 1) // 2
    angle = direction_angle - angle_diff * (i - num_of_angles_on_sides)
    if angle < 0:
        angle += 360
    if angle >= 360:
        angle -= 360
    angles.append(angle)

print(angles)