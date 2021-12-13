import obstacles
import vehicle_class
import collisionDetection
import numpy as np    

def free_conf(q: Tuple[np.ndarray, float], obstacles: List[Tuple[np.ndarray, float]]) -> bool:

    """
    Check to see if a configuration is in the free space.
    
    This function checks if the configuration q lies outside of all the obstacles in the connfiguration space.
    
    @param q: An np.ndarray describing a shape representing a random po
    @param obstacles: A list of obstacles. A circle obstacle is a tuple of the form (center, radius) representing a circle,
    a rectangle obstacle is a tuple of the form (center, length, width), and a triangle obstacle is a tuple of the 
    form (vertices).
    @return: True if the configuration is in the free space, i.e. it lies outside of all the obstacles in `obstacles`. 
             Otherwise return False.
    """
    
    # Store x,y coordinates of point
    x = q[0]
    y = q[1]
    
    for i in range(0, len(obstacles)):
        
        # Store current obstacle
        curr_obstacle = obstacles[i]
        
        # If obstacle is a circle
        if len(obstacles[i]) == 2:
            
            # Store circle center (x,y) value 
            center = curr_obstacle[0]
            center_x = center[0]
            center_y = center[1]
            
            # Store circle radius 
            r = curr_obstacle[1]
        
            # Set bounds of y for circle at current point 
            y_max = center_y + np.sqrt(np.abs(r**2 - (x-center_x)**2))
            y_min = center_y - np.sqrt(np.abs(r**2 - (x-center_x)**2))
        
            # Set bounds of x for circle at current point 
            x_max = center_x + np.sqrt(np.abs(r**2 - (y-center_y)**2))
            x_min = center_x - np.sqrt(np.abs(r**2 - (y-center_y)**2))
        
            # Check bounds of current y 
            if ((y >= y_min) and (y <= y_max) and (x >= x_min) and (x <= x_max)):
                return False 
        
        # If obstacle is a rectangle
        if len(obstacles[i]) != 2 and obstacles[i][0] == tuple:
            x1 = curr_obstacle.vertices[0]
            x2 = curr_obstacle.vertices[3]
            y1 = curr_obstacle.vertices[1]
            y2 = curr_obstacle.vertices[2]
            
            if ((x > x1) and (x < x2) and (y > y1) and (y < y2)):
                return False
            
        # If obstacle is a triangle
        else:
            ax, ay = curr_obstacle[0]
            bx, by = curr_obstacle[1]
            cx, cy = curr_obstacle[2]
            
            # Line 1
            side_1 = (x - bx) * (ay - by) - (ax - bx) * (y - by)
            # Line 2
            
            side_2 = (x - cx) * (by - cy) - (bx - cx) * (y - cy)
            
            # Line 3
            side_3 = (x - ax) * (cy - ay) - (cx - ax) * (y - ay)
            
            inside = (side_1 < 0.0) == (side_2 < 0.0) == (side_3 < 0.0)
            
            if inside == True:
                return False
        
    return True

        # Given three collinear points p, q, r, the function checks if
    # point q lies on line segment 'pr'
    def onSegment(p, q, r):
        if ( (q.x <= max(p.x, r.x)) and (q.x >= min(p.x, r.x)) and
               (q.y <= max(p.y, r.y)) and (q.y >= min(p.y, r.y))):
            return True
        return False

    def orientation(p, q, r):
        # To find the orientation of an ordered triplet (p,q,r)
        # function returns the following values:
        # 0 : Collinear points
        # 1 : Clockwise points
        # 2 : Counterclockwise
     
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

    # The main function that returns true if
    # the line segment 'p1q1' and 'p2q2' intersect.
    def doIntersect(p1,q1,p2,q2):
     
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
    
    def edge_free(edge: Tuple[np.ndarray, np.ndarray], obstacles: List[Tuple[np.ndarray, float]]) -> bool:
    """
    Check if a graph edge is in the free space.
    
    This function checks if a graph edge, i.e. a line segment specified as two end points, lies entirely outside of
    every obstacle in the configuration space.
    
    @param edge: A tuple containing the two segment endpoints.
    @param obstacles: A list of obstacles as described.
    @return: True if the edge is in the free space, i.e. it lies entirely outside of all the obstacles in `obstacles`. 
             Otherwise return False.
    """
    
    o = edge[0]
    f = edge[1]
    
    u = (f-o)
    u_norm = u/np.linalg.norm(u)
    
    for i in range(0, len(obstacles)):
        curr_obstacle = obstacles[i]
        
        # If the obstacle is a circle
        if len(curr_obstacle) == 2:
            
            # Store circle center (x,y) value 
            c = curr_obstacle[0]    
            # Store circle radius 
            r = curr_obstacle[1]
        
            # Solve for nabla
            nabla = (np.dot(u_norm, (o - c)))**2 - (np.dot(o - c, o - c) - r ** 2)
        
            if (nabla >= 0):
                return False
        
        # Obstacle is either a rectangle or a triangle
        else:
            
            # Iterates through all lines of each polygon 
            for k in obstacles[i].lines:
                new_p2 = obstacles[i].lines[k][0]
                new_q2 = obstacles[i].lines[k][1]
                
                if doIntersect(o, f, new_p2, new_q2):
                    return False
        
    return True

    def random_conf(width: float, height: float) -> np.ndarray:
    """
    Sample a random configuration from the configuration space.
    
    This function draws a uniformly random configuration from the configuration space rectangle. The configuration 
    does not necessarily have to reside in the free space.
    
    @param width: The configuration space width.
    @param height: The configuration space height.
    @return: A random configuration uniformily distributed across the configuration space.
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
    
    @param width: The configuration space width.
    @param height: The configuration space height.
    @param obstacles: The list of configuration space obstacles as defined in `edge_free` and `conf_free`.
    @return: A random configuration uniformily distributed across the configuration space.
    
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