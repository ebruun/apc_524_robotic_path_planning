import unittest
from unittest.mock import Mock

import numpy as np

from solver.solution import Solution

params = Mock()
params.n_trials = 3
params.dims = 2

domain = Mock()


class TestSolution(unittest.TestCase):
	def setUp(self):
		self.solution = Solution(params,domain)

	def tearDown(self):
		pass
		params = None
		domain = None

	def test_distance_calc1(self):

		self.solution.recorder.vertices = np.array(
			[[0.0, 0.0],
			[1.0, 1.1],
			[2.0, 2.0]]
		)

		goal = np.array([1.0,1.0])

		index,dist = self.solution.find_nearest_vertex(goal)

		self.assertEqual(index,1,"shortest index incorrect")
		self.assertEqual(dist,0.1,"shortest distance incorrect")


		
		

if __name__ == '__main__':
	unittest.main()