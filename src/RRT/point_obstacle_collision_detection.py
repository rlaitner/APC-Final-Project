import numpy as np
from polygon_functions import *
INT_MAX = 10000

def is_inside_circle(conf, circle_obstacle):
    """
    Checks to see if the configuration is in collision with a circle obstacle.

    conf: The location of the point being tested represented as an np.ndarray
    of shape (2,).
    circle_obstacle: The circle obstacle being tested.

    return: True if the configuration is in collision with the circle and False if not.
    """
    
    # Store the points that represent the randomly chosen point conf
    x = conf[0]
    y = conf[1]

    # Store circle center (x,y) value
    center = circle_obstacle.position
    center_x = center[0]
    center_y = center[1]
            
    # Store circle radius 
    r = circle_obstacle.size
        
    # Set bounds of y for circle at current point 
    y_max = center_y + np.sqrt(np.abs(r**2 - (x-center_x)**2))
    y_min = center_y - np.sqrt(np.abs(r**2 - (x-center_x)**2))
        
    # Set bounds of x for circle at current point 
    x_max = center_x + np.sqrt(np.abs(r**2 - (y-center_y)**2))
    x_min = center_x - np.sqrt(np.abs(r**2 - (y-center_y)**2))

    # Check bounds of circle
    # If point is within bounds of circle, then there is a collision and return True
    if ((y >= y_min) and (y <= y_max) and (x >= x_min) and (x <= x_max)):
        return True

    else:
        return False

def is_inside_polygon(p, points):
    """
    Function checks whether or not point 'p' is within the polygon outlined by 
    the set of vertices 'points'.
    
    p: The location of the point being tested represented as an np.ndarray of shape (2,).
    
    points: Set of vertices that represents the polygon represented as a list of tuples.
    
    returns: Returns true if the point lies within the polygon and False otherwise.
    """
    
    n = len(points)
    
    # There must be at least 3 vertices
    # in polygon
    if n < 3:
        return False

    # Create a point for line segment
    # from p to infinite
    extreme = (INT_MAX, p[1])
    count = i = 0
    
    while True:
        next = (i + 1) % n

        # Check if the line segment from 'p' to
        # 'extreme' intersects with the line
        # segment from 'polygon[i]' to 'polygon[next]'
        if (line_intersect(points[i], points[next], p, extreme)):
            
            # If the point 'p' is collinear with line
            # segment 'i-next', then check if it lies#
            # on segment. If it lies, return true, otherwise false
            if orientation(points[i], p, points[next]) == 0:
                return on_segment(points[i], p, points[next])
                
            count += 1

        i = next

        if (i == 0):
            break

    # Return true if count is odd, false otherwise
    return (count % 2 == 1)