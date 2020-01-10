# vertex.py
# Author(s): Edvard Bruun

import numpy as np

class Vertex():
	""" A class with methods for starting a new RRT iteration by generating a new vertex.

	"""

	@classmethod
	def new_config(cls,domain_object):
		""" This function returns a new random configuration point found in the domain area.

		Calls the :meth:`~algorithm.vertex.Vertex.new_config()` method.

		Parameters:
			domain_object (:obj:`~input.domain_class.Domain` object):
				Object representing the assembled solution domain.

		Returns:
			new_q (:obj:`numpy.ndarray` of :obj:`float`): The coordinates of the new random configuration.
		"""
		new_q = domain_object.domain.sample_random_point()
		return new_q

	@classmethod
	def new_vertex(cls, vertices, new_q, step_size):
		"""fill out
		
		"""
		index, distance = cls.find_nearest_vertex(vertices, new_q)
		v_near = vertices[index]

		if distance < step_size:
			return new_q, index, distance
		else:
			vector = (new_q - v_near)/distance
			new_v = np.round(v_near + vector*step_size,6)
			return new_v, index, step_size

	@classmethod
	def find_nearest_vertex(self,vertex_list,goal):
		"""  This function finds how far the nearest vertex is to a goal.

		The full list of vertices, saved in the :obj:`~solver.recorder.Recorder` object, is checked against a single goal target. Loops through the full list and calculates the L2 norm to the center of the goal. Updates the index and distance for the closest vertex through the loop.

		Parameters:
			goal (:obj:`~input.shape.Shape` object): A shape object specfied as the target for the algorithm.

		Returns:

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

