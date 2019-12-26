# shape.py
# Author(s): Vivek Kumar

from abc import ABC, abstractmethod

class Shape(ABC):
	"""docstring for Shape"""
	def __init__(self, name):
		self.name = name

	
	@abstractmethod
	def is_point_inside(self):
		pass

		