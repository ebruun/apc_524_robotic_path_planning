# vertex.py
# Author(s): Edvard Bruun

import numpy as np

class Vertex():
	""" A class for new vertex in algorithm.

	"""

	@classmethod
	def random_free_vertex(cls,domain):
		print("--Free Vertex")

		not_free = True

		while not_free:
			print("loop to find vertex")

			v = cls.random_vertex(domain)

			if cls.inside_domain(domain):
				if not cls.inside_obstacles(domain):
					return v


	def random_vertex(domain):
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

	def inside_domain(domain):
		"""
		 Check if inside domain, since it can be irregular object

		 TODO: use the domain shape method .isinside
		"""

		# return domain.shape.isinside(rand_q)

		# for now do this,since it's a regular rectangle

		return True

	def inside_obstacles(domain):
		"""
		 Check if inside obstacles

		 TODO: use the obstackes shape method .isinside
		"""	

		print(len(domain.obstacles))

		#for i in range(len(domain.obstacles))
		# return domain.obstacles.isinside(rand_q)

		return True













