'''
Create vehicle for path planning.

Classes:
    Vehicle
'''


class Vehicle:

    '''
    Create a vehicle object

    Attributes:
    -----------------------

    vehicle_type: String
        vehicle type from library

    init_poisition: array
        x : double (required)
            Position of COM along the x-axis on the map in cm

        y : double (required)
            Position of COM along the y-axis on the map in cm

        theta : double (optional)
            Angle between x-axis and centerline of vehicle in radians

    '''

    def __init__(self, init_position):
        self.x_init = init_position[0]
        self.y_init = init_position[1]
