# shape.py
# Author(s): Vivek Kumar
import numpy as np
from abc import ABC, abstractmethod

class Shape(ABC):
	"""docstring for Shape class"""

	@abstractmethod
	def __init__(self, shape_info:dict):
		"""docstring for init
		"""
		self.name = shape_info["shape_type"]
	
	@abstractmethod
	def is_point_inside(self):
		""" Abstract method for checking if point falls inside a shape.
		"""
		pass

	@abstractmethod
	def is_intersected_by_edge(self):
		""" Abstract method for checking if a line is intersected by a shape.
		"""
		pass

	@abstractmethod
	def sample_random_point(self)->np.ndarray:
		""" Abstract method for generating a random new point inside a shape.
		"""
		pass