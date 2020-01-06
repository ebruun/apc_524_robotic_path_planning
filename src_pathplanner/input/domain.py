# domain.py
# Author(s): Edvard Bruun

"""Placeholder class"""

import numpy as np
#import shapes modules

class Domain:
	"""This class is a container for the domain within which the algorithm is searching.

	Longer Description...

	"""
	dims = [] # dimension
	shape = [] # shape object for domain
	obstacles = [] # list of shape objects
	goals = [] # list of shape objects
	origin = [] # point
	extents = [] # max x,y,z coordinates 3d: [[-1,2], [-3, 4], [-5, 5]]

	def __init__(self,params_domain, params_origingoal):
		"""Initialize the Domain class.

		Longer Description...

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
		self.create_other_domain_vars()

	def create_objects(self):
		"""Create shape objects from the parameter strings

		TBD...Longer description...

		"""

		# these are just defined as numbers now
		# but define them as shape objects later
		print("-Creating objects out of input parameters")

		self.goals = self.params_origingoal.goal
		self.obstacles = self.params_domain.obstacles



	def create_other_domain_vars(self):
		"""Create other variables from the parameter strings

		TBD...Longer description...

		"""

		#using self.domain.shape to create min/max extents

		self.extents = np.array([[0,3], [0,4]])
		self.dims = self.params_domain.dims
		self.origin = self.params_origingoal.origin


