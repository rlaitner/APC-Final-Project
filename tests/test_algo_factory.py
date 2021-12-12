import pytest

from pathingSim.algo_factory import algo_factory
from pathingSim.a_star import AStar
from pathingSim.RRT import RRT
from pathingSim.pathing_algorithm import PathingAlgorithm


@pytest.mark.parametrize("algo, expectedClass", [
    ("A*", PathingAlgorithm),
    ("A*", AStar),
    ("RRT", PathingAlgorithm),
    ("RRT", RRT)
])
def test_good_inputs(algo, expectedClass):
    expectedAlgorithm = algo_factory(algo)
    assert isinstance(expectedAlgorithm, expectedClass)


@pytest.mark.parametrize("algo", [
    ("A star"),
    ("rrt"),
    (None),
    (""),
    (0)
])
def test_raise_error(algo):
    with pytest.raises(NotImplementedError):
        algo_factory(algo)
