"""
This generates a generic pathing algorithm api for all pathing
algorithms to follow.

Classes
-------
PathingAlgorithm
"""
from abc import ABC, abstractmethod
from typing import Dict, List, Union, Type

from pathingSim.environment import Environment


class PathingAlgorithm(ABC):
    """
    This class arechetypes the required api of a PathingAlgorithm

    Methods
    -------
    make_route(np.ndarray[float, float])
        Takes in a starting location and navigates a viable route to a
        goal
    set_config(Dict[str, Union[str, float, List]])
        Sets the necessary hyperparameters for a path planning algo to
        use
    """
    @abstractmethod
    def make_route(self,
                   origin
                   ):
        """
        Generates a route from a given location to a preassigned goal
        location.

        Parameters
        ----------
            origin: np.ndarray[float, float]
                The initial x,y coordinates to make a route from

        Returns
        -------
        Route: Tuple[np.ndarray, np.ndarray]
            The x and y coordinates of the required route to travel
        """
        pass

    @abstractmethod
    def set_config(self,
                   algo_dict: Dict[str, Union[str, float, List]],
                   setting: Type[Environment]
                   ) -> None:
        """
        Sets hyperparameters for the required algorithms as well as the
        goal location.

        Parameters
        ----------
            algo_dict: dict
                Contatins the necessary hyperparameters and goal info
                to build a valid path planning algorithm
            setting: Environment
                The field containing obstacles to path through
        """
        pass
