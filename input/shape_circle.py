# shape_circle.py
# Author(s): Vivek Kumar
import numpy as np
from shape import Shape

class Circle(Shape):
	"""docstring for Shape"""
	def __init__(self, dim, name):
		self.dim = dim
		self.name = name
	
	def is_point_inside(self, p1):
		pass

	def line_intersects(self, p1, p2):
		pass

		
