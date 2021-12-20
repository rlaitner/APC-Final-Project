'''
Obstacle class

'''
from obstacle_class.circleObstacle import circleObstacle
from obstacle_class.rectangleObstacle import rectangleObstacle
from obstacle_class.triangleObstacle import triangleObstacle

class Obstacle:
    def __init__(self, position, shape_data):

        self.position = position
        if (shape_data["shape"] == "circle"):
            return circleObstacle(self.position, shape_data["radius"])
        elif (shape_data["shape"] == "rectangle"):
            return rectangleObstacle(self.position, shape_data["length"], shape_data["width"])
        elif (shape_data["shape"] == "triangle"):
            return triangleObstacle(self.position)