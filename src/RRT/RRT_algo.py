import obstacles
import vehicle_class
import obstacle_collision_detection
import numpy as np

def conf_free(q: Tuple[np.ndarray, float], obstacles) -> bool:

    """
    Check to see if a configuration is in the free space.
    
    This function checks if the configuration q lies outside of all the obstacles in the connfiguration space.
    
    q: An np.ndarray describing a shape representing a random position.

    obstacles: A list of obstacles. A circle obstacle is a tuple of the form (center, radius) representing a circle,
    a rectangle obstacle is a tuple of the form (center, length, width), and a triangle obstacle is a tuple of the 
    form (vertices).

    return: True if the configuration is in the free space, i.e. it lies outside of all the obstacles in `obstacles`. 
    Otherwise return False.
    """

    for i in range(0, len(obstacles)):
        
        # If obstacle is a circle
        if len(obstacles[i]) == 2:
            collision = circle_conf_collision(q, obstacles[i])

            if collision:
                return False

        # If obstacle is a rectangle
            collision = rectangle_conf_collision(q, obstacles[i])

            if collision:
                return False

        # If obstacle is a triangle
        else:
            triangle_conf_collision(q, obstacles[i])

            if collision:
                return False
        
    return True

def edge_free(edge: Tuple[np.ndarray, np.ndarray], obstacles: List[Tuple[np.ndarray, float]]) -> bool:
    """
    Check if a graph edge is in the free space.
    
    This function checks if a graph edge, i.e. a line segment specified as two end points, lies entirely outside of
    every obstacle in the configuration space.
    
    edge: A tuple containing the two segment endpoints.

    obstacles: A list of obstacles as described.

    return: True if the edge is in the free space, i.e. it lies entirely outside of all the obstacles in `obstacles`. 
    Otherwise return False.
    """
    
    for i in range(0, len(obstacles)):
        
        # If the obstacle is a circle
        if len(curr_obstacle) == 2:
            collision = edge_circle_collision(edge, obstacles[i])
            
            if collision:
                return False
        
        # Obstacle is either a rectangle or a triangle
        else:
        
            # Iterates through all lines of each polygon 
            for k in obstacles[i].lines:
                new_p2 = obstacles[i].lines[k][0]
                new_q2 = obstacles[i].lines[k][1]
                collision = doIntersect(edge[0], edge[1], new_p2, new_q2)
                
                if collision:
                    return False
        
    return True

def random_conf(width: float, height: float) -> np.ndarray:
    """
    Sample a random configuration from the configuration space.
    
    This function draws a uniformly random configuration from the configuration space rectangle. The configuration 
    does not necessarily have to reside in the free space.
    
    width: The configuration space width.

    height: The configuration space height.

    return: A random configuration uniformily distributed across the configuration space.
    """
    
    # Randomly sample x and y values 
    x_val = width * np.random.rand()
    y_val = height * np.random.rand()
    
    conf = np.zeros(2)
    conf[0] = x_val
    conf[1] = y_val

    return conf

def random_free_conf(width: float, height: float, obstacles: List[Tuple[np.ndarray, float]]) -> np.ndarray:
    """
    Sample a random configuration from the free space.
    
    This function draws a uniformly random configuration from the configuration space
    rectangle that lies in the free space.
    
    width: The configuration space width.

    height: The configuration space height.

    obstacles: The list of configuration space obstacles as defined in `edge_free` and `conf_free`.

    return: A random configuration uniformily distributed across the configuration space.
    
    """
    
    # Check if in free space 
    free_flag = True 
    while free_flag:
        
        new_conf = random_conf(width, height)
        free = conf_free(new_conf, obstacles)
        
        if free:
            free_flag = False
            conf_result = new_conf
            
    return conf_result

def nearest_vertex(conf: np.ndarray, vertices: np.ndarray) -> int:
    """
    Finds the nearest vertex to conf in the set of vertices.
    
    This function searches through the set of vertices and finds the one that is closest to 
    conf using the L2 norm (Euclidean distance).
    
    conf: The configuration we are trying to find the closest vertex to.

    vertices: The set of vertices represented as an np.array with shape (n, 2). Each row represents
    a vertex.

    return: The index (i.e. row of `vertices`) of the vertex that is closest to `conf`.
    
    """
    
    min_dist = np.Inf
    
    # Calc Euclidean distance and store min
    for i in range(0, vertices.shape[0]):
        dist = np.sqrt((conf[0]-vertices[i][0])**2 + (conf[1] - vertices[i][1])**2)
        
        if (dist < min):
            min_dist = dist 
            index = i
    
    return index

    # Need to add extend() function
