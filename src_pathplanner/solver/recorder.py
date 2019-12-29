# recorder.py
# Author(s): Edvard Bruun

import numpy as np

class Recorder:
	"""This class serves as a container for the algorithm solution.

	"""
	
	def __init__(self,params):
		"""Initialize the Recorder class.

		The attributes arrays are initialized to the length specified by the number of trials specified in params object. Initialized to value of :obj:`numpy.nan`.

		Note:
			Input parameters are assigned to instance variables with same name.

		Args:
			params (:obj:`input.params.ParamsRRT`):
				Object containing the algorithm parameters.

		Attributes:
			vertices (:obj:`numpy.ndarray` of :obj:`float`):
				An array of coordinates for the graph vertices. The number of columns is specified by the dimensions of the solution space (2d or 3d).
			parents (:obj:`numpy.ndarray` of :obj:`float`):
				An array of indices for the parents of the graph vertices. Specified as float to allow 'NaN' assignement.
			costs (:obj:`numpy.ndarray` of :obj:`float`):
				An array of costs (distances) to reach the vertex at the specified index.

		"""

		self.params = params

		self.vertices = np.zeros((self.params.n_trials,self.params.dims),
			dtype=float)
		self.vertices.fill(np.nan)

		self.parents = np.zeros(self.params.n_trials, dtype=float)
		self.parents.fill(np.nan)

		self.costs = np.zeros(self.params.n_trials, dtype=float)
		self.costs.fill(np.nan)


