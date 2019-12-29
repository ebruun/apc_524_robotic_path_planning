# stepper.py
# Author(s): Edvard Bruun

import numpy as np

from solver.recorder import Recorder
from solver.stepper import Stepper
#import domain

class Solution:
	""" A class to step through the full RRT algorithm.

	Take the :class:`solver.stepper` module

	Take the :class:`solver.recorder` module

	"""

	path_verts = []

	def __init__(self,params):
		self.params = params
		self.solution_record = Recorder(params)
		self.stepper = Stepper(params)

	def run_algorithm(self):
		"""  Returns::

				void

		This function runs through all the iterations of the solution algorithm.

		"""	

		for trial in range(self.params.n_trials):
			print("\nIteration # ", trial+1)
			self.stepper.do_singlestep(self.solution_record, trial)


		


		
	def check_completion(self):
		"""  
		Returns::

			True -- Goal Reached.
			False -- Goal Not Reached.

		This function checks if the goal has been reached.


		"""

		index = self.nearest_vertex(goal[0], vertices)

		if np.linalg.norm(vertices[index, :] - goal[0]) < 0.25:
			print('Step 5: Path found!')
			self.path_verts = self.backtrack(index, parents)
		else:
			print('Step 5: No path found!')
			path_verts = []
		
		return completed

	def nearest_vertex(self,goal):
		"""  
		Returns::

			index of nearest vertex to the specified goal

		This function finds which vertex is closest to the goal.

		"""
		nearest_index = 0

		return nearest_index



	def backtrack(self,index):
		"""  
		Returns::

			A list of vertices as the path through the graph.

		Find the sequence of nodes from the origin of the graph to an index.
		
		This function returns a List of vertex indices going from the origin vertex to the vertex `index`.
		
		:param index: The vertex index to find the path through the tree to.
		:type index: int

		"""
		path_list = []

		return path_list







