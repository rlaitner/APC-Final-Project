import pytest
from obstacles import rectangleObstacle

@pytest.fixture
def rectangleObject():
    object = rectangleObstacle([2, 7], 4, 3)
    return object

def test_origin(rectangleObject):
    assert rectangleObject.origin == [2, 7]

def test_length(rectangleObject):
    assert rectangleObject.length == 4
pyte
def test_width(rectangleObject):
    assert rectangleObject.width == 3

def test_lines(rectangleObject):
    assert rectangleObject.lines == [[(2, 7), (5, 7)], 
                                     [(2, 7), (2, 11)], 
                                     [(2, 11), (5, 11)], 
                                     [(5, 7), (5, 11)]]