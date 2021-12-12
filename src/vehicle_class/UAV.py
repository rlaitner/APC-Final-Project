from vehicle_class.vehicle import Vehicle
import numpy as np

class UAV(Vehicle):
    
    def __init__(self, vehicle_type, init_position, scale):
        
        super().__init__(vehicle_type, init_position)
        R = 0.5 * scale
        self.size = R
        self.shape = "circle"

    def update_dynamics(self, x, y, U, dt=0.5):
        x_dot = U[0]
        y_dot = U[1]
        
        x += x_dot * dt
        y += y_dot * dt
        
        UAV_position = [x, y]
        
        return UAV_position         
    