import copy


def mesh(x_env, y_env, grid_spacing, obstacles, vehicle):
    """
    Discretize the obstacles in the environment
    """
    grid = np.zeros((y_env / grid_spacing, x_env / grid_spacing))

    for obs in obstacles:
        ################

        expand_obs = expanded_obstacle(vehicle, obs)

        if expand_obs.shape == "circle":

            center = obs.center
            x_c = center[0]
            y_c = center[1]
            r = obs.radius

            for x in range(x_c - r, x_c + r + grid_spacing, grid_spacing):
                for y in range(y_c - r, y_c + r + grid_spacing, grid_spacing):
                    if is_inside_circle(np.array([x,y]), circle_obstacle) == True:
                        grid[y / grid_spacing, x / grid_spacing] = 1


        # If obstacle is a rectangle
        elif expand_obs.shape == "rectangle":

            origin = obs.origin
            horizontal = obs.width
            vertical = obs.length

            for x in range(origin[0], origin[0] + horizontal + grid_spacing, grid_spacing):
                for y in range(origin[1], origin[1] + vertical + grid_spacing, grid_spacing):
                    grid[y / grid_spacing, x / grid_spacing] = 1

        # triangle obstacle
        elif expand_obs.shape == "triangle":

            # draw a bounding box around the triangle
            x_min = np.min(np.array([x1, x2, x3]))
            x_max = np.max(np.array([x1, x2, x3]))
            y_min = np.min(np.array([y1, y2, y3]))
            y_max = np.max(np.array([y1, y2, y3]))

            for x in range(x_min, x_max + grid_spacing, grid_spacing):
                for y in range(y_min, y_max + grid_spacing, grid_spacing):
                    if is_inside_polygon(np.array([x,y]), expands_obs.verts) == True:
                        grid[y / grid_spacing, x / grid_spacing] = 1


            """
            #################################

            # fetch vertices
            x1, y2 = obs[0]
            x2, y2 = obs[1]
            x3, y3 = obs[2]

            # draw a bounding box around the triangle
            x_min = np.min(np.array([x1, x2, x3]))
            x_max = np.max(np.array([x1, x2, x3]))
            y_min = np.min(np.array([y1, y2, y3]))
            y_max = np.max(np.array([y1, y2, y3]))

            for x in range(x_min, x_max + grid_spacing, grid_spacing):
                for y in range(y_min, y_max + grid_spacing, grid_spacing):

                    # computation of barycentric coordinates
                    denom = ((y2 - y3) * (x1 - x3) + (x3 - x2) * (y1 - y3))
                    a = ((y2 - y3) * (x - x3) + (x3 - x2) * (y - y3)) / denom
                    b = ((y3 - y1) * (x - x3) + (x1 - x3) * (y - y3)) / denom
                    c = 1 - a - b

                    # determine if the point is inside (including boundary) of the triangle obstacle
                    if a >= 0 and a <= 1 and b >= 0 and b >= 1 and c >= 0 and c <= 1:
                        grid[y / grid_spacing, x / grid_spacing] = 1

            """
    return grid






