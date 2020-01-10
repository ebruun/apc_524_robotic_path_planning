# path_planner.py
# Author(s): Edvard Bruun, Vivek Kumar

"""
The core module to execute the program

The user to specify the location of the input file in the :meth:`~path_planner.run_program()` function.

Imports the :class:`~input.parse_data_class.ParseDataJSON` class

Imports the :class:`~input.domain.Domain` class

Imports the :class:`~solver.solution.Solution` class

Imports the :class:`~output.plot1.Plot1` class

"""
# Python imports
import sys
import time

############### DELETE THIS ##############
import matplotlib.pyplot as plt
############### DELETE THIS ##############

# Import inputs
from input.parse_data_class import ParseDataJSON
from input.domain_class import Domain
from solver.solution import Solution
from output.plot import Plot


def run_program():
	"""
	Steps in program::

		Step 1. Read input parameters file (user-specified)
		Step 2. Create problem domain
		Step 3. Execute path planning algorithm
		Step 4. Generate result plot

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
		domain_info = program_input.data_dict["DomainInfo"]

		# Step 3. 
		PathPlan = Solution(rrt_algorithm_info,domain_object)
		PathPlan.run_algorithm()
		PathPlan.process_vertex_list()

		# Step 4.
		print_results()
		plot_results()


	"""

	print("\nStep 1. Reading Parameters")
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

	print("\nStep 2. Create Domain")
	domain_object = Domain(domain_info, obstacles_info, origin_goal_info)

	print("\nStep 3. Running Program")
	PathPlan = Solution(rrt_algorithm_info,domain_object)
	PathPlan.run_algorithm()
	PathPlan.process_vertex_list()

	print("Step 4. Showing Results")
	print("\n\n Vertices\n",PathPlan.recorder.vertices)
	print("\n\n Parents\n",PathPlan.recorder.parents)
	print("\n\n Costs\n",PathPlan.recorder.costs)
	print("\n\n solution_path\n",PathPlan.solution_path)

	print("Step 5. Plotting...")
	plot_object = Plot("test run", domain_object)
	plot_object.plot_domain()
	plot_object.plot_obstacles()
	plot_object.plot_origin_goals()
	plot_object.plot_solution_graph(PathPlan)
	plot_object.draw()
	print("Finished! See plot in output folder")


if __name__ == '__main__':
	run_program()

