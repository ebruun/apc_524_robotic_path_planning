# rrt.py
# Author(s): Edvard Bruun

from abc import ABC, abstractmethod

import numpy as np

class RRT(ABC):
	""" An abstract base class for RRT algorithm.

	"""
	def __init__(self):
		pass

	@abstractmethod
	def do_something():
		print("some implementation")

	@abstractmethod
	def rrt_step(cls, recorder, domain, i):
		pass