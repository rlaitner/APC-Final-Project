"""
The driver for a trajectory planning algorithm for custom environments.

Classes
-------
Simulator
"""
from pathlib import Path
import json
import numpy as np

from pathingSim.visualizer import Visualizer
from pathingSim.environment import Environment
from pathingSim.agent import Agent


class Simulator():
    def __init__(self, config_file: str) -> None:
        # Acquire config options
        path = Path(config_file)
        if path.is_file is not True:
            raise FileNotFoundError(f"Config file '{config_file}' does" +
                                    " not exist.")
        with open(config_file) as f:
            self._configs = json.load(f)

        # Parse the configs
        self._environment_configs = self._configs["environment"]
        self._vehicle_configs = self._configs["vehicle"]
        self._algorithm_configs = self._configs["algorithm"]
        self._obstacles_configs = self._configs["obstacles"]

        self._field_size = (self._environment_configs["length"],
                            self._environment_configs["width"]
                            )

        # Instantiate classes
        self._illustrator = Visualizer()
        self._setting = Environment(self._field_size, self._obstacles_configs)
        self._robot = Agent(self._vehicle_configs, self._algorithm_configs, self._setting)

        # Find relevant timing data
        self.time_horizon = self._algorithm_configs["total_time"]
        self.time_step = self._algorithm_configs["time_step"]

        # Get goal size
        self.radius = self._algorithm_configs["goal_radius"]

    def _is_in_goal(self) -> bool:
        """Checks if the agent is within the goal set"""
        diff = self._robot.pos - self._robot.goal
        circle = np.sum(diff * diff)

        return bool(circle <= self.radius * self.radius)

    def run(self) -> bool:
        """Simulates the world for a predetermined amount of time"""
        num_steps = self.time_horizon // self.time_step
        steps = np.linspace(0, self.time_horizon, num=num_steps)

        # is it initially in the goal set?
        time = 0
        if self._is_in_goal():
            print(f"The simulation converged in {time}.")
            return True
        # can it get to the goal set?
        for step in steps:
            time += step
            self._robot.step_toward_goal()
            if self._is_in_goal():
                print(f"The simulation converged in {time}.")
                return True

        return False

    def animate() -> None:
        pass

def main():
    pass

if __name__ == "main":
    main()