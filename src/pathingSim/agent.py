"""
This class combines a pathing algorithm with the dynamic constraints of
a real vehicle.

Classes
-------
Agent
"""
from pathingSim.pathing_algorithm import PathingAlgorithm
from pathingSim.algo_factory import algo_factory

class Agent():
    def __init__(self, algo: str) -> None:
        self._planner: PathingAlgorithm = algo_factory(algo)
        self._vehicle = None
