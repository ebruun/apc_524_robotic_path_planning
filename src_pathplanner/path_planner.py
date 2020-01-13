# path_planner.py
# Author(s): Edvard Bruun, Vivek Kumar, Jessica Flores

"""
The core module to execute the program

The user to specify the location of the input file in the :meth:`~path_planner.run_program()` function.

Imports the :class:`~input.parse_data_class.ParseDataJSON` class

Imports the :class:`~input.domain.Domain` class

Imports the :class:`~solver.solution.Solution` class

Imports the :class:`~output.plot.Plot` class

"""
# Python imports
import sys
import time

# Import inputs
from input.parse_data_class import ParseDataJSON
from input.domain_class import Domain
from solver.solution import Solution
from output.plot import Plot


def run_program():
	"""
	Steps in program::

		Step 1. Read parameters file (user-specified)
		Step 2. Create problem domain
		Step 3. Execute path planning algorithm
		Step 4. Print results to screen, save text file
		Step 5. Create results plot

	Function Code::
		
		# Step 1. 
		input_file = "./input/rrt_input_file.json"
		program_input = ParseDataJSON(input_file)
		program_input.parse_data()

		domain_info = program_input.data_dict["DomainInfo"]
		origin_goal_info = program_input.data_dict["OriginGoalInfo"]
		obstacles_info = program_input.data_dict["ObstaclesInfo"]
		rrt_algorithm_info = program_input.data_dict["RRTAlgorithmInfo"]
		
		# Step 2. 
		domain_object = Domain(domain_info, obstacles_info, origin_goal_info)

		# Step 3. 
		PathPlan = Solution(rrt_algorithm_info,domain_object)
		PathPlan.run_algorithm()
		PathPlan.process_vertex_list()

		# Step 4.
		print_results()
		save_results()

		# Step 5.
		plot_results()


	"""

	print("\nStep 1. Reading Parameters")
	# The input file
	#input_file = "./input/user_input_files/circle_regular_obstacles.json"
	#input_file = "./input/user_input_files/circle_freeform_obstacles.json"
	# input_file = "./input/user_input_files/circle_mixed_obstacles.json"
	# input_file = "./input/user_input_files/circle_mixed_goals_obstacles.json"
	input_file = "./input/user_input_files/profiling_3.json"

	# Parsed JSON data
	program_input = ParseDataJSON(input_file)
	program_input.parse_data()

	# Split up the parsed input
	domain_info = program_input.data_dict["DomainInfo"]
	origin_goal_info = program_input.data_dict["OriginGoalInfo"]
	obstacles_info = program_input.data_dict["ObstaclesInfo"]
	rrt_algorithm_info = program_input.data_dict["RRTAlgorithmInfo"]

	print("\nStep 2. Create Domain")
	domain_object = Domain(domain_info, obstacles_info, origin_goal_info)

	print("\nStep 3. Running Program")
	PathPlan = Solution(rrt_algorithm_info,domain_object)
	PathPlan.run_algorithm()
	PathPlan.process_vertex_list()

	print("Step 4. Print and Save Results")
	################# REPLACE WITH PRINTING FUNCTION #######################
	# print_results()
	# save_results()
	print("\n\n Vertices\n",PathPlan.recorder.vertices)
	print("\n\n Parents\n",PathPlan.recorder.parents)
	print("\n\n Costs\n",PathPlan.recorder.costs)
	################# REPLACE WITH PRINTING FUNCTION #######################

	################# REPLACE WITH SINGLE FUNCTION #######################
	print("Step 5. Plotting Results")
	#plot_object = Plot("Path Planning Solution", domain_object)
	## plot_results(arg1,arg2,arg3,...)
	#plot_object.plot_domain()
	#plot_object.plot_obstacles()
	#plot_object.plot_origin_goals()
	#plot_object.plot_solution_graph(PathPlan)
	#plot_object.draw()
	print("Finished! See plot in output folder")
	################ REPLACE WITH SINGLE FUNCTION #######################


if __name__ == '__main__':
	run_program()

