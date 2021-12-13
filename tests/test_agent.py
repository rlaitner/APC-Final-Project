import pytest
import numpy as np
import sys

from pathingSim.agent import Agent
from pathingSim.pathing_algorithm import PathingAlgorithm
from pathingSim.vehicle import Vehicle


@pytest.fixture()
def my_agent():
    dummy_vehicle_dict = {
        "vehicle_type": "UAV",
        "vehicle_size": 1
    }
    dummy_algo_dict = {
        "origin": [0, 0],
        "goal": [100, 100],
        "goal_radius": 1,
        "time_step": 0.01,
        "total_time": 100,
        "algorithm_type": "A*",
        "hyper-parameters": "0 0"
    }

    return Agent(dummy_vehicle_dict, dummy_algo_dict)


@pytest.mark.parametrize("val, cls", [
    (my_agent, Agent),
    (my_agent._planner, PathingAlgorithm),
    (my_agent._vehicle, Vehicle)
])
def test_constructor(val, cls, my_agent):
    assert isinstance(val, cls)


@pytest.mark.parametrize("pos, angle", [
    ((0, 0), 0),
    ((0, 1), 90),
    ((1, 0), 0),
    ((-1, 0), 180),
    ((1, 1), 45),
    ((sys.float_info.max, sys.float_info.max), 45)
])
def test_angle(pos, angle, my_agent):
    EPSILON = 0.01
    pos = np.asarray(pos)

    computed_angle = my_agent.get_angle(pos)
    computed_angle = np.rad2deg(computed_angle)

    assert np.abs(computed_angle - angle) < EPSILON


@pytest.mark.parametrize("pos", [
    1,
    (0, 0, 1),
    [1, 1, 1, 1]
])
def test_angle_error(pos, my_agent):
    pos = np.asarray(pos)

    with pytest.raises(ValueError):
        my_agent.get_angle(pos)


def test_step(my_agent):
    old_pos = my_agent.pos
    my_agent.step_toward_goal()
    assert old_pos != my_agent.pos
