"""
This generates a generic pathing algorithm api for all pathing
algorithms to follow.

Classes
-------
PathingAlgorithm
"""
from abc import ABC, abstractmethod
from typing import Dict, List, Tuple, Union


class PathingAlgorithm(ABC):
    @abstractmethod
    def make_route(self) -> List[Tuple[float, float]]:
        pass

    @abstractmethod
    def update_route(self, time: float) -> List[Tuple[float, float]]:
        pass

    @abstractmethod
    def set_config(self, algo_dict: Dict[str, Union[str, float, list]]):
        pass
