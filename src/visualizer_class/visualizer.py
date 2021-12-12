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
            if (obstacle.shape == "rectangle"):
                x = obstacle.position[0]
                y = obstacle.position[1]
                rect = patches.Rectangle((x, y), obstacle.width, obstacle.length)
                ax.add_patch(rect)
            elif (obstacle.shape == "circle"):
                x = obstacle.position[0]
                y = obstacle.position[1]
                circ = patches.Circle((x, y), obstacle.radius)
                ax.add_patch(circ)  
            elif (obstacle.shape == "triangle"):
                xy1 = obstacle.position[0]
                xy2 = obstacle.position[1]
                xy3 = obstacle.position[2]
                triang = patches.Polygon((xy1, xy2, xy3))
                ax.add_patch(triang) 
