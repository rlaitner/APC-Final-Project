import pytest
from obstacles import triangleObstacle

def test_vertices():
    triangleObject = triangleObstacle([[2, 7], [1, 2], [5, 4]])
    assert triangleObject.vertices == [[2, 7], [1, 2], [5, 4]]