import numpy as np


class Vehicle: 

    def __init__(self, vehicle_type):
        
        if (vehicle_type == "car"):
            self.type = "car"
        elif (vehicle_type == "UAV"):
            self.type = "UAV" 
        elif (vehicle_type == "tricycle"):
            self.type = "tricycle"
        
        
    def update_car(self, x_curr, y_curr, theta_curr, phi):
        u = 1.5
        L = 2
        W = 1
        theta_dot = u/L * np.tan(phi)
        x_dot = u * np.cos(theta_curr)
        y_dot = u * np.sin(theta_curr)
        
        t = 0.1
        x_curr += x_dot * t
        y_curr += y_dot * t
        theta_curr += theta_dot * t 
        
        center_position = [x_curr, y_curr]        
        psi = np.pi/4 - theta_curr
        nu = np.pi - np.pi/4 - theta_curr

        d = self.calc_d(L,W) 
        car_position = self.shape_coords(d, psi, nu, center_position)
        car_position.insert(0, theta_curr)
        car_position.insert(0, center_position)

        return car_position
    
    def update_tricycle(self, x_curr, y_curr, theta_curr, phi):
        u = 1.5
        L = 3
        W = 0.5
        theta_dot = u/L * np.tan(phi)
        x_dot = u * np.cos(theta_curr)
        y_dot = u * np.sin(theta_curr)
        
        t = 0.1
        x_curr += x_dot * t
        y_curr += y_dot * t
        theta_curr += theta_dot * t 
        
        center_position = [x_curr, y_curr]        
        psi = np.pi/4 - theta_curr
        nu = np.pi - np.pi/4 - theta_curr

        d = self.calc_d(L,W) 
        car_position = self.shape_coords(d, psi, nu, center_position)
        car_position.insert(0, theta_curr)
        car_position.insert(0, center_position)

        return car_position


    def update_UAV(self, x_curr, y_curr, theta_curr):
        
        x_dot = 1
        y_dot = 1
        R = 1

        t = 1
        x_curr += x_dot * t
        y_curr += y_dot * t
        
        position = np.array([x_curr, y_curr, 0])
        UAV_position = [x_curr, y_curr, R]

        return UAV_position 


    def update_dynamics(self, x_curr, y_curr, theta_curr):
        if (self.type == "car"):
            return self.update_car(x_curr, y_curr, theta_curr)
        elif (self.type == "UAV"):
            return self.update_UAV(x_curr, y_curr, theta_curr)
        elif (self.type == "tricycle"):
            return self.update_tricycle(x_curr, y_curr, theta_curr)
        

    def calc_d(self, L, W): return (np.sqrt((L/2)**2 + (W/2)**2))
    def calc_dx(self, d, angle): return (d  * np.sin(angle))
    def calc_dy(self, d, angle): return (d  * np.cos(angle))  
    def shape_coords(self, d, psi, nu, position):
        dx1 = self.calc_dx(d, psi)
        dy1 = self.calc_dy(d, psi)

        dx2 = self.calc_dx(d, nu)
        dy2 = self.calc_dy(d, nu)
        
        top_left = [position[0] + dx2, position[1] + dy2]
        bottom_right = [position[0]- dx2, position[1] - dy2]
        top_right = [position[0] + dx1, position[1] + dy1]
        bottom_left = [position[0] - dx1, position[1] - dy1]     

        vehicle_coords = [top_left, top_right, bottom_left, bottom_right]
        return vehicle_coords 
