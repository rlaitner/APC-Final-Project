from vehicle_class.vehicle import Vehicle
import numpy as np


class Tricycle(Vehicle):
    
    def __init__(self, init_position, scale):
                
        super().__init__(init_position)
        self.type = "tricycle"
        L = 1 * scale
        W = 0.25 * scale
        self.size = (L,W)
        self.theta_init = init_position[2]
        self.shape = "rectangle"
        
    def update_dynamics(self, x, y, theta, turn_angle, u=1, dt=0.1):
                
        L = self.size[0]        
        theta_dot = u/L * np.tan(turn_angle)
        x_dot = u * np.cos(theta)
        y_dot = u * np.sin(theta)
        
        x += x_dot * dt
        y += y_dot * dt
        theta += theta_dot * dt 
        
        tricycle_position = [x, y, theta]        

        return tricycle_position     
    
    def render_vehicle(self, position):
        def rect_coords(d, position):
            psi = np.pi/4 - position[2]
            nu = np.pi - np.pi/4 - position[2]

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
        
        
        d = np.sqrt((self.size[0]**2) + (self.size[1]**2))
        x,y = rect_coords(d, position)[2]
        tricycle = patches.Rectangle((x, y), self.size[1], self.size[0],
                                   angle = np.degrees(position[2]))  
        return tricycle