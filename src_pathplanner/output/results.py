# Results.py
# Author(s): Jessica Flores

"""
Text output class
"""
class Results:

	def __init__(self, solution):
		self.solution_path = solution.solution_path
		self.recorder = solution.recorder

	def save_results(self, name):
		filename = "./output/output_files/{}.txt".format(name) 
		with open(filename, "w") as f:
			print("Vertices\n",self.recorder.vertices, file=f)
			print("\n\n Parents\n",self.recorder.parents, file=f)
			print("\n\n Costs\n",self.recorder.costs, file=f)
			print("\n\n Solution Path(s)\n",self.solution_path, file=f)

	def print_results(self):
		print("Vertices\n",self.recorder.vertices)
		print("\n\n Parents\n",self.recorder.parents)
		print("\n\n Costs\n",self.recorder.costs)
		print("\n\n Solution Path(s)\n",self.solution_path)