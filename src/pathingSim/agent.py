"""
This class combines a pathing algorithm with the dynamic constraints of
a real vehicle.

Classes
-------
Agent
"""
from operator import pos
from typing import Dict, Union, Tuple, List
import numpy as np

from pathingSim.pathing_algorithm import PathingAlgorithm
from pathingSim.vehicle import Vehicle
from pathingSim.algo_factory import algo_factory

class Agent():
    def __init__(self,
                 vehicle_data: Dict[str, Union[str, float, list]],
                 algo_data: Dict[str, Union[str, float, list]]
                 ) -> None:

        # Instantiate objects
        self._planner: PathingAlgorithm = algo_factory(algo_data["algorithm_type"])
        self._vehicle: Vehicle = Vehicle(vehicle_data["vehicle_type"])

        # Configure objects
        self._planner.set_config(algo_data)
        self._vehicle.set_config(vehicle_data)

        # Configure vehicle
        self.pos: np.ndarray[float, float] = np.asarray(algo_data["origin"])
        self.goal: np.ndarray[float, float] = np.asarray(algo_data["goal"])
        self.heading = self.get_angle(self.goal)

        self.trajectory = self.pos

    def get_angle(self, point: np.ndarray[float, float]) -> float:
        if len(point) != len(self.pos):
            raise ValueError("Received a trajectory position that has"+ 
                             " the wrong number of dimensions.")

        dot_prod = np.dot(self.pos, point)
        mag = np.linalg.norm(self.pos) * np.linalg.norm(point)
        theta = np.arccos(dot_prod/mag)

        return float(theta)

    def step_toward_goal(self) -> None:
        # Get path
        pathx, pathy = self._planner.make_route(self.pos)

        # Check that the next time horizon is dynamically-viable
        angle = self.get_angle(np.array([pathx[0], pathy[0]]))
        self.pos = self._vehicle.update(pathx[0], pathy[0], angle)

        # Add the current position to the route taken
        self.trajectory = np.append(self.trajectory, self.pos)
