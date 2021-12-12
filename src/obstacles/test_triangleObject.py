import pytest
from obstacles import triangleObstacle

@pytest.fixture
def triangleObject():
    object = triangleObstacle([[2, 7], [1, 2], [5, 4]])
    return object

def test_vertices(triangleObject):
    assert triangleObject.vertices == [[2, 7], [1, 2], [5, 4]]