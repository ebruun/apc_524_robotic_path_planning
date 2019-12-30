import unittest
from unittest.mock import Mock

import numpy as np

from solver.solution import Solution

params = Mock()
params.n_trials = 5
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
		self.solution.recorder.parents = np.array([-1, 0, 4, 1, 3, 3])

		index = 2
		a = self.solution.find_path(index)

		self.assertTrue(a == [0, 1, 3, 4, 2], "goal path incorrect")


	def test_solution_08_findpath2(self):
		self.solution.recorder.parents = np.array([-1, 0, 4, 1, 3, 3])

		index = 5
		a = self.solution.find_path(index)

		self.assertTrue(a == [0, 1, 3, 5], "goal path incorrect")


	def test_solution_09_findpath3(self):
		self.solution.recorder.parents = np.array([-1, 0, 4, 1, 3, 3])

		index = 1
		a = self.solution.find_path(index)

		self.assertTrue(a == [0, 1], "goal path incorrect")	

	def test_solution_10_findpath4(self):
		self.solution.recorder.parents = np.array([-1, 0, 4, 1, 3, 3])

		index = 0
		a = self.solution.find_path(index)

		self.assertTrue(a == [0], "goal path incorrect")	


	def test_solution_11_findpath5(self):
		self.solution.recorder.parents = np.array([-1, 0, 4, 1, 3, 3])

		index = np.nan
		a = self.solution.find_path(index)

		self.assertTrue(np.isnan(a), "goal path incorrect")


	def test_solution_12_solutionpath(self):
		self.solution.recorder.parents = np.array([-1, 0, 3, 1])

		domain.goal = [
			("", np.array([1.0, 1.41]), 0.25),
			("", np.array([1.0, 3.10]), 0.25),
			("", np.array([1.0, 1.71]), 0.25)
		]

		self.solution.recorder.vertices = np.array(
			[[1.0, 1.20],
			[1.0, 1.30],
			[1.0, 1.40],
			[1.0, 1.50],
			[1.0, 1.60],
			[1.0, 1.70]]
		)

		self.solution.recorder.parents = np.array([-1, 0, 4, 1, 3, 3])

		self.solution.process_vertex_list()

		self.assertEqual(len(self.solution.solution_path), 3,
			"not enough path lists saved")

	def test_solution_13_runalgorithm_basic(self):
		params.method = "RRT_basic"

		self.solution.run_algorithm()

		self.assertFalse(np.all(np.isnan(self.solution.recorder.vertices)),
						"vertices, not fully filled")

		self.assertFalse(np.all(np.isnan(self.solution.recorder.parents)),
						"parents, not fully filled")

		self.assertFalse(np.all(np.isnan(self.solution.recorder.costs)),
						"costs, not fully filled")		


	def test_solution_14_runalgorithm_star(self):
		params.method = "RRT_star"

		self.solution.run_algorithm()

		self.assertFalse(np.all(np.isnan(self.solution.recorder.vertices)),
						"vertices, not fully filled")

		self.assertFalse(np.all(np.isnan(self.solution.recorder.parents)),
						"parents, not fully filled")

		self.assertFalse(np.all(np.isnan(self.solution.recorder.costs)),
						"costs, not fully filled")	


if __name__ == '__main__':
	unittest.main()