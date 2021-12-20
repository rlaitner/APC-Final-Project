"""
The driver for a trajectory planning algorithm for custom environments.

Classes
-------
Simulator
"""
import json
import sys
import numpy as np
from pathlib import Path
from typing import Union
from matplotlib import pyplot as plt

from visualizer_class.visualizer import Visualizer
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
        self._setting = Environment(self._field_size,
                                    self._obstacles_configs
                                    )
        self._robot = Agent(self._vehicle_configs,
                            self._algorithm_configs,
                            self._setting
                            )
        self._illustrator = Visualizer(self._field_size,
                                       self._setting.obstacles,
                                       self._robot.vehicle
                                       )

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
            try:
                self._robot.step_toward_goal()
            except Exception as e:
                raise RuntimeError(f"Simulation failed with error {e}.")
            if self._is_in_goal():
                print(f"The simulation converged in {time}.")
                return True

        return False

    def animate(self, file_name: Union[str, None] = None) -> None:
        fig, ax = self._illustrator.render_environment()
        ani = self._illustrator.render_path(self._robot.trajectory, fig, ax)

        try:
            ani.save(file_name)
        except Exception:
            pass  # Don't block KeyboardInterrupt
        finally:
            plt.show()


def main():
    try:
        JSON_file = sys.argv[1]
    except IndexError:
        raise ValueError("Please provide a valid config file path.")

    sim = Simulator(JSON_file)

    if sim.run():
        sim.animate()
    else:
        print("Simulation failed to converge.")

if __name__ == "main":
    main()
