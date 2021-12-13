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
        
    def render_environment(self):
        fig,ax = plt.subplots()  
        ax.set_xlim(0,self.x)
        ax.set_ylim(0,self.y)
        
        for obstacle in self.obstacles:
            ax.add_patch(obstacle.render_obstacle())
        
        return (fig,ax)
  
    def render_path(self, fig, ax, path):
        
        def start():
            vehicle_shape.center = (1,1)
            ax.add_patch(vehicle_shape)
            return vehicle_shape
        
        def animate(step):
            #vehicle_shape = self.vehicle.render_vehicle(path[step])
            x = path[step][0]
            y = path[step][1]
            vehicle_shape.center = (x, y)
            return vehicle_shape
        
        
        vehicle_shape = self.vehicle.render_vehicle(path[0])
        print(vehicle_shape)
        ax.add_patch(vehicle_shape)
        
        anim = animation.FuncAnimation(fig, animate, 
                               init_func=start, 
                               frames=1000, 
                               interval=200,
                               blit=True)
            
        return anim