# stepper.py
# Author(s): Edvard Bruun


class Stepper:
	""" A class to perform a single path planning step with the chosen algorithm.

	"""

	def __init__(self,input_params):
		self.params = input_params
		
	def do_singlestep(self,recorder):
		"""  This function steps through one iteration of the solution algorithm.

	    Returns:lists:
	       Updated :

	          vertex
	          vertex_parent
	          vertex_cost

		"""

		if self.params.method is "RRT":
			print("Do RRT, with stepsize ", self.params.step_size)
			#update recorder lists
			return recorder

		elif self.params.method is "RRT_star":
			print("Do RRT_Star, with stepsize ", self.params.step_size)
			#update recorder lists
			return recorder
			
			

		
