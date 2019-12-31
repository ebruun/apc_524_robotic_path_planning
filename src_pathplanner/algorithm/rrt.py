# rrt.py
# Author(s): Edvard Bruun

from abc import ABC, abstractmethod

from algorithm.vertex import Vertex
from algorithm.vertex import find_nearest_vertex

from algorithm.edge import Edge

class RRT(ABC):
	""" An abstract base class for RRT algorithm.

	"""
	@abstractmethod
	def __init__(self,domain,recorder,params):
		self.domain = domain
		self.recorder = recorder
		self.params = params

		self.recorder.vertices[0,:] = domain.origin
		self.recorder.parents[0] = -1
		self.recorder.costs[0] = 0

		self.new_q = []
		self.new_v = []
		self.new_parent = []
		self.new_cost = []

	@abstractmethod
	def rrt_step(cls, i):
		pass

	@abstractmethod
	def new_config(self):
		return Vertex.new_config(self.domain)

	@abstractmethod
	def new_vertex(self):
		return Vertex.new_vertex(
			self.recorder.vertices,
			self.new_q,
			self.params.step_size
		)

	@abstractmethod
	def is_new_edge_blocked(self):

		return Edge.is_colliding(
			self.recorder.vertices[self.new_parent],
			self.new_v,
			self.domain.obstacles)



