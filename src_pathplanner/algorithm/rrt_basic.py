# rrt_basic.py
# Author(s): Edvard Bruun

import numpy as np

from algorithm.rrt import RRT

class RRT_Basic(RRT):
	""" A class for RRT algorithm.

	Saving
		the new solution to the specified iteration number. The type of algorithm chosen
		is set by :obj:`params` 

	"""
	@classmethod
	def rrt_step(cls, recorder,domain,i):
		#print("doing algorithm")
		recorder.vertices[i,:] = [i,i]
		recorder.parents[i] = i-1
		recorder.costs[i] = i

	def do_something():
		print("some implementation")