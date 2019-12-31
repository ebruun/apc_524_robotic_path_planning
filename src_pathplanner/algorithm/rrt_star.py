# rrt_star.py
# Author(s): Edvard Bruun

import numpy as np

from algorithm.rrt import RRT

class RRT_Star(RRT):
	""" A class for RRT algorithm.

	"""

	def __init__(self,domain,recorder):
		super().__init__(domain,recorder)

	def rrt_step(self,i):
		print("\nStep", i)
		
		self.new_q = self.new_config()


		self.recorder.vertices[i,:] = self.new_q
		self.recorder.parents[i] = i-1
		self.recorder.costs[i] = i


	def new_config(self):
		return super().new_config()



	def new_edge(self):
		super().new_edge()
