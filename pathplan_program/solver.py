# solver.py
# Author(s): Edvard Bruun

import numpy as np
#import domain

class Solver:
	""" A class to step through the RRT algorithm

	:param vertex_list: description
	:type vertex_list: list
	:return: Returns somehting
	:rtype: what type it returns
	"""
	
	def __init__(self,input_params):
		print "-Initialize Solver" 

		self.params = input_params

		self.vertex_list = np.zeros(self.params.n_trials, dtype=float)
		self.parent_list = np.zeros(self.params.n_trials, dtype=int)
		self.cost_list = np.zeros(self.params.n_trials, dtype=float)
		
	def algorithm_step(self):
		print "-Solving with algorithm: ", self.params.method

	def check_completion(self):
		print("-Check Completion")

		completed = True

		if completed:
			print("--Completed")
			return True
		
		print("--Not Completed")
		return False
