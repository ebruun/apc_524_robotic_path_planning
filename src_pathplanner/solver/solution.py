# stepper.py
# Author(s): Edvard Bruun

from solver.recorder import Recorder
from solver.stepper import Stepper
#import domain

class Solution:
	""" A class to step through the full RRT algorithm.

	Take the :class:`solver.stepper` module

	"""

	def __init__(self,params):
		self.params = params
		self.solution_record = Recorder(params)
		self.stepper = Stepper(params)

	def run_algorithm(self):
		"""  Returns::

				void

		This function runs through all the iterations of the solution algorithm.

		"""	

		for trial in range(self.params.n_trials):
			print("\nIteration # ", trial+1)

			self.stepper.do_singlestep(self.solution_record, trial)

			if self.check_completion():
				# Finish the loop?
				print("--Completed")
			else:
				# continue the loop
				print("--Not Completed")


		
	def check_completion(self):
		"""  
		Returns::

			True -- Goal Reached.
			False -- Goal Not Reached.

		This function checks if the goal has been reached after an iteration.


		"""

		# check if completed
		completed = False
		
		return completed
