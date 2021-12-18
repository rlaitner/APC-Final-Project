'''
triangleObstacle subclass
'''

import numpy as np
from obstacle import Obstacle
from matplotlib import patches as patches

    
class triangleObstacle(Obstacle):
    
    # Class for triangle obstacles
    def __init__(self, position):
        
        # vertices
        super().__init__(position)
        self.shape = "triangle"
        # Lines that form the triangle
        self.verts = (self.position[0], self.position[1], 
                     self.position[2])

        self.lines = np.array([[(position[0][0], position[0][1]), (position[1][0], position[1][1])],
                      [(position[0][0], position[0][1]), (position[2][0], position[2][1])],
                      [(position[1][0], position[1][1]), (position[2][0], position[2][1])]])
    
    
    def render_obstacle(self):
        triangle = patches.Polygon(self.verts, color="brown")
        return triangle