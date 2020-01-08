import unittest
from unittest.mock import Mock

import numpy as np

from solver.solution import Solution

params = Mock()
params.n_trials = 5
params.dims = 2
params.step_size = 0.2
params.method = "rrt_basic"

domain = Mock()
domain.dims = 2
domain.origin = np.array([0.1, 0.1])
domain.extents = np.array([[0,3], [0,4]])
domain.obstacles = [
				("circle", np.array([0.5, 3.5]), 0.20),
				("circle", np.array([1.5, 3.5]), 0.20),
				("circle", np.array([1.5, 0.5]), 0.40)
				]

class TestSolution(unittest.TestCase):
	def setUp(self):
		self.solution = Solution(params,domain)

	def tearDown(self):
		self.solution = None


	def test_solution_00_goal_check_small(self):
		self.solution.recorder.vertices = np.array(
			[[1.0, 1.0],
			[1.0, 1.09],
			[1.0, 1.05]]
		)

		goal = ("", np.array([1.0, 1.1]), 0.25)

		a = self.solution.check_if_goal_reached(goal)

		self.assertEqual(a,1,"index of goal vertex wrong")


	def test_solution_01_goal_check_big(self):
		self.solution.recorder.vertices = np.array(
			[[1.0, 1.50],
			[1.0, 1.39],
			[1.0, 1.35]]
		)

		goal = ("", np.array([1.0, 1.1]), 0.25)

		a = self.solution.check_if_goal_reached(goal)

		self.assertTrue(np.isnan(a),"index of goal vertex wrong")


	def test_solution_02_findpath1(self):
		self.solution.recorder.parents = np.array([-1, 0, 4, 1, 3, 3])

		index = 2
		a = self.solution.find_path(index)

		self.assertTrue(a == [0, 1, 3, 4, 2], "goal path incorrect")


	def test_solution_03_findpath2(self):
		self.solution.recorder.parents = np.array([-1, 0, 4, 1, 3, 3])

		index = 5
		a = self.solution.find_path(index)

		self.assertTrue(a == [0, 1, 3, 5], "goal path incorrect")


	def test_solution_04_findpath3(self):
		self.solution.recorder.parents = np.array([-1, 0, 4, 1, 3, 3])

		index = 1
		a = self.solution.find_path(index)

		self.assertTrue(a == [0, 1], "goal path incorrect")	

	def test_solution_05_findpath4(self):
		self.solution.recorder.parents = np.array([-1, 0, 4, 1, 3, 3])

		index = 0
		a = self.solution.find_path(index)

		self.assertTrue(a == [0], "goal path incorrect")	


	def test_solution_06_findpath5(self):
		self.solution.recorder.parents = np.array([-1, 0, 4, 1, 3, 3])

		index = np.nan
		a = self.solution.find_path(index)

		self.assertTrue(np.isnan(a), "goal path incorrect")


	def test_solution_07_solutionpath(self):

		domain.goals = [
			("cirlce", np.array([1.0, 1.41]), 0.25),
			("cirlce", np.array([1.0, 3.10]), 0.25),
			("circle", np.array([1.0, 1.71]), 0.25)
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

	def test_solution_08_runalgorithm_basic(self):
		params.method = "rrt_basic"

		self.solution.run_algorithm()

		self.assertFalse(np.all(np.isnan(self.solution.recorder.vertices)),
						"vertices, not fully filled")

		self.assertFalse(np.all(np.isnan(self.solution.recorder.parents)),
						"parents, not fully filled")

		self.assertFalse(np.all(np.isnan(self.solution.recorder.costs)),
						"costs, not fully filled")		


	def test_solution_09_runalgorithm_star(self):
		params.method = "rrt_star"
		params.neighborhood = 0.2

		self.solution.run_algorithm()

		self.assertFalse(np.all(np.isnan(self.solution.recorder.vertices)),
						"vertices, not fully filled")

		self.assertFalse(np.all(np.isnan(self.solution.recorder.parents)),
						"parents, not fully filled")

		self.assertFalse(np.all(np.isnan(self.solution.recorder.costs)),
						"costs, not fully filled")	


	def test_solution_10_unknown_method(self):
		params.method = "unknown"
		
		with self.assertRaises(SystemExit) as cm:
			self.solution.run_algorithm()
		
		self.assertEqual(cm.exception.code, "ERROR: no valid method")


if __name__ == '__main__':
	unittest.main()