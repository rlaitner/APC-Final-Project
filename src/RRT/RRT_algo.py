from obstacle import Obstacle
#import vehicle_class
from obstacle_collision_detection import *
from point_obstacle_collision_detection import *
import numpy as np
from typing import List, Tuple

def conf_free(q, obstacles):

    """
    Check to see if a configuration is in the free space.
    
    This function checks if the configuration q lies outside of all the obstacles in the configuration space.
    
    q: An np.ndarray of shape (2,) representing a random location.

    obstacles: A list of obstacles. A circle obstacle is represented by a center and radius in the form of a tuple: 
    [np.ndarray, float]. A rectangle obstacle is represented by an origin point, length, and width in the form of a tuple:
    [np.ndarray, float, float]. A triangle obstacle is represented by three vertices in the form a tuple: 
    [np.ndarray, np.ndarray. np.ndarray].

    return: True if the configuration is in the free space, i.e. it lies outside of all the obstacles in `obstacles`. 
    Otherwise return False.
    """

    for o in obstacles:
        # If obstacle is a circle
        if o.shape == "circle":
            collision = is_inside_circle(q, o)

            if collision:
                return False
            
        # If obstacle is a polygon
        else:
            collision = is_inside_polygon(q, o.verts)
            if collision:
                return False

    return True

def edge_free(edge, obstacles):
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

def random_conf(width, height):
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

def random_free_conf(width, height, obstacles):
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

def extend(origin: np.ndarray, target: np.ndarray, step_size: float=0.2) -> np.ndarray:
    """
    Extends the RRT at most a fixed distance toward the target configuration.
    
    Given a configuration in the RRT graph `origin`, this function returns a new configuration that takes a
    step of at most `step_size` towards the `target` configuration. That is, if the L2 distance between `origin`
    and `target` is less than `step_size`, return `target`. Otherwise, return the configuration on the line
    segment between `origin` and `target` that is `step_size` distance away from `origin`.
    
    @param origin: A vertex in the RRT graph to be extended.
    @param target: The vertex that is being extended towards.
    @param step_size: The maximum allowed distance the returned vertex can be from `origin`.
    
    @return: A new configuration that is as close to `target` as possible without being more than
            `step_size` away from `origin`.
    """
   
    # Check Euclidean distance and move in that direction based on step size 
    dist = np.sqrt((origin[0]-target[0])**2 + (origin[1] - target[1])**2)
    if dist < step_size:
        return target 
    else: 
        u = (target-origin)
        u_norm = u/np.linalg.norm(u)
        new_conf = origin + (step_size * u_norm)
    
    return new_conf
