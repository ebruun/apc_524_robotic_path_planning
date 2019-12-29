# stepper.py
# Author(s): Edvard Bruun

import numpy as np

from algorithm.rrt_basic import RRT_Basic
from algorithm.rrt_star import RRT_Star


class Stepper:
	"""This class steps through one interation of an algorithm.

	Imports the :class:`algorithm.rrt_basic` module

	Imports the :class:`algorithm.rrt_star` module

	"""

	def __init__(self,params):
		"""Initialize the Stepper class.

		Note:
			Input parameters are assigned to instance variables with same name.

		Args:
			params (:obj:`input.params.ParamsRRT`):
				Object containing the algorithm parameters

		"""
		self.params = params
		
	def do_singlestep(self,recorder,trial):
		""" This function steps through one iteration of the solution algorithm.

		Takes the recorder object and calls an algorithm to act on it. Saving
		the new solution to the specified iteration number. The type of algorithm chosen
		is set by :obj:`params` 

		Args:
			recorder (:obj:`solver.recorder`):
				Object containing the algorithm solution lists
			trial (:obj:`int`):
				A counter for the number of steps taken in the algorithm solution		

		"""

		if self.params.method is "RRT_basic":
			#print("Do RRT, with stepsize ", self.params.step_size)
			RRT_Basic.rrt_step(recorder, trial)


		elif self.params.method is "RRT_star":
			#print("Do RRT_Star, with stepsize ", self.params.step_size)
			RRT_Star.rrt_step(recorder, trial)

	
			
			

		
