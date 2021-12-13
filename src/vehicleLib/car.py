from vehicle_class.vehicle import Vehicle
import numpy as np


class Car(Vehicle):

    def __init__(self, init_position, scale):

        super().__init__(init_position)
        self.type = "car"
        L = 2 * scale
        W = 1.5 * scale
        self.size = (L, W)
        self.theta_init = init_position[2]
        self.shape = "rectangle"

    def __check_max_turn(self, turn_angle):
        if (np.abs(turn_angle) >= np.pi/2):
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

    def render_vehicle(self, position):
        def calc_origin(d, position):
            psi = np.pi/4 - position[2]
            dx = d * np.sin(psi)
            dy = d * np.cos(psi)
            bottom_left = [position[0] - dx, position[1] - dy]
            return bottom_left

        d = np.sqrt((self.size[0]**2) + (self.size[1]**2))
        x, y = calc_origin(d, position)
        car = patches.Rectangle((x, y), self.size[1], self.size[0],
                                angle=np.degrees(position[2]))
        return car
