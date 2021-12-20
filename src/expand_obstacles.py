def expanded_obstacle(vehicle,obstacle):
    """
    Expands obstacles to account for agent geometry, allowing use of point particle motion algorithms.
    Implementation of a rough Minkowski sum scheme, assuming worst - case agent orientation.
    Thus, obstacles are oversized for conservative planning.

    Parameters
    ----------
        vehicle: a Vehicle object
        obstacle: an Obstacle object
    Returns
    -------
        expand_obs: the approximate Minkowski sum of the vehicle and obstacle
    """


    expand_obs = copy.deepcopy(obstacle)

    if vehicle.shape == "circle":
        if obstacle.shape == "circle":
            expand_obs.size = obstacle.size + vehicle.size

        elif obstacle.shape == "rectangle":
            expand_obs.length = obstacle.length + (2 * vehicle.size)
            expand_obs.width = obstacle.width + (2 * vehicle.size)

        elif obstacle.triangle == "triangle":

    # vehicle is rectangular
    else:
        diagonal = np.sqrt(vehicle.size[0]**2 + vehicle.size[1]**2)

        if obstacle.shape == "circle":
            expand_obs.size = obstacle.size + diagonal

        elif obstacle.shape == "rectangle":
            expand_obs.length = obstacle.length + (2 * diagonal)
            expand_obs.width = obstacle.width + (2 * diagonal)

        elif obstacle.triangle == "triangle":

    return expand_obs