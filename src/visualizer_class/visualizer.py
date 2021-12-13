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
            ax.add_patch(self.gen_obs(obstacle))
        
        return (fig, ax)
  
    def render_path(self, fig, ax, path):
        
        def start():
            vehicle_shape.center = self.vehicle.init_pos
            ax.add_patch(vehicle_shape)
            return vehicle_shape
        
        def animate(step):
            vehicle_shape = self.generate_shape(self.vehicle, path[step])
            x, y = vehicle_shape.center
            x = path[step][0]
            y = path[step][1]
            vehicle_shape.center = (x, y)
            return drone
        
        vehicle_shape = self.generate_shape(self.vehicle, path[0])
        ax.add_patch(vehicle_shape)
        
        anim = animation.FuncAnimation(fig, animate, 
                               init_func=start, 
                               frames=1000, 
                               interval=200,
                               blit=True)


    def gen_obs(self, obj, position):
        
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
   
    def gen_veh(self, vehicle, position):
        def rect_coords(d, theta, position):
            psi = np.pi/4 - theta
            nu = np.pi - np.pi/4 - theta

            dx1 = d * np.sin(psi)
            dy1 = d * np.cos(psi)
            dx2 = d * np.sin(nu)
            dy2 = d * np.cos(nu)

            top_left = [position[0] + dx2, position[1] + dy2]
            bottom_right = [position[0] - dx2, position[1] - dy2]
            top_right = [position[0] + dx1, position[1] + dy1]
            bottom_left = [position[0] - dx1, position[1] - dy1]

            gvehicle_coords = [top_left, top_right, bottom_left, bottom_right]
            return gvehicle_coords
        
        if (vehicle.type == "car" or vehicle.type == "tricycle"):
            d = np.sqrt((vehicle.size[0]**2) + (vehicle.size[1]**2))
            x,y = rect_coords(d, theta_init, position)[2]
            car = patches.Rectangle((x, y), vehicle.size[1], vehicle.size[0], 
                                   angle = vehicle.theta_init)
            
