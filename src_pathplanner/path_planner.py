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
import matplotlib.pyplot as plt

from solver.solution import Solution
from output.plot import Plot


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
	#input_file = "./input/rrt_input_file.json"
	#input_file = "./input/rrt_input_file_free_form_obstacle.json"
	input_file = "./input/rrt_input_file_plot_with_everything.json"

	# Parsed JSON data
	program_input = ParseDataJSON(input_file)
	program_input.parse_data()

	# Split up the parsed input
	domain_info = program_input.data_dict["DomainInfo"]

	origin_goal_info = program_input.data_dict["OriginGoalInfo"]
	obstacles_info = program_input.data_dict["ObstaclesInfo"]
	rrt_algorithm_info = program_input.data_dict["RRTAlgorithmInfo"]

	print("2. Creating Domain")
	domain_object = Domain(domain_info, obstacles_info, origin_goal_info)
	print(domain_object)

	print("3. Running Program")
	PathPlan = Solution(rrt_algorithm_info,domain_object)
	PathPlan.run_algorithm()
	PathPlan.process_vertex_list()

	print("4. Showing Results")

	print("\n\n Vertices\n",PathPlan.recorder.vertices)
	print("\n\n Parents\n",PathPlan.recorder.parents)
	print("\n\n Costs\n",PathPlan.recorder.costs)
	print("\n\n solution_path\n",PathPlan.solution_path)

	print("5. Plotting...")
	plot_object = Plot("test run", domain_object)
	plot_object.plot_domain()
	plot_object.plot_obstacles()
	plot_object.plot_origin_goals()
	plot_object.plot_solution_graph(PathPlan)
	plot_object.draw()
	print("Finished! See plot in output folder")


if __name__ == '__main__':
	run_program()

