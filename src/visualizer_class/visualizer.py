from matplotlib import pyplot as plt
from matplotlib import animation
from matplotlib import patches as patches
from obstacle_class import Obstacle, circleObstacle, triangleObstacle, rectangleObstacle
from vehicle_class import Vehicle, Car, UAV, Tricycle

import numpy as np



class Visualizer():
    def __init__(self, dims, obstacles, vehicle):
        (self.x, self.y) = dims
        self.obstacles = obstacles
        #self.obstacles = environment.obstacles 
        self.vehicle_shape = vehicle.type
        self.vehicle = vehicle
        self.goal = (13,13)
        
    def render_environment(self):
        fig, ax = plt.subplots()
        ax.set_xlim(0,self.x)
        ax.set_ylim(0,self.y)
        for obstacle in self.obstacles:
            ax.add_patch(obstacle.render_obstacle())
        
        ax.add_patch(patches.Rectangle(self.goal, 2, 2, color="green"))
        return (fig, ax) 
    
    
    def render_path(self, path, fig, ax):
        
        def start():
            vehicle_shape.center = (self.vehicle.x_init, self.vehicle.y_init)
            ax.add_patch(vehicle_shape)
            ax.patches.pop()
            return vehicle_shape,
        
        def animate(i):
            ax.patches.pop()
            vehicle_shape = self.vehicle.render_vehicle(path[i])
            ax.add_patch(vehicle_shape)
            return vehicle_shape,
        
        line = np.zeros((len(path), 2))
        for i in range(0, len(path)):
            line[i][0] = path[i][0]
            line[i][1] = path[i][1]
        plt.plot(line[:,0], line[:,1], color="black")
        plt.grid(True)
        vehicle_shape = self.vehicle.render_vehicle(path[0])
        ax.add_patch(vehicle_shape)
        anim = animation.FuncAnimation(fig, animate,
                               frames=1000, init_func = start,
                               interval=200, repeat = True,
                               blit=True)
        return anim
