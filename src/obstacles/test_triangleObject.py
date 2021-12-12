import pytest
from obstacles import triangleObstacle


@pytest.fixture
def triangleObject():
    object = triangleObstacle([[2, 7], [1, 2], [5, 4]])
    return object


def test_vertices(triangleObject):
<<<<<<< HEAD
    assert triangleObject.vertices == [[2, 7], [1, 2], [5, 4]]
=======
    assert triangleObject.vertices == [[2, 7], [1, 2], [5, 4]]


def test_lines(triangleObject):
    assert triangleObject.lines == [[(2, 7), (1, 2)],
                                    [(2, 7), (5, 4)],
                                    [(1, 2), (5, 4)]]
>>>>>>> 40a624cf49bcd696ee2448bccaeb99ef8ceaf50d
