# stepper.py
# Author(s): Edvard Bruun

from solver.recorder import Recorder
from solver.stepper import Stepper

class Solution:
	""" A class to step through the full RRT algorithm.

	"""

	def __init__(self,params):
		self.params = params
		self.solution_record = Recorder(params)
		self.stepper = Stepper(params)

	def run_algorithm(self):
		"""  This function runs through all the iterations of the solution algorithm.

		"""	

		for i in range(self.params.n_trials):
			print("\nIteration # ", i+1)

			self.solution_record = self.stepper.do_singlestep(self.solution_record)

			if self.check_completion():
				# Finish the loop?
				print("--Completed")
			else:
				# continue the loop
				print("--Not Completed")


		
	def check_completion(self):
		"""  This function checks if the goal has been reached after an iteration.

		Returns:
			bool.::

			 True -- Goal Reached.
			 False -- Goal Not Reached.

		"""

		# check if completed
		completed = False
		
		return completed
