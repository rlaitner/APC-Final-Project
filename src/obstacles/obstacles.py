class circleObstacle():
    
    # Class for circle obstacles
    def __init__(self, center, radius):
        # Center of circle object
        self.center = center        
        
        # Radius of circle object
        self.radius = radius

class rectangleObstacle():

    # Class for rectangle obstacles
    def __init__(self, origin, length, width):
        # Starting point of rectangle of which length and width are referenced to
        self.origin = origin
        
        # Length of rectangle object
        self.length = length
        
        # Width of rectangle object
        self.width = width
        
        # Vertices that form the rectangle
        self.vertices = [[origin[0], origin[1]],
                        [origin[0], origin[1] + length],
                        [origin[0] + width, origin[1] + length],
                        [origin[0] + width, origin[1]]]
        
class triangleObstacle():

    # Class for triangle obstacles
    def __init__(self, vertices):
        # List of vertices that belong to the triangle object
        self.vertices = vertices