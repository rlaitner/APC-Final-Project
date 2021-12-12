import numpy as np


def rect_coords(d, theta, position):
    psi = np.pi/4 - theta
    nu = np.pi - np.pi/4 - theta

    dx1 = d * np.sin(psi)
    dy1 = d * np.cos(psi)
    dx2 = d * np.sin(nu)
    dy2 = d * np.cos(nu)

    top_left = [position[0] + dx2, position[1] + dy2]
    bottom_right = [position[0] - dx2, position[1] - dy2]
    top_right = [position[0] + dx1, position[1] + dy1]
    bottom_left = [position[0] - dx1, position[1] - dy1]

    gvehicle_coords = [top_left, top_right, bottom_left, bottom_right]
    return gvehicle_coords