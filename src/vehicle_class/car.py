
import numpy as np
from matplotlib import patches as patches


class Car:

    def __init__(self, init_position, scale):
        self.x_init = init_position[0]
        self.y_init = init_position[1]
        self.type = "car"
        L = 2 * scale
        W = 1.5 * scale        
        self.size = (L,W)
        self.theta_init = init_position[2] 
        self.shape = "rectangle"

    
    def __check_max_turn(self, turn_angle):
        if (np.abs(turn_angle) >= np.pi/2):
            raise ValueError("Turn angle exceed maximum turn\
                            radius for vehicle of type 'car'")         
        

    def update_dynamics(self, x, y, theta, turn_angle, t_curr, u=1, dt=0.05):
        
        
        self.__check_max_turn(turn_angle)
        
        L = self.size[0]
        theta_dot = u/L * np.tan(turn_angle)
        x_dot = u * np.cos(theta)
        y_dot = u * np.sin(theta)

        x += x_dot * dt
        y += y_dot * dt
        theta += theta_dot * dt

        car_position = [x, y, theta]
        
        return car_position


    def check_dynamics(self, pos_0, pos_f):
        if np.abs(pos_0[2]-pos_f[2])/dt >= (np.pi/2)
            return 1
        else: 
            return 0

    def render_vehicle(self, position):
        def calc_origin(d, position):
            psi = 45 - position[2] 
            dx = d * np.sin(psi)
            dy = d * np.cos(psi)
            bottom_left = [position[0] - dx, position[1] - dy]
            return bottom_left
        
        d = np.sqrt((self.size[0]/2)**2 + (self.size[1]**2))
        x,y = calc_origin(d, position)
        car = patches.Rectangle((x, y), self.size[0],self.size[1],
                                angle=np.degrees(position[2]), 
                                color="black")
        return car