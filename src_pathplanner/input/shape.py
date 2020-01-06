# shape.py
# Author(s): Vivek Kumar

from abc import ABC, abstractmethod

class Shape(ABC):
	"""docstring for Shape"""
	def __init__(self, name: str, dim:int, init_vals:np.ndarray):
		self.dim = dim
		self.name = name
		self.init_vals = init_vals
	
	@abstractmethod
	def is_point_inside(self, p1):
		pass

	@abstractmethod
	def line_intersects(self, p1, p2):
		pass
