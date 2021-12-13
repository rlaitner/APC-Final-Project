Algorithm Factory
======================

.. py:class:: algo_factory.py
______________________________

Generates a PathingAlgorithm class to be used by higher level code.
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

**Functions:**
Returns a PathingAlgorithm object of a specified type:  

.. code-block:: python
	
	from typing import Type, Dict

	from pathingSim.pathing_algorithm import PathingAlgorithm
	from pathingSim.a_star import AStar
	from pathingSim.RRT import RRT

.. code-block:: python
	
	def algo_factory(chosen_algo: str) -> PathingAlgorithm

Returns an instantiated implementation of a PathingAlgorithm object. 

**Parameters**

chosen_aglo: str
	A string that specifies the desired pathing algorithm to use.

	The possible algorithms currently are: 

	* A*: The A* search algorithm
	* RRT: The rapidly-exploring random tree algorithm 

**Returns**

PathingAlgorithm
	Implementation of pathing algorithm specified by input parameter 

**Raises**
 
NotImplementedError
	Raised when a pathing algorithm is chosen that does not exist in the factor and cannot be provided 

.. code-block:: python

	possible: Dict[str, Type[PathingAlgorithm]]
	possible = {
		"A*": AStar,
		"RRT": RRT
	}

	try:
		return possible[chosen_algo]()
	except KeyError:
		raise NotImplementedError(f"The specified algorithm {chosen_algo}" +
					  " is invalid.")


 


