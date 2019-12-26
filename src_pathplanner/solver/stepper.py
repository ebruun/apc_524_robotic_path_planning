# stepper.py
# Author(s): Edvard Bruun


class Stepper:
	""" A class to perform a single step with the chosen algorithm.

	"""
		
	def do_singlestep(self,method):
		"""  This function steps through one iteration of the solution algorithm.

	    Returns:
	       Updated lists::

	          vertex
	          vertex_parent
	          vertex_cost

		"""
		print("find new vertex\n")

		
		if method is "RRT":
			print("Do RRT")
		elif method is "RRT_star":
			print("Do RRT_Star")
		

		return True
