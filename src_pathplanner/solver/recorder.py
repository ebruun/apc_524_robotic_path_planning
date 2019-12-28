# recorder.py
# Author(s): Edvard Bruun

import numpy as np

class Recorder:
	""" A class to save the data from the path planning algorithm.

	:param vertex: list of vertices in the graph
	:type vertex: tuple(x,y,z) - coords.
	:param vertex_parent: list of indices of parents of a vertex
	:type vertex_parent: int
	:param vertex_cost: list of costs (distances) of a path up to a vertex
	:type vertex_cost: float	

	"""
	
	def __init__(self,input_params):
		self.params = input_params

		self.vertices = np.zeros((self.params.n_trials,self.params.dims), dtype=float)
		self.vertices.fill(np.nan)

		self.parents = np.zeros(self.params.n_trials, dtype=float)
		self.parents.fill(np.nan)

		self.costs = np.zeros(self.params.n_trials, dtype=float)
		self.costs.fill(np.nan)


