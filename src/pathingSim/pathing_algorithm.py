"""
This generates a generic pathing algorithm api for all pathing
algorithms to follow.

Classes
-------
PathingAlgorithm
"""
from abc import ABC, abstractmethod
from typing import Dict, Union
import numpy as np


class PathingAlgorithm(ABC):
    @abstractmethod
    def make_route(self, origin: np.ndarray[float, float]) -> None:
        pass

    @abstractmethod
    def set_config(self, algo_dict: Dict[str, Union[str, float, list]]):
        pass
