"""
The driver for a trajectory planning algorithm for custom environments.

Classes
-------
Simulator
"""
from pathlib import Path
import json

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
        self._robot = Agent(self._vehicle_configs, self._algorithm_configs)


    def run() -> None:
        pass

    def animate() -> None:
        pass

def main():
    pass

if __name__ == "main":
    main()