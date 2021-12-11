import obstacles
import vehicle_class
import numpy as np

def avail_config(q: Tuple[np.ndarray, float], obstacles: List[Tuple[np.ndarray, float]]) -> bool:

    """
    Check if a configuration is in the free space.
    
    This function checks if the configuration q lies outside of all the obstacles in the connfiguration space.
    
    @param q: An np.ndarray of shape (2,) representing a robot configuration.
    @param obstacles: A list of obstacles. Each obstacle is a tuple of the form (center, radius) representing a circle.
    @return: True if the configuration is in the free space, i.e. it lies outside of all the circles in `obstacles`. 
             Otherwise return False.
    """

    # If the vehicle is a car or tricycle and is represented as a circle
    if len(q) == 2:
        for i in range(0, len(obstacles)):
            
            # Obstacle is a circle
            if len(obstacles[i]) == 2:
                if q[1] == obstacles[i][1]:
                    return True
                else:
                        return False

            if len(obstacles[i]):
                
            else: