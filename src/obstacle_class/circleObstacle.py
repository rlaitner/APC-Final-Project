'''
circleObstacle subclass

'''
from obstacle_class.Obstacle import Obstacle

class circleObstacle(Obstacle):

    # Class for circle obstacles    
    def __init__(self, position, radius):
        
        # position is center of circle
        super().__init__(position)
        self.shape = "circle"
        # Radius of circle object
        self.radius = radius