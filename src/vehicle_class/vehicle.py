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
        self.init_position = init_position
        self.type = None
        self.vehicle_data = vehicle_data
    
    def init_vehicle(self):
        if (self.vehicle_data["vehicle_type"] == "UAV"):
            return UAV(self.init_position, self.vehicle_data["vehicle_size"])
        elif (self.vehicle_data["vehicle_type"] == "car"):
            return Car(self.init_position, self.vehicle_data["vehicle_size"])
        elif (self.vehicle_data["vehicle_type"] == "tricycle"):
            return Tricycle(self.init_position, self.vehicle_data["vehicle_size"])