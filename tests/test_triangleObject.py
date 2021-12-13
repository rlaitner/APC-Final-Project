import pytest
from obstacles import triangleObstacle


@pytest.fixture
def triangleObject():
    object = triangleObstacle([[2, 7], [1, 2], [5, 4]])
    return object


def test_vertices(triangleObject):
    assert triangleObject.vertices == [[2, 7], [1, 2], [5, 4]]


def test_lines(triangleObject):
    assert triangleObject.lines == [[(2, 7), (1, 2)],
                                    [(2, 7), (5, 4)],
                                    [(1, 2), (5, 4)]]
