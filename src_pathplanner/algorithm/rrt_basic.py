# rrt_basic.py
# Author(s): Edvard Bruun

import numpy as np

from algorithm.rrt import RRT

class RRT_Basic(RRT):
	""" A class for RRT algorithm.

	Saving
		the new solution to the specified iteration number. The type of algorithm chosen
		is set by :obj:`params` 

	"""

	def rrt_step(self, recorder,domain,i):
		print("\nStep", i)
		new_v = self.new_vertex()
		b = self.new_edge()

		print (new_v)

		recorder.vertices[i,:] = new_v

		print(recorder.vertices)
		recorder.parents[i] = i-1
		recorder.costs[i] = i


	def new_vertex(self):
		new_v = super().new_vertex()
		return new_v

	def new_edge(self):
		super().new_edge()

