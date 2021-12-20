"""
Create environments full of obstacles.

Classes:
    Environment
"""
from warnings import warn
import typing

from obstacle_class.obstacle import Obstacle


class Environment:
    """
    Make an environment object

    Attributes:
    -----------
    x : double
        Width of the environment in arbitrary units
    y : double
        Length of the environment in arbitrary units
    obstacles : list
        A list of all of the obstacles in the environment

    This class defines an environment object which consists of a 2d
    field of pre-defined size and potentially a series of obstacles.

    Methods
    -------
    is_in_environment():
        Checks if a given obstacle is valid

    """

    def __init__(self,
                 dimensions: typing.Tuple[typing.Union[int, float], ...],
                 obstacles: typing.Optional[dict]) -> None:  # type: ignore
        """
        Constructs the necessary attributes for an environment object.

        Parameters
        ----------
            dimensions : tuple
                Positive width and length of the working field
            obstacles : dict
                Necessary data for creation of obstacle hazards

        Returns
        -------
            None

        Raises
        ------
            TypeError : Invalid parameters given for field size
            ValueError : Out of bounds parameters given for field size
        """
        (self.x, self.y, *self.z) = dimensions
        if not isinstance(self.x, (int, float)) \
           or not isinstance(self.y, (int, float)):
            raise TypeError(f"Expected numeric values for field size but \
                            received {self.x} and {self.y}")
        if self.x <= 0 or self.y <= 0:
            raise ValueError("The working field must have positive,"
                             " non-zero width and length.")
        if self.z is not None:
            warn("An environment with more than 2 dimensions was specified, \
                  but only 2 are currently supported.")

        if obstacles is None:  # allow for an empty field
            return

        potential_obstacles = []
        while True:
            try:
                print(f"{obstacles=}")
                item = obstacles.popitem()
                print(f"{item=}")
                key = item[0]
                print(f"{obstacles=}")
                for i in range(obstacles[key]["number"]):
                    # i'm sorry :'(
                    if key == "circle":
                        pos = (obstacles[key]["center_x"], obstacles[key]["center_y"])
                    elif key == "triangle":
                        pos = obstacles[key]["vertices"][i]
                    elif key == "rectangles":
                        pos = obstacles[key]["origin"][i]
                    else:
                        raise ValueError("Received an invalid obstacle type.")

                    data = {k:v[i] for (k, v) in obstacles[key].items()}
                    potential_obstacles.append(Obstacle(pos, data))
            except KeyError:
                break

        self.obstacles = [obstacle for obstacle in potential_obstacles
                          if self.is_in_environment(obstacle)]

    def __str__(self) -> str:
        try:
            return f"Size: ({self.x}, {self.y}) with {len(self.obstacles)} \
                    obstacles: {self.obstacles}"
        except TypeError:
            return f"Size: ({self.x}, {self.y}) with 0 obstacles"

    def __repr__(self) -> str:
        return f"Evironment({self.x}, {self.y}, {self.obstacles})"

    def is_in_environment(self, hazard: Obstacle) -> bool:
        """
        Checks if a given obstacle is inside of the environment

        Parameters
        ----------
            hazard: Obstacle
                obstacle to validate

        Returns
        -------
            bool
        """
        for vertex in hazard.vertices:
            if (vertex[0] > 0 and vertex[0] < self.x and
               vertex[1] > 0 and vertex[1] < self.y):
                return True

        return False
