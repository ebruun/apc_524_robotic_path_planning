# solver.py
# Author(s): Edvard Bruun

import numpy as np

class Solver:
	"""A class to step through the RRT algorithm"""

	vertex_list = []
	parent_list = []
	cost_list = []
	
	def __init__(self,n):
		#Initialize with parameters
		self.vertex_list = np.zeros(n, dtype=float)
		self.parent_list = np.zeros(n, dtype=int)
		self.cost_list = np.zeros(n, dtype=float)
		

	def solve_rrt(self):
		#Call the RRT algorithm
		print("Solving RRT")

	def check_completion(self):
		return True
