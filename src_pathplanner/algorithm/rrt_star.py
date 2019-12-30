# rrt_star.py
# Author(s): Edvard Bruun

import numpy as np

from algorithm.rrt import RRT

class RRT_Star(RRT):
	""" A class for RRT algorithm.

	"""
	@classmethod
	def rrt_step(cls, recorder,i):
		print("doing algorithm")
		recorder.vertices[i,:] = [i,i]
		recorder.parents[i] = i-1
		recorder.costs[i] = i

		print(Solution.domain)
