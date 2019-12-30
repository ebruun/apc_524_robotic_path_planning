import unittest
from unittest.mock import Mock

import numpy as np

from solver.recorder import Recorder

testparams = Mock()
testparams.n_trials = 10
testparams.dims = 2

class TestRecorder(unittest.TestCase):
	def setUp(self):
		self.recorder = Recorder(testparams)

	def tearDown(self):
		self.recorder = None		

	def test_recorder_00_vert_size(self):
		self.assertEqual(self.recorder.vertices.shape,
						(self.recorder.params.n_trials,
							self.recorder.params.dims),
						"vert, not right matrix size")		

	def test_recorder_01_cost_length(self):
		self.assertEqual(self.recorder.params.n_trials,
						len(self.recorder.costs),
						"costs, not right length")

	def test_recorder_02_parent_length(self):
		self.assertEqual(self.recorder.params.n_trials,
						len(self.recorder.parents),
						"parents, not right length")

	def test_recorder_03_zeros(self):
		self.assertTrue(np.all(np.isnan(self.recorder.vertices)),
						"vertices, not fully initialized to NaN")

		self.assertTrue(np.all(np.isnan(self.recorder.parents)),
						"parents, not initialized to NaN")

		self.assertTrue(np.all(np.any(self.recorder.costs)),
						"costs, not initialized to NaN")

if __name__ == '__main__':
	unittest.main()