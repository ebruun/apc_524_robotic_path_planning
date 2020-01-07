# vertex.py
# Author(s): Edvard Bruun

import numpy as np


def find_nearest_vertex(vertex_list,goal):
	"""  This function finds how far the nearest vertex is to a goal.

	The full list of vertices, saved in the :obj:`~solver.recorder.Recorder` object, is checked against a single goal target. Loops through the full list and calculates the L2 norm to the center of the goal. Updates the index and distance for the closest vertex through the loop.

	Parameters:
		goal (:obj:`~input.shape.Shape` object): A shape object specfied as the target for the algorithm.

	Returns:
		(tuple): tuple containing:

			shortest_index (:obj:`int`): The index of the vertex that is closest to the goal.

			shortest_distance (:obj:`float`): The distance from the closest vertex to the center point of the object

	"""
	dist_new = 0.0
	shortest_distance = float('+inf') 
	shortest_index = 0
	
	for i, vertex in enumerate(vertex_list):

		if any(x == True for x in np.isnan(vertex)):
			# Ends loop when final vertex reached
			break
		else:
			dist_new = np.linalg.norm(goal - vertex)
			dist_new = round(dist_new,6)

			if dist_new < shortest_distance:					
				shortest_distance = dist_new
				shortest_index = i
	
	return shortest_index, shortest_distance



class Vertex():
	""" A class for new vertex in algorithm.

	"""

	@classmethod
	def new_config(cls,domain):


		######################
		# REPLACE with .sample_random_point()
		# RETURN THE NEW POINT
		#######################

		new_q = cls.random_config(domain)
		#print(new_q)

		while not cls.is_inside_domain(domain,new_q):
			new_q = cls.random_config(domain)
	
		return new_q


	@classmethod
	def new_vertex(cls, vertices, new_q, step_size):

		index, distance = find_nearest_vertex(vertices, new_q)

		v_near = vertices[index]

		if distance < step_size:
			return new_q, index, distance
		else:
			vector = (new_q - v_near)/distance
			new_v = np.round(v_near + vector*step_size,6)
			return new_v, index, step_size


	######################
	# DELETE THIS FUNCTION ONCE .sample_random_point() IMPLEMENTED
	######################
	def random_config(domain):
		"""
		 Generate coordinates between domain extents

		 Round to 3 decimal

		"""

		rand_v = []

		for i in range(domain.dims):
			rand_v.append(np.random.uniform(
				domain.extents[i][0],
				domain.extents[i][1])
			)

		rand_v = [round(elem, 3) for elem in rand_v ]
		
		return rand_v



	######################
	# DELETE THIS FUNCTION ONCE .sample_random_point() IMPLEMENTED
	#######################
	def is_inside_domain(domain,vertex):
		"""
		 Check if inside domain, since it can be irregular object

		 TODO: use the domain shape method .isinside
		"""

		# return domain.shape.isinside(vertex)

		# for now just return true,since it's a regular rectangle so will for sure be inside the fomain

		return True
















