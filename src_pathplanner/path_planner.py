# path_planner.py
# Author(s): Edvard Bruun

"""
The core module of the project and executes the program

imports...

"""

from solver.solution import Solution
from input.params import ParamsRRT, ParamsOriginGoal, ParamsDomain
from input.domain import Domain
from output.plot import Plot
from output.plot1 import Plot1


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


	print("3. Showing Results")

	print("\n\n Vertices",PathPlan.recorder.vertices)
	print("\n\n Parents",PathPlan.recorder.parents)
	#print("\n\n Costs",PathPlan.recorder.costs)
	print("\n\n solution_path",PathPlan.solution_path)

	
	p1 = Plot("test run", d1)
	p1.plot_obstacles()
	p1.plot_origin_goals()
	p1.plot_solution_graph(PathPlan)
	p1.set_axes()
	p1.draw()

	Plot1.simple_plot1(d1,
		PathPlan.recorder.parents,
		PathPlan.recorder.vertices,
		PathPlan.solution_path)

if __name__ == '__main__':
	run_program()

