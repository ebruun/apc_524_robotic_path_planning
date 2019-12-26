# path_planner.py
# Author(s): Edvard Bruun

"""
The core module of the project, executes the program
"""


from solver.solution import Solution

from input.params import ParamsRRT
from input.params import ParamsOriginGoal
from input.params import ParamsDomain


def run_program():
	"""Function for executing the program

	Three stages:
		1. Get program parameters.
		2. Compute path from origin to goal.
		3. Present results.

	"""

	print("1. Parameters")
	input_file = "parameters.txt"

	p1 = ParamsRRT(input_file)
	p2 = ParamsOriginGoal(input_file)
	p3 = ParamsDomain(input_file)

	print("2. Running Program")
	RRT = Solution(p1)

	print("3. Showing Results")


if __name__ == '__main__':
	run_program()

