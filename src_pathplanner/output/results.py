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

		self.solution_vertices = []
		for idx, solution in enumerate(self.solution_path):
			self.solution_vertices.append([])
			for i in solution:
				if np.isnan(i):
					self.solution_vertices[idx] = i
				else:
					self.solution_vertices[idx].append(self.recorder.vertices[i].tolist())

		self.solution_costs = []
		for idx, solution in enumerate(self.solution_path):
			self.solution_costs.append(0)
			for i in solution:
				if np.isnan(i):
					self.solution_costs[idx] = i
				else:
					self.solution_costs[idx] += self.recorder.costs[i]

	def save_results(self, name):
		""" Saves the text output results of the algorithm to a .txt file"""
		filename = "./output/output_files/{}.txt".format(name) 
		with open(filename, "w") as f:
			with np.printoptions(precision=3, suppress=True, threshold=np.inf):
				print("Solution Path(s)\n",*self.solution_path,sep='\n', file=f)
				print("\n\nSolution Vertices(s)\n", file=f)
				for solution in self.solution_vertices:
					if np.isnan(solution).any():
						print(solution, "\n", file=f)
					else:
						print(*solution, sep='\n', file=f)
						print("\n", file=f)
				print("\nSolution Cost(s)\n",*self.solution_costs,sep='\n', file=f)


	def print_results(self):
		""" Prints the text output results of the algorithm"""
		with np.printoptions(precision=3, suppress=True, threshold=np.inf):
			print("Solution Path(s)\n",*self.solution_path,sep='\n')
			print("\n\nSolution Vertices(s)\n")
			for solution in self.solution_vertices:
				if np.isnan(solution).any():
					print(solution, "\n")
				else:
					print(*solution, sep='\n')
					print("\n")
			print("\nSolution Cost(s)\n",*self.solution_costs,sep='\n')
