# shape.py
# Author(s): Vivek Kumar

from abc import ABC, abstractmethod

class Shape(ABC):
	"""docstring for Shape"""
	@abstractmethod
	def __init__(self, shape_info:dict):
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

		