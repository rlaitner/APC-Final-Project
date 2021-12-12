from matplotlib import pyplot as plt
from matplotlib import animation
from matplotlib import patches as patches


class Visualizer():
    
    def __init__(self, dims, obstacles, vehicle):
        (self.x, self.y) = dims
        self.obstacles = obstacles
        #self.obstacles = environment.obstacles 
        self.vehicle_shape = vehicle.type
        
    def render_environment(self):
        fig,ax = plt.subplots()  
        ax.set_xlim(0,self.x)
        ax.set_ylim(0,self.y)
        
        for obstacle in self.obstacles:
            ax.add_patch(self.generate_shape(obstacle))

  
    def generate_shape(self, obstacle):
        if (obstacle.shape == "rectangle"):
            x,y = (obstacle.position[0], obstacle.position[1])
            rectangle = patches.Rectangle((x, y), obstacle.width, obstacle.length)
            return rectangle
        elif (obstacle.shape == "circle"):
            x,y = (obstacle.position[0], obstacle.position[1])
            circle = patches.Circle((x, y), obstacle.radius)
            return circle
        elif (obstacle.shape == "triangle"):
            verts = (obstacle.position[0], obstacle.position[1], 
                     obstacle.position[2])
            triangle = patches.Polygon(verts)
            return triangle
    