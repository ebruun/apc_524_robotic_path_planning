# rrt.py
# Author(s): Edvard Bruun

from abc import ABC, abstractmethod

from algorithm.vertex import Vertex
from algorithm.edge import Edge

class RRT(ABC):
	""" An abstract base class for RRT algorithm.

	"""
	def __init__(self,domain):
		self.domain = domain
		pass

	@abstractmethod
	def rrt_step(cls, recorder, domain, i):
		pass


	@abstractmethod
	def new_vertex(self):
		Vertex.random_free_vertex(self.domain)

		#print(self.domain.extents)

		#new_v = Vertex.random_config(self.domain)


		return new_v

	@abstractmethod
	def new_edge(self):
		Edge.do_something()
		return 1


