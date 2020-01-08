# rrt.py
# Author(s): Edvard Bruun

"""
Imports the :class:`~algorithm.vertex.Vertex` class

Imports the :func:`~algorithm.vertex.find_nearest_vertex` function
"""

from abc import ABC, abstractmethod
import numpy as np

from algorithm.vertex import Vertex
from algorithm.vertex import find_nearest_vertex


class RRT(ABC):
	""" An abstract base class for RRT algorithm.
	"""
	@abstractmethod
	def __init__(self,domain_object,recorder,params):
		self.domain_object = domain_object
		self.recorder = recorder
		self.params = params

		self.recorder.vertices[0,:] = domain_object.origin
		self.recorder.parents[0] = -1
		self.recorder.costs[0] = 0

		self.new_q = []
		self.new_v = []
		self.new_parent = []
		self.new_cost = []

	@abstractmethod
	def rrt_step(cls, i):
		""" step function.

		"""
		pass

	def new_config(self):
		return Vertex.new_config(self.domain_object)

	def new_vertex(self):
		""" new vertex function

		"""
		return Vertex.new_vertex(
			self.recorder.vertices,
			self.new_q,
			self.params["step_size"]
		)

	def update_path_cost(self,new_parent,new_cost):
		""" Update path costs

		"""
		return self.recorder.costs[new_parent] + new_cost

	def is_new_edge_blocked(self,v1,v2):
		for obstacle in self.domain_object.obstacles:
			if(obstacle.is_point_inside(v1) or obstacle.is_point_inside(v2)):
				return True
			if(obstacle.is_intersected_by_edge(v1,v2)):
				return True
		return False

	# def inside_obstacles(self,obstacles,vertex):
	# 	for obstacle in obstacles:
	# 		if(obstacle.is_point_inside(vertex)):
	# 			return True
	# 	#print("not inside")
	# 	return False
