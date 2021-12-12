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
    update_gvehicle():
        Updates the position of the ground vehicle given its dynamics
        returns:
            List of
    update_UAV():
        Updates the position of the Unmanned Aerial Vehicle given its dynamics
    set_vehicle_size():
        Sets the appropriate dimensions of the vehicle given the scaling factor
    update_dynamics():
        Updates vehicle dynamics given vehicle type and control input
    '''

    def __init__(self, vehicle_type, scale, x_init, y_init, theta_init):
        if (vehicle_type == "car"):
            self.type = "car"
            self.shape = "rectangle"
        elif (vehicle_type == "tricycle"):
            self.type = "tricycle"
            self.shape = "rectangle"
        elif (vehicle_type == "UAV"):
            self.type = "UAV"
            self.shape = "circle"

        self.size = self.__set_vehicle_size(scale)
        self.x_init = x_init
        self.y_init = y_init
        self.theta_init = theta_init

    def update_dynamics(self, x, y, theta, turn_angle):
        if (self.type == "car"):
            return self.__update_gvehicle(x, y, theta, turn_angle)
        elif (self.type == "tricycle"):
            return self.__update_gvehicle(x, y, theta, turn_angle)
        elif (self.type == "UAV"):
            return self.__update_UAV(x, y)

    def __update_gvehicle(self, x, y, theta, turn_angle, u=1, dt=0.1):

        self.__check_max_turn(turn_angle)

        L = self.size[0]
        theta_dot = u/L * np.tan(turn_angle)
        x_dot = u * np.cos(theta)
        y_dot = u * np.sin(theta)

        x += x_dot * dt
        y += y_dot * dt
        theta += theta_dot * dt

        gvehicle_position = [x, y, theta]

        return gvehicle_position

    def __update_UAV(self, x, y, dt=0.1):
        x_dot = 1
        y_dot = 1

        x += x_dot * dt
        y += y_dot * dt

        UAV_position = [x, y]

        return UAV_position

    def __check_max_turn(self, turn_angle):
        if (self.type == "car" and np.abs(turn_angle) >= np.pi/2):
            raise ValueError("Turn angle exceed maximum turn\
                            radius for vehicle of type 'car'")

    def __set_vehicle_size(self, scale):
        if (self.type == "car"):
            L = 2 * scale
            W = 1.5 * scale
            return (L, W)
        elif (self.type == "tricycle"):
            L = 2 * scale
            W = 0.5 * scale
            return (L, W)
        elif (self.type == "UAV"):
            R = 0.5 * scale
            return R