# stepper.py
# Author(s): Edvard Bruun

import numpy as np
from sys import exit

from algorithm.rrt_basic import RRT_Basic
from algorithm.rrt_star import RRT_Star


class Stepper:
	"""This class steps through one interation of an algorithm.

	Imports the :class:`algorithm.rrt_basic.RRT_Basic` class.

	Imports the :class:`algorithm.rrt_star.RRT_Star` class.

	"""

	def __init__(self,params):
		"""Initialize the Stepper class.

		Note:
			Input parameters are assigned to instance variables with same name.

		Args:
			params (:obj:`input.params.ParamsRRT`):
				Object containing the algorithm parameters.

		"""
		self.params = params


	def do_singlestep(self,recorder,trial):
		""" This function calls the appropriate algorithm to increment the solution by a step.

		Takes the recorder object and calls the specified algorithm to act on it (increment the vertices, parents, costs lists by a single step). The trial number tells the algorithm step function where to save the new data. 

		Args:
			recorder (:obj:`solver.recorder.Recorder`):
				Object containing the algorithm solution lists.
			trial (:obj:`int`):
				A counter for the number of steps taken in the algorithm solution.

		Error:
			Exits the program with an error if no correct method is specified.	
		"""

		if self.params.method is "RRT_basic":
			RRT_Basic.rrt_step(recorder, trial)
		elif self.params.method is "RRT_star":
			RRT_Star.rrt_step(recorder, trial)
		else:
			exit("ERROR: no valid method")


	
			
			

		
