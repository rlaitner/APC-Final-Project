"""
Generates a PathingAlgorithm class to be used by higher level code

Functions
---------
algo_factory()
    Returns a PathingAlgorithm object of a specified type
"""
from typing import Type, Dict

from pathingSim.pathing_algorithm import PathingAlgorithm
# ---------------------------------------------------------------------
# Add PathingAlgorithm implmentations here
#from pathingSim.a_star import AStar
from RRT.RRT_algo import RRT
# ---------------------------------------------------------------------


def algo_factory(chosen_algo: str, vehicle) -> PathingAlgorithm:
    """
    Returns an instantiated implementation of a PathingAlgorithm
    object.

    Parameters
    ---------
    chosen_algo: str
        A string that specifies the desired pathing algortihm to use.
        The possible algorithms currently are:
            "A*": The A* search algorithm
            "RRT": The rapidly-exploring random tree algorithm
    vehicle: Vehicle
        A vehicle object that is used to determine the size of the hit
        box for collisions

    Returns
    -------
    PathingAlgorithm
        Implementation of pathing algorithm specified by input
        parameter

    Raises
    ------
    NotImplementedError
        Raised when a pathing algorithm is chosen that does not exist
        in the factory and cannot be provided.
    """
    # add new PathingAlgorithm to this dictionary to instantiate them
    possible: Dict[str, Type[PathingAlgorithm]]
    possible = {
        #"A*": AStar,
        "RRT": RRT
    }

    try:
        return possible[chosen_algo]()
    except KeyError:
        raise NotImplementedError(f"The specified algorithm {chosen_algo}" +
                                  " is invalid.")
