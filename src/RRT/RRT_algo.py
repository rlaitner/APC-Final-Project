from pathingSim.pathing_algorithm import PathingAlgorithm
from RRT.obstacle_collision_detection import *
from RRT.point_obstacle_collision_detection import *
import numpy as np
from typing import List, Tuple

class RRT(PathingAlgorithm):
    def __init__(self, vehicle):
        self.vehicle = vehicle
        self.path_list = None
        self.configured = False

    def set_config(self, algo_dict, setting):
        self.origin = algo_dict["origin"]
        self.width = setting.x
        self.height = setting.y
        self.obstacles = setting.obstacles
        self.trials = algo_dict["hyper-parameters"][0]
        self.step_size = algo_dict["hyper-parameters"][1]
        self.goal = algo_dict["goal"]
        self.configured = True

    def make_route(self, origin):
        if self.configured == False:
            raise RuntimeError("No information available to be configured with")
            
        if self.path_list is None:
            vertices, parents = self.rrt(origin, self.width, self.height, self.obstacles, self.trials, self.step_size, self.vehicle, self.goal)
            index = self.nearest_vertex(self.goal, vertices)
            self.path_list = self.backtrack(index, parents)
            for i in range(len(path_list)):
                # List of vertices
                self.path_list.append([vertices[self.path_list[i]][0], vertices[self.path_list[i]][1]])
                self.path_list.pop(0)

        else:
            index = None
            for i in range(len(self.path_list)):
                if self.path_list[i] == origin:
                    index = i
            
            if self.path_list[i] != origin:
                self.path_list = None
                return self.make_route(origin)

            else:
                return self.path_list[index:]

    def conf_free(q, obstacles):

        """
        Checks to see if a configuration is in free space.
        
        This function checks if the configuration q lies outside of all the obstacles in the environment.
        
        q: A configuration represented as an np.ndarray of shape (2,) representing a random location.
        obstacles: A list of obstacle objects.

        return: True if the configuration is in free space, i.e. it lies outside of all the obstacles in 'obstacles'. 
        Otherwise return False.
        """

        for o in obstacles:
            # If obstacle is a circle
            if o.shape == "circle":
                collision = is_inside_circle(q, o)

                if collision:
                    return False
                
            # If obstacle is a polygon
            else:
                collision = is_inside_polygon(q, o.verts)
                if collision:
                    return False

        return True

    def random_conf(width, height):
        """
        Sample a random configuration from the environment.
        
        This function draws a uniformly random configuration from the environment rectangle. The configuration 
        does not necessarily have to reside in the free space.
        
        width: The configuration space width.
        height: The configuration space height.

        return: A random configuration uniformily distributed across the environment.
        """
        
        # Randomly sample x and y values 
        x_val = width * np.random.rand()
        y_val = height * np.random.rand()
        
        conf = np.zeros(2)
        conf[0] = x_val
        conf[1] = y_val

        return conf

    def random_free_conf(width, height, obstacles):
        """
        Sample a random configuration from free space.
        
        This function draws a uniformly random configuration from the environment rectangle that lies in free space.
        
        width: The configuration space width.
        height: The configuration space height.
        obstacles: The list of configuration space obstacles as defined in 'edge_free' and 'conf_free'.

        return: A random configuration uniformily distributed across the environment.
        """
        
        # Check if in free space 
        free_flag = True 
        while free_flag:
            
            new_conf = random_conf(width, height)
            free = conf_free(new_conf, obstacles)
            
            if free:
                free_flag = False
                conf_result = new_conf
                
        return conf_result

    def nearest_vertex(conf: np.ndarray, vertices: np.ndarray) -> int:
        """
        Finds the nearest vertex to conf in the set of vertices.
        
        This function searches through the set of vertices and finds the one that is closest to 
        conf using the L2 norm (Euclidean distance).
        
        conf: The configuration we are trying to find the closest vertex to.
        vertices: The set of vertices represented as an np.array with shape (n, 2). Each row represents
        a vertex.

        return: The index (i.e. row of `vertices`) of the vertex that is closest to 'conf'.
        """
        
        min_dist = np.Inf
        
        # Calc Euclidean distance and store min
        for i in range(0, vertices.shape[0]):
            dist = np.sqrt((conf[0]-vertices[i][0])**2 + (conf[1] - vertices[i][1])**2)
            
            if (dist < min_dist):
                min_dist = dist 
                index = i
        
        return index

    def extend(origin, target, step_size: float=0.2):
        """
        Extends the RRT at most a fixed distance towards the target configuration. Given a configuration in the RRT graph 'origin', 
        this function returns a new configuration that takes a step of at most 'step_size' towards the 'target' configuration. 

        origin: A vertex in the RRT graph to be extended.
        target: The vertex that is being extended towards.
        step_size: The maximum allowed distance the returned vertex can be from 'origin'.
        
        return: A new configuration that is as close to 'target' as possible without being more than 'step_size' away from 'origin'.
        """
    
        # Check Euclidean distance and move in that direction based on step size 
        dist = np.sqrt((origin[0]-target[0])**2 + (origin[1] - target[1])**2)
        if dist < step_size:
            return target 
        else: 
            u = (target-origin)
            u_norm = u/np.linalg.norm(u)
            new_conf = origin + (step_size * u_norm)
        
        return new_conf

    def rrt(origin, width, height, obstacles, trials, step_size, vehicle):
        """
        Explore a workspace using the RRT algorithm.
        
        This function builds an RRT using `trials` samples from the free space.
        
        origin: The starting configuration of the robot.
        width: The width of the configuration space.
        height: The height of the configuration space.
        obstacles: A list of obstacles.
        trials: The number of configurations to sample from the free space.
        step_size: The step_size to pass to 'extend'.
        
        return: A tuple ('vertices', 'parents'), where 'vertices' is an (n, 2) 'np.ndarray' where each row is 
        a configuration vertex and 'parents' is an array identifying the parent, i.e. 'parents[i]' is the parent 
        of the vertex in the i'th row of 'vertices'.
        """
        
        # Check if initialized vehicle collides w/ obstacles
        obstacle_free = free_vehicle(vehicle, [vehicle.x_init, vehicle.y_init], obstacles)
        
        if obstacle_free == False:
            raise RuntimeError("Vehicle in collision w/ obstacle")
            
        num_verts = 1
        
        vertices = np.zeros((trials + 1, len(origin)))
        vertices[0, :] = origin
        parents = np.zeros(trials + 1, dtype=int)
        parents[0] = -1
        
        # Run RRT 
        for trial in range(trials):
            
            # Samples a new random configuration
            q_rand = random_free_conf(width, height, obstacles)
            
            # Finds index of the vertex that is the closest to the newly sampled configuration
            q_near_index = nearest_vertex(q_rand, vertices)
            q_near = vertices[q_near_index, :]
            
            # Extends from the identified closest vertex to the direction of the newly sampled configuration
            q_s = extend(q_near, q_rand)
            
            if free_vehicle(vehicle, q_s, obstacles):  
                vertices[num_verts, :] = q_s
                parents[num_verts] =  q_near_index
                num_verts +=1
                
        return vertices[:num_verts, :], parents[:num_verts]

    def backtrack(index, parents):
        """
        Find the sequence of nodes from the origin of the graph to an index.
        
        This function returns a List of vertex indices going from the origin vertex to the vertex 'index'.
        
        index: The vertex to find the path through the tree to.
        parents: The array of vertex parents as specified in the 'rrt' function.
        
        return: The list of vertex indicies such that specifies a path through the graph to 'index'.
        """
        
        # Track the root 
        path_reverse = []
        path = []
        path_reverse.append(index)
        current_index = index
        
        while current_index != -1:
            parent_index = parents[current_index] 
            path_reverse.append(parent_index)
            current_index = parent_index 
            
        for i in range(0, len(path_reverse)):
            path.append(path_reverse[len(path_reverse) - i - 1])
            
        return path
