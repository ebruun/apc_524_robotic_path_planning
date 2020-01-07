# solution.py
# Author(s): Edvard Bruun

"""
Imports the :class:`solver.stepper.Stepper` class

Imports the :class:`solver.recorder.Recorder` class

Imports the :func:`algorithm.vertex.find_nearest_vertex` function
"""

import numpy as np
from sys import exit

from solver.recorder import Recorder

from algorithm.vertex import find_nearest_vertex
from algorithm.rrt_basic import RRT_Basic
from algorithm.rrt_star import RRT_Star


class Solution:
	"""This class executes and saves the solution to the path planning problem.
	sdfsfdsf sdfasfsfs sdfsdfs
	"""

	def __init__(self,params,domain):
		"""Initialize the Solution class.

		The intialization consists of creating new Recorder and Stepper objects, which are initialized based on the params object.

		Note:
			The input parameters are assigned to instance variables with same name.

		Parameters:
			params (:obj:`~input.params.ParamsRRT` object):
				Object containing the algorithm parameters.
			domain (:obj:`~input.domain.Domain` object):
				Object containing the assembled solution domain.

		Attributes:
			params: see Parameters
			domain: see Parameters
			recorder (:class:`~solver.recorder.Recorder` object):
				Initialized recorder object with input parameters.
			stepper (:obj:`~solver.stepper.Stepper` object):
				Initialized stepper object with input parameters.	
			solution_path (:obj:`list` of :obj:`list` of :obj:`int`):
				A path from origin to each goal in the form of vertex indices. A single path is generated for each goal.
		
		"""
		self.params = params
		self.domain = domain

		self.recorder = Recorder(params)

		self.solution_path = [] 
		self.algorithm = []


	def run_algorithm(self):
		"""  This function runs through the full algorithm.

		A single trial of the algorithm is executed in each iteration of the loop called in this function. The maximum number of trials is specified in the :obj:`~input.params.ParamsRRT` object.

		Calls the :meth:`stepper.do_singlestep() 
		<solver.stepper.Stepper.do_singlestep>` function in the loop.

		"""

		if self.params.method is "rrt_basic":
			self.algorithm = RRT_Basic(
				self.domain, 
				self.recorder,
				self.params
			)

		elif self.params.method is "rrt_star":
			self.algorithm = RRT_Star(
				self.domain,
				self.recorder,
				self.params)
		else:
			exit("ERROR: no valid method")		

		for trial in range(1,self.params.n_trials):
			self.algorithm.rrt_step(trial)
			

	def process_vertex_list(self):
		"""  This function post-processes the full vertex list resulting from  completing the algorithm.

		Loop iterations based on number of goals to evaluate against.

		Calls the :meth:`~solver.solution.Solution.check_if_goal_reached` function in the loop. Returns the index of the vertex to reach the goal.

		Calls the :meth:`~solver.solution.Solution.find_path()` function in the loop. Finds the path from the origin to the vertex to reach the goal.

		"""
		for i in range(len(self.domain.goals)):
			index = self.check_if_goal_reached(self.domain.goals[i])
			self.solution_path.append(self.find_path(index))


	def check_if_goal_reached(self,goal):
		"""  This function checks if a single goal has been reached.

		Calls the :meth:`~solver.solution.Solution.find_nearest_vertex()` function to find the index of the closest vertex and its distance to the center of the goal.

		Checks to see if the closest vertex is within the boundary (perimeter) of the goal object. If it is within the boundary then the goal is reached.

		Error:
			TO DO:
			Goal - currently in the form ["string", middle point, radius]

			distance is measured from the center of the goal object, and its perimeter is the outer edge

			Change this check to .isinside(point) function once the goal is defined as a shape

		Parameters:
			goal (:obj:`~input.shape.Shape` object): A shape object specfied as the target for the algorithm.	

		Returns:
			index (:obj:`int`): The index of the vertex that reached the goal. This is set to :obj:`numpy.nan` if the goal is not reached.

		"""

		##############
		# REPLACE WITH .is_point_inside() of the goal object
		# LOOP THROUGH self.recorder.vertices LIST
		#
		# FOR NOW: 
		# 	RETURN THE INDEX OF THE FIRST POINT TO FALL INSIDE
		# 	RETURN np.nan if nothing falls within
		#
		# LATER: CHANGE THE SUCCESS CRITERIA TO CHOOSE THE VERTEX THAT IS INSIDE
		#	THAT ALSO HAS THE LOWEST VALUE IN self.recorder.costs
		##############

		index, distance = find_nearest_vertex(
			self.recorder.vertices,
			goal[1]
		)

		#print("--Shortest distance:", distance,", Found with vertex at index:", index)

		if (distance < goal[2]):
			#print('Path found!')
			return index
		else:
			#print('No path found!')
			index = np.nan
			return index


	def find_path(self,index):
		"""  This function creates a path of indices from the origin to the end vertex.

		Finds the sequence of nodes working back from a specifed vertex index to the starting origin using the values in the parents list, saved in the :obj:`~solver.recorder.Recorder` object.

		The list of vertex indices for the full path is appended to the :attr:`solution_path` list of lists.
		
		Note:
			Parent of vertex i is j, then parents[i] == j

			For the origin vertex, parents[0] == -1

		"""
		path_list = []
		path_list.append(index)
		child = index

		while child > 0:
			parent = int(self.recorder.parents[child])
			path_list.append(parent)
			
			child = parent #Set the parent index, as the child for next loop
		
		path_list.reverse()		

		return path_list

