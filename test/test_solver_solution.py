import unittest
from unittest.mock import Mock

unittest.TestLoader.sortTestMethodsUsing = None

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
		self.solution = None


	def test_solution_00_distance_calc_normal1(self):

		self.solution.recorder.vertices = np.array(
			[[0.0, 0.0],
			[1.0, 1.10],
			[1.0, 1.05]]
		)

		goal = np.array([1.0,1.0])

		index,dist = self.solution.find_nearest_vertex(goal)

		self.assertEqual(index,2,"shortest index incorrect")
		self.assertEqual(dist,0.05,"shortest distance incorrect")


	def test_solution_01_distance_calc_normal3d(self):

		self.solution.recorder.vertices = np.array(
			[[0.0, 0.0, 0.0],
			[1.0, 1.10, 1.0],
			[1.0, 1.05, 2.0]]
		)

		goal = np.array([1.0,1.0,2.0])

		index,dist = self.solution.find_nearest_vertex(goal)

		self.assertEqual(index,2,"shortest index incorrect")
		self.assertEqual(dist,0.05,"shortest distance incorrect")

	def test_solution_02_distance_calc_zeros(self):

		self.solution.recorder.vertices = np.array(
			[[1.0, 1.0],
			[0.0, 0.00],
			[1.0, 1.05]]
		)

		goal = np.array([0.0,0.0])

		index,dist = self.solution.find_nearest_vertex(goal)

		self.assertEqual(index,1,"shortest index incorrect")
		self.assertEqual(dist,0.0,"shortest distance incorrect")


	def test_solution_03_distance_calc_nan(self):

		self.solution.recorder.vertices = np.array(
			[[0.0, 0.0],
			[1.0, 1.1],
			[np.nan, np.nan]]
		)

		goal = np.array([1.0,1.0])

		index,dist = self.solution.find_nearest_vertex(goal)

		self.assertEqual(index,1,"shortest index incorrect")
		self.assertEqual(dist,0.1,"shortest distance incorrect")

	def test_solution_04_distance_calc_inf(self):

		self.solution.recorder.vertices = np.array(
			[[float('+inf'), float('+inf')],
			[float('+inf'), float('+inf')],
			[float('+inf'), float('+inf')]]
		)

		goal = np.array([0.0,0.0])

		index,dist = self.solution.find_nearest_vertex(goal)

		self.assertEqual(index,0,"shortest index incorrect")
		self.assertEqual(dist,float('+inf'),"shortest distance incorrect")


	def test_solution_05_goal_check_small(self):

		self.solution.recorder.vertices = np.array(
			[[1.0, 1.0],
			[1.0, 1.09],
			[1.0, 1.05]]
		)

		goal = ("", np.array([1.0, 1.1]), 0.25)

		a = self.solution.check_if_goal_reached(goal)

		self.assertEqual(a,1,"index of goal vertex wrong")


	def test_solution_06_goal_check_big(self):

		self.solution.recorder.vertices = np.array(
			[[1.0, 1.50],
			[1.0, 1.39],
			[1.0, 1.35]]
		)

		goal = ("", np.array([1.0, 1.1]), 0.25)

		a = self.solution.check_if_goal_reached(goal)

		self.assertTrue(np.isnan(a),"index of goal vertex wrong")


	def test_solution_07_findpath1(self):
		self.solution.recorder.parents = np.array([-1, 0, 3, 1])

		index = 2
		a = self.solution.find_path(index)

		print(a)

		self.assertTrue(a == [-1, 0, 2, 3], "goal path incorrect")


	def test_solution_08_findpath2(self):
		self.solution.recorder.parents = np.array([-1, 0, 3, 1])

		index = 1
		a = self.solution.find_path(index)

		print(a)

		self.assertTrue(a == [-1, 0], "goal path incorrect")	




if __name__ == '__main__':
	unittest.main()