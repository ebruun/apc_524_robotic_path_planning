# stepper.py
# Author(s): Edvard Bruun

import numpy as np

from algorithm.rrt import RRT
from algorithm.rrt_basic import RRT_Basic
from algorithm.rrt_star import RRT_Star


class Stepper:
	""" A class to perform a single path planning step with the chosen algorithm.

	"""

	def __init__(self,input_params):
		self.params = input_params
		
	def do_singlestep(self,recorder,trial):
		""" This function steps through one iteration of the solution algorithm.

			Updates the recorder object lists based on the trial number

		"""

		if self.params.method is "RRT_basic":
			#print("Do RRT, with stepsize ", self.params.step_size)
			RRT.rrt_step(recorder, trial)



		elif self.params.method is "RRT_star":
			#print("Do RRT_Star, with stepsize ", self.params.step_size)
			RRT.rrt_step(recorder, trial)

	
			
			

		
