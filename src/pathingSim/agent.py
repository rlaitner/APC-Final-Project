"""
This class combines a pathing algorithm with the dynamic constraints of
a real vehicle.

Classes
-------
Agent
"""
from typing import Dict, Union

from pathingSim.pathing_algorithm import PathingAlgorithm
from pathingSim.vehicle import Vehicle
from pathingSim.vehicle_factory import vehicle_factory
from pathingSim.algo_factory import algo_factory

class Agent():
    def __init__(self,
                 vehicle_data: Dict[str, Union[str, float, list]],
                 algo_data: Dict[str, Union[str, float, list]]
                 ) -> None:

        # Instantiate objects
        self._planner: PathingAlgorithm = algo_factory(algo_data["algorithm_type"])
        self._vehicle: Vehicle = vehicle_factory(vehicle_data["vehicle_type"])

        # Configure objects
        self._planner.set_config(algo_data)
        self._vehicle.set_config(vehicle_data)

        self._trajectory = None

    def is_valid(self):
        pass

    def get_valid_trajectory(self):
        pass
