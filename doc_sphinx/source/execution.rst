Program Execution
=================

Create a virtual python environment based on the requirements.txt file

Run the program in the terminal from where the top-level folder is located in user directory::

	$ cd USER_PATH/apc_524_robotic_path_planning/src_pathplanner

	$ python path_planner.py

User Input
**********

User input .json file and path specified in path_planner.py module.

Any freeform shapes must be specified in bitmap (.pbm) format and located in::

	$ cd USER_PATH/apc_524_robotic_path_planning/src_pathplanner/input/bitmap_files

Example input .json file format::
	
	{
	"DomainInfo":{
		"dim" : 2,
		"shape_type": "rectangle",
		"lower_left": [0.0, 0.0],
		"upper_right": [3.0,4.0]
		},

	"OriginGoalInfo":{
		"origin" : [0.1,0.1],
		"goals":{
			"goal_1":{"dim":2, "shape_type":"circle","radius":0.2, "center":[0.3, 2.1]},
			"goal_2":{"dim":2, "shape_type":"rectangle", "lower_left": [0.0, 0.0], "upper_right": [3.0,4.0]},
			"goal_3"::{"dim":2, "shape_type": "free_form", "bitmap_file":"mouse.pbm"}
			}
		},

	"ObstaclesInfo":{
		"obstacle_1":{"dim":2, "shape_type": "circle", "radius":0.1, "center":[0.5,0.5]},
		"obstacle_2":{"dim":2, "shape_type": "circle", "radius":0.2, "center":[1.5,3.5]},
		"obstacle_3":{"dim":2, "shape_type": "free_form", "bitmap_file":"cat.pbm"}
		},

	"RRTAlgorithmInfo":{
		"method": "rrt_star",
		"n_trials": 1000,
		"step_size": 0.2,
		"dim": 2,
		"neighborhood": 0.3
		}
	}




path_planner module
*******************

.. automodule:: path_planner
   :members:
