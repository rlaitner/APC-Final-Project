PathingSim
______________________________________________________________

Contains the following classes: 

.. py:class:: agent.py

Attributes 


	.. code-block:: python

	   pos: np.ndarray[float, float]
	   heading: float
           vehicle: Vehicle
	   trajectory: np.ndarray[np.ndarray[float, ...], np.ndarray[float, ...]]
	   goal: np.ndarray[float, float]

Functions 


	.. code-block:: python

	   def get_angle()
	   def step_toward_goal()



-

.. py:class:: algo_factory.py

Functions

	
	.. code-block:: python 

	   def algo_factory()




-

.. py:class:: environment.py

Attributes


	.. code-block:: python

	   x: double
	   y: double
	   obstacles: list

Functions 


	.. code-block:: python

	   def is_in_environment()

-

.. py:class:: pathing_algorithm.py

Functions


	.. code-block:: python

	   def make_route()
	   def set_config()



-

.. py:class:: simulator.py 

Functions

	.. code-block:: python

	   def _is_in_goal()
	   def run()
	   def animate()
	   def main()




