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
		print("Vertex", trial+1)
		
		self.new_q = self.new_config()
		self.new_v, self.new_parent, self.new_cost = self.new_vertex()

		while self.is_new_edge_blocked(self.recorder.vertices[self.new_parent],self.new_v):	
			self.new_q = self.new_config()
			self.new_v, self.new_parent, self.new_cost = self.new_vertex()		

		self.recorder.vertices[trial,:] = self.new_v
		self.recorder.parents[trial] = self.new_parent
		self.recorder.costs[trial] = self.recorder.costs[self.new_parent] + self.new_cost


