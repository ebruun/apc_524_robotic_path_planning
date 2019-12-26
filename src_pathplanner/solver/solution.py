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
		self.solution_step = Stepper()

	def run_algorithm(self):
		"""  This function runs through all the iterations of the solution algorithm.

		"""	

		for i in range(5):
			print("Iteration # ", i+1)
			self.solution_step.do_singlestep(self.params.method)
			
		
		
	def check_completion(self):
		"""  This function checks if the goal has been reached after an iteration.

		Returns:
			bool.::

			 True -- Goal Reached.
			 False -- Goal Not Reached.

		"""

		completed = True

		if completed:
			print("--Completed")
			return True
		
		print("--Not Completed")
		return False
