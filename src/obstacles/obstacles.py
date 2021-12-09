class circleObstacle():
    
    # Class for circle obstacles
    def __init__(self, center, radius):
        self.center = center        # Center of circle object
        self.radius = radius        # Radius of circle object

class rectangleObstacle():

    # Class for rectangle obstacles
    def __init__(self, origin, length, width):
        self.origin = origin        # Starting point of rectangle of which length and width are referenced to
        self.length = length        # Length of rectangle object
        self.width = width          # Width of rectangle object

class triangleObstacle():

    # Class for triangle obstacles
    def __init__(self, vertices):
        self.vertices = vertices    # List of vertices that belong to the triangle object