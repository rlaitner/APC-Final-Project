import numpy as np
import math
from RRT.polygon_functions import *
from RRT.point_obstacle_collision_detection import *
from typing import List, Tuple

def edge_obstacle_collision(edge, obstacles):
    """
    Checks if an edge/line will interesect with an obstacle.

    edge: A tuple containing the two segment endpoints, each represented by an np.ndarray.
    obstacles: A list of obstacles.

    return: True if the edge does collide with an obstacle and False otherwise.
    """
    
    for o in obstacles:
        
        # If the obstacle is a circle
        if o.shape == "circle":
            intersect = line_circle_intersect(edge, o)
            
            if intersect:
                return True
            
        # If the obstacle is a polygon
        else:
            for l in o.lines:
                intersect = line_intersect(edge[0], edge[1], l[0], l[1])
                
                if intersect:
                    return True

    return False

# Following two functions are for circle-circle and circle-polygon collisions

def circle_circle_collision(circle1, circle2):
    """
    Checks if a circle vehicle is in collision with a circle obstacle.

    circle1: Circle that represents the UAV vehicle and is configured as a (2, ) np.ndarray.
    circle2: Circle that represents the circle obstacle and is configured as a (2, ) np.ndarray.

    return: Returns True if the two circles are in collision and False otherwise.
    """
    
    radiiDiff = (circle1.size - circle2.size) ** 2
    radiiSum = (circle1.size + circle2.size) ** 2
    positionDiff = ((circle1.position[0] - circle2.position[0]) ** 2) + ((circle1.position[1] - circle2.position[1]) ** 2)
                
    # Compare radii; if expression is satisfied, that means the circles intersect
    if radiiDiff <= positionDiff and positionDiff <= radiiSum:
        return True
    else:
        return False

def circle_polygon_collision(circle, obstacle):
    """
    Checks if a circle and polygon are in collision by checking if there are any circle-line collisions,
    if the center of the circle is inside the polygon, and if the distances between the circle and the vertices
    of the polygon are greater than or less than the radius of the circle.

    circle: Circle vehicle/obstacle.
    obstacle: Polygon obstacle/vehicle.

    return: True if the circle and polygon are in collision, False otherwise.
    """

    # Checks if any of the polygon's edges intersect w/ the circle
    for l in obstacle.lines:
        intersect = line_circle_intersect(l, circle)
        if intersect:
            return True
    
    # Checks if the center of the circle is within the polygon
    inside_polygon = is_inside_polygon(circle.position, obstacle.verts)
    if inside_polygon:
        return True
    
    distance = math.inf
    
    # Calculates the distance between the vertices of the polygon and the circle's center
    for v in obstacle.verts:
        if euc_distance(v, circle) < distance:
            distance = euc_distance(v, circle)
    
    if distance > circle.size:
        return False
    else:
        return True

# Following four functions are for polygon-polygon collisions

def edges_of(vertices):
    """
    Finds the edges formed by the vertices of the polygon.

    vertices: Vertices of a polygon in the form of a (n, 2) np.ndarray.
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
    Returns a 90 degree clockwise rotation of the vector v.

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

    return: True if 'o' is a separating axis of p1 and p2 and False if otherwise.
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

def free_vehicle(vehicle, new_position, obstacles):
    """
    Checks when a vehicle gets initialized in the environment, whether or not it is in collision with an obstacle.

    vehicle: Vehicle object.
    new_position: Location of testing whether or not the vehicle can exist without colliding with other obstacles.
    obstacles: List of obstacle objects.

    returns: True if the vehicle is not in collision with an obstacle and False otherwise.
    """
    
    vehicle.position = new_position
    for o in obstacles:
        
        # If the vehicle is a circle/UAV
        if vehicle.shape == "circle":
            
            # Checks for circle obstacle collisions
            if o.shape == "circle":
                circle_collision = circle_circle_collision(vehicle, o)
                
                if circle_collision:
                    return False

            # Checks for polygon obstacle collisions
            else:
                p_collision = circle_polygon_collision(vehicle, o)
            
                if p_collision:
                    return False

        # If the vehicle is rectangle
        else:

            # Checks for circle obstacle collisions
            if o.shape == "circle":
                c_p_collision = circle_polygon_collision(o, vehicle)
                
                if c_p_collision:
                    return False
            
            # Checks for polygon obstacle collisions
            else:
                collision = polygon_collision(vehicle.verts, o.verts)
                
                if collision:
                    return False
    return True