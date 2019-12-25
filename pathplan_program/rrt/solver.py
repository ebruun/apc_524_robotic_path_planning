# solver.py
# Author(s): Edvard Bruun

import numpy as np

#import domain

class Solver:
	"""A class to step through the RRT algorithm"""
	
	def __init__(self,x):
		print "-Initialize Solver" 

		self.params = x

		self.vertex_list = np.zeros(self.params.n_trials, dtype=float)
		self.parent_list = np.zeros(self.params.n_trials, dtype=int)
		self.cost_list = np.zeros(self.params.n_trials, dtype=float)
		
	def solve_rrt(self):
		print "-Solving with: ", self.params.method

	def check_completion(self):
		print("-Check Completion")

		completed = True

		if completed:
			print("--Completed")
			return True
		
		print("--Not Completed")
		return False
