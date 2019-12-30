# rrt_star.py
# Author(s): Edvard Bruun

import numpy as np

from algorithm.rrt import RRT

class RRT_Star(RRT):
	""" A class for RRT algorithm.

	"""

	def rrt_step(self, recorder,domain,i):
		print("\nStep", i)
		a = self.new_vertex()
		b = self.new_edge()

		print (a)

		recorder.vertices[i,:] = [i,i]
		recorder.parents[i] = i-1
		recorder.costs[i] = i


	def new_vertex(self):
		a = super().new_vertex()
		return 1

	def new_edge(self):
		super().new_edge()

