# params.py
# Author(s): Edvard Bruun

"""Placeholder class"""

import numpy as np

class ParamsRRT:
	"""Parameters definining the RRT algorithm

	Longer Description...
	"""

	filename = "default_file.txt"
	#method = "RRT_basic"
	method = "RRT_star"
	n_trials = 5
	step_size = 0.1
	dims = 2

	def __init__(self,file=None):
		"""Initialize the ParamsRRT class.

		Longer Description...

		"""

	def get_params(self):
		"""Get parameters.

		Longer Description...

		"""
		print('-Getting RRT Parameters: ', self.filename)


class ParamsOriginGoal:
	"""Parameters defining the start and end goals

	Longer Description...

	"""

	filename = "default_file.txt"

	origin = np.array([0.1, 0.1])
	goal = [
			("circle", np.array([1.0, 1.1]), 0.25),
			("circle", np.array([3.0, 3.5]), 0.25)
			]


	def __init__(self,file=None):
		"""Initialize the ParamsGoalOrigin class.

		Longer Description...

		"""
		self.filename = file if file is not None else self.filename
		self.get_params()

	def get_params(self):
		"""Get parameters.

		Longer Description...

		"""
		print ("-Getting Origin/Goal Parameters: ", self.filename)	


class ParamsDomain:
	"""Parameters defining the domain

	Longer Description...

	"""

	filename = "default_file.txt"

	dims = 2

	shape = ("rectangle", np.array([0.0, 0.0]), (3.0,4.0))

	obstacles = [
				("rectangle", np.array([2.0, 2.5]), (0.2,0.2)),
				("rectangle", np.array([1.0, 2.3]), (0.3,0.4)),
				("circle", np.array([1.5, 3.5]), 0.20)
				]

	def __init__(self,file=None):
		"""Initialize the ParamsGoalOrigin class.

		Longer Description...

		"""
		self.filename = file if file is not None else self.filename
		self.get_params()

	def get_params(self):
		"""Get parameters.

		Longer Description...
		
		"""
		print ("-Getting Domain Parameters: ", self.filename)


