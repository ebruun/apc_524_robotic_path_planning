import unittest
from unittest.mock import Mock

from src_pathplanner.solver.recorder import Recorder

params = Mock()

print(params)

class TestStepper(unittest.TestCase):
    #def setUp(self):
        #self.func = Recorder()

    def test_1(self):
    	self.assertTrue(True)

if __name__ == '__main__':
    unittest.main()