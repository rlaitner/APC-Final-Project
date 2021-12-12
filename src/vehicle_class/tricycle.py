from vehicle_class.vehicle import Vehicle
import numpy as np

class Tricycle(Vehicle):
    
    def __init__(self, vehicle_type, init_position, scale):
        
        super().__init__(vehicle_type, init_position)
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
    