'''
circleObstacle subclass

'''
from obstacle_class.Obstacle import Obstacle
from matplotlib import patches as patches

class circleObstacle(Obstacle):

    # Class for circle obstacles    
    def __init__(self, position, radius):
        
        # position is center of circle
        super().__init__(position)
        self.shape = "circle"
        # Radius of circle object
        self.radius = radius

    def render_obstacle(self):
        x,y = (self.position[0], self.position[1])
        circle = patches.Circle((x, y), self.radius)
        return circle