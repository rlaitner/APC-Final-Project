import numpy as np
import obstacles
import vehicle_class


class Vertex():
    """A class for vertices"""
    def __init__(self, parent=None, position=None):
        self.parent = parent  # Keeps track of parent of a vertex
        self.position = position  # Keeps track of position of a vertex

        self.C = float('inf')  # Initialize cost-to-come (origin -> current vertex)
        self.H = 0  # Initialize cost-to-go (current vertex -> goal)
        self.F = float('inf')  # total cost F = C + H

    def __eq__(self, other):  # Check if two vertices are the same by doing "vertex_1 == vertex_2"
        return self.position == other.position


def getNeighbors(x_vertex, maze):
    """Get neighbors of x_vertex"""
    neighbors = []
    for new_position in [(-1, 0), (0, 1), (1, 0), (0, -1)]:  # Adjacent vertices

        # Get node position
        vertex_position = (x_vertex.position[0] + new_position[0], x_vertex.position[1] + new_position[1])

        # Make sure it is within range
        if vertex_position[0] > (len(maze) - 1) or vertex_position[0] < 0 or vertex_position[1] > (
                len(maze[len(maze) - 1]) - 1) or vertex_position[1] < 0:
            continue

        # Make sure it is not occupied by an obstacle
        if maze[len(maze) - vertex_position[1] - 1][vertex_position[0]] != 0:
            continue

        # Create new vertex
        new_vertex = Vertex(None, vertex_position)

        # Append
        neighbors.append(new_vertex)

    return neighbors


############################################################################################################


def GetBestVertex(Q):
    """Get the vertex "x_vertex" in Q that has the lowest value of F"""
    """Returns x_vertex and the index of x_vertex in Q"""
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
    """Function for computing heuristic H(vertex). To compute H(vertex), use computeH(vertex,B_vertex)"""
    """Recall that the heuristic is an underestimate of the cost-to-go from a vertex to the goal"""

    H = abs(vertex.position[0] - B_vertex.position[0]) + abs(vertex.position[1] - B_vertex.position[1])

    return H


##########################################################################################


######### This is the function that implements A star #########
def astar(maze, A, B):
    """Returns a list of tuples as a path from A to B in the given maze"""

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
    ############################################################################################

    # Loop until you get to the goal
    while len(Q) > 0:

        # Get the current vertex: "x_vertex", i.e., the one that has the lowest value of F
        x_vertex, x_index = GetBestVertex(Q)  # Implement this function
        ########################################################################################

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
        #####################################################################################

        # Generate neighbors
        neighbors = getNeighbors(x_vertex, maze)
        #####################################################################################

        # Loop through neighbors, update costs, etc.
        for x_prime in neighbors:

            if x_prime in DeadSet:
                continue

            # x_vertex.C = abs(x.position[0] - A_vertex.position[0]) + abs(x.position[1] - A_vertex.position[1])
            # x_vertex.H = computeH(x_vertex,B_vertex)
            # x_vertex.F = x_vertex.C + x_vertex.H

            # x_prime.C = abs(x.position[0] - A_vertex.position[0]) + abs(x.position[1] - A_vertex.position[1])
            # x_prime.H = computeH(x_prime,B_vertex)
            # x_prime.F = x_vertex.C + x_vertex.H

            tentative_C = x_vertex.C + 1

            if tentative_C < x_prime.C:
                x_prime.parent = x_vertex
                x_prime.C = tentative_C
                x_prime.H = computeH(x_prime, B_vertex)
                x_prime.F = x_prime.C + x_prime.H
                if x_prime not in Q:
                    Q.append(x_prime)

        ##########################################################


##############################################################################################


maze = [[0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 1, 0, 1, 1, 1, 0],
        [0, 0, 1, 1, 1, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 1, 1, 1, 1, 1, 1, 1, 1, 0],
        [0, 0, 0, 0, 0, 0, 1, 1, 0, 0],
        [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 1, 0, 1, 0, 0, 0],
        [1, 1, 1, 1, 1, 0, 1, 1, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 1, 0, 0]]

A = (0, 0)
B = (7, 6)

path = astar(maze, A, B)
print(path)

############################################################################################


# Visualization
%matplotlib inline
import matplotlib.pyplot as plt
import numpy as np

maze_modified = 1.0 - np.array(maze)
for v in path:
    maze_modified[len(maze) - v[1] - 1][v[0]] = 0.8
maze_modified[len(maze) - A[1] - 1][A[0]] = 0.7
maze_modified[len(maze) - B[1] - 1][B[0]] = 0.7

plt.imshow(maze_modified);  # , cmap='hot');
plt.axis('off');

