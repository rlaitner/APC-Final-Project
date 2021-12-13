from vehicle_class.vehicle import Vehicle


class UAV(Vehicle):

    def __init__(self, init_position, scale):

        super().__init__(init_position)
        self.type = "UAV"
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

    def render_vehicle(self, position):
        x, y = (position[0], position[1])
        drone = patches.Circle((x, y), self.size)

        return drone
