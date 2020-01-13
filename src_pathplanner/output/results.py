# Results.py
# Author(s): Jessica Flores

"""
Text output class
"""
import numpy as np

class Results:
	""" A class to save and print the vertices, parents, costs, and final solution path.	
	"""
	
	def __init__(self, solution):
		"""
		Initializes the Results class.  

		The attributes values are initialized using the solution object passed.

		Note:
			The solution_path and recorder object are assigned to instance attributes with same name.

		Parameters:
			solution(:obj:`~solver.solution.Solution` object): 
				Solution object which holds the recorder object and solution path.

		Attributes:
			solution_path(:obj:`~solver.solution.Solution` attribute): 
				see Solution	

			recorder (:obj:`~solver.recorder.Recorder` object): 
				see Recorder	
				
		Note:
			The output .txt file will be saved in a folder within the output folder named "output_files"
		"""
		self.solution_path = solution.solution_path
		self.recorder = solution.recorder

	def save_results(self, name):
		""" Saves the text output results of the algorithm to a .txt file"""
		filename = "./output/output_files/{}.txt".format(name) 
		with open(filename, "w") as f:
			with np.printoptions(precision=3, suppress=True, threshold=np.inf):
				print("Vertices\n",self.recorder.vertices, file=f)
				print("\n\n Parents\n",self.recorder.parents, file=f)
				print("\n\n Costs\n",self.recorder.costs, file=f)
				print("\n\n Solution Path(s)\n",self.solution_path, file=f)

	def print_results(self):
		""" Prints the text output results of the algorithm"""
		print("Vertices\n",self.recorder.vertices)
		print("\n\n Parents\n",self.recorder.parents)
		print("\n\n Costs\n",self.recorder.costs)
		print("\n\n Solution Path(s)\n",self.solution_path)
