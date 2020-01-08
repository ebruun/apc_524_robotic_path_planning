# rrt.py
# Author(s): Edvard Bruun

from abc import ABC, abstractmethod
import numpy as np

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

	def new_config(self):
		return Vertex.new_config(self.domain)

	def new_vertex(self):
		return Vertex.new_vertex(
			self.recorder.vertices,
			self.new_q,
			self.params.step_size
		)

	def update_path_cost(self,new_parent,new_cost):
		return self.recorder.costs[new_parent] + new_cost


	#Replace with shape checks
	############################
	def is_new_edge_blocked(self,v1,v2):
		n_divisions = 10
		edge_points = np.linspace(v1,v2,n_divisions)

		for point in edge_points:
			if self.inside_obstacles(self.domain.obstacles,point):
				print("inside")
				return True

		#print("not inside")
		return False

	def inside_obstacles(self,obstacles,vertex):
		"""
		 Check if inside obstacles

		 TODO: use the obstackes shape method .isinside
		"""	

		for obstacle in obstacles:

			#if obstacle.isinside(vertex)
				#return True

			#replace this below once the onbstacle is defined as object
			dist = np.linalg.norm(obstacle[1] - vertex)
			dist = round(dist,6)

			if 	dist < obstacle[2]:
				#print("inside")
				return True

		#print("not inside")
		return False
#####################################




