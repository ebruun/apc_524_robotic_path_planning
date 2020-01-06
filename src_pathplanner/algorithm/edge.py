# vertex.py
# Author(s): Edvard Bruun

import numpy as np

class Edge():
	""" A class for new vertex in algorithm.

	"""

	n_divisions = 4

	@classmethod
	def is_colliding(cls, v1, v2, obstacles):
		#print("New Edge")

		edge_points = np.linspace(v1,v2,Edge.n_divisions)

		for point in edge_points:
			if cls.inside_obstacles(obstacles,point):
				return True

		return False


	def inside_obstacles(obstacles,vertex):
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



