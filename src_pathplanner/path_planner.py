# path_planner.py
# Author(s): Edvard Bruun, Vivek Kumar

"""
The core module of the project and executes the program

imports...

"""
# Python imports
import sys
import time

# Import inputs
from input.parse_data_class import ParseDataJSON
from input.domain_class import Domain

from solver.solution import Solution
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

	print("1. Reading Parameters")
	# The input file
	input_file = "./input/rrt_input_file.json"
	# Parsed JSON data
	program_input = ParseDataJSON(input_file)
	program_input.parse_data()

	# Split up the parsed input
	domain_info = program_input.data_dict["DomainInfo"]
	origin_goal_info = program_input.data_dict["OriginGoalInfo"]
	obstacles_info = program_input.data_dict["ObstaclesInfo"]
	rrt_algorithm_info = program_input.data_dict["RRTAlgorithmInfo"]

	print("2. Create Domain")

	domain_object = Domain(domain_info, obstacles_info, origin_goal_info)


	print("3. Running Program")
	PathPlan = Solution(rrt_algorithm_info,domain_object)
	PathPlan.run_algorithm()
	PathPlan.process_vertex_list()

	print("4. Showing Results")

	# print("\n\n Vertices",PathPlan.recorder.vertices)
	# print("\n\n Parents",PathPlan.recorder.parents)
	# #print("\n\n Costs",PathPlan.recorder.costs)
	# print("\n\n solution_path",PathPlan.solution_path)

	plot_object = Plot("test run", domain_object)
	plot_object.plot_obstacles()
	plot_object.plot_origin_goals()
	plot_object.plot_solution_graph(PathPlan)
	plot_object.set_layout()
	plot_object.draw()

	Plot1().simple_plot1(
		domain_object,
		PathPlan.recorder.parents,
		PathPlan.recorder.vertices,
		PathPlan.solution_path
		)


if __name__ == '__main__':
	run_program()

