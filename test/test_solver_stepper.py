import unittest
from unittest.mock import Mock

import numpy as np

from solver.stepper import Stepper

params = Mock()
params.method = "RRT_basic"
recorder = Mock()
domain = Mock()

class TestStepper(unittest.TestCase):
	def setUp(self):
		self.stepper = Stepper(params,domain)

		recorder.vertices = np.zeros((3,2), dtype=float)
		recorder.vertices.fill(np.nan)
		recorder.vertices[0,:] = [3.4, 4.5]

		recorder.parents = np.zeros((3,1), dtype=float)
		recorder.parents.fill(np.nan)
		recorder.parents[0] = [1]

		recorder.costs = np.zeros((3,1), dtype=float)
		recorder.costs.fill(np.nan)
		recorder.costs[0] = [3.444]

	def tearDown(self):
		self.stepper = None

	def get_last_row_index(self,step):
		self.stepper.do_singlestep(recorder,domain,step)

		bool_array = (np.isnan(recorder.vertices))
		bool_index = np.where(bool_array == False)
		index = np.amax(bool_index[0])

		return index

	def test_stepper_00_vertices_increment1(self):
		params.method = "RRT_basic"
		
		step = 1
		index = self.get_last_row_index(step)
		self.assertEqual(step,index,"vertices list not incremented")

		step += 1
		index = self.get_last_row_index(step)
		self.assertEqual(step,index,"vertices list not incremented")

	def test_stepper_01_vertices_increment2(self):
		params.method = "RRT_star"
		
		step = 1
		index = self.get_last_row_index(step)
		self.assertEqual(step,index,"vertices list not incremented")

		step += 1
		index = self.get_last_row_index(step)
		self.assertEqual(step,index,"vertices list not incremented")		


	def test_stepper_02_parents_increment1(self):
		params.method = "RRT_basic"

		step = 1
		index = self.get_last_row_index(step)
		self.assertEqual(step,index,"parents list not incremented")

		step += 1
		index = self.get_last_row_index(step)
		self.assertEqual(step,index,"parents list not incremented")


	def test_stepper_03_parents_increment2(self):
		params.method = "RRT_star"

		step = 1
		index = self.get_last_row_index(step)
		self.assertEqual(step,index,"parents list not incremented")

		step += 1
		index = self.get_last_row_index(step)
		self.assertEqual(step,index,"parents list not incremented")


	def test_stepper_04_costs_increment1(self):
		params.method = "RRT_basic"

		step = 1
		index = self.get_last_row_index(step)
		self.assertEqual(step,index,"costs list not incremented")

		step += 1
		index = self.get_last_row_index(step)
		self.assertEqual(step,index,"costs list not incremented")


	def test_stepper_05_costs_increment2(self):
		params.method = "RRT_star"

		step = 1
		index = self.get_last_row_index(step)
		self.assertEqual(step,index,"costs list not incremented")

		step += 1
		index = self.get_last_row_index(step)
		self.assertEqual(step,index,"costs list not incremented")


	def test_stepper_06_unknown_method(self):
		params.method = "unknown"
		
		with self.assertRaises(SystemExit) as cm:
			self.stepper = Stepper(params,domain)
		
		self.assertEqual(cm.exception.code, "ERROR: no valid method")


if __name__ == '__main__':
	unittest.main()