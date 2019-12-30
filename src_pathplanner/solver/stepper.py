# stepper.py
# Author(s): Edvard Bruun

"""
Imports the :class:`algorithm.rrt_basic.RRT_Basic` class.

Imports the :class:`algorithm.rrt_star.RRT_Star` class.
"""

import numpy as np
from sys import exit

from algorithm.rrt_basic import RRT_Basic
from algorithm.rrt_star import RRT_Star


class Stepper:
	"""This class steps through one interation of an algorithm.

	"""

	def __init__(self,params,domain):
		"""Initialize the Stepper class.

		Args:
			params (:obj:`~input.params.ParamsRRT` object):
				Object containing the algorithm parameters.

		Note:
			Input parameters are assigned to instance variables with same name.

		Attributes:
			params: see Parameters			

		"""
		self.params = params

		if self.params.method is "RRT_basic":
			self.algorithm = RRT_Basic(domain)
		elif self.params.method is "RRT_star":
			self.algorithm = RRT_Star(domain)
		else:
			exit("ERROR: no valid method")



	def do_singlestep(self,recorder, domain, trial):
		""" This function calls the appropriate algorithm to increment the solution by a step.

		Takes the recorder object and calls the specified algorithm to act on it (increment the vertices, parents, costs lists by a single step). The trial number tells the algorithm step function where to save the new data. 

		Args:
			recorder (:obj:`~solver.recorder.Recorder` object):
				Object containing the algorithm solution lists.
			trial (:obj:`int`):
				A counter for the number of steps taken in the algorithm solution.

		Error:
			Exits the program with an error if no correct method is specified.	
		
		"""
		self.algorithm.rrt_step(recorder,domain,trial)

		"""

		if self.params.method is "RRT_basic":
			RRT_Basic.rrt_step(recorder, domain, trial)
		elif self.params.method is "RRT_star":
			RRT_Star.rrt_step(recorder, domain, trial)
		else:
			exit("ERROR: no valid method")
			"""


	
			
			

		
