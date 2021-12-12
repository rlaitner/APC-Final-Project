'''
triangleObstacle subclass

'''
from obstacle_class.Obstacle import Obstacle

class triangleObstacle(Obstacle):
    
    # Class for triangle obstacles
    def __init__(self, position):
        
        # vertices
        super().__init__(position)
        self.shape = "triangle"
        # Lines that form the triangle
        self.lines = [[(position[0][0], position[0][1]), (position[1][0], position[1][1])],
                      [(position[0][0], position[0][1]), (position[2][0], position[2][1])],
                      [(position[1][0], position[1][1]), (position[2][0], position[2][1])]]

