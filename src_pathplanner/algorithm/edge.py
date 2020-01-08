# vertex.py
# Author(s): Edvard Bruun

import numpy as np

class Edge():
	""" A class for new vertex in algorithm.

	"""

	#splitting the line between two vertices into points to check
	######################
	# DELETE THIS ONCE .is_intersected_by_edge() IMPLEMENTED
	######################
	n_divisions = 4

	@classmethod
	def is_colliding(cls, v1, v2, obstacles):
		
		##############
		# REPLACE WITH .is_intersected_by_edge()
		# CREATE A LOOP HERE TO LOOK THROUGH ALL THE OBSTACLES
		# INSTEAD OF DOING THAT IN THE FUNCTION BELOW
		# RETURN = FALSE (not inside)
		# TRUE = (inside), terminate loop
		##############

		edge_points = np.linspace(v1,v2,Edge.n_divisions)

		for point in edge_points:
			if cls.inside_obstacles(obstacles,point):
				#print("inside")
				return True

		#print("not inside")
		return False



	######################
	# DELETE THIS FUNCTION ONCE .is_intersected_by_edge() IMPLEMENTED
	######################
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



