# rrt_basic.py
# Author(s): Edvard Bruun

import numpy as np

class RRT_Basic:
	""" A class for RRT algorithm.

	"""
	@classmethod
	def rrt_step(cls, recorder,i):
		print("doing algorithm")
		recorder.vertices[i,:] = [i,i]