# Results.py
# Author(s): Jessica Flores

"""
Text output class
"""
class Results:

	def __init__(self, recorder):
		self.recorder = recorder

	def save_results(self):
		with open("./output/results.txt", "a") as f:
			print("Vertices\n",self.recorder.vertices, file=f)
			print("\n\n Parents\n",self.recorder.parents, file=f)
			print("\n\n Costs\n",self.recorder.costs, file=f)

	def print_results(self):
		print("Vertices\n",self.recorder.vertices)
		print("\n\n Parents\n",self.recorder.parents)
		print("\n\n Costs\n",self.recorder.costs)