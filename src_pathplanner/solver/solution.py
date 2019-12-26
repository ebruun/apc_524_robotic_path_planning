# solution.py
# Author(s): Edvard Bruun

import numpy as np
#import domain

class Solution:
	""" A class to step through the RRT algorithm and store solution graph.

	:param vertex: list of vertices in the graph
	:type vertex: tuple(x,y,z) - coords.
	:param vertex_parent: list of indices of parents of a vertex
	:type vertex_parent: int
	:param vertex_cost: list of costs (distances) of a path up to a vertex
	:type vertex_cost: float	

	"""
	
	def __init__(self,input_params):
		self.params = input_params

		self.vertices = np.zeros(self.params.n_trials, dtype=float)
		self.parents = np.zeros(self.params.n_trials, dtype=int)
		self.costs = np.zeros(self.params.n_trials, dtype=float)
		
	def algorithm_step(self):
		"""  This function steps through one iteration of the solution algorithm.

	    Returns:
	       Updated lists::

	          vertex
	          vertex_parent
	          vertex_cost

		"""

		#TO DO...

		return True
		
	def check_completion(self):
		"""  This function checks if the goal has been reached after an iteration.

		Returns:
			bool.::

			 True -- Goal Reached.
			 False -- Goal Not Reached.

		"""

		completed = True

		if completed:
			print("--Completed")
			return True
		
		print("--Not Completed")
		return False
