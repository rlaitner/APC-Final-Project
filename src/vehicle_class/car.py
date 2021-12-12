from vehicle_class.vehicle import Vehicle
import numpy as np

class Car(Vehicle):
    
    def __init__(self, vehicle_type, init_position, scale):
        
        L = 2 * scale
        W = 1.5 * scale        
        self.size = (L,W)
        self.theta_init = init_position[2]
        self.shape = "rectangle"


    
    def __check_max_turn(self, turn_angle):
        if (self.type == "car" and np.abs(turn_angle) >= np.pi/2):
            raise ValueError("Turn angle exceed maximum turn\
                            radius for vehicle of type 'car'")         
        

    def update_dynamics(self, x, y, theta, turn_angle, u=1, dt=0.1):
        
        self.__check_max_turn(theta)
        
        L = self.size[0]        
        theta_dot = u/L * np.tan(turn_angle)
        x_dot = u * np.cos(theta)
        y_dot = u * np.sin(theta)
        
        x += x_dot * dt
        y += y_dot * dt
        theta += theta_dot * dt 
        
        car_position = [x, y, theta]        

        return car_position
    
    def get_shape(self):
        return self.shape        