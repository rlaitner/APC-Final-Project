import obstacles
import vehicle_class
import collisionDetection
import numpy as np    

def free_conf(q: Tuple[np.ndarray, float], obstacles: List[Tuple[np.ndarray, float]]) -> bool:

    """
    Check to see if a configuration is in the free space.
    
    This function checks if the configuration q lies outside of all the obstacles in the connfiguration space.
    
    @param q: An np.ndarray describing a shape representing a random point
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