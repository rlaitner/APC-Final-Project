class circleObstacle():
    
    # Class for circle obstacles
    def __init__(self, center, radius, cost):
        self.center = vertices      # Center of circle object
        self.radius = radius        # Radius of circle object
        self.cost = cost            # Cost associated with the circle object

class quadrilateralObstacle():

    # Class for quadrilateral obstacles
    def __init__(self, origin, height, width, cost):
        self.origin = origin        # Starting point of quadrilateral of which height and width are referenced to
        self.height = height        # Height of quadrilateral object
        self.width = width          # Width of quadrilateral object
        self.cost = cost            # Cost associated with the quadrilateral object

class triangleObstacle():

    # Class for triangle obstacles
    def __init__(self, vertices, cost):
        self.vertices = vertices    # List of vertices that belong to the triangle object
        self.cost = cost            # Cost associated with the triangle object