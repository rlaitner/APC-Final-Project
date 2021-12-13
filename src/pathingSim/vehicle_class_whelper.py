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


    Methods:
    ----------------------


    '''

    def __init__(self, vehicle_type, scale, x_init, y_init, angle):
        if (vehicle_type == "car"):
            self.type = "car"
            self.shape = "rectangle"
        elif (vehicle_type == "tricycle"):
            self.type = "tricycle"
            self.shape = "rectangle"
        elif (vehicle_type == "UAV"):
            self.type = "UAV"
            self.shape = "circle"

        self.scale = scale
        self.size = self.set_vehicle_size()
        self.x_init = x_init
        self.y_init = y_init
        self.angle = angle

    def update_gvehicle(self, x, y, theta, turn_angle, u=1, dt=0.1):

        if (np.abs(turn_angle) >= np.pi/2):
            raise ValueError("Turn angle exceed maximum turn radius\
                            for vehicle of type 'car'")
        L = self.size[0]
        W = self.size[1]

        theta_dot = u/L * np.tan(turn_angle)
        x_dot = u * np.cos(theta)
        y_dot = u * np.sin(theta)

        x += x_dot * dt
        y += y_dot * dt
        theta += theta_dot * dt

        center_position = [x, y]

        d = (np.sqrt((L/2)**2 + (W/2)**2))
        gvehicle_position = self.shape_coords(d, theta, center_position)
        gvehicle_position.insert(0, theta)
        gvehicle_position.insert(0, center_position)

        return gvehicle_position

    def update_UAV(self, x, y, theta, turn_angle, dt=0.1):
        x_dot = 1
        y_dot = 1

        x += x_dot * dt
        y += y_dot * dt

        UAV_position = [x, y, self.size]

        return UAV_position

    def set_vehicle_size(self):
        if (self.type == "car"):
            L = 2 * self.scale
            W = 1.5 * self.scale
            return (L, W)
        elif (self.type == "tricycle"):
            L = 2 * self.scale
            W = 0.5 * self.scale
            return (L, W)
        elif (self.type == "UAV"):
            R = 0.5 * self.scale
            return R

    def update_dynamics(self, x, y, theta, turn_angle):
        if (self.type == "car"):
            return self.update_gvehicle(x, y, theta, turn_angle)
        elif (self.type == "tricycle"):
            return self.update_gvehicle(x, y, theta, turn_angle)
        elif (self.type == "UAV"):
            return self.update_UAV(x, y, theta, turn_angle)

    def shape_coords(self, d, theta, position):
        psi = np.pi/4 - theta
        nu = np.pi - np.pi/4 - theta
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
