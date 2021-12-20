import numpy as np
from point_obstacle_collision_detection import *


def mesh(x_env, y_env, resolution, obstacles, vehicle):
    """
    Discretizes the expanded obstacles in the environment.
    Returns a matrix indicating the presence or absence of an expanded obstacle at each point.

    Parameters
    ----------
        x_env: horizontal length of the field
        y_env: vertical length of the field
        resolution: number of grid points per unit length
        obstacles: list of obstacles
        vehicle: Vehicle object

    Returns
    -------
        grid: an n x n matrix where g(y * resolution, x * resolution) = 1 indicates a blocked
            position due to vehicle geometry and obstacles at the point (x,y) and
            g(y * resolution, x * resolution) = 0 indicates no obstacles at (x,y).
    """

    grid = np.zeros((y_env * resolution, x_env * resolution))

    # space between adjacent nodes
    grid_spacing = 1 / resolution

    for obs in obstacles:
        expand_obs = expanded_obstacle(vehicle, obs)

        if expand_obs.shape == "circle":

            center = obs.center
            x_c = center[0]
            y_c = center[1]
            r = obs.radius

            for x in range(x_c - r, x_c + r + grid_spacing, grid_spacing):
                for y in range(y_c - r, y_c + r + grid_spacing, grid_spacing):
                    if is_inside_circle(np.array([x,y]), expand_obs) == True:

                        # set g(y,x) = 1 for each point (x,y) occupied by the obstacle
                        grid[y * resolution, x * resolution] = 1

        # rectangle obstacle
        elif expand_obs.shape == "rectangle":

            origin = obs.origin
            horizontal = obs.width
            vertical = obs.length

            for x in range(origin[0], origin[0] + horizontal + grid_spacing, grid_spacing):
                for y in range(origin[1], origin[1] + vertical + grid_spacing, grid_spacing):
                    grid[y * resolution, x * resolution] = 1

        # triangle obstacle
        elif expand_obs.shape == "triangle":

            # draw a bounding box around the triangle
            x_min = np.min(np.array([x1, x2, x3]))
            x_max = np.max(np.array([x1, x2, x3]))
            y_min = np.min(np.array([y1, y2, y3]))
            y_max = np.max(np.array([y1, y2, y3]))

            for x in range(x_min, x_max + grid_spacing, grid_spacing):
                for y in range(y_min, y_max + grid_spacing, grid_spacing):
                    if is_inside_polygon(np.array([x,y]), expand_obs.verts) == True:
                        grid[y * resolution, x * resolution] = 1

    return grid






