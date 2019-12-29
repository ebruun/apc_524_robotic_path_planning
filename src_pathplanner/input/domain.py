# domain.py
# Author(s): Edvard Bruun

"""Placeholder class"""

import numpy as np
#import shapes modules

class Domain:
	"""This class is a container for the domain within which the algorithm is searching.

	"""

	dims = [] # dimension
	shape = [] # shape object for domain
	obstacles = [] # list of shape objects
	goal = [] # list of shape objects
	origin = [] # point

	def __init__(self,params_domain, params_origingoal):
		"""Initialize the Domain class.

		TBD...Longer description...

		Note:
			Input parameters are assigned to instance variables with same name.

		Args:
			params (:obj:`input.params.ParamsDomain`):
				Object containing the domain parameters.
			params (:obj:`input.params.ParamsOriginGoal`):
				Object containing the origin/goal parameters.				

		Attributes:
			TBD...

		"""
		self.params_domain = params_domain
		self.params_origingoal = params_origingoal

		self.create_objects()

	def create_objects(self):
		"""Describe function...

		TBD...Longer description...

		"""

		print("-Creating objects out of input parameters")

		self.goal = self.params_origingoal.goal
		#print(self.params_origingoal.origin)
		#print(self.params_origingoal.goal)

