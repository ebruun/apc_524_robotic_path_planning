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
		pass

		