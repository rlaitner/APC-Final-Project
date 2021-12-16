import numpy as np
import obstacles

# Following three functions are to detect configuration-obstacle collisions

def circle_conf_collision(conf, obstacle):
    """

    Checks to see if the configuration is in collision with a circle obstacle.

    conf: The configuration being tested.

    obstacle: The circle obstacle.

    return: True if the configuration is in collision with the circle and false
    if not.
    """

    # Store circle center (x,y) value 
    center = obstacle[0]
    center_x = center[0]
    center_y = center[1]
            
    # Store circle radius 
    r = obstacle[1]
        
    # Set bounds of y for circle at current point 
    y_max = center_y + np.sqrt(np.abs(r**2 - (x-center_x)**2))
    y_min = center_y - np.sqrt(np.abs(r**2 - (x-center_x)**2))
        
    # Set bounds of x for circle at current point 
    x_max = center_x + np.sqrt(np.abs(r**2 - (y-center_y)**2))
    x_min = center_x - np.sqrt(np.abs(r**2 - (y-center_y)**2))
        
    # Check bounds of current y 
    if ((y >= y_min) and (y <= y_max) and (x >= x_min) and (x <= x_max)):
        return False
    else:
        return True

def rectangle_conf_collision(conf, obstacle):
    """

    Checks to see if the configuration is in collision with a rectangle obstacle.

    conf: The configuration being tested.

    obstacle: The rectangle obstacle.

    return: True if the configuration is in collision with the rectangle and false
    if not.
    """
    
    # Stores points of configuration
    x = conf[0]
    y = conf[1]

    # Stores vertices of rectangle
    x1 = obstacle.vertices[0]
    x2 = obstacle.vertices[3]
    y1 = obstacle.vertices[1]
    y2 = obstacle.vertices[2]
            
    # Checks if configuration is within the bounds of the rectangle
    if ((x > x1) and (x < x2) and (y > y1) and (y < y2)):
        return False
    else:
        return True

def triangle_conf_collision(conf, obstacle):
    """

    Checks to see if the configuration is in collision with a triangle obstacle.

    conf: The configuration being tested.

    obstacle: The triangle obstacle.

    return: True if the configuration is in collision with the triangle and false
    if not.
    """

    # Stores points of triangle
    ax, ay = obstacle[0]
    bx, by = obstacle[1]
    cx, cy = obstacle[2]
            
    # Line 1
    side_1 = (x - bx) * (ay - by) - (ax - bx) * (y - by)
            
    # Line 2
    side_2 = (x - cx) * (by - cy) - (bx - cx) * (y - cy)
            
    # Line 3
    side_3 = (x - ax) * (cy - ay) - (cx - ax) * (y - ay)
            
    inside = (side_1 < 0.0) == (side_2 < 0.0) == (side_3 < 0.0)
            
    if inside == True:
        return False
    else:
        return True

# Following four functions are for line-circle and line-polygon collisions

def edge_circle_collision(edge, obstacle):
    """
    Checks if a edge/line will interesect with a circle.

    edge: A tuple containing the two segment endpoints.
    obstacles: A list of obstacles as described in `config_free`.
    @return: True if the edge is in the free space. Otherwise return False.
    """

    o = edge[0]
    f = edge[1]
    
    u = (f-o)
    u_norm = u/np.linalg.norm(u)
    
    for i in range(0, len(obstacles)):
        # Store current obstacle
        curr_obstacle = obstacles[i]
        
        # Store circle center (x,y) value 
        c = curr_obstacle[0]    
        # Store circle radius 
        r = curr_obstacle[1]
        
        # Solve for nabla
        nabla = (np.dot(u_norm, (o-c)))**2 - (np.dot(o-c, o-c) - r**2)
        
        if (nabla >= 0):
            return False

    return True 
    
def onSegment(p, q, r):
    """
    Checks to see if given three collinear points p, q, r, the function checks if
    point q lies on line segment 'pr'.

    p: First vertex of triangle.

    q: Second vertex of triangle.

    r: Third vertex of triangle.

    return: True if the point is in collision with the line.
    """
    if ( (q[0] <= max(p[0], r[0])) and (q[0] >= min(p[0], r[0])) and (q[1] <= max(p[1], r[1])) and (q[1]] >= min(p[1], r[1]))):
        return True
    else:
        return False

def orientation(p, q, r):
    """
    To find the orientation of an ordered triplet (p, q, r).

    p: First endpoint of line.

    q: Point being tested if it is on the line formed by 'p' and 'r'.

    r: Second end point of line.

    returns: 
    0 : Collinear points
    1 : Clockwise points
    2 : Counterclockwise
    """
     
    val = (float(q.y - p.y) * (r.x - q.x)) - (float(q.x - p.x) * (r.y - q.y))
    if (val > 0):
         
        # Clockwise orientation
        return 1

    elif (val < 0):
         
        # Counterclockwise orientation
        return 2
    else:
         
        # Collinear orientation
        return 0


def doCollide(p1,q1,p2,q2):
    """
    Checks if two lines 'p1q1' and 'p2q2' interesect.
    
    p1: First end point of the first line.
    q1: Second end point of the first line.
    p2: First end point of the second line.
    q2: Second end point of the second line.

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
    if ((o1 == 0) and onSegment(p1, p2, q1)):
        return True
 
    # p1 , q1 and q2 are collinear and q2 lies on segment p1q1
    if ((o2 == 0) and onSegment(p1, q2, q1)):
        return True
 
    # p2 , q2 and p1 are collinear and p1 lies on segment p2q2
    if ((o3 == 0) and onSegment(p2, p1, q2)):
        return True
 
    # p2 , q2 and q1 are collinear and q1 lies on segment p2q2
    if ((o4 == 0) and onSegment(p2, q1, q2)):
        return True
 
    # If none of the cases
    return False

# Following four functions are for polygon-polygon collisions

def edges_of(vertices):
    """
    Return the vectors for the edges of the polygon p.
    p is a polygon.
    """
    edges = []
    N = len(vertices)

    for i in range(N):
        edge = vertices[(i + 1)%N] - vertices[i]
        edges.append(edge)

    return edges

def orthogonal(v):
    """
    Return a 90 degree clockwise rotation of the vector v.
    """
    return np.array([-v[1], v[0]])

def is_separating_axis(o, p1, p2):
    """
    Return True and the push vector if o is a separating axis of p1 and p2.
    Otherwise, return False and None.
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

def centers_displacement(p1, p2):
    """
    Return the displacement between the geometric center of p1 and p2.
    """
    # Geometric center
    c1 = np.mean(np.array(p1), axis=0)
    c2 = np.mean(np.array(p2), axis=0)
    return c2 - c1
    

def polygon_collision(p1, p2):
    '''
    Return True if the shapes collide. Otherwise, return False.

    p1 and p2 are lists of ordered pairs, the vertices of the polygons in the
    counterclockwise direction.
    '''

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
