import unittest
from unittest.mock import Mock

import numpy as np

from src_pathplanner.solver.recorder import Recorder

testparams = Mock()
testparams.n_trials = 10
testparams.dims = 2

class TestRecorder(unittest.TestCase):
	def setUp(self):
		self.recorder = Recorder(testparams)

	def tearDown(self):
		self.recorder = None		

	def test_vert_size(self):
		self.assertEqual(self.recorder.vertices.shape,
						(self.recorder.params.n_trials, self.recorder.params.dims),
						"vert, not right matrix size")		

	def test_cost_length(self):
		self.assertEqual(self.recorder.params.n_trials,
						len(self.recorder.costs),
						"costs, not right length")

	def test_parent_length(self):
		self.assertEqual(self.recorder.params.n_trials,
						len(self.recorder.parents),
						"parents, not right length")

	def test_zeros(self):
		self.assertFalse(np.any(self.recorder.vertices), "vert, not initialized to zero")
		self.assertFalse(np.any(self.recorder.parents), "parents, not initialized to zero")
		self.assertFalse(np.any(self.recorder.costs), "costs, not initialized to zero")

if __name__ == '__main__':
	unittest.main()