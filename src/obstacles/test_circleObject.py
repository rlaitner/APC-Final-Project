import pytest
from obstacles import circleObstacle


@pytest.fixture
def circleObject():
    object = circleObstacle([1, 1], 1)
    return object


def test_center(circleObject):
    assert circleObject.center == [1, 1]


def test_radius(circleObject):
    assert circleObject.radius == 1
