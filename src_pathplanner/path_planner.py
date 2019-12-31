# path_planner.py
# Author(s): Edvard Bruun

"""
The core module of the project and executes the program

imports...

"""

from solver.solution import Solution

from input.params import ParamsRRT
from input.params import ParamsOriginGoal
from input.params import ParamsDomain

from input.domain import Domain



def run_program():
	"""Function for executing the program

	Three stages:
		1. Get program specific parameters from textfile.
		2. Create domain.
		3. Solve trajectories with path planning algorithm.
		4. Present results.

	Example to run...

	"""

	print("1. Parameters")
	input_file = "parameters.txt"

	p1 = ParamsRRT(input_file)
	p2 = ParamsDomain(input_file)
	p3 = ParamsOriginGoal(input_file)
	
	print("2. Create Domain")
	d1 = Domain(p2,p3)

	print("3. Running Program")
	PathPlan = Solution(p1,d1)

	PathPlan.run_algorithm()
	PathPlan.process_vertex_list()

	print("\n\n",PathPlan.recorder.vertices)
	print("\n\n",PathPlan.recorder.parents)
	print("\n\n",PathPlan.recorder.costs)





	print("3. Showing Results")


if __name__ == '__main__':
	run_program()

