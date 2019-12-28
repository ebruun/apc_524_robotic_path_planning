# params.py
# Author(s): Edvard Bruun

import numpy as np

class ParamsRRT:
	"""Parameters definining the RRT algorithm"""

	filename = "default_file.txt"
	method = "RRT_star"
	n_trials = 5
	step_size = 0.1
	dims = 2

	def __init__(self,file=None):
		self.filename = file if file is not None else self.filename
		self.get_params()

	def get_params(self):
		print('-Getting RRT Parameters: ', self.filename)


class ParamsOriginGoal:
	"""Parameters defining the start and end goals"""

	filename = "default_file.txt"

	origin = ("circle", np.array([0.1, 0.1]), 0.05)
	goal = ("circle", np.array([2.5, 3.5]), 0.25)


	def __init__(self,file=None):
		self.filename = file if file is not None else self.filename
		self.get_params()

	def get_params(self):
		print ("-Getting Origin/Goal Parameters: ", self.filename)	


class ParamsDomain:
	"""Parameters defining the domain"""

	filename = "default_file.txt"

	domain = ("rectangle", np.array([0.0, 0.0]), (3.0,4.0))

	obstacles = [
				("rectangle", np.array([2.0, 2.5]), (0.2,0.2)),
				("rectangle", np.array([1.0, 2.3]), (0.3,0.4)),
				("circle", np.array([1.5, 3.5]), 0.20)
				]

	def __init__(self,file=None):
		self.filename = file if file is not None else self.filename
		self.get_params()

	def get_params(self):
		print ("-Getting Domain Parameters: ", self.filename)


