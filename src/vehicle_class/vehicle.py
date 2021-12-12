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

    def __init__(self, vehicle_type, init_position):
        self.type = vehicle_type    
        self.x_init = init_position[0]
        self.y_init = init_position[1] 
        