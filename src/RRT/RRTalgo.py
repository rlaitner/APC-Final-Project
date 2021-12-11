import obstacles
import vehicle_class
import numpy as np

def rectangleLines(obstacle: List[Tuple[np.ndarray, float]]):
    # Creates lines of a rectangle
    lines = [[(obstacles[0][0], obstacles[0][1]), (obstacles[0][0] + obstacles[2], obstacles[0][1])], 
             [(obstacles[0][0], obstacles[0][1]), (obstacles[0][0], obstacles[0][1] + obstacles[1])],
             [(obstacles[0][0], obstacles[0][1] + obstacles[1]), (obstacles[0][0] + obstacles[2], obstacles[1] + obstacles[1])],
             [(obstacles[0] + obstacles[2], obstacles[1]), (obstacles[0] + obstacles[2], obstacles[1] + obstacles[1])]]
    
    return lines

def triangleLines(obstacle: List[Tuple[np.ndarray, float]]):
    # Creates lines of a triangle
    lines = [[(obstacles[0][0], obstacles[0][1]), (obstacles[1][0], obstacles[1][1])],
             [(obstacles[0][0], obstacles[0][1]), (obstacles[2][0], obstacles[2][1])],
             [(obstacles[1][0], obstacles[1][1]), (obstacles[2][0], obstacles[2][1])]]
    
    return lines

def avail_config(q: Tuple[np.ndarray, float], obstacles: List[Tuple[np.ndarray, float]]) -> bool:

    """
    Check if a configuration is in the free space.
    
    This function checks if the configuration q lies outside of all the obstacles in the connfiguration space.
    
    @param q: An np.ndarray of shape (2,) representing a robot configuration.
    @param obstacles: A list of obstacles. Each obstacle is a tuple of the form (center, radius) representing a circle.
    @return: True if the configuration is in the free space, i.e. it lies outside of all the circles in `obstacles`. 
             Otherwise return False.
    """

    # If the vehicle is a UAV and is represented as a circle
    if len(q) == 2:
        for i in range(0, len(obstacles)):
            
            # Obstacle is a circle
            if len(obstacles[i]) == 2:
                
                # Compare radii
                if q[1] == obstacles[i][1]:
                    return True
                else:
                    return False
            
            # Obstacle is a rectangle
            if len(obstacles[i]) != 2 and obstacles[i][0] == tuple:
                lines = rectangleLines(obstacles[i])
                for k in lines:
                    initPoint = lines[k][0]
                    endPoint = lines[k][1]
                    selectedLine = endPoint - initPoint
                    selectedLineNorm = selectedLine / np.linalg.norm(selectedLine)
                    nabla = (np.dot(selectedLineNorm, (initPoint - q[0]))) ** 2 - (np.dot(initPoint - q[0], initPoint - q[0]) - q[1] ** 2)
                    
                    # If nabla >= 0, then the vehicle is in collision with the obstacle
                    if nabla >= 0:
                        return False
                    else:
                        return True
            
            # Obstacle is a triangle
            else:
                lines = triangleLines(obstacles[i])
                for k in lines:
                    initPoint = lines[k][0]
                    endPoint = lines[k][1]
                    selectedLine = endPoint - initPoint
                    selectedLineNorm = selectedLine / np.linalg.norm(selectedLine)
                    nabla = (np.dot(selectedLineNorm, (initPoint - q[0]))) ** 2 - (np.dot(initPoint - q[0], initPoint - q[0]) - q[1] ** 2)
                    
                    # If nabla >= 0, then the vehicle is in collision with the obstacle
                    if nabla >= 0:
                        return False
                    else:
                        return True
                    
    # If the vehicle is a car or tricycle and is represented as a rectangle
    else:
        for i in range(0, len(obstacles)):
            
            # Obstacle is a circle
            if len(obstacles[i]) == 2:
                lines = rectangleLines(obstacles[i])
                for k in lines:
                    initPoint = lines[k][0]
                    endPoint = lines[k][1]
                    selectedLine = endPoint - initPoint
                    selectedLineNorm = selectedLine / np.linalg.norm(selectedLine)
                    nabla = (np.dot(selectedLineNorm, (initPoint - q[0]))) ** 2 - (np.dot(initPoint - q[0], initPoint - q[0]) - q[1] ** 2)
                    
                    # If nabla >= 0, then the vehicle is in collision with the obstacle
                    if nabla >= 0:
                        return False
                    else:
                        return True
            
            if len(obstacles[i]) != 2 and obstacles[i][0] == tuple:
                