'''
Create vehicle for path planning.

Classes:
    Vehicle
'''

from vehicle_class.UAV import UAV
from vehicle_class.car import Car
from vehicle_class.tricycle import Tricycle

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

    def __init__(self, vehicle_data):

        init_position = vehicle_data["origin"]
        self.x_init = init_position[0]
        self.y_init = init_position[1]
        self.type = None

        if (vehicle_data["vehicle_type"] == "UAV"):
            return UAV(init_position, vehicle_data["vehicle_size"])
        elif (vehicle_data["vehicle_type"] == "car"):
            return Car(init_position, vehicle_data["vehicle_size"])
        elif (vehicle_data["vehicle_type"] == "tricycle"):
            return Tricycle(init_position, vehicle_data["vehicle_size"])