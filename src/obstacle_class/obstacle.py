'''
Obstacle class

'''
from circleObstacle import circleObstacle
from rectangleObstacle import rectangleObstacle
from triangleObstacle import triangleObstacle

class Obstacle:
    def __init__(self, position, shape_data):

        self.position = position
        if (shape_data["shape"] == "circle"):
            return circleObstacle(self.position, shape_data["radius"])
        elif (shape_data["shape"] == "rectangle"):
            return rectangleObstacle(self.position, shape_data["length"], shape_data["width"])
        elif (shape_data["shape"] == "triangle"):
            return rectangleObstacle(self.position)