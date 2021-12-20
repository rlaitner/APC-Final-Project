import numpy as np
import obstacles
import vehicle_class



###########

class A_star(PathingAlgorithm):
    """
    This class contains all methods necessary for the A* graph search algorithm.
    It is a concrete implementation of the abstract PathingAlgorithm class.

    Methods
    -------



    make_route(np.ndarray[float, float])
        Takes in a starting location and navigates a viable route to a
        goal
    """

    def __init__(self):




    class Vertex():
        """
        A class to store vertices and their associated information.

        Attributes:
        ----------
            parent: the originating node of the vertex
            position: coordinates of the vertex
            C: cost-to-come (origin -> current vertex)
            H: estimated cost-to-go (current vertex -> goal)
            F: total cost (F = C + H)

        Methods:
        -------
            None
        """

        def __init__(self, parent=None, position=None):
            self.parent = parent
            self.position = position

            self.C = float('inf')
            self.H = 0
            self.F = float('inf')

        def __eq__(self, other):
            return self.position == other.position

    def getNeighbors(x_vertex, grid, resolution):
        """
        Get neighbors of x_vertex
        """

        neighbors = []
        for new_position in [(-1, 0), (0, 1), (1, 0), (0, -1)]:  # adjacent vertices

            # get node position
            vertex_position = (x_vertex.position[0] + new_position[0], x_vertex.position[1] + new_position[1])

            # make sure it is within range
            if vertex_position[0] > ((np.shape(grid)[1] / resolution) - 1) or vertex_position[0] < 0 or vertex_position[1] > \
                    ((np.shape(grid)[0] / resolution) - 1) or vertex_position[1] < 0:
                continue

            # make sure it is not occupied by an obstacle
            if grid[vertex_position[1] * resolution, vertex_position[0] * resolution] != 0:
                continue

            # create new vertex
            new_vertex = Vertex(None, vertex_position)
            neighbors.append(new_vertex)

        return neighbors

    def GetBestVertex(Q):
        """
        Get the vertex "x_vertex" in Q that has the lowest value of F
        Returns x_vertex and the index of x_vertex in Q
        """

        F = []

        for i in range(len(Q)):
            candidate_vertex = Q[i]
            F.append(candidate_vertex.F)

        F_min = min(F)

        for i in range(len(F)):
            if F[i] == F_min:
                x_index = i
                break

        x_vertex = Q[x_index]
        return x_vertex, x_index

    def computeH(vertex, B_vertex):
        """
        Function for computing heuristic H(vertex). To compute H(vertex), use computeH(vertex,B_vertex)
        the heuristic is an underestimate of the cost-to-go from a vertex to the goal
        """

        H = abs(vertex.position[0] - B_vertex.position[0]) + abs(vertex.position[1] - B_vertex.position[1])

        return H


    ######### This is the function that implements A star #########
    def make_route(grid, A, B):
        """
        Returns a list of tuples as a path from A to B in the given maze
        """

        # Create start and end vertices
        A_vertex = Vertex(None, A)
        B_vertex = Vertex(None, B)
        A_vertex.C = 0
        A_vertex.H = computeH(A_vertex, B_vertex)
        A_vertex.F = A_vertex.H

        # Initialize Q and "dead" state list
        Q = []
        Q.append(A_vertex)
        DeadSet = []


        # Loop until you get to the goal
        while len(Q) > 0:

            # Get the current vertex: "x_vertex", i.e., the one that has the lowest value of F
            x_vertex, x_index = GetBestVertex(Q)  # Implement this function


            # Check if we are at the goal vertex B
            if x_vertex == B_vertex:
                # If we are, backtrack to get the path
                path = []
                current = x_vertex
                while current is not None:
                    path.append(current.position)
                    current = current.parent
                return path[::-1]  # Return reversed path
            #####################################################################################

            # Remove x_vertex from Q, add to dead list

            Q.remove(Q[x_index])

            DeadSet.append(x_vertex)


            # Generate neighbors
            neighbors = getNeighbors(x_vertex, grid, resolution)


            # Loop through neighbors, update costs, etc.
            for x_prime in neighbors:

                if x_prime in DeadSet:
                    continue

                tentative_C = x_vertex.C + 1

                if tentative_C < x_prime.C:
                    x_prime.parent = x_vertex
                    x_prime.C = tentative_C
                    x_prime.H = computeH(x_prime, B_vertex)
                    x_prime.F = x_prime.C + x_prime.H
                    if x_prime not in Q:
                        Q.append(x_prime)


