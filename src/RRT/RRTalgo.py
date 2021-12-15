from obstacle_class.obstacle import Obstacle
from vehicle_class.vehicle import Vehicle
from pathingSim.pathing_algorithm import PathingAlgorithm
from pathingSim.environment import Environment

import numpy as np
from typing import Dict, List, Union, Tuple, Type


class RRT(PathingAlgorithm):
    MAX_ITERATIONS = 100,000

    def __init__(self) -> None:
        super().__init__()
        self.initialized = False

    def set_config(self,
                   algo_dict: Dict[str, Union[str, float, List]],
                   setting: Type[Environment]
                   ) -> None:
        super().set_config(algo_dict, setting)
        self.hazards = setting.obstacles
        self.start = np.asarray(algo_dict["origin"])
        self.pos = self.start
        self.goal = np.asarray(algo_dict["goal"])
        self.radius = self._algorithm_configs["goal_radius"]
        self.width = setting.x
        self.height = setting.y
        self.initialized = True

    def make_route(self,
                   origin: np.ndarray[float, float]
                   ) -> Tuple[np.ndarray, np.ndarray]:
        super().make_route(origin)
        if not self.initialized:
            raise RuntimeError("Algorithm is not properly initialized." +
                               " Call set_config().")

        x = self.width
        y = self.height
        obstacles = self.hazards

        iteration = 0
        while np.exp(self.pos - self.goal, 2) <= self.radius \
                    and iteration < self.MAX_ITERATIONS:
            rand_state = self.random_free_conf(x, y, obstacles)
            # Got tired and its 0645. Someone else finish this out. 

    def free_conf(self, q: Tuple[np.ndarray, float], obstacles: List[Tuple[np.ndarray, float]]) -> bool:

        """
        Check to see if a configuration is in the free space.

        This function checks if the configuration q lies outside of all the obstacles in the connfiguration space.

        @param q: An np.ndarray describing a shape representing a random po
        @param obstacles: A list of obstacles. A circle obstacle is a tuple of the form (center, radius) representing a circle,
        a rectangle obstacle is a tuple of the form (center, length, width), and a triangle obstacle is a tuple of the
        form (vertices).
        @return: True if the configuration is in the free space, i.e. it lies outside of all the obstacles in `obstacles`.
                Otherwise return False.
        """

        # Store x,y coordinates of point
        x = q[0]
        y = q[1]

        for i in range(0, len(obstacles)):

            # Store current obstacle
            curr_obstacle = obstacles[i]

            # If obstacle is a circle
            if len(obstacles[i]) == 2:

                # Store circle center (x,y) value
                center = curr_obstacle[0]
                center_x = center[0]
                center_y = center[1]

                # Store circle radius
                r = curr_obstacle[1]

                # Set bounds of y for circle at current point
                y_max = center_y + np.sqrt(np.abs(r**2 - (x-center_x)**2))
                y_min = center_y - np.sqrt(np.abs(r**2 - (x-center_x)**2))

                # Set bounds of x for circle at current point
                x_max = center_x + np.sqrt(np.abs(r**2 - (y-center_y)**2))
                x_min = center_x - np.sqrt(np.abs(r**2 - (y-center_y)**2))

                # Check bounds of current y
                if ((y >= y_min) and (y <= y_max) and (x >= x_min) and (x <= x_max)):
                    return False

            # If obstacle is a rectangle
            if len(obstacles[i]) != 2 and obstacles[i][0] == tuple:
                x1 = curr_obstacle.vertices[0]
                x2 = curr_obstacle.vertices[3]
                y1 = curr_obstacle.vertices[1]
                y2 = curr_obstacle.vertices[2]

                if ((x > x1) and (x < x2) and (y > y1) and (y < y2)):
                    return False

            # If obstacle is a triangle
            else:
                ax, ay = curr_obstacle[0]
                bx, by = curr_obstacle[1]
                cx, cy = curr_obstacle[2]

                # Line 1
                side_1 = (x - bx) * (ay - by) - (ax - bx) * (y - by)
                # Line 2

                side_2 = (x - cx) * (by - cy) - (bx - cx) * (y - cy)

                # Line 3
                side_3 = (x - ax) * (cy - ay) - (cx - ax) * (y - ay)

                inside = (side_1 < 0.0) == (side_2 < 0.0) == (side_3 < 0.0)

                if inside is True:
                    return False

        return True

    # Given three collinear points p, q, r, the function checks if
    # point q lies on line segment 'pr'
    def onSegment(self, p, q, r):
        if ((q.x <= max(p.x, r.x)) and (q.x >= min(p.x, r.x)) and
                (q.y <= max(p.y, r.y)) and (q.y >= min(p.y, r.y))):
            return True
        return False

    def orientation(self, p, q, r):
        # To find the orientation of an ordered triplet (p,q,r)
        # function returns the following values:
        # 0 : Collinear points
        # 1 : Clockwise points
        # 2 : Counterclockwise

        val = (float(q.y - p.y) * (r.x - q.x)) - (float(q.x - p.x) * (r.y - q.y))
        if (val > 0):

            # Clockwise orientation
            return 1
        elif (val < 0):

            # Counterclockwise orientation
            return 2
        else:

            # Collinear orientation
            return 0

    # The main function that returns true if
    # the line segment 'p1q1' and 'p2q2' intersect.
    def doIntersect(self, p1, q1, p2, q2):

        # Find the 4 orientations required for
        # the general and special cases
        o1 = self.orientation(p1, q1, p2)
        o2 = self.orientation(p1, q1, q2)
        o3 = self.orientation(p2, q2, p1)
        o4 = self.orientation(p2, q2, q1)

        # General case
        if ((o1 != o2) and (o3 != o4)):
            return True

        # Special Cases

        # p1 , q1 and p2 are collinear and p2 lies on segment p1q1
        if ((o1 == 0) and self.onSegment(p1, p2, q1)):
            return True

        # p1 , q1 and q2 are collinear and q2 lies on segment p1q1
        if ((o2 == 0) and self.onSegment(p1, q2, q1)):
            return True

        # p2 , q2 and p1 are collinear and p1 lies on segment p2q2
        if ((o3 == 0) and self.onSegment(p2, p1, q2)):
            return True

        # p2 , q2 and q1 are collinear and q1 lies on segment p2q2
        if ((o4 == 0) and self.onSegment(p2, q1, q2)):
            return True

        # If none of the cases
        return False

    def edge_free(self, edge: Tuple[np.ndarray, np.ndarray], obstacles: List[Tuple[np.ndarray, float]]) -> bool:
        """
        Check if a graph edge is in the free space.

        This function checks if a graph edge, i.e. a line segment specified as two end points, lies entirely outside of
        every obstacle in the configuration space.

        @param edge: A tuple containing the two segment endpoints.
        @param obstacles: A list of obstacles as described.
        @return: True if the edge is in the free space, i.e. it lies entirely outside of all the obstacles in `obstacles`.
                    Otherwise return False.
        """

        o = edge[0]
        f = edge[1]

        u = (f-o)
        u_norm = u/np.linalg.norm(u)

        for i in range(0, len(obstacles)):
            curr_obstacle = obstacles[i]

            # If the obstacle is a circle
            if len(curr_obstacle) == 2:

                # Store circle center (x,y) value
                c = curr_obstacle[0]
                # Store circle radius
                r = curr_obstacle[1]

                # Solve for nabla
                nabla = (np.dot(u_norm, (o - c)))**2 - (np.dot(o - c, o - c) - r ** 2)

                if (nabla >= 0):
                    return False

            # Obstacle is either a rectangle or a triangle
            else:

                # Iterates through all lines of each polygon
                for k in obstacles[i].lines:
                    new_p2 = obstacles[i].lines[k][0]
                    new_q2 = obstacles[i].lines[k][1]

                    if self.doIntersect(o, f, new_p2, new_q2):
                        return False

        return True

    def random_conf(self, width: float, height: float) -> np.ndarray:
        """
        Sample a random configuration from the configuration space.

        This function draws a uniformly random configuration from the configuration space rectangle. The configuration
        does not necessarily have to reside in the free space.

        @param width: The configuration space width.
        @param height: The configuration space height.
        @return: A random configuration uniformily distributed across the configuration space.
        """

        # Randomly sample x and y values
        x_val = width * np.random.rand()
        y_val = height * np.random.rand()

        conf = np.zeros(2)
        conf[0] = x_val
        conf[1] = y_val

        return conf

    def random_free_conf(self, width: float, height: float, obstacles: List[Tuple[np.ndarray, float]]) -> np.ndarray:
        """
        Sample a random configuration from the free space.

        This function draws a uniformly random configuration from the configuration space
        rectangle that lies in the free space.

        @param width: The configuration space width.
        @param height: The configuration space height.
        @param obstacles: The list of configuration space obstacles as defined in `edge_free` and `conf_free`.
        @return: A random configuration uniformily distributed across the configuration space.

        """

        # Check if in free space
        free_flag = True
        while free_flag:

            new_conf = self.random_conf(width, height)
            free = self.conf_free(new_conf, obstacles)

            if free:
                free_flag = False
                conf_result = new_conf

        return conf_result

    def nearest_vertex(self, conf: np.ndarray, vertices: np.ndarray) -> int:
        """
        Finds the nearest vertex to conf in the set of vertices.

        This function searches through the set of vertices and finds the one that is closest to
        conf using the L2 norm (Euclidean distance).

        @param conf: The configuration we are trying to find the closest vertex to.
        @param vertices: The set of vertices represented as an np.array with shape (n, 2). Each row represents
                        a vertex.
        @return: The index (i.e. row of `vertices`) of the vertex that is closest to `conf`.

        """

        min_dist = np.Inf

        # Calc Euclidean distance and store min
        for i in range(0, vertices.shape[0]):
            dist = np.sqrt((conf[0]-vertices[i][0])**2 + (conf[1] - vertices[i][1])**2)

            if (dist < min):
                min_dist = dist
                index = i

        return index

        # Need to add extend() function

    def edges_of(self, vertices):
        """
        Return the vectors for the edges of the polygon p.

        p is a polygon.
        """
        edges = []
        N = len(vertices)

        for i in range(N):
            edge = vertices[(i + 1) % N] - vertices[i]
            edges.append(edge)

        return edges

    def orthogonal(self, v):
        """
        Return a 90 degree clockwise rotation of the vector v.
        """
        return np.array([-v[1], v[0]])

    def is_separating_axis(self, o, p1, p2):
        """
        Return True and the push vector if o is a separating axis of p1 and p2.
        Otherwise, return False and None.
        """
        min1, max1 = float('+inf'), float('-inf')
        min2, max2 = float('+inf'), float('-inf')

        for v in p1:
            projection = np.dot(v, o)

            min1 = min(min1, projection)
            max1 = max(max1, projection)

        for v in p2:
            projection = np.dot(v, o)

            min2 = min(min2, projection)
            max2 = max(max2, projection)

        if max1 >= min2 and max2 >= min1:
            d = min(max2 - min1, max1 - min2)
            # push a bit more than needed so the shapes do not overlap in future
            # tests due to float precision
            d_over_o_squared = d/np.dot(o, o) + 1e-10
            pv = d_over_o_squared*o
            return False, pv
        else:
            return True, None

    def polygonCollide(self, p1, p2):
        '''
        Return True and the MPV if the shapes collide. Otherwise, return False and
        None.

        p1 and p2 are lists of ordered pairs, the vertices of the polygons in the
        counterclockwise direction.
        '''

        p1 = [np.array(v, 'float64') for v in p1]
        p2 = [np.array(v, 'float64') for v in p2]

        edges = self.edges_of(p1)
        edges += self.edges_of(p2)
        orthogonals = [self.orthogonal(e) for e in edges]

        push_vectors = []
        for o in orthogonals:
            separates, pv = self.is_separating_axis(o, p1, p2)

            if separates:
                # they do not collide and there is no push vector
                return False, None
            else:
                push_vectors.append(pv)

        # they do collide and the push_vector with the smallest length is the MPV
        mpv = min(push_vectors, key=(lambda v: np.dot(v, v)))

        # assert mpv pushes p1 away from p2
        d = self.centers_displacement(p1, p2)  # direction from p1 to p2
        if np.dot(d, mpv) > 0:  # if it's the same direction, then invert
            mpv = -mpv

        return True, mpv

    def centers_displacement(self, p1, p2):
        """
        Return the displacement between the geometric center of p1 and p2.
        """
        # Geometric center
        c1 = np.mean(np.array(p1), axis=0)
        c2 = np.mean(np.array(p2), axis=0)
        return c2 - c1