# rrt_star.py
# Author(s): Edvard Bruun

import numpy as np

from algorithm.rrt import RRT

class RRT_Star(RRT):
	""" A class for RRT algorithm.

	"""

	def __init__(self,domain,recorder,params):
		super().__init__(domain,recorder,params)
		self.neighbor_indices = []
		self.neighbor_dist = []



	def rrt_step(self,trial):
		print("Vertex", trial+1)
		
		self.new_q = self.new_config()
		self.new_v, self.new_parent, self.new_cost = self.new_vertex()

		if self.is_new_edge_blocked():
			self.rrt_step(trial)

		self.recorder.vertices[trial,:] = self.new_v

		self.choose_parent()
		self.find_vertices_in_neighborhood()




		self.recorder.parents[trial] = self.new_parent
		self.recorder.costs[trial] = self.recorder.costs[self.new_parent] + self.new_cost
		#self.update_path_cost(trial)


	def new_config(self):
		return super().new_config()

	def new_vertex(self):
		return super().new_vertex()

	def is_new_edge_blocked(self):
		return super().is_new_edge_blocked()

	def choose_parent(self):
		print("choose parent")
		pass

	def find_vertices_in_neighborhood(self):

		print("verts in neighborhood")
		del self.neighbor_indices[:]
		del self.neighbor_dist[:]

		for i, vertex in enumerate(self.recorder.vertices):

			if any(x == True for x in np.isnan(vertex)):
				# Ends loop when final vertex in current list reached
				break
			else:
				dist_new = np.linalg.norm(self.new_v - vertex)
				dist_new = round(dist_new,6)

				if dist_new < self.params.neighborhood:
					print("yes, in the hood")					
					self.neighbor_indices.append(i)
					self.neighbor_dist.append(dist_new)

			print(self.neighbor_indices)
			print(self.neighbor_dist)


	def lowest_neighborhood_path(self):

		pass

