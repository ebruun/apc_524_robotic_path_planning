import unittest
from unittest.mock import Mock

import numpy as np

from algorithm.vertex import find_nearest_vertex

params = Mock()
params.n_trials = 5
params.dims = 2
params.method = "RRT_basic"

domain = Mock()
domain.dims = 2
domain.extents = np.array([[0,3], [0,4]])
domain.obstacles = [
				("circle", np.array([0.5, 3.5]), 0.20),
				("circle", np.array([1.5, 3.5]), 0.20),
				("circle", np.array([1.5, 0.5]), 0.40)
				]

class TestVertex(unittest.TestCase):
	def setUp(self):
		pass
		#self.solution = Solution(params,domain)

	def tearDown(self):
		self.solution = None


	def test_vertex_00_distance_calc_normal1(self):
			vertices = np.array(
				[[0.0, 0.0],
				[1.0, 1.10],
				[1.0, 1.05]]
			)

			goal = np.array([1.0,1.0])

			index,dist = find_nearest_vertex(vertices,goal)

			self.assertEqual(index,2,"shortest index incorrect")
			self.assertEqual(dist,0.05,"shortest distance incorrect")


	def test_vertex_01_distance_calc_normal3d(self):
		vertices = np.array(
			[[0.0, 0.0, 0.0],
			[1.0, 1.10, 1.0],
			[1.0, 1.05, 2.0]]
		)

		goal = np.array([1.0,1.0,2.0])

		index,dist = find_nearest_vertex(vertices,goal)

		self.assertEqual(index,2,"shortest index incorrect")
		self.assertEqual(dist,0.05,"shortest distance incorrect")


	def test_solution_02_distance_calc_zeros(self):
		vertices = np.array(
			[[1.0, 1.0],
			[0.0, 0.00],
			[1.0, 1.05]]
		)

		goal = np.array([0.0,0.0])

		index,dist = find_nearest_vertex(vertices,goal)

		self.assertEqual(index,1,"shortest index incorrect")
		self.assertEqual(dist,0.0,"shortest distance incorrect")


	def test_solution_03_distance_calc_nan(self):
		vertices = np.array(
			[[0.0, 0.0],
			[1.0, 1.1],
			[np.nan, np.nan]]
		)

		goal = np.array([1.0,1.0])

		index,dist = find_nearest_vertex(vertices,goal)

		self.assertEqual(index,1,"shortest index incorrect")
		self.assertEqual(dist,0.1,"shortest distance incorrect")

	def test_solution_04_distance_calc_inf(self):
		vertices = np.array(
			[[float('+inf'), float('+inf')],
			[float('+inf'), float('+inf')],
			[float('+inf'), float('+inf')]]
		)

		goal = np.array([0.0,0.0])

		index,dist = find_nearest_vertex(vertices,goal)

		self.assertEqual(index,0,"shortest index incorrect")
		self.assertEqual(dist,float('+inf'),"shortest distance incorrect")

if __name__ == '__main__':
	unittest.main()