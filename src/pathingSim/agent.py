"""
This class combines a pathing algorithm with the dynamic constraints of
a real vehicle.

Classes
-------
Agent
"""
from typing import Dict, Union
import numpy as np

from pathingSim.pathing_algorithm import PathingAlgorithm
from vehicle_class.vehicle import Vehicle
from pathingSim.algo_factory import algo_factory
from pathingSim.environment import Environment


class Agent():
    """
    This class uses physical models and path planning algorithms to
    generate valid tractories for a given system to follow.

    Attributes
    ----------
    pos: np.ndarray[float, float]
        The current (x,y) position of the center of the robot
    heading: float
        The angle in radians of the front of the robot. This value is
        initialized so that the the robot starts pointing towards the
        goal.
    vehicle: Vehicle
        Contains a vehicle class that defines the robot dynamically and
        provides an illustrator for visualization
    trajectory: np.ndarray[np.ndarray[float, ...], np.ndarray[float, ...]]
        Holds the current path that has been traveled by the robot as a
        list of coordinates in x and y.
    goal: np.ndarray[float, float]
        List of the (x,y) position of the current pathing goal

    Methods
    -------
    get_angle(np.ndarray[float, float])
        Calculates the angle between the current heading of the given
        robot at a known location and a given point
    step_toward_goal()
        Moves the robot one step toward the goal location

    Raises
    ------
    ValueError
        Raised when given a point that is not 2 dimensional
    """
    def __init__(self,
                 vehicle_data: Dict[str, Union[str, float, list]],
                 algo_data: Dict[str, Union[str, float, list]],
                 setting: Environment
                 ) -> None:
        """
        Generates an Agent class and sets the required attributes

        Parameters
        ----------
        vehicle_data: Dict[str, Union[str, float, list]]
            A dictionary containg all of the necessary information for
            initializing a vehicle object
        algo_data: Dict[str, Union[str, float, list]]
            A dictionary containg all of the necessary information for
            initializing a path planning algorithm
        setting: Environment
            An obstacles filled environment to path through
        """
        # Instantiate objects
        self.vehicle: Vehicle = Vehicle(vehicle_data["vehicle_type"])
        self._planner: PathingAlgorithm = algo_factory(algo_data["algorithm_type"], self.vehicle)

        # Configure objects
        self._planner.set_config(algo_data, setting)

        # Configure vehicle
        self.pos = np.asarray(algo_data["origin"])
        self.goal= np.asarray(algo_data["goal"])
        self.heading: float = self.get_angle(self.goal)

        self.trajectory = np.transpose(self.pos)

    def get_angle(self, point) -> float:
        """
        Get the angle between the current heading and a given point in
        radians

        Parameters
        ----------
        point: np.ndarray[float, float]
            The location in (x,y) space of the next point

        Returns
        -------
        angle: float
            The angle in radians

        Raises
        ------
        ValueError
            Raised when the point given is not a unique point in 2-space
        """
        EPSILON = 0.00002

        if len(point) != len(self.pos):
            raise ValueError("Received a trajectory position that has" +
                             " the wrong number of dimensions.")
        if (self.pos == point).all():
            return 0

        dot_prod = np.dot(self.pos, point)
        mag = np.linalg.norm(self.pos) * np.linalg.norm(point)
        if mag - EPSILON < 0.0:
            return 0.0
        theta = float(np.arccos(dot_prod/mag))

        return theta

    def step_toward_goal(self) -> None:
        """
        Moves the robot one timestep forward using model-predictive
        control to validate that each step is dynamically possible.

        Raises
        ------
        RuntimeError:
            Raised when a trajectory cannot be found that is dynamically
            valid the matches a predicted path
        """
        # The number of attempts before the dynamics are declared infeasible
        MAX_ATTEMPTS = 100

        for attempt in range(MAX_ATTEMPTS):
            # Get infinite-time horizon path
            pathx, pathy = self._planner.make_route(self.pos)

            # Check that the finite time horizon is dynamically-viable
            angle = self.get_angle(np.array([pathx[0], pathy[0]]))
            self.pos = self.vehicle.update(pathx[0], pathy[0], angle)

            # If it found a trajectory, good, if it didn't then how many times has it failed?
            if (pathx, pathy) == self.pos:
                continue
            elif attempt == (MAX_ATTEMPTS - 1):
                raise RuntimeError("The goal is dynamically unreachable.")
            else:
                pass

        # Move to the first point
        self.trajectory = np.append(self.trajectory, np.transpose(self.pos))
        self.heading = angle
