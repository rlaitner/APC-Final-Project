'''
rectangleObstacle subclass
'''

import numpy as np
from matplotlib import patches as patches


class rectangleObstacle:
    
    # Class for rectangle obstacles
    def __init__(self, position, length, width):
        
        # Starting point of rectangle of which length and width are referenced to
        self.shape = "rectangle"
        # Length of rectangle object
        self.length = length
        # Width of rectangle object
        self.width = width
        self.verts = [[position[0], position[1]],
                      [position[0], position[1] + length],
                      [position[0] + width, position[1] + length],
                      [position[0] + width, position[1]]]
                      
        # Lines that form the rectangle
        self.lines = np.array([[(position[0], position[1]), (position[0] + width, position[1])],
                      [(position[0], position[1]), (position[0], position[1] + length)],
                      [(position[0], position[1] + length), (position[0] + width, position[1] + length)],
                      [(position[0] + width, position[1]), (position[0] + width, position[1] + length)]])

    def render_obstacle(self):
        x,y = (self.position[0], self.position[1])
        rectangle = patches.Rectangle((x, y), self.width, self.length, color="brown")
        return rectangle