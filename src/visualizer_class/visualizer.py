from matplotlib import pyplot as plt
from matplotlib import animation
from matplotlib import patches as patches
from obstacle import Obstacle, circleObstacle, triangleObstacle, rectangleObstacle
from vehicle import Vehicle, Car, UAV, Tricycle

import numpy as np


class Visualizer():
    def __init__(self, dims, obstacles, vehicle):
        (self.x, self.y) = dims
        self.obstacles = obstacles
        #self.obstacles = environment.obstacles 
        self.vehicle_shape = vehicle.type
        self.vehicle = vehicle
        
    def render_environment(self):
        fig, ax = plt.subplots()
        ax.set_xlim(0,self.x)
        ax.set_ylim(0,self.y)
        
        for obstacle in self.obstacles:
            ax.add_patch(obstacle.render_obstacle())
        return (fig, ax) 
    
    
    def render_path(self, path, fig, ax):
        
        def start():
            vehicle_shape.center = (vehicle.x_init, vehicle.y_init)
            ax.add_patch(vehicle_shape)
            ax.patches.pop()
            return vehicle_shape,
        
        def animate(i):
            ax.patches.pop()
            vehicle_shape = vehicle.render_vehicle(path[i])
            ax.add_patch(vehicle_shape)
            return vehicle_shape,
        
        vehicle_shape = self.vehicle.render_vehicle(path[0])
        ax.add_patch(vehicle_shape)
        anim = animation.FuncAnimation(fig, animate,
                               frames=1000, init_func = start,
                               interval=50, repeat = True,
                               blit=True)
        return anim
