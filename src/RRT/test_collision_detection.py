import pytest
import numpy as np
from obstacles import rectangleObstacle
from obstacles import triangleObstacle
from collision_detection import edges_of
from collision_detection import orthogonal
from collision_detection import is_separating_axis
from collision_detection import polygon_collide

@pytest.fixture
def rectangleObject1():
    r1Object = rectangleObstacle([2, 2], 2, 2)
    return r1Object.vertices

@pytest.fixture
def rectangleObject2():
    r2Object = rectangleObstacle([3, 3], 2, 2)
    return r2Object.vertices

@pytest.fixture
def rectangleObject3():
    r3Object = rectangleObstacle([6, 6], 2, 2)
    return r3Object.vertices

@pytest.fixture
def triangleObject1():
    t1Object = triangleObstacle([[1, 1], [2, 4], [3, 2]])
    return t1Object.vertices

@pytest.fixture
def triangleObject2():
    t2Object = triangleObstacle([[3, 2], [6, 3], [6, 1]])
    return t2Object.vertices

@pytest.fixture
def triangleObject3():
    t3Object = triangleObstacle([[9, 6], [11, 8], [11, 9]])
    return t3Object.vertices

# Test if two rectangles that should collide will indeed collide
def test_colliding_rectangle_polygon_collide(rectangleObject1, rectangleObject2):
    assert polygon_collide(rectangleObject1, rectangleObject2) == True

# Test if two rectangles that should not collide will indeed not collide
def test_not_colliding_rectangle_polygon_collide(rectangleObject1, rectangleObject3):
    assert polygon_collide(rectangleObject1, rectangleObject3) == False

# Test if two triangles that should collide will indeed collide
def test_colliding_triangle_polygon_collide(triangleObject1, triangleObject2):
    assert polygon_collide(triangleObject1, triangleObject2) == True

# Test if two triangles that should not collide will indeed not collide
def test_not_colliding_triangle_polygon_collide(triangleObject1, triangleObject3):
    assert polygon_collide(triangleObject1, triangleObject3) == False

# Test if a triangle and rectangle that should collide actually collide
def test_colliding_rectangle_triangle_polygon_collide(rectangleObject1, triangleObject1):
    assert polygon_collide(rectangleObject1, triangleObject1) == True

# Test if a triangle and rectangle that should not collide actually not collide
def test_not_colliding_rectangle_triangle_polygon_collide(rectangleObject2, triangleObject2):
    assert polygon_collide(rectangleObject2, triangleObject2) == False