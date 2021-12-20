'''
Obstacle class

'''
from obstacle_class.circleObstacle import circleObstacle
from obstacle_class.rectangleObstacle import rectangleObstacle
from obstacle_class.triangleObstacle import triangleObstacle

class Obstacle:
    def __init__(self, position, shape_data):
        self.shape_data = shape_data
        self.position = position

    def init_obs(self):
        if (self.shape_data["shape"] == "circle"):
            return circleObstacle(self.position, self.shape_data["radius"])
        elif (self.shape_data["shape"] == "rectangle"):
            return rectangleObstacle(self.position, self.shape_data["length"], self.shape_data["width"])
        elif (self.shape_data["shape"] == "triangle"):
            return triangleObstacle(self.position)