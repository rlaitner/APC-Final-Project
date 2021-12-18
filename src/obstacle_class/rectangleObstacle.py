'''
rectangleObstacle subclass
'''

import numpy as np
from obstacle import Obstacle
from matplotlib import patches as patches


class rectangleObstacle(Obstacle):
    
    # Class for rectangle obstacles
    def __init__(self, position, length, width):
        
        # Starting point of rectangle of which length and width are referenced to
        super().__init__(position)
        self.shape = "rectangle"
        # Length of rectangle object
        self.length = length
        # Width of rectangle object
        self.width = width
<<<<<<< HEAD
        self.verts = [[position[0], position[1]],
                      [position[0], position[1] + length],
                      [position[0] + width, position[1] + length],
                      [position[0] + width, position[1]]]
                      
=======
>>>>>>> 49f1966530fcf0afa8396091b30f4948440b0cd7
        # Lines that form the rectangle
        self.lines = np.array([[(position[0], position[1]), (position[0] + width, position[1])],
                      [(position[0], position[1]), (position[0], position[1] + length)],
                      [(position[0], position[1] + length), (position[0] + width, position[1] + length)],
                      [(position[0] + width, position[1]), (position[0] + width, position[1] + length)]])

    def render_obstacle(self):
        x,y = (self.position[0], self.position[1])
        rectangle = patches.Rectangle((x, y), self.width, self.length, color="brown")
        return rectangle