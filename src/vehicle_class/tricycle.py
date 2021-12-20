from vehicle_class.vehicle import Vehicle

import numpy as np
from matplotlib import patches as patches

class Tricycle(Vehicle):
    
    def __init__(self, init_position, scale):
                
        self.type = "tricycle"
        L = 1 * scale
        W = 0.5 * scale
        self.size = (L,W)
        self.theta_init = init_position[2]
        self.shape = "rectangle"
        

    def update_dynamics(self, x, y, theta, turn_angle, t_curr, u=1, dt=0.05):
        
                
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
        def calc_origin(d, position):
            psi = 45 - position[2] 
            dx = d * np.sin(psi)
            dy = d * np.cos(psi)
            bottom_left = [position[0] - dx, position[1] - dy]
            return bottom_left
        
        d = np.sqrt((self.size[0]/2)**2 + (self.size[1]**2))
        x,y = calc_origin(d, position)
        tricycle = patches.Rectangle((x, y), self.size[0],self.size[1],
                                angle=np.degrees(position[2]), 
                                color="black")
        return tricycle
               