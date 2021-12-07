import json
import numpy as np
import matplotlib.pyplot as plt
from typing import List, Tuple
from scipy.spatial import distance

%matplotlib notebook

width = 
height = 
circleObstacles = [(np.array([1, 1]), 0.25), (np.array([2, 2]), 0.25), (np.array([1, 3]), 0.3)]
quadrilateralObstacles = [(np.array([3, 4]), 4, 5), (np.array([6, 3]), 2, 1), (np.array([2, 2]), 1, 1)]
triangleObstacles = [(np.array([3, 4]), np.array([4, 4]), np.array([5, 5])), (np.array([8, 2]), np.array([1, 0]), np.array([2, 2]))]

%matplotlib inline
fig, ax = plt.subplots()

ax.set_xlim([0, width])
ax.set_ylim([0, height])
ax.set_aspect('equal')

for c in circleObstacles:
    ax.add_artist(plt.Circle(tuple(c[0]), c[1]))

for q in quadrilateralObstacles:
    ax.add_artist(plt.Rectangle(tuple(q[0]), q[1], q[2]))

for t in triangleObstacles:
    ax.add_artist(plt.Polygon(tuple(t[0]), tuple(t[1]), tuple(t[2])))