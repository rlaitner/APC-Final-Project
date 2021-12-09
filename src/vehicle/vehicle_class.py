# Vehicle Class


import numpy as np

class Vehicle: 

    def __init__(self, vehicle_type, x_curr, y_curr, theta_curr):
        
        if (vehicle_type == "car"):
            self.dynamics = update_car(x_curr, y_curr, theta_curr)
        elif (vehicle_type == "UAV"):
            self.dynamics = update_UAV(x_curr, y_curr, theta_curr)       

    
    def update_car(x_curr, y_curr, theta_curr):
        u = 1
        L = 1
        W = 1
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

        d = calc_d(L,W) 
        car_position = shape_coords(d, psi, nu, position)

        return car_position 


    def update_UAV(x_curr, y_curr, theta_curr):

        x_dot = 1
        y_dot = 1
        R = 1


        t = 1
        x_curr += x_dot * t
        y_curr += y_dot * t

        position = np.array([x_curr, y_curr, 0])
        UAV_position = [x_curr, y_curr, R]

        return UAV_position 



    def calc_d(L, W):
        return (np.sqrt((L/2)**2 + (H/2)**2))
    def calc_dx(d, angle):
        return (d  * np.sin(theta))
    def calc_dy(d, angle):
        return (d  * np.cos(theta))  
    def shape_coords(d, psi, nu, position):
        dx1 = calc_dx(d, psi)
        dy1 = calc_dy(d, psi)
        dx2 = calc_dx(d, nu)
        dy2 = calc_dy(d, nu)

        top_left = [position[0] + dx2, position[1] + dy2]
        bottom_right = [position[0]- dx2, position[1] - dy2]
 
        top_right = [position[0] + dx1, position[1] + dy1]
        bottom_left = [position[0] - dx1, position[1] - dy1]     

        vehicle_coords = [top_left, top_right, bottom_left, bottom_right]
        return vehicle_coords



