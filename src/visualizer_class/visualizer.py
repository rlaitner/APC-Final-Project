from matplotlib import pyplot as plt
from matplotlib import animation
from matplotlib import patches as patches


class Visualizer():
    def __init__(self, dims, obstacles, vehicle):
        (self.x, self.y) = dims
        self.obstacles = obstacles
        #self.obstacles = environment.obstacles 
        self.vehicle_shape = vehicle.type
        self.vehicle = vehicle
        self.fig, self.ax = plt.subplots()
        
    def render_environment(self):
        self.ax.set_xlim(0,self.x)
        self.ax.set_ylim(0,self.y)
        
        for obstacle in self.obstacles:
            self.ax.add_patch(obstacle.render_obstacle())
          
    def render_path(self,path):
        
        def start():
            vehicle_shape.center = (vehicle.init_pos[0], vehicle.init_pos[1])
            self.ax.add_patch(vehicle_shape)
            return vehicle_shape
        
        def animate(step):
            vehicle_shape = self.vehicle.render_vehicle(path[step])
            x = path[step][0]
            y = path[step][1]   
            vehicle_shape.center = (x, y)
            return vehicle_shape
        
        
        vehicle_shape = self.vehicle.render_vehicle(path[0])
        self.ax.add_patch(vehicle_shape)
        self.anim = animation.FuncAnimation(self.fig, animate,
                               frames=1000, init_func = start,
                               interval=50, repeat = True,
                               blit=True)
