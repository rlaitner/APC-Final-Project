'''
Create vehicle for path planning. 

Classes:
    Vehicle

'''
import numpy as np


class Vehicle: 

    '''
    Create a vehicle object 

    Attributes:
    -----------------------

    x : double 
        Position of COM along the x-axis on the map in cm

    y : double 
        Position of COM along the y-axis on the map in cm

    theta : double 
        Angle between x-axis and centerline of vehicle in radians 


    ''' 

    def __init__(self, vehicle_type, scale):
        if (vehicle_type == "car"):
            self.type = "car"
        elif (vehicle_type == "UAV"):
            self.type = "UAV" 
        elif (vehicle_type == "tricycle"):
            self.type = "tricycle"
        self.scale = scale
        
        
    def update_vehicle(self, x, y, theta, turn_angle):

        if (self.type == "car"):     
            L = 2 * self.scale
            W = 1 * self.scale
            if (np.abs(turn_angle) >= np.pi/2):
                raise ValueError("Turn angle exceed maximum turn radius for vehicle of type 'car'")
        elif (self.type == "tricycle"):
            L = 2 * self.scale
            W = 0.5 * self.scale            
        
        u = 1
        theta_dot = u/L * np.tan(turn_angle)
        x_dot = u * np.cos(theta)
        y_dot = u * np.sin(theta)
        
        dt = 0.1
        x += x_dot * dt
        y += y_dot * dt
        theta += theta_dot * dt 
        
        center_position = [x, y]        
        psi = np.pi/4 - theta
        nu = np.pi - np.pi/4 - theta

        d = self.calc_d(L,W) 
        car_position = self.shape_coords(d, psi, nu, center_position)
        car_position.insert(0, theta)
        car_position.insert(0, center_position)

        return car_position
    

    def update_UAV(self, x, y, theta, turn_angle):
        x_dot = 1
        y_dot = 1
        R = 1

        dt = 0.1
        x += x_dot * dt
        y += y_dot * dt
        UAV_position = [x, y, R]

        return UAV_position 


    def update_dynamics(self, x, y, theta, turn_angle):
        if (self.type == "car"):
            return self.update_vehicle(x, y, theta, turn_angle)
        elif (self.type == "tricycle"):
            return self.update_vehicle(x, y, theta, turn_angle)
        elif (self.type == "UAV"):
            return self.update_UAV(x, y, theta, turn_angle)


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
