import numpy as np
import math

def on_segment(p, q, r):
    """
    Checks to see if given three collinear points p, q, r, the function checks if
    point q lies on line segment 'pr'.

    p: First endpoint of line 'pr' described by a tuple.

    q: Point being tested described by a tuple.

    r: Second endpoint of line 'pr' described by a tuple.

    return: True if the point is in collision with tuple.
    """
    
    if ((q[0] <= max(p[0], r[0])) &
        (q[0] >= min(p[0], r[0])) &
        (q[1] <= max(p[1], r[1])) &
        (q[1] >= min(p[1], r[1]))):
        return True

    return False

def orientation(p, q, r):
    """
    Finds the orientation of an ordered set of vertices(p, q, r).

    p: First vertex represented as a tuple.

    q: Second vertex represented as a tuple.

    r: Third vertex represented as a tuple.

    returns: 
    0 : Collinear points
    1 : Clockwise points
    2 : Counterclockwise
    """

    val = ((q[1] - p[1]) *(r[0] - q[0])) - ((q[0] - p[0]) * (r[1] - q[1]))

    if val == 0:
        #Collinear
        return 0
    if val > 0:
        # Clock
        return 1
    else:
        # Counterclock
        return 2

def line_intersect(p1, q1, p2, q2):
    """
    Checks if two lines 'p1q1' and 'p2q2' interesect.
    
    p1: First end point of the first line represented as an np.ndarray.

    q1: Second end point of the first line represented as an np.ndarray.

    p2: First end point of the second line represented as an np.ndarray.

    q2: Second end point of the second line represented as an np.ndarray.

    returns: True if the two lines intersect and false if they don't.
    """
     
    # Find the 4 orientations required for
    # the general and special cases
    o1 = orientation(p1, q1, p2)
    o2 = orientation(p1, q1, q2)
    o3 = orientation(p2, q2, p1)
    o4 = orientation(p2, q2, q1)
 
    # General case
    if ((o1 != o2) and (o3 != o4)):
        return True   
        
    # Special Cases
 
    # p1 , q1 and p2 are collinear and p2 lies on segment p1q1
    if ((o1 == 0) and on_segment(p1, p2, q1)):
        return True
 
    # p1 , q1 and q2 are collinear and q2 lies on segment p1q1
    if ((o2 == 0) and on_segment(p1, q2, q1)):
        return True
 
    # p2 , q2 and p1 are collinear and p1 lies on segment p2q2
    if ((o3 == 0) and on_segment(p2, p1, q2)):
        return True
 
    # p2 , q2 and q1 are collinear and q1 lies on segment p2q2
    if ((o4 == 0) and on_segment(p2, q1, q2)):
        return True
 
    # If none of the cases
    return False

def line_circle_intersect(edge, circle_obstacle):
    """
    Checks whether or not an edge or line intersects with a circle.
    
    edge: A tuple containing the two segment endpoints, each represented by an np.ndarray.
    
    obstacle: Represents the circle obstacle object.
    
    return: True if the edge/line intersects with the circle obstacle and False otherwise.
    """

    o = edge[0]
    f = edge[1]
    
    u = (f-o)
    u_norm = u/np.linalg.norm(u)
            
    # Store circle center (x,y) value 
    c = circle_obstacle.position
    
    # Store circle radius 
    r = circle_obstacle.radius
        
    # Solve for nabla
    nabla = (np.dot(u_norm, (o-c)))**2 - (np.dot(o-c, o-c)**2 - r**2)
        
    if (nabla >= 0):
        return True
    
    return False
    
def euc_distance(vertex, circle_obstacle):
    x = vertex[0] - circle_obstacle.position[0]
    y = vertex[1] - circle_obstacle.position[1]
    
    dist = ((x ** 2) + (y ** 2)) ** 0.5
    
    return dist