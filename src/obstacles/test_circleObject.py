import pytest
from obstacles import circleObstacle

def test_center(self):
    circleObject = circleObstacle([1, 1], 0, 0)
    assert circleObject.center == [1, 1]