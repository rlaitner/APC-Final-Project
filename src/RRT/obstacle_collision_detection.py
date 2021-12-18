import numpy as np
import obstacle
import math
from polygon_functions import *
from point_obstacle_collision_detection import *
from typing import List, Tuple

def edge_obstacle_collision(edge, obstacle):
    """
    Checks if an edge/line will interesect with a circle.

    edge: A tuple containing the two segment endpoints, each represented by an np.ndarray.

    obstacle: A list of obstacles as described in `conf_free`.

    @return: True if the edge does collide with an obstacle and False otherwise.
    """
    
    for o in obstacle:
        if o.shape == "circle":
            intersect = line_circle_intersect(edge, o)
            
            if intersect:
                return True
            
        else:
            for l in o.lines:
                intersect = line_intersect(edge[0], edge[1], l[0], l[1])
                
                if intersect:
                    return True

    return False

# Following functions are for circle-circle and circle-polygon collisions

def circle_circle_collision(circle1, circle2):
    """
    Checks if a circle vehicle is in collision with a circle obstacle.

    circle1: The circle that represents the vehicle and is configured as a (2, ) np.ndarray.

    circle2: The circle that represnts the circle obstacle and is configured as a (2, ) np.ndarray.

    return: Returns True if the two circles are in collision and False otherwise.
    """
    
    radiiDiff = (circle1.radius - circle2.radius) ** 2
    radiiSum = (circle1.radius + circle2.radius) ** 2
    positionDiff = ((circle1.position[0] - circle2.position[0]) ** 2) + ((circle1.position[1] - circle2.position[1]) ** 2)
                
    # Compare radii
    if radiiDiff <= positionDiff and positionDiff <= radiiSum:
        return True
    else:
        return False

def circle_polygon_collision(circle, obstacle):

    for l in obstacle.lines:
        print(obstacle.lines)
        intersect = line_circle_intersect(l, circle)
        print(intersect)
        
        if intersect:
            print('hi23')
            return True
    
    inside_polygon = is_inside_polygon(circle.position, obstacle.verts)
    if inside_polygon:
        print('hi24')
        return True
    
    distance = 0
    
    for v in obstacle.verts:
        if abs(math.dist(circle.position, v) > distance):
            distance = abs(math.dist(circle.position, v))
            print('hi')
    
    if distance > circle.radius:
        return False
    else:
        return True

# Following four functions are for polygon-polygon collisions
def edges_of(vertices):
    """
    Finds the edges formed by the vertices of the polygon.

    vertices: Vertices of a polygon of form of a (n, 2) np.ndarray.

    returns: Vectors for the edges of the polygon p.
    """

    edges = []
    N = len(vertices)

    for i in range(N):
        edge = vertices[(i + 1)%N] - vertices[i]
        edges.append(edge)

    return edges

def orthogonal(v: np.ndarray) -> np.ndarray:
    """
    Return a 90 degree clockwise rotation of the vector v.

    v: Vector 'v' of form np.ndarray.

    return: A 90 degree rotated version of vector 'v' of form np.ndarray.
    """
    
    return np.array([-v[1], v[0]])

def is_separating_axis(o: np.ndarray, p1: List[np.ndarray], p2: List[np.ndarray]) -> bool:
    """
    Checks to see if 'o' is a separating axis of p1 and p2.

    o: Separating axis represented by an np.ndarray.

    p1: List of np.ndarrays (that each represent a vertex) that define the polygon p1.

    p2: List of np.ndarrays (that each represent a vertex) that define the polygon p2.

    return: True if 'o' is a separating axis of p1 and p2 and False if otherwise
    """

    min1, max1 = float('+inf'), float('-inf')
    min2, max2 = float('+inf'), float('-inf')

    for v in p1:
        projection = np.dot(v, o)

        min1 = min(min1, projection)
        max1 = max(max1, projection)

    for v in p2:
        projection = np.dot(v, o)

        min2 = min(min2, projection)
        max2 = max(max2, projection)

    if max1 >= min2 and max2 >= min1:
        d = min(max2 - min1, max1 - min2)

        return False
    else:
        return True

def centers_displacement(p1: np.ndarray, p2: np.ndarray) -> float:
    """
    Return the displacement between the geometric center of p1 and p2.
    """

    # Geometric center
    c1 = np.mean(np.array(p1), axis=0)
    c2 = np.mean(np.array(p2), axis=0)

    return c2 - c1
    
def polygon_collision(p1: List[np.ndarray], p2: List[np.ndarray]) -> bool:
    """
    Checks whether or not two polygons collide.

    p1: List of np.ndarrays (that each represent a vertex) that define the polygon p1.

    p2: List of np.ndarrays (that each represent a vertex) that define the polygon p2.
    
    return: Returns True if the p1 and p2 collide and False otherwise.
    """

    p1 = [np.array(v) for v in p1]
    p2 = [np.array(v) for v in p2]

    edges = edges_of(p1)
    edges += edges_of(p2)
    orthogonals = [orthogonal(e) for e in edges]

    push_vectors = []
    for o in orthogonals:
        separates = is_separating_axis(o, p1, p2)

        if separates:
            # They do not collide
            return False

    return True
