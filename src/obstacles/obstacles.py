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
<<<<<<< HEAD
        
        # Vertices that form the rectangle
        self.vertices = [[origin[0], origin[1]],
                        [origin[0], origin[1] + length],
                        [origin[0] + width, origin[1] + length],
                        [origin[0] + width, origin[1]]]
        
=======

        # Lines that form the rectangle
        self.lines = [[(origin[0], origin[1]), (origin[0] + width, origin[1])],
                      [(origin[0], origin[1]), (origin[0], origin[1] + length)],
                      [(origin[0], origin[1] + length), (origin[0] + width, origin[1] + length)],
                      [(origin[0] + width, origin[1]), (origin[0] + width, origin[1] + length)]]


>>>>>>> 40a624cf49bcd696ee2448bccaeb99ef8ceaf50d
class triangleObstacle():

    # Class for triangle obstacles
    def __init__(self, vertices):
        # List of vertices that belong to the triangle object
<<<<<<< HEAD
        self.vertices = vertices
=======
        self.vertices = vertices

        # Lines that form the triangle
        self.lines = [[(vertices[0][0], vertices[0][1]), (vertices[1][0], vertices[1][1])],
                      [(vertices[0][0], vertices[0][1]), (vertices[2][0], vertices[2][1])],
                      [(vertices[1][0], vertices[1][1]), (vertices[2][0], vertices[2][1])]]
>>>>>>> 40a624cf49bcd696ee2448bccaeb99ef8ceaf50d
