import unittest
from unittest.mock import Mock

import numpy as np

from algorithm.rrt_star import RRT_Star

params = Mock()
params.dims = 2
params.step_size = 0.2
params.neighborhood = 0.3
params.method = "rrt_star"


recorder = Mock()

domain = Mock()
domain.dims = 2
domain.origin = np.array([0.1, 0.1])
domain.extents = np.array([[0,3], [0,4]])
domain.obstacles = [
				("circle", np.array([0.5, 3.5]), 0.20),
				("circle", np.array([1.5, 3.5]), 0.20),
				("circle", np.array([1.5, 0.5]), 0.40)
				]

class TestRRT_Star(unittest.TestCase):
	def setUp(self):

		recorder.vertices = np.zeros((6,2), dtype=float)
		recorder.vertices.fill(np.nan)

		recorder.parents = np.zeros(6, dtype=float)
		recorder.parents.fill(np.nan)

		recorder.costs = np.zeros(6, dtype=float)
		recorder.costs.fill(np.nan)

		recorder.parents_history = np.zeros((6,6*2), dtype=float)
		recorder.parents_history.fill(np.nan)

		self.algorithm = RRT_Star(domain, recorder, params)

	def tearDown(self):
		self.algorithm = None


	def get_last_row_index(self,step):
		self.algorithm.rrt_step(step)

		bool_array = (np.isnan(recorder.vertices))
		bool_index = np.where(bool_array == False)
		index = np.amax(bool_index[0])

		return index

	def test_rrt_star_00_vertices_increment(self):
		
		recorder.vertices = np.array(
			[[0.0, 0.0],
			[1.0, 1.30],
			[1.0, 1.40],
			[np.nan, np.nan],
			[np.nan, np.nan],
			[np.nan, np.nan]]
		)	

		step = 3
		index = self.get_last_row_index(step)
		self.assertEqual(step,index,"vertices list not incremented")

		step += 1
		index = self.get_last_row_index(step)
		self.assertEqual(step,index,"vertices list not incremented")		


	def test_rrt_star_01_parents_increment(self):
		recorder.parents = np.array([0,1,3,4,np.nan,np.nan])

		step = 4
		index = self.get_last_row_index(step)
		self.assertEqual(step,index,"parents list not incremented")

		step += 1
		index = self.get_last_row_index(step)
		self.assertEqual(step,index,"parents list not incremented")


	def test_rrt_star_02_costs_increment(self):
		recorder.parents = np.array(
			[0.0,1.2,np.nan,np.nan,np.nan,np.nan])

		step = 2
		index = self.get_last_row_index(step)
		self.assertEqual(step,index,"costs list not incremented")

		step += 1
		index = self.get_last_row_index(step)
		self.assertEqual(step,index,"costs list not incremented")

"""
	def test_stepper_06_unknown_method(self):
		params.method = "unknown"
		
		with self.assertRaises(SystemExit) as cm:
			self.stepper = Stepper(params,domain)
		
		self.assertEqual(cm.exception.code, "ERROR: no valid method")
"""

if __name__ == '__main__':
	unittest.main()