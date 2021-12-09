# Vehicle Class





import numpy as np


class Vehicle: 

    def __init__(self,
                vehicle_type, x_curr, y_curr, theta_curr):
        
        if (vehicle_type == "car"):
            self.dynamics = car_dynamics()
        
    
    def car_dynamics(x_curr, y_curr, theta_curr):
        u = 1
        L = 1
        x_dot = u * np.cos(theta)
        y_dot = u * np.sin(theta)
        theta_dot = u/L * tan(phi)

        t = 1
        x_curr += x_dot * t
        y_curr += y_dot * t
        theta_curr += theta_dot * t 

        position = np.array([x_curr, y_curr, theta_curr])

        psi = 45 - theta_curr
        nu = 180 - 45 - theta_curr

        d = 1
        
        dx1 = d * np.sin(psi)
        dy1 = d * np.cos(psi)

        dx2 = d * np.sin(nu)
        dy2 = d * np.cos(nu)

        top_left = [position[0]+ dx2, position[1] + dy2]
        bottom_right = [position[0]- dx2, position[1] - dy2]
 
        top_right = [position[0]+ dx1, position[1] + dy1]
        bottom_left = [position[0]- dx1, position[1] - dy1]       
    
        car_position = [top_left, top_right, bottom_left, bottom_right]
        return car_position 

    def UAV_dynamics(x_curr, y_curr, theta_curr, t):

    
        return position 



