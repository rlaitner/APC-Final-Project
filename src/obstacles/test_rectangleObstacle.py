import pytest
from obstacles import rectangleObstacle

def test_origin():
    rectangleObject = rectangleObstacle([2, 7], 4, 3)
    assert rectangleObject.origin == [2, 7]

def test_length():
    rectangleObject = rectangleObstacle([2, 7], 4 ,3)
    assert rectangleObject.length == 4

def test_width():
    rectangleObject = rectangleObstacle([2, 7], 4, 3)
    assert rectangleObject.width == 3