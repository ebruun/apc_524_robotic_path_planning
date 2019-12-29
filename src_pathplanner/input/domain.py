# domain.py
# Author(s): Edvard Bruun

"""Placeholder class"""

import numpy as np
#import shapes modules

class Domain:
	"""The domain within which the algorithm is searching"""

	dims = [] # dimension
	shape = [] # shape object for domain
	obstacles = [] # list of shape objects
	goal = [] # list of shape objects
	origin = [] # point

	def __init__(self,params_domain, params_origingoal):
		# temporary lists, these should be lists of objects
		self.params_domain = params_domain
		self.params_origingoal = params_origingoal

		self.create_objects()

	def create_objects(self):
		print("-Creating objects out of input parameters")

		self.goal = self.params_origingoal.goal
		#print(self.params_origingoal.origin)
		#print(self.params_origingoal.goal)

