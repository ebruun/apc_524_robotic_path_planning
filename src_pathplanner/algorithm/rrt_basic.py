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
	def __init__(self,domain,recorder,params):
		super().__init__(domain,recorder,params)


	def rrt_step(self,trial):
		print("\nVertex", trial+1)
		
		self.new_q = self.new_config()
		self.new_v, self.new_parent, self.new_cost = self.new_vertex()

		if self.is_new_edge_blocked():
			print("blocked")
			self.rrt_step(trial)

		self.recorder.vertices[trial,:] = self.new_v
		self.recorder.parents[trial] = self.new_parent
		self.recorder.costs[trial] = self.new_cost


	def new_config(self):
		return super().new_config()

	def new_vertex(self):
		return super().new_vertex()

	def is_new_edge_blocked(self):
		return super().is_new_edge_blocked()

